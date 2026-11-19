# The Enchan Field

**An Effective Field Framework for Geometric Stabilization and Non-Linear Relaxation**

This repository contains the LaTeX source code, figures, and compiled PDF for *The Enchan Field*. The `main` branch contains the **v1.0.5 (November 19, 2026) manuscript**; its GitHub Actions workflow compiles `main.tex` and synchronizes the resulting `main.pdf` to this repository. The previously published **v1.0.4** remains preserved in the frozen `zenodo_bundle/` and Zenodo archival record. GitHub v1.0.5 is not yet a new Zenodo publication.

## Abstract
The Enchan Field is proposed as an effective field framework for describing geometric stabilization across continuous and discrete systems. Its starting point is the possibility that gravity-like stabilization phenomena are not governed solely by material source terms, but also by the relaxation structure of geometry itself. In this view, coherent large-scale structures arise from a field medium whose response becomes non-linear when deformation, concentration, or interaction intensity exceeds a characteristic scale.

This paper introduces the Enchan Field as a geometric order field $S(x)$, formulates its effective relaxation equation, and interprets its non-linear screening response as finite field tension rather than as an externally imposed correction. The same stabilization principle is then translated into discrete graph dynamics, where high-degree hub nodes act as localized over-concentrations of interaction intensity.

## Related Resources
- **Public API & Implementation:** [Enchan Cosmic (Enchan-Web-OS)](https://github.com/EnchanTheory/Enchan-Web-OS)
- **Precursor Notes:** [Enchan Field Notes](https://github.com/EnchanTheory/Enchan-Field-Notes)

## v1.0.5 Revision

This revision corrects the Euler--Lagrange response normalization, distinguishes coefficient attenuation from flux/kinetic saturation, and makes explicit that screening alone does not prove asymptotic convergence. The abstract, introduction, and conclusion now preserve that claim boundary. It adds no new numerical results or changes to the existing astrophysical demonstration. See [`REVISION_v1.0.5.md`](./REVISION_v1.0.5.md) for the exact scope.

## Citation / DOI
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20121825.svg)](https://doi.org/10.5281/zenodo.20121825)

The citation below refers to the **published v1.0.4**, not to the GitHub v1.0.5 revision. No v1.0.5 Zenodo record or DOI has been issued by this commit. For the published version, cite the Zenodo record above.

## How to Cite

Kobayashi, M. (2026). *The Enchan Field: An Effective Field Framework for Geometric Stabilization and Non-Linear Relaxation* (v1.0.4). Zenodo. https://doi.org/10.5281/zenodo.20121825

### BibTeX

```bibtex
@misc{kobayashi2026enchanfield,
  author       = {Kobayashi, Mitsuhiro},
  title        = {The Enchan Field: An Effective Field Framework for Geometric Stabilization and Non-Linear Relaxation},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v1.0.4},
  doi          = {10.5281/zenodo.20121825},
  url          = {https://doi.org/10.5281/zenodo.20121825}
}
```