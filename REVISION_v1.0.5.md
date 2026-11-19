# v1.0.5 — Mathematical clarification (source revision)

Date: 2026-11-19

This is a **GitHub manuscript and compiled-PDF revision**, not a new Zenodo publication or release. GitHub Actions compiles `main.tex` and synchronizes the resulting `main.pdf` onto `main`. The archived Zenodo v1.0.4 ZIP/PDF and frozen `zenodo_bundle/` remain unchanged.

## Scope of changes

1. **Variational normalization (§3):** Keep `X=(grad S)^2/a0^2` and normalize the response as `mu(X)=(2/a0^2) dK/dX`. This makes the printed Euler--Lagrange equation consistent with the stated Lagrangian and the weak-gradient precursor.
2. **Finite-tension language (§3–4):** Distinguish decreasing `mu(D)`, the transmitted magnitude `J(D)=abs(D)mu(D)`, and the kinetic function `K(X)`. The response example is illustrative and branch-local; no universal hard cap is inferred.
3. **Convergence scope (§3 and discussion):** Screening changes constitutive coupling but does not, on its own, prove boundedness, regularity, or asymptotic convergence. State the need for model-specific relaxation/boundary conditions.
4. **Large-graph evidence scope (§7):** Identify the original observations as reported runs, not a screening-only matched ablation. Preserve all numerical claims and figures unchanged.
5. **Version clarity:** Replace two historical manuscript references to “present v1.0.0” with version-independent wording.

6. **Cross-section claim consistency:** Qualify the abstract, introduction, finite-tension explanation, discussion, and conclusion so that no unconditional convergence, boundedness, or collapse-prevention claim remains.

## Intentionally unchanged

- Astrophysical logarithmic example and high-acceleration diagnostic.
- Benchmark scores, plots, implementation disclosures, and proprietary solver core.
- The frozen `zenodo_bundle/` and existing published v1.0.4 DOI. The repository `main.pdf` is updated to the current v1.0.5 manuscript.
- Other published papers, canonical research maps, and historical audit decisions.

The paper continues to claim a **three-layer effective proposal** (continuous field, computational analogue, implementation), not an exact continuous-to-graph derivation or a global convergence theorem.
