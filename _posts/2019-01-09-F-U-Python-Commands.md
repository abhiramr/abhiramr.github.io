---
layout: post
title: Frequently Used Python Commands
tags: [python, code, commands]
---

The previous post was for commands Unix. This post is about the Python commands I use or Google frequently.

1) To find the absolute path of the directory of the current file being executed -

```python
abs_path = os.path.dirname(os.path.realpath(__file__))
```
<hr/>
2) To copy a file from source to destination (using shutil)-
```python
from shutil import copyfile
  copyfile(src, dst)
```
<hr/>
3) To copy a file or directory from source to destination (using shutil)-
```python
from shutil import copy
  copy(src, dst)
```
<hr/>
4) To create a directory if it doesn't exist -
```python
import os
if not os.path.exists(directory):
    os.makedirs(directory)
```
5) To write a JSON to a file -
```python
import json
with open('data.json', 'w') as f:
    json.dump(data, f)
```
