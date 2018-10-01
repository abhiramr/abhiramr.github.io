---
layout: post
title: Links I looked up while learning how to configure Nginx and Gunicorn for my Flask application
tags: [flask, python, code]
---
So, I looked up a lot of links while learning how to configure Gunicorn and Nginx for a Flask app I'm building -

### First of all, you're probably asking - Why do I need Gunicorn and Nginx? That's what I looked up first as well.

- [https://serverfault.com/questions/331256/why-do-i-need-nginx-and-something-like-gunicorn](https://serverfault.com/questions/331256/why-do-i-need-nginx-and-something-like-gunicorn)

### Next, how to actually go about the whole process?

The obvious links:
- [https://gunicorn.org/#quickstart](https://gunicorn.org/#quickstart)
- [https://www.linode.com/docs/web-servers/nginx/how-to-configure-nginx/](https://www.linode.com/docs/web-servers/nginx/how-to-configure-nginx/)
- [http://nginx.org/en/docs/beginners_guide.html](http://nginx.org/en/docs/beginners_guide.html)
- [https://www.fullstackpython.com/green-unicorn-gunicorn.html](https://www.fullstackpython.com/green-unicorn-gunicorn.html)

Quora is generally useless nowadays but this was as a proper answer:
- [https://www.quora.com/What-are-the-differences-between-nginx-and-gunicorn/answer/Pramod-Lakshmanan](https://www.quora.com/What-are-the-differences-between-nginx-and-gunicorn/answer/Pramod-Lakshmanan)

The architecture of Nginx is very well explained here:
- [http://www.aosabook.org/en/nginx.html](http://www.aosabook.org/en/nginx.html)

This link was really helpful
- [https://realpython.com/kickstarting-flask-on-ubuntu-setup-and-deployment/](https://realpython.com/kickstarting-flask-on-ubuntu-setup-and-deployment/)

Some Stackoverflow answers that helped:
- [https://stackoverflow.com/questions/11061788/correct-configuration-for-nginx-to-localhost](https://stackoverflow.com/questions/11061788/correct-configuration-for-nginx-to-localhost)
- [https://stackoverflow.com/questions/43044659/what-is-the-purpose-of-using-nginx-with-gunicorn](https://stackoverflow.com/questions/43044659/what-is-the-purpose-of-using-nginx-with-gunicorn)
- [https://stackoverflow.com/questions/30165746/nginx-return-301-vs-rewrite])https://stackoverflow.com/questions/30165746/nginx-return-301-vs-rewrite

Other useful links:
- [https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18](https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18)
- [https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
)
- [https://www.digitalocean.com/community/tutorials/how-to-move-an-nginx-web-root-to-a-new-location-on-ubuntu-16-04](https://www.digitalocean.com/community/tutorials/how-to-move-an-nginx-web-root-to-a-new-location-on-ubuntu-16-04)
- [https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
- [https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04)
- [https://www.agiliq.com/blog/2013/08/minimal-nginx-and-gunicorn-configuration-for-djang/](https://www.agiliq.com/blog/2013/08/minimal-nginx-and-gunicorn-configuration-for-djang/)
- [https://gist.github.com/netpoetica/5879685](https://gist.github.com/netpoetica/5879685)

### What's next?

I want to hook up icinga to see if it's going to serve my monitoring purpose. I don't know anything about Icinga at the time of writing this note -

- [https://www.digitalocean.com/community/tutorials/how-to-use-icinga-to-monitor-your-servers-and-services-on-ubuntu-14-04](https://www.digitalocean.com/community/tutorials/how-to-use-icinga-to-monitor-your-servers-and-services-on-ubuntu-14-04)

### Note -
This link I accidentally found in the process explaining architectures of a lot of Open Source systems. This is pretty awesome.

- [http://www.aosabook.org/en/index.html](http://www.aosabook.org/en/index.html)



{% if page.comments %}
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = abhiramr.github.io/2018-10-01-Nginx-Gunicorn-Ref-Links;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = 2018-10-01-Nginx-Gunicorn-Ref-Links; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
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