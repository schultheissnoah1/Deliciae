---
layout: default
title: Home
phone: ""
email: ""
---
# Deliciae

Interior and exterior services for airplanes and helicopters.

[Explore our services]({{ '/services/' | relative_url }})

## About

Deliciae provides interior and exterior services exclusively for airplanes and helicopters.

![Illustration of an airplane]({{ '/assets/airplane.svg' | relative_url }})

## Contact

{% if page.phone != "" %}[{{ page.phone }}](tel:{{ page.phone | remove: ' ' }}){% endif %}

{% if page.email != "" %}[{{ page.email }}](mailto:{{ page.email }}){% endif %}

{% if page.phone == "" and page.email == "" %}
Contact details will be available soon.
{% endif %}
