---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 3
description: Curriculum vitae of Feng Guo, FWO Senior Postdoctoral Fellow, including academic appointments, education, publications, battery modelling projects, awards, conference talks, open-source software, and scholarly service.
keywords: Feng Guo CV, Feng Guo curriculum vitae, FWO Senior Postdoctoral Fellow, VITO, UHasselt, electrochemical battery modelling, battery state estimation, CPG-SPMT, Electrochemical Battery Model Atlas, conference talks, scholarly service
last_modified_at: 2026-10-21
academic_style: true
section_key: cv
page_intro: Academic appointments, research, and scholarly contributions.
footer_fixed: false
cv_sections:
  - id: academic--industry-appointments
    label: Appointments
  - id: education
    label: Education
  - id: publications-overview
    label: Publications
  - id: research-projects-pi
    label: Research projects
  - id: awards--honors
    label: Awards & honors
  - id: conferences--symposia-selected
    label: Conferences
  - id: open-source--community
    label: Open research
  - id: scholarly-service
    label: Scholarly service
---

{% include research-metrics.liquid %}

<div class="cv-layout" markdown="1">
<nav class="cv-section-nav" aria-label="CV sections">
  {% for section in page.cv_sections %}
    <a href="#{{ section.id }}">{{ section.label }}</a>
  {% endfor %}
</nav>
<div class="cv-content" markdown="1">

<h2 id="academic--industry-appointments"><i class="fa-solid fa-briefcase" aria-hidden="true"></i> Academic &amp; Industry Appointments</h2>

- **Visiting Researcher**, Warwick Manufacturing Group (WMG), University of Warwick, United Kingdom (Sep. 2026–Present)<br>
  Collaborating professor: Prof. James Marco
- **FWO Senior Postdoctoral Fellow**, Research Foundation – Flanders (FWO), Belgium (Oct. 2025–Present)
- **Postdoctoral Researcher**, Flemish Institute for Technological Research (VITO), Belgium (Dec. 2022–Sep. 2025)
- **Researcher**, EnergyVille, Belgium (Dec. 2022–Sep. 2025)

<h2 id="education"><i class="fa-solid fa-graduation-cap" aria-hidden="true"></i> Education</h2>

- **Ph.D., Automotive Engineering**, Southwest Jiaotong University (Sep. 2015–Jul. 2020)<br>
  Thesis: _Advanced Battery State Estimation Techniques for Electric Vehicle Battery Management Systems_<br>
  Advisor: Prof. Guangdi Hu

- **B.Sc., Mechanical Engineering**, Southwest Jiaotong University (Sep. 2011–Jul. 2015)<br>
  Top 5% · Thesis: _State of Charge Estimation for Batteries Using Extended Kalman Filter_

<h2 id="publications-overview"><i class="fa-solid fa-book-open" aria-hidden="true"></i> Publications Overview</h2>

- **{{ site.data.publication_metrics.published_accepted }}** published or accepted peer-reviewed papers
- **{{ site.data.publication_metrics.preprints }}** preprints with arXiv or SSRN links

For full details with DOI/preprint links, JCR quartiles, and impact factors, see the [Publications page](/feng-guo-academic/publications/).

<h2 id="research-projects-pi"><i class="fa-solid fa-flask" aria-hidden="true"></i> Research Projects (PI)</h2>

- **FWO Senior Postdoctoral Fellowship, Belgium** (2025–present)<br>
  Research on battery fault mechanism and fault-tolerant control based on electrochemical models in cloud BMS.

- **Sichuan Provincial “Miaozi” Project, China** (2016–2018)<br>
  Development of hybrid power systems for new energy vehicles (Grant No. 2016RZ0043).

<h2 id="awards--honors"><i class="fa-solid fa-trophy" aria-hidden="true"></i> Awards &amp; Honors</h2>

- FWO Senior Postdoctoral Fellowship (2025)
- IEEE Senior Member (2025)
- Sichuan Province First-Class Undergraduate Course Award (2022)
- Outstanding Graduate (Doctoral), Southwest Jiaotong University (2020)
- National Scholarship for Doctoral Students, Ministry of Education of China (2019)
- First-Class Academic Scholarship, Southwest Jiaotong University (2015)
- Outstanding Graduate (Undergraduate), Southwest Jiaotong University (2015)
- First Prize, National Undergraduate Mathematical Modeling Competition (Sichuan Division, 2014)

<h2 id="conferences--symposia-selected"><i class="fa-solid fa-users" aria-hidden="true"></i> Conferences &amp; Symposia (selected)</h2>

- **The 9th International Conference on Energy Storage and Intelligent Vehicles (ICEIV 2026)**, Macau, China (2026)<br>
  Role: Session Co-Chair, _Energy Storage and Integrated Energy Systems I_ · Topic: _Snapshot-Based Aging Interpretation of Field-Aged Graphite/NMC Cells Using a Grouped Electrochemical Model_
- **Computer Physics Communications Seminar Series** (2026)<br>
  Topic: _Bridging Electrochemical Models and Real-Time Battery Control_ · [Event page](https://cassyni.com/events/VLjRX69RDuTd3ozPGfWmWu)
- **The 22nd Symposium on Modeling and Validation of Electrochemical Energy Technologies (ModVal 2026)**, Lausanne, Switzerland (2026)<br>
  Topic: _Electrochemical-Model-Based Voltage Sensor Fault Diagnosis and Fault-Tolerant SOC Estimation for LFP Batteries_
- **The 23rd IFAC World Congress**, Busan, Republic of Korea (2026)<br>
  Topic: _Stability-Guaranteed Dual Kalman Filtering for Electrochemical Battery State Estimation_
- **European Control Conference (ECC 2026)**, Reykjavík, Iceland (2026)<br>
  Topic: _Residual Bias Compensation Dual Extended Kalman Filter for Physics-Based SOC Estimation in Lithium Iron Phosphate Batteries_ · [IEEE Xplore](https://ieeexplore.ieee.org/document/11625570) · [arXiv](https://arxiv.org/abs/2510.22813)
- **American Control Conference (ACC 2025)**, Denver, CO, USA (2025)<br>
  Topic: _Identifiability Analysis of a Pseudo-Two-Dimensional Model & Single Particle Model-Aided Parameter Estimation_
- **10th IEEE International Conference on Optimization and Applications (ICOA 2024)**, Almería, Spain (2024)<br>
  Topic: _Efficiency and Optimality in Electrochemical Battery Model Parameter Identification: A Comparative Study of Estimation Techniques_
- Symposium on Physics and Machine Learning for Batteries, Aachen, Germany (2025)
- OMES Symposium, Genk, Belgium (2025)

<h2 id="open-source--community"><i class="fa-solid fa-code-branch" aria-hidden="true"></i> Open-Source &amp; Community</h2>

Open-source contributions include [CPG-SPMT on GitHub](https://github.com/FrankSuperG/CPG-SPMT), a control-oriented parameter-grouped single-particle model with thermal effects, and [Electrochemical Battery Model Atlas](https://github.com/FrankSuperG/electrochemical-battery-model-atlas), a curated reproducibility guide for public electrochemical battery model repositories.

Open datasets include [RoboBATT: Multirate Robot Battery and Actuator Telemetry Traces](https://zenodo.org/records/21853137), co-authored with Hongxing Liu. RoboBATT links battery-management-system measurements from two parallel lithium iron phosphate battery packs with joint-drive and chassis telemetry from an AGIBOT G2 Pro mobile dual-arm robot. The dataset includes aligned 10 Hz tables, field dictionaries, validation records, and analysis code, released under CC BY 4.0. DOI: [10.5281/zenodo.21853137](https://doi.org/10.5281/zenodo.21853137).

<h2 id="scholarly-service"><i class="fa-solid fa-pen-nib" aria-hidden="true"></i> Scholarly Service</h2>

Reviewer for leading journals including: _Renewable & Sustainable Energy Reviews, Energy, Journal of Energy Storage, Battery Energy, Renewable Energy, Journal of Electroanalytical Chemistry, Electrical Engineering, World Electric Vehicle Journal, Electronics, Batteries, The Journal of Supercomputing,_ and _Complex & Intelligent Systems_.

</div>
</div>
