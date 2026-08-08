---
layout: page
permalink: /publications/
title: Publications
description: Publications by Feng Guo on electrochemical battery modelling, battery state estimation, physics-guided AI, graph transformers, Mamba state evolution, and 3D multi-object tracking, with DOI, preprint, JCR quartile, and impact-factor links.
keywords: Feng Guo publications, electrochemical battery modelling papers, graph transformer, Mamba state evolution, 3D multi-object tracking, Complex and Intelligent Systems, Journal of Power Sources, Journal of Energy Chemistry, SOC estimation, physics-guided AI, arXiv battery preprints, JCR quartile, impact factor
last_modified_at: 2026-08-08
nav: true
nav_order: 2
---

<section class="pub-overview">
  <div>
    <p class="pub-kicker">Research Output</p>
    <h2>Papers, preprints, and conference reports by year</h2>
    <p>
      Published papers, accepted papers, preprints, and conference talks/reports are shown together in reverse chronological order, with published and accepted work appearing first within each year.
    </p>
  </div>
  <div class="pub-metrics" aria-label="Publication metrics">
    <div><strong>24</strong><span>published & accepted papers</span></div>
    <div><strong>11</strong><span>preprints</span></div>
    <div><strong>{{ site.data.citations.profile.citations | default: 459 }}</strong><span>Google Scholar citations</span></div>
    <div><strong>{{ site.data.citations.profile.h_index | default: 12 }}</strong><span>h-index</span></div>
  </div>
</section>

{% include bib_search.liquid %}

<section class="pub-section" id="works">
  <div class="pub-section-heading">
    <p>Chronological List</p>
    <h2>Papers, Preprints & Talks</h2>
  </div>
  <div class="publications">
    {% bibliography --query @* --group_by year %}
  </div>
</section>
