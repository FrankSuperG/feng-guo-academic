---
layout: page
permalink: /publications/
title: Publications
description: Representative and full publication list, including under-review and published papers in battery modeling, estimation, and AI for BMS.
nav: true
nav_order: 2
_styles: |
  .pub-filters {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 0.6rem 0 1rem;
  }
  .pub-filters button {
    border: 1px solid var(--global-divider-color);
    background: var(--global-card-bg-color);
    color: var(--global-text-color);
    border-radius: 999px;
    padding: 0.25rem 0.8rem;
    font-size: 0.85rem;
    cursor: pointer;
  }
  .pub-filters button.active {
    border-color: var(--global-theme-color);
    color: var(--global-theme-color);
    font-weight: 600;
  }
---

{% include bib_search.liquid %}

## Representative Papers
<div class="publications" id="pub-representative">
{% bibliography --query @*[selected=true] --group_by year %}
</div>

<div class="pub-filters" aria-label="Publication filters">
  <button class="active" onclick="filterPubs('all', this)">All</button>
  <button onclick="filterPubs('rep', this)">Representative</button>
  <button onclick="filterPubs('review', this)">Under Review</button>
  <button onclick="filterPubs('published', this)">Published</button>
</div>

## Under Review / Re-submission
<div class="publications" id="pub-under-review">
{% bibliography --query @*[pubstate=under_review] --group_by year %}
</div>

## Published / Accepted
<div class="publications" id="pub-published">
{% bibliography --query @*[pubstate=published] --group_by year %}
</div>

<script>
  function filterPubs(mode, btn) {
    const rep = document.getElementById('pub-representative');
    const review = document.getElementById('pub-under-review');
    const pub = document.getElementById('pub-published');
    const buttons = document.querySelectorAll('.pub-filters button');
    buttons.forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');

    rep.style.display = (mode === 'all' || mode === 'rep') ? '' : 'none';
    review.style.display = (mode === 'all' || mode === 'review') ? '' : 'none';
    pub.style.display = (mode === 'all' || mode === 'published') ? '' : 'none';
  }
</script>
