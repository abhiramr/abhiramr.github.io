---
layout: post
title: Bangpypers Pre-Workshop Setup
tags: [python, unix, code, commands]
---

<a href="../2019-11-07-Setting-Up-Python38-Jupyter-lab" style="color:red">A guide to installing a newer version of Python is available here.</a>

We at Bangpypers conduct a lot of workshops and some steps are common for all of them. To that end, this post is meant to serve as guide for people to install Python on Ubuntu and Windows (if required), setting up virtualenv and installing the package(s) germane to the corresponding Workshop.
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
 $sudo add-apt-repository ppa:jonathonf/python-3.6
~~~~
<p/>

- Update packages and install Python 3.6 using the following commands:

~~~~
 $sudo apt-get update
 $sudo apt-get install python3.6
 $sudo apt-get install python3-pip
 $sudo apt-get install python3.6-dev
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
 $virtualenv -p python3.6 venv
 $source venv/bin/activate
 $pip install twisted (For the Twisted Workshop)
~~~~
<hr/>
### Windows
<p/>

- Download and install the binary from [https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe](https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe)
<p/>
- Add the location of the Python folder at the point of installation to the $PATH environment variable.
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
 C:\Users\abhiram\Desktop>virtualenv -p python3.6 venv
 C:\Users\abhiram\Desktop>venv/Scripts/activate
 C:\Users\abhiram\Desktop>pip install twisted (For the Twisted Workshop)
~~~~

I hope this helps in setting up the environment so we can get minimize time required in getting started with the meat of the workshop :) If you have any questions, leave them in the comments and I'll get back to you.

For details related to Bangpypers, check [the website](https://bangalore.python.org.in/) and [the meetup page](https://www.meetup.com/BangPypers/).

{% if page.comments %}
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = abhiramr.github.io/2019-02-22-Bangpypers-PreWorkshop-Setup;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = 2019-02-22-Bangpypers-PreWorkshop-Setup; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://abhiramr.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
                            
{% endif %}