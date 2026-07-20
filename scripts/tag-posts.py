#!/usr/bin/env python3
"""
Infer and write tags for all Hugo content posts using rule-based matching.
Run from repo root: python3 scripts/tag-posts.py [--force]
"""

import re
import sys
import argparse
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "hugo-site" / "content"

# ──────────────────────────────────────────────────────────────────────────────
# Tag rules: (pattern, tag) pairs checked against lowercased title+body
# Ordered from most specific to most general.
# ──────────────────────────────────────────────────────────────────────────────
TECH_RULES = [
    # Specific tools / libraries
    (r'\bspark\b',                      "spark"),
    (r'\bpyspark\b',                    "spark"),
    (r'\bairflow\b',                    "airflow"),
    (r'\bdjango\b',                     "django"),
    (r'\bfastapi\b',                    "fastapi"),
    (r'\bflask\b',                      "flask"),
    (r'\bnginx\b',                      "nginx"),
    (r'\bgunicorn\b',                   "nginx"),
    (r'\bjupyter\b',                    "jupyter"),
    (r'\bjupyterlab\b',                 "jupyter"),
    (r'\bpandas\b',                     "pandas"),
    (r'\bnumpy\b',                      "numpy"),
    (r'\bstreamlit\b',                  "streamlit"),
    (r'\bmatplotlib\b',                 "data-visualization"),
    (r'\bd3\.?js\b',                    "data-visualization"),
    (r'\bplotly\b',                     "data-visualization"),
    (r'\bdata.?vis(uali[sz]ation)?\b',  "data-visualization"),
    (r'\bpostgres(ql)?\b',              "postgres"),
    (r'\bmongodb\b',                    "mongodb"),
    (r'\bredis\b',                      "redis"),
    (r'\bdocker\b',                     "docker"),
    (r'\bkubernetes\b',                 "kubernetes"),
    (r'\bgit\b',                        "git"),
    (r'\bgithub\b',                     "git"),
    (r'\bffmpeg\b',                     "ffmpeg"),
    (r'\bmanim\b',                      "manim"),
    (r'\bchrome.?ext',                  "chrome-extension"),
    (r'\bextension\b.{0,30}\bchrome\b', "chrome-extension"),
    (r'\bllm\b',                        "llm"),
    (r'\bclaude\b',                      "llm"),
    (r'\bgpt\b',                        "llm"),
    (r'\bolm?a\b',                      "llm"),
    (r'\bai\s+inf',                     "llm"),
    (r'\bvibe.?cod',                    "vibe-coding"),
    (r'\bstatus.?dashboard\b',          "vibe-coding"),
    (r'\bitertools\b',                  "itertools"),
    (r'\bdecorator',                    "decorators"),
    (r'\bdataclass',                    "dataclasses"),
    (r'\bdesign.?pattern',             "design-patterns"),
    (r'\bconcurren',                    "concurrency"),
    (r'\bthread',                       "concurrency"),
    (r'\basync\b',                      "concurrency"),
    (r'\bfrozen',                       "data-structures"),
    (r'\blist.?comprehension',          "python-basics"),
    (r'\bimport\s+re\b',               "regex"),
    (r'\bregex\b',                      "regex"),
    (r'\bregular.?expression',          "regex"),
    (r'\bclassmethods?\b',              "python-oop"),
    (r'\boop\b',                        "python-oop"),
    (r'\bclass\s+\w+.*:',              "python-oop"),
    (r'\bmachine.?learn',               "machine-learning"),
    (r'\bml\s+interpret',               "machine-learning"),
    (r'\binterp(ret)?abil',             "machine-learning"),
    (r'\bxgboost\b',                    "machine-learning"),
    (r'\bsklearn\b',                    "machine-learning"),
    (r'\bdata.?engineer',               "data-engineering"),
    (r'\bddia\b',                       "data-engineering"),
    (r'\bdesigning.?data.?intensive',   "data-engineering"),
    (r'\biceberg\b',                    "data-engineering"),
    (r'\bchange.?stream',               "data-engineering"),
    (r'\bunix\b',                       "unix"),
    (r'\bbash\b',                       "unix"),
    (r'\bcommand.?line\b',             "unix"),
    (r'\bterminal\b',                   "unix"),
    (r'\bwindows\b',                    "windows"),
    (r'\balias\b.{0,20}\bwindows\b',   "windows"),
    (r'\bazure\b',                      "azure"),
    (r'\bdevops\b',                     "devops"),
    (r'\bci/?cd\b',                     "devops"),
    (r'\bwebsocket',                    "websockets"),
    (r'\breal.?time\b',                 "real-time"),
    (r'\bstreaming\b',                  "real-time"),
    (r'\btimeline.?chart',              "data-visualization"),
    (r'\bhacker.?news\b',               "web-scraping"),
    (r'\bscraping\b',                   "web-scraping"),
    (r'\bgoogle.?news\b',               "web-scraping"),
    (r'\bnapkin.?math\b',               "system-design"),
    (r'\bsystem.?design\b',             "system-design"),
    (r'\bdistributed\b',                "distributed-systems"),
    (r'\breplica\b',                    "distributed-systems"),
    (r'\bleet.?code\b',                 "leetcode"),
    (r'\bneetcode\b',                   "leetcode"),
    (r'\bpython\b',                     "python"),
    (r'\bpy(thon)?.{0,5}\b3\b',        "python"),
    (r'\btutorial\b',                   "tutorial"),
    (r'\bsetup\b',                      "tutorial"),
    (r'\bhow.?to\b',                    "tutorial"),
    (r'\binstall',                      "tutorial"),
    (r'\bblog\b.{0,40}\bmkdocs\b',     "blogging"),
    (r'\bmkdocs\b',                     "blogging"),
    (r'\bhipc\b',                       "conference"),
    (r'\bbangpypers\b',                 "community"),
    (r'\bworkshop\b',                   "community"),
    (r'\bsurvey\b',                     "data-analysis"),
    (r'\bfacebook.?api\b',              "data-analysis"),
]

BOOK_RULES = [
    (r'\bagatha\s+christie\b',          "agatha-christie"),
    (r'\bgeorge\s+orwell\b',            "george-orwell"),
    (r'\bsanderson\b',                  "brandon-sanderson"),
    (r'\bmistborn\b',                   "brandon-sanderson"),
    (r'\bwarbreaker\b',                 "brandon-sanderson"),
    (r'\bstormlight\b',                 "brandon-sanderson"),
    (r'\blocke\s+lamora\b',             "lynch"),
    (r'\brepublic\s+of\s+thieves\b',    "lynch"),
    (r'\bred\s+seas\b',                 "lynch"),
    (r'\bchecklist\b',                  "reading-list"),
    (r'\bfiction\b',                    "fiction"),
    (r'\bnovel\b',                      "fiction"),
    (r'\bmystery\b',                    "mystery"),
    (r'\bcrime\b',                      "mystery"),
    (r'\bdetective\b',                  "mystery"),
    (r'\bthriller\b',                   "thriller"),
    (r'\bfantasy\b',                    "fantasy"),
    (r'\bmagic\b',                      "fantasy"),
    (r'\bwizard\b',                     "fantasy"),
    (r'\bsci.?fi\b',                    "sci-fi"),
    (r'\bscience\s+fiction\b',          "sci-fi"),
    (r'\bdystop',                       "dystopian"),
    (r'\bheist\b',                      "heist"),
    (r'\bjapan(ese)?\b',                "japanese-fiction"),
    (r'\bswedish\b',                    "swedish-fiction"),
    (r'\bhumour\b',                     "humour"),
    (r'\bfunny\b',                      "humour"),
    (r'\bcozy\b',                       "cozy"),
    (r'\bnon.?fiction\b',               "non-fiction"),
    (r'\bself.?help\b',                 "self-help"),
    (r'\bdesign\b',                     "design"),
    (r'\bbook.?review\b',               "book-review"),
    (r'\breview\b',                     "book-review"),
    (r'\breading\b',                    "book-review"),
    (r'\bread\b',                       "book-review"),
]

WRITING_RULES = [
    (r'\bbangalore\b',                  "bangalore"),
    (r'\bindia\b',                      "india"),
    (r'\bkerala\b',                     "kerala"),
    (r'\bflood\b',                      "kerala"),
    (r'\bbook\s+club\b',                "book-club"),
    (r'\bbroke\s+bibliophile',          "book-club"),
    (r'\breading\b',                    "reading"),
    (r'\bwriting\b',                    "writing"),
    (r'\binternet\b',                   "internet"),
    (r'\bsocial.?media\b',             "social-media"),
    (r'\bpodcast',                      "podcasts"),
    (r'\bmusic\b',                      "music"),
    (r'\bsports?\b',                    "sports"),
    (r'\bcricket\b',                    "sports"),
    (r'\bfootball\b',                   "sports"),
    (r'\bnature\b',                     "nature"),
    (r'\btrees?\b',                     "nature"),
    (r'\binsects?\b',                   "nature"),
    (r'\bants?\b',                      "nature"),
    (r'\bsunset',                       "nature"),
    (r'\bsea\b',                        "nature"),
    (r'\bphilosoph',                    "philosophy"),
    (r'\bexistence\b',                  "philosophy"),
    (r'\bcomplexity\b',                 "philosophy"),
    (r'\bcontrol\b',                    "philosophy"),
    (r'\bfate\b',                       "philosophy"),
    (r'\btime\b',                       "reflections"),
    (r'\bnostalgi',                     "nostalgia"),
    (r'\bmemor',                        "nostalgia"),
    (r'\bfood\b',                       "food"),
    (r'\beat(ing)?\b',                  "food"),
    (r'\bshop\b',                       "everyday-life"),
    (r'\bcommute\b',                    "everyday-life"),
    (r'\bcovid\b',                      "covid"),
    (r'\bpandemic\b',                   "covid"),
    (r'\bschool\b',                     "education"),
    (r'\bcollege\b',                    "education"),
    (r'\bexam\b',                       "education"),
    (r'\bfilm\b',                       "movies"),
    (r'\bmovie\b',                      "movies"),
    (r'\bnetflix\b',                    "movies"),
    (r'\bshow\b',                       "tv-shows"),
    (r'\bseries\b',                     "tv-shows"),
    (r'\bhumour\b',                     "humour"),
    (r'\bfunny\b',                      "humour"),
    (r'\bfiction\b',                    "fiction"),
    (r'\bstory\b',                      "fiction"),
    (r'\bshort.?story\b',               "fiction"),
    (r'\bpoem\b',                       "poetry"),
    (r'\bverse\b',                      "poetry"),
    (r'\bgita\b',                       "spirituality"),
    (r'\bbhagavad\b',                   "spirituality"),
]

MOVIE_RULES = [
    (r'\bsuperhero\b',                  "superhero"),
    (r'\bmarvel\b',                     "marvel"),
    (r'\bmcu\b',                        "marvel"),
    (r'\bavengers\b',                   "marvel"),
    (r'\bmalayalam\b',                  "malayalam"),
    (r'\bindian\b',                     "indian-cinema"),
    (r'\btamil\b',                      "tamil"),
    (r'\bkollywood\b',                  "tamil"),
    (r'\bthriller\b',                   "thriller"),
    (r'\bsuperhero\b',                  "superhero"),
    (r'\bcomedy\b',                     "comedy"),
    (r'\baction\b',                     "action"),
    (r'\bsci.?fi\b',                    "sci-fi"),
    (r'\bhorror\b',                     "horror"),
    (r'\bdrama\b',                      "drama"),
]

# Section to rule-set mapping (ordered; first match wins for category tags)
SECTION_RULES = {
    "blog":      TECH_RULES,
    "az-series": WRITING_RULES,
    "writing":   WRITING_RULES,
    "books":     BOOK_RULES,
    "movies":    MOVIE_RULES,
    "misc":      TECH_RULES + WRITING_RULES,
}

# Section-level default tags always added
SECTION_DEFAULTS = {
    "az-series": ["fiction", "a-to-z"],
    "movies":    ["movie-review"],
    "books":     ["book-review"],
}


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
    if not m:
        return None, text
    return m.group(1), m.group(2)


def get_existing_tags(fm_text):
    # tags: ["a", "b"]  or  tags: [a, b]
    m = re.search(r"^tags:\s*\[([^\]]*)\]", fm_text, re.MULTILINE)
    if m:
        content = m.group(1).strip()
        if not content:
            return []
        return [t.strip().strip('"\'') for t in content.split(',') if t.strip()]
    # tags:\n  - "a"\n  - "b"
    m = re.search(r"^tags:\s*\n((?:[ \t]+-[^\n]+\n?)+)", fm_text, re.MULTILINE)
    if m:
        return [re.sub(r'^[ \t]+-\s*["\']?|["\']?\s*$', '', line).strip()
                for line in m.group(1).splitlines() if line.strip()]
    return []


def set_tags(fm_text, tags):
    tag_block = "tags:\n" + "\n".join(f'  - "{t}"' for t in sorted(set(tags)))

    if re.search(r"^tags:\s*\[.*?\]", fm_text, re.MULTILINE):
        return re.sub(r"^tags:\s*\[.*?\]", tag_block, fm_text, flags=re.MULTILINE)

    if re.search(r"^tags:\s*\n(?:[ \t]+-[^\n]+\n?)+", fm_text, re.MULTILINE):
        return re.sub(r"^tags:\s*\n(?:[ \t]+-[^\n]+\n?)+", tag_block + "\n",
                      fm_text, flags=re.MULTILINE)

    if re.search(r"^tags:\s*$", fm_text, re.MULTILINE):
        return re.sub(r"^tags:\s*$", tag_block, fm_text, flags=re.MULTILINE)

    return fm_text


def normalize_tag(tag):
    """Convert a tag to lowercase kebab-case, dropping junk chars."""
    tag = tag.lower().strip()
    tag = re.sub(r'[^a-z0-9]+', '-', tag)  # non-alnum → hyphen
    tag = re.sub(r'-+', '-', tag).strip('-')
    return tag


# Known mappings for old MkDocs tags that are noisy or redundant
TAG_ALIASES = {
    "d3js": "data-visualization",
    "d3-js": "data-visualization",
    "data-visualization": "data-visualization",
    "data-vis": "data-visualization",
    "facebook": "data-analysis",
    "facebook-api": "data-analysis",
    "seinfeld": "tv-shows",
    "google-trends": "data-analysis",
    "til": "til",
    "code-snippet": "tutorial",
    "reference": "reference",
    "bookreviews": "book-review",
    "ddia": "data-engineering",
    "-ddia": "data-engineering",
    "not-python": "misc",
    "llms": "llm",
    "application": "tutorial",
    "books": "book-review",
    "setup": "tutorial",
    "blogs": "blogging",
    "computing": "systems",
    "desktop-widget": "tools",
    "ubunto": "unix",
    "ubuntu": "unix",
    "tools": "tools",
    "data-science": "machine-learning",
    "data-exploration": "data-analysis",
    "curiosities": "data-analysis",
    "databases": "databases",
    "virtualenv": "python",
    "css": "web",
    "jupyterlab": "jupyter",
    "video-editing": "ffmpeg",
    "cli-tools": "unix",
    "interpretability": "machine-learning",
    "science-fiction": "sci-fi",
    "discworld": "fantasy",
    "pop-culture": "misc",
    "television": "tv-shows",
    "daniel-keyes": None,    # author tag — drop
    "ernest-cline": None,
    "fredrik-backman": None,
    "andy-greene": None,
    "leigh-bardugo": None,
    "past": None,
    "present": None,
    "subbu": "fiction",      # character name from A-Z series
    "anthropomorphization": "fiction",
    "work-in-progress": None,
    "learning": "education",
    "literature": "reading",
    "mistborn": "brandon-sanderson",
    "ollama": "llm",
}


def resolve_tag(tag):
    """Normalize and apply alias mapping. Returns None to drop a tag."""
    n = normalize_tag(tag)
    if n in TAG_ALIASES:
        return TAG_ALIASES[n]
    return n if n else None


def infer_tags(section, title, body, existing_tags):
    haystack = (title + " " + body).lower()
    rules = SECTION_RULES.get(section, TECH_RULES + WRITING_RULES)

    matched = []
    for pattern, tag in rules:
        if re.search(pattern, haystack):
            matched.append(tag)

    # Add section defaults
    matched += SECTION_DEFAULTS.get(section, [])

    # Normalize existing tags
    existing_norm = [resolve_tag(t) for t in existing_tags]
    existing_norm = [t for t in existing_norm if t]

    all_tags = existing_norm + [t for t in matched if t not in existing_norm]

    # De-duplicate preserving order, drop Nones, limit to 6
    seen = []
    for t in all_tags:
        resolved = resolve_tag(t) if t else None
        if resolved and resolved not in seen:
            seen.append(resolved)
    return seen[:6]


def process_file(md_path, force=False):
    """Returns (new_tags, was_written) or (None, None) if no frontmatter."""
    text = md_path.read_text(encoding="utf-8")
    fm_text, body = parse_frontmatter(text)
    if fm_text is None:
        return None, None

    existing = get_existing_tags(fm_text)
    if existing and not force:
        return existing, False  # already has tags, skip

    m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
    title = m.group(1).strip('"\'') if m else md_path.stem

    section = md_path.parent.name
    new_tags = infer_tags(section, title, body, existing)

    if not new_tags:
        new_tags = ["misc"]

    new_fm = set_tags(fm_text, new_tags)
    md_path.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")
    return new_tags, True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true",
                        help="Re-tag posts that already have tags")
    args = parser.parse_args()

    all_files = sorted(
        f for f in CONTENT_DIR.rglob("*.md")
        if f.name != "_index.md"
    )

    print(f"Found {len(all_files)} posts.\n")
    updated = skipped = 0

    for f in all_files:
        new_tags, was_written = process_file(f, force=args.force)
        section = f.parent.name

        if new_tags is None:
            print(f"  SKIP (no frontmatter): {f.name}")
            continue

        if was_written:
            print(f"  [{section:10}] {f.stem[:45]:<45}  →  {new_tags}")
            updated += 1
        else:
            skipped += 1

    print(f"\nDone. Tagged: {updated}  Already had tags (skipped): {skipped}")
    print("Run with --force to re-tag everything.")


if __name__ == "__main__":
    main()
