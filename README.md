# X-ray Ghost Imaging

> A method map, a paper index and runnable reference implementations for **X-ray ghost
> imaging (XGI)** — imaging with penetrating radiation where a single bucket detector
> replaces a pixelated camera.

![papers](https://img.shields.io/badge/papers-29-blue) ![status](https://img.shields.io/badge/status-v0.1-orange)

**XGI in one paragraph.** A spatially unresolved detector records the total transmitted
intensity for each of many known illumination patterns. Because the patterns are known, the
object can be recovered from many thousands of scalars — no optics, no lens, no 2D detector.
In the hard-X-ray regime the payoff is dose, speed and resolution: single-photon-order dose,
100 kHz frame rates, and resolution no longer capped by the pixel pitch of a scintillator.

**Chinese glossary:** 术语中英对照见 [`docs/glossary.md`](docs/glossary.md)。

## 1. Quick start

```bash
git clone https://github.com/ZBY1900/xray-ghost-imaging
cd xray-ghost-imaging
pip install -r scripts/requirements.txt
python scripts/render.py          # regenerate README tables from data/papers.yaml
```

Reference code is under construction — see [ROADMAP](ROADMAP.md).

## 2. Why it matters

| Claim | Number | Where |
|---|---|---|
| Radiation dose | single-photon order on a table-top source | Zhang 2017 |
| Frame rate | 100 kHz, no read-out dead time | Sefi 2020 |
| Resolution gain | 25x over commercial CT | Sefi 2024 |
| Dose reduction | provable only under specific conditions | Kingston 2021 |

## 3. Must-read (9 papers)

| Year | Paper | Venue | Source | Method | What it shows |
|---|---|---|---|---|---|
| 2025 | [Noise2Ghost: Self-supervised deep convolutional reconstruction for ghost imaging](https://arxiv.org/abs/2504.10288) | arXiv preprint | theory | deep-learning, correlation | Self-supervised denoising for low-count GI; no clean reference needed. |
| 2025 | [Multi-wavelength ghost imaging: a review](https://doi.org/10.1007/s44336-025-00013-0) | Vicinagearth 2, 4 | theory | correlation, computational | Survey from XUV to THz and matter waves; best single entry point to the wider field. |
| 2024 | [25-Fold Resolution Enhancement of X-ray Microscopy Using Multipixel Ghost Imaging](https://arxiv.org/abs/2402.14023) | arXiv preprint | lab | multipixel, computational | Multipixel GI with hard X-rays gives 25x resolution gain over commercial CT. |
| 2023 | [Universal mask for hard X rays](https://doi.org/10.1364/OPTICA.490006) | Optica 10, 1067-1073 | synchrotron | ghost-projection | Ghost projection: reversed GI with a translated static mask; experimental proof with hard X-rays. |
| 2021 | [On the Inherent Dose-Reduction Potential of Classical Ghost Imaging](https://doi.org/10.1103/PhysRevA.103.033503) | Phys. Rev. A 103, 033503 | theory | correlation | Foundational dose analysis: when CGI genuinely reduces dose and when it does not. |
| 2021 | [Phase-sensitive x-ray ghost imaging](https://doi.org/10.1364/OPTICA.437481) | Optica 8, 1538-1544 | synchrotron | correlation, phase-contrast | Extends XGI to propagation-based phase contrast; low dose at high energy. |
| 2019 | [What are the advantages of ghost imaging? Multiplexing for x-ray and electron imaging](https://doi.org/10.1364/OE.379503) | Opt. Express | theory | correlation, hadamard | Multiplexing framework for error/dose; the reference text on when GI wins. |
| 2017 | [Table-top X-ray Ghost Imaging with Ultra-Low Radiation](https://arxiv.org/abs/1709.01016) | arXiv preprint | lab | computational | Lab microfocus source, single-photon-order radiation dose; images plane and natural objects. |
| 2016 | [Experimental x-ray ghost imaging](https://doi.org/10.1103/PhysRevLett.117.113902) | Phys. Rev. Lett. 117, 113902 | synchrotron | correlation | First experimental proof of hard X-ray ghost imaging; Laue-split beam + isolated-bunch speckle. |

Full index: 29 entries in [`data/papers.yaml`](data/papers.yaml) ·
[by method](docs/by-method.md) · [timeline](docs/timeline.md) · [BibTeX](bib/xgi.bib)

## 4. Landscape — four groups, four routes

| Group | Route | Representative |
|---|---|---|
| La Trobe / Melbourne (Paganin, Pelliccia, Kingston, Ceddia) | theory-heavy; synchrotron, phase contrast, ghost projection | Pelliccia PRL 2016 |
| Bar-Ilan / Israel (Ben-Yehuda, Klein, Sefi, Shukrun) | experiment-heavy; lab source, multipixel, fluorescence, Monte Carlo | Sefi 2024 |
| IOP-CAS / SJTU (Wu, Zhang, He, Li, Zeng) | table-top, ultra-low dose, coding disk, deep learning | Zhang 2017 |
| Other groups | foundational theory and cross-wavelength context | Lane & Ratner 2019 |

## 5. Taxonomy

Three independent axes. A paper can sit in several cells.

- **source** — `synchrotron` · `lab` · `xfel` · `theory`
- **modality** — `absorption` · `phase` · `fluorescence` · `scattering`
- **method** — `correlation` · `computational` · `fourier` · `hadamard` · `compressive` ·
  `deep-learning` · `multipixel` · `ghost-projection` · `ghost-tomography` ·
  `phase-contrast` · `fluorescence` · `scattered`

## 6. Related work outside X-rays

Method reference only, deliberately **not indexed here** — see [RELATED.md](RELATED.md).

## 7. Contributing

Open an issue using the templates in `.github/ISSUE_TEMPLATE/`. Every entry needs a DOI or
arXiv id and at least one controlled-vocabulary tag. Entries are merged once a maintainer has
set `verified` — **unverified entries are welcome, unsourced entries are not**.

## 8. Citation

```bibtex
@misc{zby1900_xgi,
  title  = {X-ray Ghost Imaging: method map and reference implementations},
  author = {ZBY1900 and contributors},
  year   = {2026},
  url    = {https://github.com/ZBY1900/xray-ghost-imaging}
}
```

## 9. License

Docs and data: CC0-1.0 · Code: MIT. Paper metadata is factual; **no PDFs are hosted here**.
