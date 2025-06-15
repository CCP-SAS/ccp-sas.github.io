---
layout: single
title: "People"
permalink: /people/
author_profile: false
---
The CCP-SAS project was initiated through a joint NSF/EPRSRC grant. Work on
further developing the GenApp framework SASSIE-web and deployment continues
through various independent support mechanism from NSF, NIST, and EPSRC.
Planning, direction and are facilitated through a UK/US Leadership Counsel
which meets roughly monthly.

{% assign groups = site.data.people %}

{% for section in groups %}
<details open>
  <summary><strong><h2 class="people-heading">{{ section[1].title }}</h2>
</strong></summary>
  <div class="people-grid">
    {% for p in section[1].members %}
      <div class="person-card">
        {% if p.image %}
          <img src="{{ p.image }}" alt="{{ p.name }}" class="profile-pic">
        {% endif %}
        <strong>{{ p.name }}</strong><br>
        {{ p.affiliation }}<br>
        {% if p.email %}<a href="mailto:{{ p.email }}">{{ p.email }}</a>{% endif %}
      </div>
    {% endfor %}
  </div>
</details>
{% endfor %}

---

## Acknowledgments

This work benefited from CCP‑SAS software developed through a joint EPSRC (EP/K039121/1) and NSF (CHE‑1265821) grant.

If you have used CCP‑SAS, please consider acknowledging its use in your publications and notifying us by email.
