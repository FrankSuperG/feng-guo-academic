---
layout: page
permalink: /repositories/
title: repositories
description: Featured repositories and open-source work by Feng Guo, with emphasis on CPG-SPMT.
nav: true
nav_order: 4
---

## Featured Open-Source Project

### CPG-SPMT

**CPG-SPMT: Control-oriented Parameter-Grouped Single Particle Model with Thermal effects** is an open-source electrochemical battery model designed for **state estimation and control-oriented BMS applications**.

<div align="center">
  <img src="https://raw.githubusercontent.com/FrankSuperG/CPG-SPMT/main/cpg_spmt_logo.png" alt="CPG-SPMT logo" style="max-width: 520px; width: 100%; border-radius: 12px;" />
</div>

- **GitHub:** [FrankSuperG/CPG-SPMT](https://github.com/FrankSuperG/CPG-SPMT)
- **Model idea:** uses a **parabolic approximation** to discretize SPM PDEs into efficient ODE/state-space form
- **Efficiency:** reported to be **over 100× faster** than implicit Euler FDM (72-node reference) while keeping high accuracy
- **Parameter design:** **14 grouped parameters** (9 core + 5 temperature-dependent activation-energy terms)
- **Inputs/Output:** current (A) + temperature (°C) → terminal voltage (V)
- **Validation coverage:** 24 conditions (8 temperatures × 3 drive cycles: DST/US06/FUDS)
- **Reported performance:** average RMSE ≈ 0.0331 V, average R² ≈ 0.9683

### Project value

- Keeps physical interpretability while improving computational efficiency
- Supports real-time estimation/control workflows for advanced BMS
- Provides reproducible validation scripts and multi-temperature benchmark data
