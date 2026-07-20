#!/usr/bin/env python3
"""
Extract content from MkDocs-built HTML files and convert to Hugo markdown.
Run from repo root: python3 scripts/extract-content.py
"""

import os
import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup
import html2text

REPO_ROOT = Path(__file__).parent.parent
HTML_ROOT = REPO_ROOT
HUGO_CONTENT = REPO_ROOT / "hugo-site" / "content"

MONTH_MAP = {
    "jan": 1, "january": 1,
    "feb": 2, "february": 2,
    "mar": 3, "march": 3,
    "apr": 4, "april": 4,
    "may": 5,
    "jun": 6, "june": 6,
    "jul": 7, "july": 7,
    "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10,
    "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}


def try_parse_date_from_slug(slug):
    """Try to extract a YYYY-MM-DD date from a slug like 'july-5-2021' or '14-july-2021'."""
    slug_lower = slug.lower()

    # Pattern: day-month-year (14-july-2021)
    m = re.match(r"^(\d{1,2})[-_]([a-z]+)[-_](\d{4})", slug_lower)
    if m:
        month = MONTH_MAP.get(m.group(2))
        if month:
            return f"{m.group(3)}-{month:02d}-{int(m.group(1)):02d}"

    # Pattern: month-day-year (july-04-2021, jun-29-2021)
    m = re.match(r"^([a-z]+)[-_](\d{1,2})[-_](\d{4})", slug_lower)
    if m:
        month = MONTH_MAP.get(m.group(1))
        if month:
            return f"{m.group(3)}-{month:02d}-{int(m.group(2)):02d}"

    # Pattern: DD-MM-YYYY (31-03-2023)
    m = re.match(r"^(\d{2})[-_](\d{2})[-_](\d{4})$", slug_lower)
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"

    # Pattern: YYYY-MM-DD in slug prefix (2019-07-08-podcasts-i-like)
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", slug_lower)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"

    return None


def extract_article(html_path):
    """Extract title, tags, and body markdown from an MkDocs HTML file."""
    with open(html_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # Title: strip " - Abhiram R" suffix
    title_tag = soup.find("title")
    title = title_tag.text.strip() if title_tag else "Untitled"
    title = re.sub(r"\s*-\s*Abhiram R\s*$", "", title).strip()

    # Article content
    article = soup.find("article", class_="md-content__inner")
    if not article:
        return title, [], ""

    # Tags from nav.md-tags
    tags = []
    nav_tags = article.find("nav", class_="md-tags")
    if nav_tags:
        tags = [a.text.strip() for a in nav_tags.find_all("a", class_="md-tag")]
        nav_tags.decompose()

    # Remove the h1 (we'll use the frontmatter title instead)
    h1 = article.find("h1")
    if h1:
        h1.decompose()

    # Remove edit/feedback buttons MkDocs adds
    for el in article.find_all(class_=re.compile(r"md-content__button|md-source")):
        el.decompose()

    # Convert to markdown
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.body_width = 0
    converter.protect_links = False
    converter.wrap_links = False
    markdown = converter.handle(str(article))

    # Fix relative image paths: ../../../../img/ → /img/
    markdown = re.sub(r"(?:\.\.\/)+img/", "/img/", markdown)
    # Fix any remaining relative img paths
    markdown = re.sub(r"\]\((?:\.\.\/)+", "](/", markdown)

    return title, tags, markdown.strip()


def write_md(output_path, title, date, slug, tags, draft, body, url=None):
    """Write a Hugo markdown file with YAML frontmatter."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Escape quotes in title
    title_escaped = title.replace('"', '\\"')

    tags_yaml = ""
    if tags:
        tag_items = "\n".join(f'  - "{t}"' for t in tags)
        tags_yaml = f"tags:\n{tag_items}"
    else:
        tags_yaml = "tags: []"

    date_line = f"date: {date}" if date else "# date: FILL-IN"
    url_line = f'url: "{url}"' if url else ""

    frontmatter_parts = [
        "---",
        f'title: "{title_escaped}"',
        date_line,
        f'slug: "{slug}"',
        tags_yaml,
        f"draft: {str(draft).lower()}",
    ]
    if url_line:
        frontmatter_parts.append(url_line)
    frontmatter_parts.append("---")

    content = "\n".join(frontmatter_parts) + "\n\n" + body + "\n"
    output_path.write_text(content, encoding="utf-8")
    print(f"  ✓ {output_path.relative_to(REPO_ROOT)}")


def process_blog_posts():
    """Process /blog/YYYY/MM/DD/slug/ → content/blog/YYYY-MM-DD-slug.md"""
    print("\n=== Blog posts ===")
    blog_root = HTML_ROOT / "blog"
    out_dir = HUGO_CONTENT / "blog"

    # Find all YYYY/MM/DD/slug/index.html paths
    pattern = re.compile(r"(\d{4})/(\d{2})/(\d{2})/([^/]+)$")
    count = 0

    for html_file in sorted(blog_root.rglob("index.html")):
        rel = html_file.parent.relative_to(blog_root)
        m = pattern.match(str(rel))
        if not m:
            continue

        year, month, day, slug = m.groups()
        date = f"{year}-{month}-{day}"
        title, tags, body = extract_article(html_file)

        # Preserve original URL structure
        url = f"/blog/{year}/{month}/{day}/{slug}/"
        out_file = out_dir / f"{date}-{slug}.md"
        write_md(out_file, title, date, slug, tags, False, body, url=url)
        count += 1

    print(f"  Total: {count} posts")


def process_section(html_dir, out_dir_name, section_label, slug_transform=None):
    """Generic processor for non-tech sections."""
    print(f"\n=== {section_label} ===")
    html_dir = Path(html_dir)
    out_dir = HUGO_CONTENT / out_dir_name
    count = 0
    no_date = []

    for html_file in sorted(html_dir.rglob("index.html")):
        # Skip the section index page itself
        if html_file.parent == html_dir:
            continue

        slug = html_file.parent.name
        if slug_transform:
            slug = slug_transform(slug)

        date = try_parse_date_from_slug(html_file.parent.name)
        title, tags, body = extract_article(html_file)

        out_file = out_dir / f"{slug}.md"
        write_md(out_file, title, date, slug, tags, False, body)
        count += 1

        if not date:
            no_date.append(slug)

    print(f"  Total: {count} posts")
    if no_date:
        print(f"  ⚠ Needs manual date ({len(no_date)}): {', '.join(no_date)}")


def process_misc():
    """Process /misc/slug/ → content/misc/slug.md"""
    print("\n=== Misc ===")
    misc_root = HTML_ROOT / "misc"
    out_dir = HUGO_CONTENT / "misc"
    count = 0

    for html_file in sorted(misc_root.rglob("index.html")):
        if html_file.parent == misc_root:
            continue

        slug = html_file.parent.name
        date = try_parse_date_from_slug(slug)
        title, tags, body = extract_article(html_file)

        out_file = out_dir / f"{slug}.md"
        write_md(out_file, title, date, slug, tags, False, body)
        count += 1

    print(f"  Total: {count} posts")


def create_section_indexes():
    """Create _index.md files for each section."""
    sections = {
        "blog": ("Technical Articles", "Technical posts on ML, Python, and data engineering."),
        "writing": ("Writing", "Essays and thoughts."),
        "books": ("Books", "Book reviews and thoughts."),
        "az-series": ("A to Z Series", "An A to Z series of short essays."),
        "movies": ("Movies", "Movie reviews."),
        "misc": ("Misc", "Miscellaneous posts."),
    }
    print("\n=== Section index files ===")
    for section, (title, desc) in sections.items():
        path = HUGO_CONTENT / section / "_index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f'---\ntitle: "{title}"\ndescription: "{desc}"\n---\n',
            encoding="utf-8",
        )
        print(f"  ✓ {path.relative_to(REPO_ROOT)}")


def main():
    print(f"Extracting content from: {HTML_ROOT}")
    print(f"Writing Hugo content to: {HUGO_CONTENT}")

    if not (HTML_ROOT / "blog").exists():
        print("ERROR: Run from repo root, or blog/ directory not found.", file=sys.stderr)
        sys.exit(1)

    HUGO_CONTENT.mkdir(parents=True, exist_ok=True)

    # Blog technical posts
    process_blog_posts()

    # Non-tech sections
    process_section(HTML_ROOT / "non-tech" / "mini-essays", "writing", "Writing / Mini-essays")
    process_section(HTML_ROOT / "non-tech" / "books", "books", "Books")
    process_section(HTML_ROOT / "non-tech" / "a-z-series", "az-series", "A-Z Series")
    process_section(HTML_ROOT / "non-tech" / "movies", "movies", "Movies")

    # Misc (includes mainstream, anxious-people under non-tech, and misc/)
    process_section(HTML_ROOT / "non-tech" / "mainstream", "misc", "Mainstream (→ misc)")

    # Non-tech standalone posts (not in any sub-section folder)
    print("\n=== Non-tech standalone (→ misc) ===")
    known_subsections = {"a-z-series", "books", "mainstream", "mini-essays", "movies"}
    non_tech_root = HTML_ROOT / "non-tech"
    out_dir = HUGO_CONTENT / "misc"
    for entry in sorted(non_tech_root.iterdir()):
        if entry.is_dir() and entry.name not in known_subsections:
            html_file = entry / "index.html"
            if html_file.exists():
                slug = entry.name
                date = try_parse_date_from_slug(slug)
                title, tags, body = extract_article(html_file)
                out_file = out_dir / f"{slug}.md"
                write_md(out_file, title, date, slug, tags, False, body)

    process_misc()

    create_section_indexes()

    print("\nDone! Review the output in hugo-site/content/")
    print("Posts with '# date: FILL-IN' need manual dates.")


if __name__ == "__main__":
    main()
