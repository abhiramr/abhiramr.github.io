---
title: "Git Jupyterlab Ext"
date: 2019-10-31
slug: "git-jupyterlab-ext"
tags:
  - "git"
  - "jupyter"
  - "python"
  - "tools"
  - "tutorial"
draft: false
url: "/blog/2019/10/31/git-jupyterlab-ext/"
---

_Disclaimer : Extensions in Jupyter-lab are still very much experimental. But this one seems to be working fabulously so far._

`jupyterlab-git` is an extension that lets you stage and commit changes to notebooks made right from within the Jupyterlab interface.

This is best installed within the confines of a virtual environment, as is anything experimental.

* * *

#### Installation steps -

a) Ensure that you have the latest version of jupyterlab (=1.2.0 at the time of this writing) and NodeJS(=12.13.0 at this time)
    
    
     pip install -U jupyterlab
    

b) Install jupyterlab-git
    
    
     pip install --upgrade jupyterlab-git
    

c) Build jupyter
    
    
     jupyter lab build
    

d) Enable jupyterlab_git
    
    
     jupyter serverextension enable --py jupyterlab_git --sys-prefix
    

e) Run jupyter-lab
    
    
     jupyter-lab
    

_In Jupyter-lab_

f) Enable the Extensions Manager (experimental)

![git0](/img/jupyter/jupyter_git_0.jpg)

g) Search for and Install jupyterlab-git extension. You'll be asked to Rebuild Jupyter.

![git1](/img/jupyter/git_ext/jupyter_git_1.jpg)

h) Once the Git extension shows up post rebuilding, you can stage any changes made per notebook.

![git2](/img/jupyter/git_ext/jupyter_git_2.jpg)

i) Commit post-staging

![git3](/img/jupyter/git_ext/jupyter_git_3.jpg)

j) Push!

![git4](/img/jupyter/git_ext/jupyter_git_4.jpg)

If you see this, you're successfully done :)

![git5](/img/jupyter/git_ext/jupyter_git_5.jpg)

* * *

#### Additional reference links -

  * <https://github.com/jupyterlab/jupyterlab-git>
  * [Looking through the issues help a lot!](https://github.com/jupyterlab/jupyterlab-git/issues)



{% if page.comments %}

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)

{% endif %}
