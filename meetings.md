---
layout: default # Use the default layout for the index page
title: "Meetings & Events"
permalink: /meetings/ # Sets the URL to /meetings/
---

# Past Meetings and Events

This page lists our historical meetings and significant events. Click on each title for more details and photos.

<ul class="meeting-list">
  {% assign meetings = site.meetings | sort: "date" | reverse %}  {% comment %} Sort by date, most recent first {% endcomment %}
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
### Annual Meetings:
* [CCP-SAS: New developments in computational modelling of X-ray and neutron scattering curves](/Meetings/BBS2020/Program.html){:target="_blank"}. 
A Satellite workshop at the virtual [BBS 60th Anniversary meeting](https://britishbiophysics.org/posts/2020/2020-06-01-bbs2020online/), Sep 14-18, 2020
* [4th](/Meetings/Fifth/Program.html){:target="_blank"} Annual Joint Project Meeting in Cardiff, Wales, UK - Jun 19-21, 2017 - (Report)
* [3rd](/Meetings/Fourth/Program.html){:target="_blank"} Annual Joint Project Meeting in Gaithersburg, MD, USA - May 23-24, 2016
* A Project Steering Meeting was held at TU Berlin, Germany - Sep 13, 2015 (NB: Invitation only)
* [2nd](/Meetings/Second/Program.html){:target="_blank"} Annual Joint Project Meeting at Diamond Light Source,
Oxon, UK - Oct 6-7, 2014
* [1st](/Meetings/Kickoff/Program.html){:target="_blank"} ('Kickoff') Annual Joint Project Meeting in Gaithersburg,
MD, USA - Feb 7-9, 2014