# Time Lattice Theory

This repository contains all materials accompanying the manuscript:

**“The Time Lattice: A Minimal Tri-Axial Model of Temporal Structure and Conscious Navigation”**  
**Author:** Noam Shai Vatashsky  
**Date:** May 2025  
**DOI:** https://doi.org/10.5281/zenodo.XXXXX

---

## 🧭 Overview

The Time Lattice model proposes a discrete, tri-axial structure of time, consisting of:

- **Linear time** — traditional temporal progression  
- **Cyclic time** — capturing intrinsic periodicities  
- **Subjective time** — accounting for experienced duration  

The framework introduces:

- **Lemma 1**: Uniqueness of minimal-cost resonant paths in a 3D time lattice  
- A testable prediction of **revival combs** in periodically driven quantum systems  
- A bridge between physical time, cyclic recurrence, and conscious experience  

---

## 📁 Repository Structure

```
time-lattice-theory/
├── manuscript/
│   ├── manuscript.tex
│   ├── Time Lattice Theory.pdf
│   └── time_lattice_refs.bib
├── figures/
│   ├── fig_minpath_with_labels.png
│   └── revival_comb_plot_final.png
├── data/
│   ├── minimal_path_nodes.csv
│   └── revival_comb_data.csv
├── code/
│   ├── minimal_path_demo.py
│   └── revival_comb.py
├── LICENSE
└── README.md
```

---

## 🔁 Reproducing Results

### Requirements

- Python ≥ 3.7  
- Install dependencies:

```
pip install numpy matplotlib networkx
```

### Run Scripts

```bash
cd code
python3 minimal_path_demo.py     # → generates fig_minpath_with_labels.png, minimal_path_nodes.csv
python3 revival_comb.py          # → generates revival_comb_plot_final.png, revival_comb_data.csv
```

---

## 📊 Outputs

- `fig_minpath_with_labels.png` — Lattice trajectory visualization
- `minimal_path_nodes.csv` — Coordinates for Table 2
- `revival_comb_plot_final.png` — Fidelity revival comb
- `revival_comb_data.csv` — Time points for Table 1

---

## 📜 License

Licensed under the [MIT License](./LICENSE)

---

## 📚 Citation

To cite this repository or manuscript, use the Zenodo DOI above (to be updated after release).