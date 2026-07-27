---
layout: page
title: 归档日历
permalink: /archive/
description: 按月份浏览博客文章归档
---

{%- assign date_format = site.minima.date_format | default: "%Y-%m-%d" -%}
{%- assign posts_by_month = site.posts | group_by_exp: "post", "post.date | date: '%Y-%m'" -%}

{%- if posts_by_month.size > 0 -%}
<p>按月份查看文章归档。</p>

<ul class="archive-month-index">
{%- for month in posts_by_month -%}
<li>
<a href="#month-{{ month.name }}">{{ month.name }}</a>
<span>({{ month.items | size }})</span>
</li>
{%- endfor -%}
</ul>

{%- for month in posts_by_month -%}
{%- assign parts = month.name | split: "-" -%}
<h2 id="month-{{ month.name }}" class="archive-month-title">{{ parts[0] }} 年 {{ parts[1] }} 月</h2>
<ul class="archive-posts">
{%- for post in month.items -%}
<li>
<span class="archive-post-day">{{ post.date | date: "%m-%d" }}</span>
<a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
</li>
{%- endfor -%}
</ul>
{%- endfor -%}
{%- else -%}
<p>当前还没有可归档的文章。</p>
{%- endif -%}