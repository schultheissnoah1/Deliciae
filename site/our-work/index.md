---
layout: default
title: Our Work
projects: []
---
# Our Work

{% if page.projects.size > 0 %}
<div class="card-grid">
  {% for project in page.projects %}
  <figure>
    <img src="{{ project.image | relative_url }}" alt="{{ project.alt | escape }}">
    {% if project.caption %}<figcaption>{{ project.caption | escape }}</figcaption>{% endif %}
  </figure>
  {% endfor %}
</div>
{% else %}
Portfolio coming soon.
{% endif %}
