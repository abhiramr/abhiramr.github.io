---
layout: post
title: Bangpypers Pre-Workshop Setup
tags: [python, unix, code, commands]
---

This post is a guide for people to install Python on Ubuntu and Windows (if required), setting up virtualenv and installing the package(s) germane to the corresponding Workshop.
<hr/>
### Ubuntu 
<p/>

- Check your existing version of Python to see if you already have what's required.

~~~~
 $python --version
~~~~
<p/>
-  Open terminal using `Ctrl+Alt+T` or searching for “Terminal” from app launcher. Once it opens, run the following command to add the  Personal Package Archive (PPA):

~~~~
 $sudo add-apt-repository ppa:jonathonf/python-3.5
~~~~
<p/>

- Update packages and install Python 3.6 using the following commands:

~~~~
 $sudo apt-get update
 $sudo apt-get install python3.5
 sudo apt-get install python3-pip
~~~~
<p/>
- Install virtualenv:

~~~~
 $sudo apt-get install virtualenv
~~~~
<p/>
- Create a new virtual environment and activate it:

~~~~
 $cd ~
 $mkdir twisted_workshop
 $cd twisted_wokshop
 $virtualenv -p python3.5 venv
 $source venv/bin/activate
 $pip install twisted (For the Twisted Workshop)
~~~~
<hr/>
### Windows
<p/>

- Download and install the binary from [https://www.python.org/ftp/python/3.5.4/python-3.5.4-amd64.exe](https://www.python.org/ftp/python/3.5.4/python-3.5.4-amd64.exe)
<p/>
- Save the file from here [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) and run it using :

~~~~
 C:\Users\abhiram\Desktop>python get-pip.py
~~~~
<p/>

- Install virtualenv :

~~~~
 C:\Users\abhiram\Desktop>pip install virtualenv
~~~~
<p/>

- Create a new virtual environment and install Twisted in it :

~~~~
 C:\Users\abhiram\Desktop>virtualenv -p python3.5 venv
 C:\Users\abhiram\Desktop>source venv/bin/activate
 C:\Users\abhiram\Desktop>pip install twisted (For the Twisted Workshop)
~~~~

I hope this helps in setting up the environment so we can get minimize time required in getting started with the meat of the workshop :) 