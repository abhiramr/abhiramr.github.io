---
layout: post
title: Unix Commands I Use
tags: [unix, linux, code, commands]
---

I keep Googling commands for some of these situations regularly -

 <text id="svg_text" x="0" y="130" fill="red" font-size="56"><u><b>General -</b></u></text>

<b>1) To find files one level below your current directory - </b>

I was trying to find which repos in my set of folders have a setup.py file. So, this is what I'd use.

`find . -maxdepth 2 -iname setup.py`

<b>2)  To find what process is running on port 2181 -</b> 

`sudo lsof -n -i :2181 | grep LISTEN`

<b>3) Reduce prompt width on bash - </b>

If the current directory you're in is very deep in the directory tree, chances are, your System Prompt is pretty long and this wastes a lot of screen space. Starting from bash v4 though, there's a new variable called `PROMPT_DIRTRIM` that you can set.

- Before :
![Before](../img/tech/unix/1.png)

- After:
![After](../img/tech/unix/2.png)

 <text id="svg_text" x="0" y="130" fill="red" font-size="56"><u><b>Github -</b></u></text>

<b>4) To change your git remote-url -</b>

`git remote set-url origin <url_name>`

<b>5) Steps for deleting a branch:</b>

- for deleting the remote branch: `git push origin --delete <your_branch>`
- for deleting the local branch: `git branch -D <branch_name>`

<b>6) To delete a file from remote while retaining your local copy -</b>

- For single file: `git rm --cached mylogfile.log`
- For single directory: `git rm --cached -r mydirectory`