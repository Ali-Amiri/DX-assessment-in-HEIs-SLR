# Digital Transformation Assessment Models in Higher Education Institutions

## Overview

This repository provides datasets, screening records, quality appraisal documentation, Python notebooks, and analytical outputs related to the systematic analysis of institution-level digital transformation (DX) assessment models in higher education institutions (HEIs).

The repository is organized to support transparency, reproducibility, and independent examination of the research procedures, including academic and grey-literature screening, quality assessment, semantic topic modeling, and clustering stability analysis.

## 1. Repository Contents

### 1.1. Academic Literature Screening

**File:** `01_Academic_Literature_Screening.xlsx`

Contains the academic literature screening records used in the systematic review, documenting the identification, screening, and selection of relevant academic studies.

### 1.2. Grey Literature Screening

**File:** `02_Grey_Literature_Screening.xlsx`

Contains the grey-literature screening records, including source information and web addresses for the identified assessment models, frameworks, indices, and reports.

The screening process comprises three stages:

- **After removing duplicates:** 60 records.
- **Eligibility assessment:** 11 records.
- **Final inclusion:** 7 records.

### 1.3. Quality Appraisal

**File:** `03_Quality_Appraisal.docx`

Contains the adapted Critical Appraisal Skills Programme (CASP) quality assessment procedures and results, including:

- Eight quality appraisal criteria.
- Individual assessments of 31 eligible studies.
- Study-level quality scores and inclusion decisions.
- Inter-rater agreement statistics based on Cohen's kappa.

The final quality appraisal resulted in 29 included studies.

### 1.4. BERTopic Dataset

**File:** `data/NEW DATASET 29 Studies.csv`

Contains the source dataset used for semantic topic modeling.

The original dataset contains 262 data rows, including blank dimension entries. The analytical notebooks extract 188 nonempty construct labels for topic modeling.

The original CSV encoding is preserved, with encoding fallback procedures implemented in the notebooks.

### 1.5. BERTopic Notebooks

The `notebooks/` directory contains five Python notebooks:

| Notebook | Description |
|---|---|
| `01_baseline_seed42.ipynb` | Baseline BERTopic model with random seed 42 |
| `02_stability_seed21.ipynb` | Stability analysis with random seed 21 |
| `03_stability_seed123.ipynb` | Stability analysis with random seed 123 |
| `04_umap_neighbors10.ipynb` | UMAP sensitivity analysis with 10 neighbors |
| `05_hdbscan_cluster8.ipynb` | HDBSCAN sensitivity analysis with minimum cluster size 8 |

The baseline model uses the following principal settings:

- Embedding model: `all-MiniLM-L6-v2`
- UMAP: `n_neighbors=15`, `n_components=5`, `min_dist=0.0`, `metric=cosine`
- HDBSCAN: `min_cluster_size=10`, `min_samples=3`, `metric=euclidean`
- Random seed: `42`

The sensitivity analyses examine changes in random initialization, neighborhood size, and clustering parameters.

### 1.6. Topic Modeling Results

The `results/` directory contains the analytical outputs from the five BERTopic runs, including:

- Topic assignments.
- Topic summaries and representative terms.
- Topic tables.
- HTML analytical outputs.
- Cluster stability comparisons.
- Adjusted Rand Index (ARI) results.

Each run is stored in a separate directory to distinguish the corresponding outputs.

### 1.7. Stability Verification

**File:** `results/ari_stability_matrix.csv`

Contains the pairwise ARI comparisons across the five BERTopic runs.

The reported stability statistics are:

| Metric | Value |
|---|---:|
| Mean pairwise ARI | 0.686 |
| Minimum pairwise ARI | 0.584 |
| Maximum pairwise ARI | 0.783 |
| Sample standard deviation | 0.059 |
| Pairwise comparisons | 10 |

The ARI calculations include all 188 construct labels, including outlier assignments (`topic_id=-1`).

### 1.8. Analysis Scripts and Dependencies

**Files:**

- `scripts/compute_stability.py` — recomputes pairwise ARI values from the five topic-assignment outputs.
- `requirements.txt` — lists the Python dependencies required for executing the analysis.

The dependency list does not necessarily represent the exact package versions of the original analytical environment.

## 2. Reproducing the Analysis

### Step 1: Download the repository

Download or clone the repository to your local computer.

### Step 2: Install Python dependencies

Open a terminal in the repository's root directory and execute:

```bash
pip install -r requirements.txt
```

### Step 3: Install the spaCy language model

```bash
python -m spacy download en_core_web_sm
```

### Step 4: Execute the BERTopic notebooks

Open Jupyter Notebook or JupyterLab from the repository root.

Execute the notebooks in the following order:

1. Baseline model (seed 42).
2. Stability model (seed 21).
3. Stability model (seed 123).
4. UMAP sensitivity analysis.
5. HDBSCAN sensitivity analysis.

### Step 5: Verify clustering stability

To independently recompute the ARI statistics from the exported topic assignments, run:

```bash
python scripts/compute_stability.py
```

The resulting statistics can be compared with the values reported in the stability matrix.

## 3. Methodological Notes

The BERTopic analysis uses semantic embeddings, dimensionality reduction, and density-based clustering to identify recurring patterns among the extracted construct labels.

The baseline analysis identifies eight non-outlier topic groups, with 175 labels assigned to clusters and 13 classified as outliers.

The five-run sensitivity assessment examines the consistency of cluster assignments under different analytical configurations.

Clustering stability and semantic separation provide information about the consistency of the computational grouping process. They do not independently establish the conceptual validity of the identified dimensions.

## 4. Reproducibility Considerations

The analytical notebooks use relative file paths to support execution outside the original Kaggle environment.

The original modeling procedures and saved analytical outputs have been preserved, apart from the adjustments required for file-path portability.

The notebooks have not been independently rerun from scratch in a completely fresh computational environment as part of preparing this repository.

Results may vary with different versions of Python, BERTopic, UMAP, HDBSCAN, PyTorch, and related libraries.

For exact computational reproduction, the software versions and relevant environment configurations used in the original analyses should be retained.

## 5. Data Organization and Transparency

The repository provides supporting materials for examining the principal stages of the research process:

- Academic literature identification and screening.
- Grey-literature screening and selection.
- Quality appraisal and inter-rater agreement.
- Construct-label extraction and semantic topic modeling.
- Five-run clustering sensitivity analysis.
- Computational verification of stability statistics.

The original datasets and analytical outputs are retained to support traceability. Any subsequent corrections or updates should be documented through the repository's version history.

## 6. Data Use and Limitations

The materials are provided for academic examination, methodological verification, and research reproducibility.

Users should consider the methodological assumptions, inclusion criteria, data characteristics, and computational environment when interpreting or reproducing the results.

The presence of a dataset or computational output does not, by itself, establish the conceptual or empirical validity of an assessment model.

All materials should be used in accordance with applicable data-use permissions and intellectual property requirements.
