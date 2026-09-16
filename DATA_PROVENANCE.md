# Data Provenance and Reproducibility Record

Status: Resolved under the strict Policy 310 (No Third-Party Bundling). Updated for v1.1 release (16 September 2026).

This document registers the official data provenance and retrieval instructions for the real-world benchmarks presented in the accompanying report on **The Enchan Field**.

## Real-World Dataset: SNAP Web-Google

The real-world web graph benchmark presented in Section 7 (Figure 1) is based on the official Stanford Large Network Dataset Collection (SNAP):

* **Official Source Link:** https://snap.stanford.edu/data/web-Google.html
* **Dataset Name:** `web-Google` (web-Google.txt.gz)
* **Metadata Profile:** 
  * Nodes: 875,713
  * Edges: 5,105,039
* **Primary Citation:** J. Leskovec, L. Backstrom, R. Lada, and J. Kleinberg. "Community Structure in Large Networks: Natural Cluster Sizes and the Absence of Large Well-Defined Clusters." *Internet Mathematics*, 6(1):29-123, 2009. (Cited in manuscript as `\cite{Leskovec2009}`).

## Non-Bundling Compliance (Policy 310)

To ensure strict compliance with Policy 310 (No Third-Party Bundling), the raw `web-Google.txt.gz` graph data is **NOT** bundled inside this repository or the Zenodo release archive. 

Interested researchers must download the raw dataset directly from the official SNAP Stanford repository, decompress the file, and place it in their local processing cache to execute the edge-stream optimization and verify the best-found cut ($3,677,724$) reported in the paper.
