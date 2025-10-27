# Graphene-quantum-capacitance / Quantum Capacitance and Voltage Drop Ratio Calculator
Calculate quantum capacitance and relative distribution of applied potential for OSET


This repository provides Python scripts for calculating and visualizing quantum capacitance (\(C_q\)) and the potential drop ratio (\(V_q / V_{app}\)) across Graphene-electrolyte double layer interfaces. The code replicates canonical models from experimental electron transfer studies ([see reference](https://www.nature.com/articles/nnano.2009.177)) and is ideal for evaluating energy-dependent capacitance effects in material systems such as graphene.

**Features:**
- Computes \(C_q\) using Fermi energy, temperature, and interfacial energy offset.
- Plots \(C_q\) vs Fermi energy and \(V_q / V_{app}\) vs applied potential for multiple offsets.
- Exports all computed data to an Excel spreadsheet for further analysis.
- Implements published physical constants and formulas for direct comparison.
- Easy to modify for different material properties or experimental conditions.

This tool is useful for researchers studying quantum capacitance, interfacial charge transfer, or electrical double-layer phenomena in nanomaterials.

---

**How to use:**
1. Install dependencies: `numpy`, `matplotlib`, `pandas` (and `openpyxl` for Excel export).
2. Run the Python script in your preferred environment (Jupyter Notebook or console).
3. Visualize the results and access the exported data file for further analysis.

--- 
