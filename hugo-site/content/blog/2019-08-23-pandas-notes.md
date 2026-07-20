---
title: "Pandas Notes"
date: 2019-08-23
slug: "pandas-notes"
tags:
  - "jupyter"
  - "machine-learning"
  - "pandas"
  - "python"
draft: false
url: "/blog/2019/08/23/pandas-notes/"
---

These are the commands I use a lot using Pandas - 

**Get rows with NaNs in any column**

> `df[df.isna().any(axis=1)]`

![TailDF](/img/tech/pandas/1.png)

* * *

**Get dataframe excluding all NaNs in a particular Column**

> `df[df['<col_name>'].notnull()]`

![TailDF](/img/tech/pandas/2.png)

* * *

**Get counts of number of Nulls per column**

> `df.isnull().sum()`

* * *

**Increase width of columns displayed in Jupyter Notebooks** \- This is possibly one of my most used commands for every notebook that involves dataframes.

> `pd.set_option('display.max_colwidth',400)`
