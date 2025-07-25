---
layout: page
title: "People"
permalink: /people/
author_profile: false
classes: wide

---
The CCP-SAS project was initiated through a joint NSF/EPSRC grant. Ongoing
development of the GenApp framework, SASSIE-web, and related deployment
continues with support from various sources, including NSF, NIST, and EPSRC.
Strategic planning and coordination are overseen by a UK/US Leadership Council,
which meets approximately once a month.

{% assign groups = site.data.people %}

{% for section in groups %}
<details open>
  <summary class="people-heading">{{ section[1].title }}</summary>
  <div class="people-grid">
    {% for p in section[1].members %}
      <div class="person-card">
        {% if p.image %}
          <img src="{{ p.image }}" alt="{{ p.name }}" class="profile-pic">
        {% endif %}
        <strong>{{ p.name }}</strong> {{ p.affiliation }} {% if p.email %}<a href="mailto:{{ p.email }}">{{ p.email }}</a>{% endif %}
      </div>
    {% endfor %}
  </div>
</details>
<br>
<br>
{% endfor %}

---

## Acknowledgments

This work benefited from CCP‑SAS software developed through a joint EPSRC (EP/K039121/1) and NSF (CHE‑1265821) grant.

If you have used CCP‑SAS, please consider acknowledging its use in your publications and notifying us by email.
