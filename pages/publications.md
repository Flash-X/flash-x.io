---
layout: page
title: Publications
---

<ol type="1">
 {% for pub in site.data.publications %}
  <li>
   <div>
   <p>
    {{pub.title}}, {{pub.authors}}, {{pub.year}}, {{pub.journal}}
   </p>
   </div>
  </li>
 {% endfor %}
</ol>  
