---
title: "F U Python Commands"
date: 2019-01-09
slug: "f-u-python-commands"
tags:
  - "python"
  - "reference"
  - "unix"
draft: false
url: "/blog/2019/01/09/f-u-python-commands/"
---

The previous post was for commands Unix. This post is about the Python commands I use or Google frequently.

1) To find the absolute path of the directory of the current file being executed -
    
    
    abs_path = os.path.dirname(os.path.realpath(__file__))
    

* * *

2) To copy a file from source to destination (using shutil)-
    
    
    from shutil import copyfile
      copyfile(src, dst)
    

* * *

3) To copy a file or directory from source to destination (using shutil)-
    
    
    from shutil import copy
      copy(src, dst)
    

* * *

4) To create a directory if it doesn't exist -
    
    
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)
    

5) To write a JSON to a file -
    
    
    import json
    with open('data.json', 'w') as f:
        json.dump(data, f)
