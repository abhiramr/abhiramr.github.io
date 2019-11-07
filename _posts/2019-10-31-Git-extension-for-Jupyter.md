---
layout: post
title: Git extension for Jupyterlab
tags: [python, git, code, intermediate]
---

[Extensions in Jupyter-lab are still very much experimental. But this one seems to be working fabulously so far.]

Jupyterlab-git is an extension that lets you stage and commit changes to notebooks made right from within the Jupyterlab interface.

This is best installed within the confines of a virtual environment, as is anything experimental.
<hr/>

#### Installation steps -

a) Ensure that you have the latest version of jupyterlab (=1.2.0 at the time of this writing) and NodeJS(=12.13.0 at this time)
~~~~
 pip install -U jupyterlab
~~~~

b) Install jupyterlab-git
~~~~
 pip install --upgrade jupyterlab-git
~~~~

c) Build jupyter
~~~~
 jupyter lab build
~~~~


d) Enable jupyterlab_git
~~~~
 jupyter serverextension enable --py jupyterlab_git --sys-prefix
~~~~

e) Run jupyter-lab
~~~~
 jupyter-lab
~~~~


<u>In Jupyter-lab</u>

f) Enable the Extensions Manager (experimental)

![git0](../img/jupyter/jupyter_git_0.jpg)

g) Search for and Install jupyterlab-git extension. You'll be asked to Rebuild Jupyter.

![git1](../img/jupyter/jupyter_git_1.jpg)

h) Once the Git extension shows up post rebuilding, you can stage any changes made per notebook.

![git2](../img/jupyter/jupyter_git_2.jpg)

i) Commit post-staging

![git3](../img/jupyter/jupyter_git_3.jpg)

j) Push!

![git4](../img/jupyter/jupyter_git_4.jpg)

If you see this, you're successfully done :)

![git5](../img/jupyter/jupyter_git_5.jpg)

<hr/>

#### Additional reference links - 


- <a href="https://github.com/jupyterlab/jupyterlab-git" style="color:blue">https://github.com/jupyterlab/jupyterlab-git</a>
- <a href="https://github.com/jupyterlab/jupyterlab-git/issues" style="color:blue">Looking through the issues help a lot!</a>
<p/>
{% if page.comments %}
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = abhiramr.github.io/2019-10-31-Git-extension-for-Jupyter;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = 2019-10-31-Git-extension-for-Jupyter; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
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
