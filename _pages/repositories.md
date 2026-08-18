---
layout: page
permalink: /repositories/
title: Repositories
description: Open-source software and datasets by Feng Guo, including the RoboBATT robot battery telemetry dataset, CPG-SPMT, and the Electrochemical Battery Model Atlas for reproducible battery modelling and BMS research.
keywords: Feng Guo datasets, RoboBATT, robot battery telemetry dataset, AGIBOT G2 Pro, lithium iron phosphate battery data, BMS telemetry, robot actuator telemetry, Zenodo dataset, CPG-SPMT, Electrochemical Battery Model Atlas, battery model reproducibility, open-source BMS tools
last_modified_at: 2026-08-18
nav: true
nav_order: 4
---

<section class="repo-intro">
  <p class="pub-kicker">Open Research</p>
  <h2>Datasets and tools for reproducible battery research</h2>
  <p>
    My open research work combines reusable battery datasets, control-oriented models, and reproducibility resources for battery management systems and electrochemical modelling.
  </p>
</section>

<div class="repo-showcase">
  <article class="repo-card">
    <img src="https://raw.githubusercontent.com/FrankSuperG/CPG-SPMT/main/cpg_spmt_logo.png" alt="CPG-SPMT logo" />
    <div>
      <p class="repo-eyebrow">Control-oriented model implementation</p>
      <h2>CPG-SPMT</h2>
      <p>
        A control-oriented parameter-grouped single particle model with thermal effects for efficient lithium-ion battery simulation, state estimation, and BMS control workflows.
      </p>
      <ul>
        <li>Parabolic approximation for efficient SPM state-space implementation</li>
        <li>14 grouped parameters, including temperature-dependent activation-energy terms</li>
        <li>Validated across 24 conditions: 8 temperatures and 3 drive cycles</li>
      </ul>
      <a href="https://github.com/FrankSuperG/CPG-SPMT" class="repo-link" target="_blank" rel="noopener noreferrer">
        <i class="fa-brands fa-github"></i>
        <span>FrankSuperG/CPG-SPMT</span>
      </a>
    </div>
  </article>

  <article class="repo-card">
    <img src="https://raw.githubusercontent.com/FrankSuperG/electrochemical-battery-model-atlas/main/assets/logo.png" alt="Electrochemical Battery Model Atlas logo" />
    <div>
      <p class="repo-eyebrow">Reproducibility atlas</p>
      <h2>Electrochemical Battery Model Atlas</h2>
      <p>
        A curated, reproducibility-focused guide to public electrochemical battery model repositories and workflows, covering DFN/P2D, SPM, SPMe, thermal coupling, and degradation models.
      </p>
      <ul>
        <li>Indexes 19 public model repositories or workflows</li>
        <li>Documents 16 successful reproductions with command-level evidence</li>
        <li>Includes model pages, numerical-method notes, reproduction dashboards, and a staged reading roadmap</li>
      </ul>
      <a href="https://github.com/FrankSuperG/electrochemical-battery-model-atlas" class="repo-link" target="_blank" rel="noopener noreferrer">
        <i class="fa-brands fa-github"></i>
        <span>FrankSuperG/electrochemical-battery-model-atlas</span>
      </a>
    </div>
  </article>

  <article class="repo-card repo-card--featured" itemscope itemtype="https://schema.org/Dataset">
    <img src="{{ '/assets/img/robobatt-dataset.jpg' | relative_url }}" alt="RoboBATT robot battery and actuator telemetry dataset icon" />
    <div>
      <p class="repo-eyebrow">Open robot battery dataset · Zenodo</p>
      <h2 itemprop="name">RoboBATT: Multirate Robot Battery and Actuator Telemetry Traces</h2>
      <p itemprop="description">
        Two approximately 4.3-hour scripted operating records from an AGIBOT G2 Pro mobile dual-arm robot, linking multirate actuator telemetry with pack-level measurements from two parallel 48 V, 17 Ah lithium iron phosphate batteries.
      </p>
      <p class="repo-byline">
        Feng Guo and Hongxing Liu · Version 1.0.0 · Published 8 August 2026 · CC BY 4.0
      </p>
      <ul>
        <li>Native-cadence 22-channel joint-drive messages and pack-level BMS reports</li>
        <li>Aligned 10 Hz tables covering current, voltage, SOC, SOH, temperature, joint, and chassis states</li>
        <li>Reproducible catalogues of 5,920 counter-phase arm cycles and 127 telemetry-derived macrocycles</li>
        <li>Includes field dictionaries, validation records, analysis code, checksums, and battery duty-cycle profiles</li>
      </ul>
      <meta itemprop="version" content="1.0.0" />
      <meta itemprop="datePublished" content="2026-08-08" />
      <div class="repo-actions">
        <a href="https://zenodo.org/records/21853137" class="repo-link" target="_blank" rel="noopener noreferrer" itemprop="url">
          <i class="fa-solid fa-database"></i>
          <span>View dataset</span>
        </a>
        <a href="https://doi.org/10.5281/zenodo.21853137" class="repo-link repo-link--secondary" target="_blank" rel="noopener noreferrer" itemprop="sameAs">
          <i class="fa-solid fa-fingerprint"></i>
          <span>DOI 10.5281/zenodo.21853137</span>
        </a>
        <a href="https://creativecommons.org/licenses/by/4.0/" class="repo-link repo-link--secondary" target="_blank" rel="license noopener noreferrer">
          <i class="fa-solid fa-scale-balanced"></i>
          <span>CC BY 4.0</span>
        </a>
      </div>
    </div>
  </article>
</div>
