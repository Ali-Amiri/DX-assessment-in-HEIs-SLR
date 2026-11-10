# Institution-Level Digital Transformation Assessment Models in Higher Education — BERTopic Supplement

This repository contains research materials accompanying the revised manuscript:

**Digital Transformation Assessment Models in Higher Education Institutions: A Systematic Literature Review and Research Agenda** (submission 261848631, *Cogent Education*).

## Repository contents

- `data/NEW DATASET 29 Studies.csv` — source dataset provided by the authors. The spreadsheet has **262 data rows**, including blank dimension entries; the modeling notebooks select **188 nonempty labels** for the topic model. The CSV retains its original Windows-1252-compatible encoding (the notebook includes encoding fallbacks).
- `notebooks/01_baseline_seed42.ipynb` — baseline model, UMAP `n_neighbors=15`, random seed `42`, HDBSCAN `min_cluster_size=10`.
- `notebooks/02_stability_seed21.ipynb` — seed `21`.
- `notebooks/03_stability_seed123.ipynb` — seed `123`.
- `notebooks/04_umap_neighbors10.ipynb` — UMAP `n_neighbors=10` (seed `42`).
- `notebooks/05_hdbscan_cluster8.ipynb` — HDBSCAN `min_cluster_size=8` (seed `42`).
- `results/run_*/` — the authors' exported topic assignments, topic summaries, topic tables, and HTML tables from each run. Note: the original export filenames were identical across the five runs; the enclosing run directories distinguish them.
- `results/ari_stability_matrix.csv` — pairwise ARI matrix independently computed from the five provided assignment files.
- `scripts/compute_stability.py` — script to recompute ARI values, including outlier assignments (`topic_id=-1`).
- `requirements.txt` — unpinned dependencies used in the notebooks, **not** a record of exact original package versions.

## Verification of reported stability results

Each topic assignment file contains 188 aligned construct labels. The pairwise Adjusted Rand Index values, recomputed independently from the supplied exports, yield:

| Metric | Value |
| --- | ---: |
| Mean pairwise ARI | 0.686 |
| Minimum pairwise ARI | 0.584 |
| Maximum pairwise ARI | 0.783 |
| Sample standard deviation | 0.059 |

Verify with:

```bash
pip install scikit-learn
python scripts/compute_stability.py
```

## Running the supplied BERTopic notebooks

1. Download or clone the repository and open Jupyter Notebook or JupyterLab **from the repository root**.
2. Install dependencies (`pip install -r requirements.txt`).
3. Install the spaCy English model (`python -m spacy download en_core_web_sm`).
4. Run `notebooks/01_baseline_seed42.ipynb`, then the four sensitivity notebooks, top to bottom.
5. Generated CSV/HTML files are written to their corresponding `results/run_*/` directories.

**Portability-only edits:** The five notebooks preserve the original modeling code and saved analytical outputs, except that their hard-coded Kaggle input and output paths have been replaced by relative paths to `data/` and `results/`. Thus, the notebooks can find files when run outside Kaggle. The notebooks have **not been rerun from scratch** in a fresh environment as part of preparing this repository.

## Reproducibility qualifications

- Topic modeling may vary across versions of BERTopic, UMAP, HDBSCAN, PyTorch and other dependencies. The original environment's exact package versions were not supplied; for strict reruns, add a frozen `pip freeze` or Kaggle environment export matching the original analyses.
- The dataset and five notebooks support reproducibility of the **topic modeling component**; they do not by themselves constitute the full systematic review screening dataset, CASP ratings, or complete comparative coding framework requested by reviewers.
- Semantic grouping and ARI stability do **not** independently establish conceptual validity of the eight named dimensions. Any external validation evidence should be deposited separately.
- Before making the repository public, authors should check that all uploaded data and notebook metadata are authorized for public release and contain no sensitive information or credentials.

## Citation

Please cite the accompanying manuscript and this repository's archived version (add a Zenodo DOI upon release, if applicable).
