---
layout: page
title: Publications
---

<ol type="1">
 {% for pub in site.data.publications %}
  <li>
   <div>
   <p>
    {{pub.title}}; {% for author in pub.author %}; {{author.name}}{% endfor %}; {{pub.year}}; {{pub.journal.name}}
   </p>
   </div>
  </li>
 {% endfor %}
</ol>  
