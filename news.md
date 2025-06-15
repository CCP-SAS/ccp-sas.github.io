---
layout: archive
title: "News"
permalink: /news/
paginate: 10
---

Welcome to the CCP‑SAS News Archive. Here you'll find all our latest updates, events, and achievements.

{% for post in paginator.posts %}
### [{{ post.title }}]({{ post.url }})
{{ post.date | date: "%B %d, %Y" }}

> {{ post.excerpt }}

{% endfor %}

{% include paginator %}
