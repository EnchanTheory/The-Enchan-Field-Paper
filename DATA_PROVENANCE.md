# Data Provenance and Reproducibility Record

Status: Resolved under the strict Policy 310 (No Third-Party Bundling). Updated for v1.0.4 release (16 September 2026).

This document registers the official data provenance, retrieval instructions, and exact cryptographic checksums for the real-world benchmarks presented in **The Enchan Field** manuscript.

## Real-World Dataset: SNAP Web-Google

The real-world web graph benchmark presented in Section 7 (Figure 3) is based on the official Stanford Large Network Dataset Collection (SNAP):

* **Official Source Link:** https://snap.stanford.edu/data/web-Google.html
* **Dataset Name:** `web-Google` (web-Google.txt.gz)
* **Metadata Profile:** 
  * Nodes: 875,713
  * Edges: 5,105,039
* **Primary Citation:** J. Leskovec, K. Lang, A. Dasgupta, and M. Mahoney. "Community Structure in Large Networks: Natural Cluster Sizes and the Absence of Large Well-Defined Clusters." *Internet Mathematics*, 6(1):29-123, 2009. (Cited in manuscript as `\cite{Leskovec2009}`).
* **Retrieval Date:** August 14, 2025 (Initial freeze / Enchan series benchmarking)
* **Expected Archive MD5 Checksum:** `f6f39d79b700075d4a27d77f3be5f437`
* **Expected Archive SHA-256 Checksum:** `bcac0af0471d749f4a8c010bca92b61cf2868a0570741de06892fc062f265ea6`

## Non-Bundling Compliance (Policy 310)

To ensure strict compliance with Policy 310 (No Third-Party Bundling), the raw `web-Google.txt.gz` graph data is **NOT** bundled inside this repository or the Zenodo release archive. 

Interested researchers must download the raw dataset directly from the official SNAP Stanford repository, decompress the file, verify the checksums, and place it in their local processing cache to execute the edge-stream optimization and verify the best-found cut ($3,677,724$) reported in the paper.
