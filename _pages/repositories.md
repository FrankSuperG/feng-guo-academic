---
layout: page
permalink: /repositories/
title: Repositories
description: Open-source battery modelling software and reproducibility resources by Feng Guo, including CPG-SPMT and Electrochemical Battery Model Atlas for electrochemical battery model implementation, comparison, and validation.
keywords: Feng Guo GitHub, CPG-SPMT, Electrochemical Battery Model Atlas, electrochemical battery model software, battery model reproducibility, lithium-ion battery simulation, control-oriented battery modelling, open-source BMS tools
last_modified_at: 2026-06-30
nav: true
nav_order: 4
---

<section class="repo-intro">
  <p class="pub-kicker">Open Source</p>
  <h2>Tools for reproducible electrochemical battery modelling</h2>
  <p>
    My open-source work focuses on making electrochemical battery models easier to run, compare, validate, and reuse in control-oriented BMS research.
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
</div>
