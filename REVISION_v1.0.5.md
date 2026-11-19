# v1.0.5 — Mathematical clarification (source revision)

Date: 2026-11-19

This is a **GitHub manuscript and compiled-PDF revision**. GitHub Actions compiles `main.tex`, synchronizes `main.pdf`, and builds the version-matched PDF and source ZIP in `zenodo_bundle/` for manual Zenodo file updates. The original Zenodo v1.0.4 record and Git history remain preserved. Updating the published Zenodo v1.0.5 record itself is a separate operation.

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
- The existing published v1.0.4 DOI and Git history. The distribution files in `zenodo_bundle/` are updated to match v1.0.5; the earlier Zenodo record itself is not changed.
- Other published papers, canonical research maps, and historical audit decisions.

The paper continues to claim a **three-layer effective proposal** (continuous field, computational analogue, implementation), not an exact continuous-to-graph derivation or a global convergence theorem.
