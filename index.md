---
layout: splash
title: "Welcome to CCP-SAS"
permalink: /
header:
  overlay_color: "#000"
  overlay_filter: "0.3"
  overlay_image: /assets/images/ccpsas-hero.jpg
  actions:
    - label: "Learn More"
      url: "/about/"
    - label: "Software"
      url: "/software/"
---

<div class="intro">
  <p><strong>CCP-SAS</strong> is a joint US/UK effort to develop open-source software infrastructure for atomistic and coarse-grained modeling of small-angle scattering (SAS) data from biological and soft matter systems.</p>

  <p>We provide <a href="/software/">modeling tools</a> that bridge experimental SAS data and structural models using molecular simulation and computational analysis. Our efforts aim to accelerate scientific discovery through reproducible, extensible tools supported by an international collaborative community.</p>
</div>

<hr>

## Latest News

<ul class="post-list">
  {% for post in site.posts limit:3 %}
    <li>
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
      <p>{{ post.excerpt }}</p>
    </li>
  {% endfor %}
</ul>

<p><a href="/news/">View all news →</a></p>
