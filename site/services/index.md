---
layout: default
title: Services
services:
  - name: Interio
    levels: 3
  - name: Exterio
    levels: 4
---
# Services

Deliciae provides interior and exterior services exclusively for airplanes and helicopters.

{% for service in page.services %}
<section aria-labelledby="{{ service.name | slugify }}">
  <h2 id="{{ service.name | slugify }}">{{ service.name }}</h2>
  <ul class="card-grid">
    {% for level in (1..service.levels) %}
    <li class="card">
      <h3>Level {{ level }}</h3>
      <p>Service details coming soon.</p>
    </li>
    {% endfor %}
  </ul>
</section>
{% endfor %}

[Contact Deliciae]({{ '/' | relative_url }}#contact)
