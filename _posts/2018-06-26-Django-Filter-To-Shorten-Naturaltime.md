---
layout: post
title: Django Filter snippet to Shorten naturaltime format
tags: [django, python, code]
---

- This is a filter snippet to shorten the natural time value obtained using naturaltime function from humanize.


{% raw %}
~~~~
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
~~~~
{% endraw %}



{% if page.comments %}
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = abhiramr.github.io/2018-06-26-Django-Filter-To-Shorten-Naturaltime;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = 2018-06-26-Django-Filter-To-Shorten-Naturaltime; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
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