---
title: "Django Filter To Shorten Naturaltime"
date: 2018-06-26
slug: "django-filter-to-shorten-naturaltime"
tags:
  - "django"
  - "python"
  - "tutorial"
draft: false
url: "/blog/2018/06/26/django-filter-to-shorten-naturaltime/"
---

* This is a filter snippet to shorten the natural time value obtained using naturaltime function from humanize.


    
    
    #In templatetag file , say file_tags.py
    from django import template
    register = template.Library()
    
    @register.filter
    def shorten_naturaltime(naturaltime):
        naturaltime = naturaltime.replace('minutes','m').replace('hours','h').replace('days','d')
        naturaltime = naturaltime.replace('months','mon').replace('weeks','w').replace('week','w')
        return naturaltime
    
    #In Usage file
    {% load file_tags %} 
    {{start_time|naturaltime|shorten_naturaltime}} #where start_time is the datetime object to be modified
    

{% if page.comments %}

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)

{% endif %}
