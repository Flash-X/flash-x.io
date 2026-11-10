---
layout: page
title: Publications
---

{% assign pubs = site.data.publications | sort: "year" | reverse %}
{% assign current_year = "" %}
{% for pub in pubs %}
  {% if pub.year != current_year %}
    {% unless forloop.first %}</ol>{% endunless %}
    <h2>{{ pub.year | escape }}</h2>
    <ol type="1">
    {% assign current_year = pub.year %}
  {% endif %}
  <li>
   <div>
   <p>
    {% if pub.url %}<a href="{{ pub.url | escape }}">{% endif %}{{ pub.title | escape }}{% if pub.url %}</a>{% endif %}—{% for author in pub.author %}{% if forloop.first == false %}; {% endif %}{{ author.name | escape }}{% endfor %}—{% if pub.journal.name %}{{ pub.journal.name | escape }}, {% endif %}{{ pub.year | escape }}
  </p>
   </div>
  </li>
{% endfor %}
</ol>
