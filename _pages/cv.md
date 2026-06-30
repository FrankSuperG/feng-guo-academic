---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 3
description: Curriculum vitae of Feng Guo, FWO Senior Postdoctoral Fellow, including academic appointments, education, publications, battery modelling projects, awards, conference talks, open-source software, and scholarly service.
keywords: Feng Guo CV, Feng Guo curriculum vitae, FWO Senior Postdoctoral Fellow, VITO, UHasselt, electrochemical battery modelling, battery state estimation, CPG-SPMT, Electrochemical Battery Model Atlas, conference talks, scholarly service
_styles: |
  .post .post-title {
    letter-spacing: 0;
    margin-bottom: 0.4rem;
  }
  .post .post-description {
    color: var(--global-text-color-light);
    margin-bottom: 1.1rem;
  }
  .post article h2 {
    margin-top: 1.8rem;
    margin-bottom: 0.8rem;
    padding-bottom: 0.35rem;
    border-bottom: 1px solid var(--global-divider-color);
    font-size: 1.35rem;
    display: flex;
    align-items: center;
    gap: 0.45rem;
  }
  .post article h2 i {
    color: var(--global-theme-color);
    font-size: 0.95em;
    width: 1.15em;
    text-align: center;
  }
  .post article ul {
    margin-bottom: 0.9rem;
  }
  .post article ul li {
    margin-bottom: 0.35rem;
    line-height: 1.6;
  }
  .post article p {
    line-height: 1.7;
  }
  .cv-quick-stats {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin: 0.4rem 0 1.2rem;
  }
  .cv-quick-stats span {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 999px;
    padding: 0.22rem 0.72rem;
    font-size: 0.82rem;
    color: var(--global-text-color-light);
    background: var(--global-card-bg-color);
  }
  .cv-quick-stats i {
    color: var(--global-theme-color);
  }
  @media (max-width: 768px) {
    .post .post-title { font-size: 2rem; }
    .post article h2 {
      font-size: 1.15rem;
      gap: 0.35rem;
    }
    .post article ul li { margin-bottom: 0.28rem; }
    .cv-quick-stats { gap: 0.35rem; }
    .cv-quick-stats span { font-size: 0.75rem; padding: 0.2rem 0.62rem; }
  }
---

<div class="cv-quick-stats">
  <span><i class="fa-solid fa-book-open"></i> 23 published/accepted papers</span>
  <span><i class="fa-solid fa-link"></i> 11 preprints</span>
  <span><i class="fa-solid fa-quote-right"></i> {{ site.data.citations.profile.citations | default: 459 }} citations</span>
  <span><i class="fa-solid fa-chart-line"></i> h-index {{ site.data.citations.profile.h_index | default: 12 }}</span>
</div>

## <i class="fa-solid fa-briefcase"></i> Academic & Industry Appointments

- **FWO Senior Postdoctoral Fellow**, Research Foundation – Flanders (FWO), Belgium (Oct. 2025–Present)
- **Postdoctoral Researcher**, Flemish Institute for Technological Research (VITO), Belgium (Dec. 2022–Sep. 2025)
- **Researcher**, EnergyVille, Belgium (Dec. 2022–Sep. 2025)

## <i class="fa-solid fa-graduation-cap"></i> Education

- **Ph.D., Automotive Engineering**, Southwest Jiaotong University (Sep. 2015–Jul. 2020)<br>
  Thesis: _Advanced Battery State Estimation Techniques for Electric Vehicle Battery Management Systems_<br>
  Advisor: Prof. Guangdi Hu

- **B.Sc., Mechanical Engineering**, Southwest Jiaotong University (Sep. 2011–Jul. 2015)<br>
  Top 5% · Thesis: _State of Charge Estimation for Batteries Using Extended Kalman Filter_

## <i class="fa-solid fa-book-open"></i> Publications Overview

- **23** published or accepted peer-reviewed papers
- **11** preprints with arXiv or SSRN links

For full details with DOI/preprint links, JCR quartiles, and impact factors, see the [Publications page](/feng-guo-academic/publications/).

## <i class="fa-solid fa-flask"></i> Research Projects (PI)

- **FWO Senior Postdoctoral Fellowship, Belgium** (2025–present)<br>
  Research on battery fault mechanism and fault-tolerant control based on electrochemical models in cloud BMS.

- **Sichuan Provincial “Miaozi” Project, China** (2016–2018)<br>
  Development of hybrid power systems for new energy vehicles (Grant No. 2016RZ0043).

## <i class="fa-solid fa-trophy"></i> Awards & Honors

- FWO Senior Postdoctoral Fellowship (2025)
- IEEE Senior Member (2025)
- Sichuan Province First-Class Undergraduate Course Award (2022)
- Outstanding Graduate (Doctoral), Southwest Jiaotong University (2020)
- National Scholarship for Doctoral Students, Ministry of Education of China (2019)
- First-Class Academic Scholarship, Southwest Jiaotong University (2015)
- Outstanding Graduate (Undergraduate), Southwest Jiaotong University (2015)
- First Prize, National Undergraduate Mathematical Modeling Competition (Sichuan Division, 2014)

## <i class="fa-solid fa-users"></i> Conferences & Symposia (selected)

- **Computer Physics Communications Seminar Series** (2026)<br>
  Topic: _Bridging Electrochemical Models and Real-Time Battery Control_ · [Event page](https://cassyni.com/events/VLjRX69RDuTd3ozPGfWmWu)
- **The 22nd Symposium on Modeling and Validation of Electrochemical Energy Technologies (ModVal 2026)**, Lausanne, Switzerland (2026)<br>
  Topic: _Electrochemical-Model-Based Voltage Sensor Fault Diagnosis and Fault-Tolerant SOC Estimation for LFP Batteries_
- **The 23rd IFAC World Congress**, Busan, Republic of Korea (2026)<br>
  Topic: _Stability-Guaranteed Dual Kalman Filtering for Electrochemical Battery State Estimation_
- **European Control Conference (ECC 2026)**, Reykjavík, Iceland (2026)<br>
  Topic: _Residual Bias Compensation Filter for Physics-Based SOC Estimation in Lithium Iron Phosphate Batteries_
- **American Control Conference (ACC 2025)**, Denver, CO, USA (2025)<br>
  Topic: _Identifiability Analysis of a Pseudo-Two-Dimensional Model & Single Particle Model-Aided Parameter Estimation_
- **10th IEEE International Conference on Optimization and Applications (ICOA 2024)**, Almería, Spain (2024)<br>
  Topic: _Efficiency and Optimality in Electrochemical Battery Model Parameter Identification: A Comparative Study of Estimation Techniques_
- Symposium on Physics and Machine Learning for Batteries, Aachen, Germany (2025)
- OMES Symposium, Genk, Belgium (2025)

## <i class="fa-solid fa-code-branch"></i> Open-Source & Community

Open-source contributions include [CPG-SPMT on GitHub](https://github.com/FrankSuperG/CPG-SPMT), a control-oriented parameter-grouped single-particle model with thermal effects, and [Electrochemical Battery Model Atlas](https://github.com/FrankSuperG/electrochemical-battery-model-atlas), a curated reproducibility guide for public electrochemical battery model repositories.

## <i class="fa-solid fa-pen-nib"></i> Scholarly Service

Reviewer for leading journals including: _Renewable & Sustainable Energy Reviews, Energy, Journal of Energy Storage, Battery Energy, Renewable Energy, Journal of Electroanalytical Chemistry, Electrical Engineering, World Electric Vehicle Journal, Electronics, Batteries, The Journal of Supercomputing,_ and _Complex & Intelligent Systems_.
