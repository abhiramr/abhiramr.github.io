---
layout: post
title: Pandas Notes - A reckoner
tags: [python, pandas, data, code]
---

1. **Get rows with NaNs in any column** 
> `df[df.isna().any(axis=1)]`

![TailDF](../img/tech/pandas/1.png)

2. **Get dataframe excluding all NaNs in a particular Column** 
> `df[df['<col_name>'].notnull()]`

![TailDF](../img/tech/pandas/2.png)

