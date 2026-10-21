---
layout: page
permalink: /publications/
title: Publications
academic_style: true
section_key: publications
page_intro: Peer-reviewed research, preprints, and conference contributions.
footer_fixed: false
description: Publications by Feng Guo on electrochemical battery modelling, battery state estimation, residual bias compensation, physics-guided AI, graph transformers, and 3D multi-object tracking, with DOI, IEEE Xplore, arXiv, JCR quartile, and impact-factor links.
keywords: Feng Guo publications, electrochemical battery modelling papers, European Control Conference, ECC 2026, residual bias compensation dual extended Kalman filter, LFP SOC estimation, IEEE Xplore, graph transformer, Mamba state evolution, Journal of Power Sources, Journal of Energy Chemistry, physics-guided AI, arXiv battery preprints
last_modified_at: 2026-10-21
nav: true
nav_order: 2
---

{% include research-metrics.liquid %}

{% include bib_search.liquid %}

<section class="pub-section" id="works">
  <div class="pub-section-heading">
    <h2>Papers, Preprints & Talks</h2>
  </div>
  <div class="publications">
    {% bibliography --query @* --group_by year %}
  </div>
</section>
