---
layout: post
title: Unix Commands I Use
tags: [unix, linux, code, commands]
---

I keep Googling some commands regularly and I'm sure many people are just like me in this department where you simply can't remember that command even though you know that's the one you have to use. This post will be regularly updated and hopefully, a one-stop shop for me to refer these commands from. I hope it helps you, the reader as well!

#### To find files one level below your current directory - 

I was trying to find which repos in my set of folders have a setup.py file. So, this is what I'd use.

`find . -maxdepth 2 -iname setup.py`


#### To change your git remote-url -

`git remote set-url origin <url_name>`