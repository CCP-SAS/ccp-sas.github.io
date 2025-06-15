---
layout: single
title: "People"
permalink: /people/
author_profile: false
---

{% assign groups = site.data.people %}
{% for section in groups %}
## {{ section[1].title }}

{% for p in section[1].members %}
- **{{ p.name }}**, {{ p.affiliation }}{% if p.email %} — [{{ p.email }}](mailto:{{ p.email }}){% endif %}
{% endfor %}

{% endfor %}

---

## Acknowledgments

This work benefited from CCP‑SAS software developed through a joint EPSRC (EP/K039121/1) and NSF (CHE‑1265821) grant.

If you have used CCP‑SAS, please consider acknowledging its use in your publications and notifying us by email.
