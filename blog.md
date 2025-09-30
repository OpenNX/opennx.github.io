---
layout: default
title: Blog
permalink: /blog/
---

<section class="guides-section">
  <h1>Our Guides</h1>
  <p>A complete archive of all our guides and articles.</p>
  <div class="posts-list" style="margin-top: 30px;">
    {% for post in site.posts %}
      <a href="{{ site.baseurl }}{{ post.url }}" class="post-link">
        <div class="post-categories">
          {% for category in post.categories %}
            <span class="post-category">{{ category }}</span>
          {% endfor %}
        </div>
        <h3 class="post-title">{{ post.title }}</h3>
        <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
        <span class="post-date">{{ post.date | date: "%B %d, %Y" }}</span>
      </a>
    {% endfor %}
  </div>
</section>
