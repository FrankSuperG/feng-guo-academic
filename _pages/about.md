---
layout: about
title: About
description: Feng Guo is an FWO Senior Postdoctoral Fellow at VITO and UHasselt working on control-oriented electrochemical battery modelling, SOC estimation, fault diagnosis, and physics-guided AI for battery management systems.
keywords: Feng Guo, FWO Senior Postdoctoral Fellow, VITO, UHasselt, electrochemical battery modelling, battery state estimation, parameter identification, SOC estimation, lithium iron phosphate batteries, battery safety, fault diagnosis, fault-tolerant control, physics-guided AI, battery management systems
last_modified_at: 2026-10-21
permalink: /
subtitle: FWO Senior Postdoctoral Fellow · Joint Postdoc at VITO & UHasselt (Belgium)
research_visuals: true
footer_fixed: false

hero:
  eyebrow: FWO Senior Postdoctoral Fellow · IEEE Senior Member
  title: Feng Guo
  headline: Electrochemical models.<br>Intelligent battery systems.
  lead: I connect battery physics with estimation, diagnosis, and learning to make battery management more reliable in the real world.
  affiliations: VITO & UHasselt · Belgium<br>Visiting Researcher · WMG, University of Warwick
  metrics:
    - key: published_accepted
      label: published & accepted papers
    - key: citations
      value: "459"
      label: Google Scholar citations
    - key: h_index
      value: "12"
      label: h-index
    - key: preprints
      label: preprints
  actions:
    - label: Publications
      url: /publications/
      icon: fa-solid fa-book-open
    - label: CV
      url: /cv/
      icon: fa-solid fa-file-lines
    - label: Open Source
      url: /repositories/
      icon: fa-brands fa-github
  links:
    - label: Google Scholar
      url: https://scholar.google.com/citations?user=z2SHUxkAAAAJ&hl=en
      icon: ai ai-google-scholar-square ai-1x
    - label: ORCID
      url: https://orcid.org/0000-0002-5141-8672
      icon: ai ai-orcid-square ai-1x
    - label: GitHub
      url: https://github.com/FrankSuperG
      icon: fa-brands fa-github
    - label: ResearchGate
      url: https://www.researchgate.net/profile/Feng-Guo-20
      icon: fa-brands fa-researchgate
    - label: LinkedIn
      url: https://www.linkedin.com/in/feng-guo-a3187a259/
      icon: fa-brands fa-linkedin

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p><strong>Email:</strong> <a href="mailto:feng.guo@vito.be">feng.guo@vito.be</a></p>

selected_papers: false
social: false

announcements:
  enabled: false

latest_posts:
  enabled: false
---

<section class="home-section home-section--lead" aria-labelledby="research-perspective">
  <p class="home-kicker">Research Perspective</p>
  <h2 id="research-perspective">Physics at the core. Real systems in mind.</h2>
  <p>
    I am <strong>Feng Guo</strong>, an <strong>FWO Senior Postdoctoral Fellow</strong> and <strong>IEEE Senior Member</strong>, working jointly with <strong>VITO</strong> and <strong>UHasselt</strong> in Belgium. My research develops physically meaningful, computationally efficient methods that support battery management across temperatures, operating profiles, and sensor uncertainty.
  </p>
</section>

<section class="home-section home-section--research">
  <p class="home-kicker">From Understanding to Deployment</p>
  <h2>Research Interests</h2>
  {% include research-framework.liquid %}
  <div class="research-grid">
    <article id="research-modelling">
      <span class="research-index">01 / MODELS</span>
      <i class="fa-solid fa-wave-square"></i>
      <h3>Control-oriented electrochemical battery modelling</h3>
      <p>Efficient SPM/P2D simplification, parameter grouping, thermal coupling, and state-space implementations for control and BMS use.</p>
    </article>
    <article id="research-estimation">
      <span class="research-index">02 / ESTIMATION</span>
      <i class="fa-solid fa-crosshairs"></i>
      <h3>Battery state estimation and parameter identification</h3>
      <p>Robust SOC estimation, Kalman filtering, observer design, and operating-profile-aware electrochemical parameter estimation.</p>
    </article>
    <article id="research-safety">
      <span class="research-index">03 / SAFETY</span>
      <i class="fa-solid fa-shield-halved"></i>
      <h3>Battery safety, fault diagnosis, and fault-tolerant control</h3>
      <p>Sensor-fault diagnosis, safety-aware estimation, and fault-tolerant control methods for reliable battery operation.</p>
    </article>
    <article id="research-learning">
      <span class="research-index">04 / LEARNING</span>
      <i class="fa-solid fa-brain"></i>
      <h3>Physics-guided AI for battery management systems</h3>
      <p>Hybrid physics-learning models that preserve interpretability while improving robustness under real operating conditions.</p>
    </article>
  </div>
</section>

{% include publication-chart.liquid %}

<section class="home-section home-open-research" aria-labelledby="home-open-title">
  <div class="home-section-heading">
    <div>
      <p class="home-kicker">Open Research</p>
      <h2 id="home-open-title">Models, methods, and data. Shared.</h2>
    </div>
    <a class="home-inline-link" href="{{ '/repositories/' | relative_url }}">All resources <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
  </div>
  <div class="home-resource-grid">
    <a class="home-resource" href="https://github.com/FrankSuperG/CPG-SPMT" target="_blank" rel="noopener noreferrer">
      <img src="https://raw.githubusercontent.com/FrankSuperG/CPG-SPMT/main/cpg_spmt_logo.png" width="72" height="72" alt="CPG-SPMT logo" loading="lazy">
      <span class="home-resource-type">Open-source model</span>
      <h3>CPG-SPMT</h3>
      <p>Control-oriented, parameter-grouped electrochemical modelling with thermal effects.</p>
      <span class="home-resource-destination"><i class="fa-brands fa-github" aria-hidden="true"></i> GitHub <i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i></span>
    </a>
    <a class="home-resource" href="https://github.com/FrankSuperG/electrochemical-battery-model-atlas" target="_blank" rel="noopener noreferrer">
      <img src="https://raw.githubusercontent.com/FrankSuperG/electrochemical-battery-model-atlas/main/assets/logo.png" width="72" height="72" alt="Electrochemical Battery Model Atlas logo" loading="lazy">
      <span class="home-resource-type">Reproducibility guide</span>
      <h3>Battery Model Atlas</h3>
      <p>A curated guide to public electrochemical battery models and reproducible workflows.</p>
      <span class="home-resource-destination"><i class="fa-brands fa-github" aria-hidden="true"></i> GitHub <i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i></span>
    </a>
    <a class="home-resource" href="https://zenodo.org/records/21853137" target="_blank" rel="noopener noreferrer">
      <img src="{{ '/assets/img/robobatt-dataset.jpg' | relative_url }}" width="72" height="72" alt="RoboBATT dataset logo" loading="lazy">
      <span class="home-resource-type">Open dataset</span>
      <h3>RoboBATT</h3>
      <p>Real-world robot battery and actuator telemetry for battery systems research.</p>
      <span class="home-resource-destination"><i class="fa-solid fa-database" aria-hidden="true"></i> Zenodo <i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i></span>
    </a>
  </div>
</section>

<section class="home-section home-section--collab">
  <p class="home-kicker">Connect</p>
  <h2>Collaboration</h2>
  <p>
    I welcome collaboration on electrochemical model reduction, battery state estimation, physics-informed machine learning, fault-tolerant control, and open-source tools for battery research.
  </p>
  <a class="text-link-strong" href="mailto:feng.guo@vito.be">feng.guo@vito.be</a>
</section>
