---
layout: default # Use the default layout for the index page
title: "Meetings & Events"
permalink: /meetings/ # Sets the URL to /meetings/
---

# Past Meetings and Events

This page lists our historical meetings and significant events. Click on each title for more details and photos.

<ul class="meeting-list">
  {% assign meetings = site.meetings | sort: "date" | reverse %} {# Sort by date, most recent first #}
  {% for meeting in meetings %}
    <li class="meeting-list-item">
      <a href="{{ meeting.url | relative_url }}">
        <span class="meeting-list-date">{{ meeting.date | date: "%b %-d, %Y" }}:</span>
        <span class="meeting-list-title">{{ meeting.title | escape }}</span>
      </a>
      {% if meeting.excerpt %}
        <div class="meeting-list-excerpt">
          {{ meeting.excerpt | markdownify | strip_html | truncatewords: 30 }}
        </div>
      {% endif %}
    </li>
  {% endfor %}
</ul>