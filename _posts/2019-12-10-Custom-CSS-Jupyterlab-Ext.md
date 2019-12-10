---
layout: post
title: Custom CSS extension for Jupyterlab
tags: [setup, jupyterlab, intermediate]
---


Jupyterlab is a definite improvement on the older IPython notebook interface - both in features and in appearance. There is now even an in-built "Dark Theme" that can be enabled. 

But is that all?

As we know, Jupyterlab is a browser based app and is ipso facto, written on a base of HTML, CSS and Javascript. So if we want to change the appearance over and above what we get out of the box with jupyterlab, we can. 
Now, it <i>is</i> possible to make any CSS changes by hacking into the internals of the notebook, but thanks to a nifty Jupyterlab extension by Adam Wallner, we don't have to.
<hr/>

Check out <a href="https://abhiramr.com/2019-11-07-Setting-Up-Python38-Jupyter-lab/" style="color:blue">Step 4 of my previous post</a> for preliminary installation steps, if you don't already have Jupyterlab installed.

#### Steps -

a) Install custom_css
~~~~
 jupyter labextension install @wallneradam/custom_css
~~~~

b) Run jupyter-lab
~~~~
 jupyter-lab
~~~~


<u>In Jupyter-lab</u>

c) Enable the Extensions Manager (experimental)

![git0](../img/jupyter/jupyter_git_0.jpg)

d) Navigate to the advanced settings editor

![git1](../img/jupyter/css_ext/3__01.png)

e) Navigate to the custom-css pane and your "User Preferences" section is expected to be largely empty unlike in the populated figure below.

![git2](../img/jupyter/css_ext/custom_css.png)


f) Let me explain the block of code added above in "User Preferences" (sans comments)

~~~~
{
  "rules": 
  [
    {
	"selector": "#jp-MainLogo",
	"styles": 
    [
    "display:block",
    "background: url('https://abhiramr.com/img/sharingan.jpeg') no-repeat",
    "background-size: contain",
    "width: 23px",
    "height: 45px",
    "padding-left: 0px",
    "-moz-box-sizing: border-box",
    "box-sizing: border-box"
    ]
	},
	{
    "selector": ".jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser",
    "styles": ["background:#50bd30"]
	}
  ]
}
~~~~

We have a list of `rules` whose members are elements that are to be styled. Each element member is a dictionary, identified by a `selector` that can be a tag, a class or an id (or any selector). Each member also consists of list - `style` in which we list out every custom property we wish to bestow upon the element. If a particular element is identified by multiple ids or classes as is normally the case, they are just all listed in the `selector` separated by spaces.

In this example, I've chosen to modify two elements - (i) the icon on the top left corner of the notebook that is normally the standard Jupyter notebook icon and (ii) The highlighted color that indicates the current active cell in the notebook. 

And now, in classic weight-loss program fashion, here are the before and after pics for each of the changes made.



<style>
.column {
  float: left;
  width: 50%;
  padding: 5px;
}

/* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
}
</style>
#### Before :
<div class="row">
<div class="column">
<img src="../img/jupyter/css_ext/1-pre__01.png" alt="Mona Lisa" style="width:600px;height:300px"/>
</div>
<div class="column">
<img src="../img/jupyter/css_ext/2-pre__01.png" alt="Mona Lisa" style="width:600px;height:300px"/>
</div>
</div>
<hr/>
#### After :

<div class="row">
<div class="column">
<img src="../img/jupyter/css_ext/1-post__01.png" alt="Mona Lisa" style="width:600px;height:300px"/>
</div>
<div class="column">
<img src="../img/jupyter/css_ext/2-post__01.png" alt="Mona Lisa" style="width:600px;height:300px"/>
</div>
</div>

<hr/>

#### Finally - 

<div class="row">
<img src="../img/jupyter/css_ext/final.png" alt="Mona Lisa" style="width:100%;height:100%"/>
</div>

<hr/>

#### Additional reference links - 


- <a href="https://github.com/wallneradam/jupyterlab-custom-css" style="color:blue">https://github.com/wallneradam/jupyterlab-custom-css</a>

<p/>
{% if page.comments %}
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = abhiramr.github.io/2019-12-10-Custom-CSS-Jupyterlab-Ext;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = 2019-12-10-Custom-CSS-Jupyterlab-Ext; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
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
