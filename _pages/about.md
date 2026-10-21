---
layout: about
title: About
description: Feng Guo researches Physics-Informed Battery Intelligence at VITO and UHasselt, connecting electrochemical modelling, fast parameter identification, robust state estimation, and sensor-fault tolerance for reliable battery management.
keywords: Feng Guo, Physics-Informed Battery Intelligence, FWO Senior Postdoctoral Fellow, VITO, UHasselt, electrochemical battery modelling, robust battery state estimation, parameter identification, SOC estimation, lithium iron phosphate batteries, battery safety, sensor fault diagnosis, fault-tolerant control, physics-guided AI, battery management systems
last_modified_at: 2026-10-21
permalink: /
subtitle: FWO Senior Postdoctoral Fellow · Joint Postdoc at VITO & UHasselt (Belgium)
footer_fixed: false

hero:
  eyebrow: FWO Senior Postdoctoral Fellow · IEEE Senior Member
  title: Feng Guo
  headline: Physics-Informed<br>Battery Intelligence
  lead: Developing physics-informed models and estimation methods to make battery management systems more accurate, robust, and interpretable.
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

research_interests:
  - id: research-modelling
    key: model
    step: MODEL
    diagram_label: Electrochemical modelling
    title: Control-oriented electrochemical battery modelling
    description: SPM/P2D model reduction, grouped electrochemical parameters, thermal coupling, and fast parameter identification with BOLT.
  - id: research-estimation
    key: estimate
    step: ESTIMATE
    diagram_label: State & parameter estimation
    title: Battery state estimation and parameter identification
    description: Robust SOC estimation, physics-guided Kalman filtering, observer design, and joint state-parameter estimation under uncertainty.
  - id: research-safety
    key: safety
    step: PROTECT
    diagram_label: Safety & fault tolerance
    title: Battery safety, fault diagnosis, and fault-tolerant control
    description: Sensor-fault diagnosis and fault-tolerant SOC estimation for reliable battery operation, extending towards interpretable ageing diagnostics and safety- and lifetime-aware control.
  - id: research-learning
    key: learning
    step: LEARN
    diagram_label: Physics-guided intelligence
    title: Physics-guided AI for battery management systems
    description: Hybrid physics-learning models that preserve interpretability while improving robustness under real operating conditions.

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

<section class="home-section home-section--lead" aria-label="About Feng Guo">
  <p>
    I am <strong>Feng Guo</strong>, an <strong>FWO Senior Postdoctoral Fellow</strong> and <strong>IEEE Senior Member</strong>, working jointly with <strong>VITO</strong> and <strong>UHasselt</strong> in Belgium. My research connects electrochemical modelling and parameter identification with robust state estimation and fault-tolerant battery management.
  </p>
  <p class="home-research-question">
    <strong>Research question</strong>
    How can we estimate battery states accurately, reliably, and efficiently when sensing is limited, model parameters are uncertain, and sensors can fail?
  </p>
</section>

<section class="home-section home-section--research">
  <h2>Research Interests</h2>
  {% include research-framework.liquid %}
  <div class="research-grid">
    {% for interest in page.research_interests %}
      <article id="{{ interest.id }}">
        <span class="research-index">0{{ forloop.index }} · {{ interest.step }}</span>
        <h3>{{ interest.title }}</h3>
        <p>{{ interest.description }}</p>
      </article>
    {% endfor %}
  </div>
</section>

<section class="home-section home-open-research" aria-labelledby="home-open-title">
  <div class="home-section-heading">
    <div>
      <p class="home-kicker">Open Research</p>
      <h2 id="home-open-title">Open-source Software & Datasets</h2>
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
