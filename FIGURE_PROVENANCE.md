# Figure Provenance and Reproducibility Record

Status: Resolved under the strict Policy 310 (No Third-Party Bundling). Updated for v1.1 release (16 September 2026).

This document serves as the official reproducibility and provenance register for the benchmark figures presented in **The Enchan Field** manuscript.

## Figure 1: SNAP Web-Google Audit Snapshot

* **Target Figure:** Figure 1 (`figures/enchan_web_google_audit.png`)
* **Image SHA-256 Checksum:** `002529c4926244a4b714550023aa25b4c02d10e8a8d877bf7c9fab9f1ae1be10`
* **Provenance:** This figure represents an audit snapshot generated from a local benchmark run of the Enchan(cosmic) Edge-Stream solver on the legally obtained SNAP Web-Google dataset. The run metrics shown in the plot (875,713 active nodes, 5,105,039 edges, a best-found cut of 3,677,724, and +44.08% improvement against the random baseline) are exact empirical artifacts and reflect the solver's computational stability on large-scale discrete topologies.

## Figure 2: 10,000-spin Ising/Max-Cut Comparison

* **Target Figure:** Figure 2 (`figures/enchan_ising_tabu_comparison.png`)
* **Image SHA-256 Checksum:** `a0f6226b03a7bb5add9cad4fd47ec2dc13728d3094dc6f41e54b15bbd0c72b19`
* **Provenance:** This figure represents a comparative audit snapshot compiled from a local parallel comparison run on a 10,000-spin Ising Max-Cut instance using our multithreaded Tabu Search baseline reference. The run reports the wall-clock timings, energy states, and the deterministic solution hash for the benchmark instance on our classical hardware. No third-party solver or baseline code is bundled in this repository, ensuring complete independence under Policy 310.
