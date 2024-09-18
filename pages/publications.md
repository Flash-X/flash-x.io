---
layout: page
title: Publications
---

<ol type="1">
 {% for pub in site.data.publications %}
  <li>
   <div>
   <p>
    {% if pub.url %}<a href="{{pub.url}}">{% endif %}{{pub.title}}{% if pub.url %}</a>{% endif %}—{% for author in pub.author %}{% if forloop.first == false %}; {% endif %}{{author.name}}{% endfor %}—{% if pub.journal.name %}{{pub.journal.name}}, {% endif %}{{pub.year}}
  </p>
   </div>
  </li>
 {% endfor %}
</ol>  
