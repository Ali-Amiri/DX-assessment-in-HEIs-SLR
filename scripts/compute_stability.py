#!/usr/bin/env python3
"""Reproduce manuscript stability ARI matrix from five exported topic assignment CSVs.
Run from repository root: python scripts/compute_stability.py
Requires: scikit-learn
"""
from pathlib import Path
import csv
from itertools import combinations
from statistics import mean, stdev
from sklearn.metrics import adjusted_rand_score

root = Path(__file__).resolve().parents[1]
runs = [
    "run_01_baseline", "run_02_seed21", "run_03_seed123",
    "run_04_umap_neighbors10", "run_05_hdbscan_cluster8"
]
records = []
for run in runs:
    filepath = root / "results" / run / "topic_assignments_baseline.csv"
    with filepath.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    keys = [(int(row["row_index"]), row["construct_label"]) for row in rows]
    topics = [int(row["topic_id"]) for row in rows]
    records.append((keys, topics))

if any(keys != records[0][0] for keys, _ in records[1:]):
    raise ValueError("Assignment rows are not aligned across the five runs")

pairwise = []
print("Pairwise Adjusted Rand Index (includes topic -1 outliers):")
for i, j in combinations(range(5), 2):
    score = adjusted_rand_score(records[i][1], records[j][1])
    pairwise.append(score)
    print(f"Run {i + 1} vs Run {j + 1}: {score:.6f}")

print(f"\nMean: {mean(pairwise):.6f}")
print(f"Minimum: {min(pairwise):.6f}")
print(f"Maximum: {max(pairwise):.6f}")
print(f"Sample SD: {stdev(pairwise):.6f}")
