#!/usr/bin/env python3
"""Render README tables, BibTeX and docs pages from data/papers.yaml.

Usage:  python scripts/render.py [--check]
        --check : 只校验并报告缺失 DOI，不写文件
"""
from __future__ import annotations

import sys

try:  # Windows 控制台默认 GBK，强制 UTF-8 输出（否则 ✓/→ 会报 UnicodeEncodeError）
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "data" / "papers.yaml"
README = ROOT / "README.md"
BIB = ROOT / "bib" / "xgi.bib"
DOCS = ROOT / "docs"

# --- 受控词表：改这里就是改规范 -------------------------------
VOCAB = {
    "source": {"synchrotron", "lab", "xfel", "theory"},
    "modality": {"absorption", "phase", "fluorescence", "scattering"},
    "detector": {"bucket", "multipixel", "ccd"},
    "method": {
        "correlation", "computational", "fourier", "hadamard", "compressive",
        "deep-learning", "multipixel", "ghost-projection", "ghost-tomography",
        "phase-contrast", "fluorescence", "scattered",
    },
}
GROUPS = {
    "latrobe": "La Trobe / Melbourne (Paganin, Pelliccia, Kingston, Ceddia)",
    "barilan": "Bar-Ilan / Israel (Ben-Yehuda, Klein, Sefi, Shukrun)",
    "cas": "IOP-CAS / SJTU (Wu, Zhang, He, Li, Zeng)",
    "other": "Other groups",
}

# 首页只放这些；顺序即展示顺序
MUST_READ = [
    "pelliccia2016experimental",
    "zhang2017tabletop",
    "kingston2021dose",
    "lane2019advantages",
    "olbinado2021phase",
    "ceddia2023universalmask",
    "sefi2024multipixel",
    "manni2025noise2ghost",
    "tian2025review",
]


def load() -> list[dict]:
    with PAPERS.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def validate(papers: list[dict]) -> list[str]:
    problems, seen = [], set()
    for p in papers:
        pid = p.get("id", "<no id>")
        if pid in seen:
            problems.append(f"{pid}: duplicate id")
        seen.add(pid)
        for key in ("id", "title", "authors", "year", "venue"):
            if not p.get(key):
                problems.append(f"{pid}: missing required field {key}")
        for field in ("source", "method"):
            for v in p.get(field) or []:
                if v not in VOCAB[field]:
                    problems.append(f"{pid}: {field} value '{v}' not in vocabulary")
        for field in ("modality", "detector"):
            v = p.get(field)
            if v and v not in VOCAB[field]:
                problems.append(f"{pid}: {field} value '{v}' not in vocabulary")
        if p.get("group") and p["group"] not in GROUPS:
            problems.append(f"{pid}: unknown group '{p['group']}'")
        if not p.get("doi") and not p.get("arxiv"):
            problems.append(f"{pid}: has neither doi nor arxiv id")
    return problems


def link(p: dict) -> str:
    if p.get("doi"):
        return f"https://doi.org/{p['doi']}"
    return f"https://arxiv.org/abs/{p['arxiv']}"


def md_link(p: dict) -> str:
    return f"[{p['title']}]({link(p)})"


def table(papers: list[dict], with_claim: bool = False) -> str:
    head = "| Year | Paper | Venue | Source | Method |"
    rule = "|---|---|---|---|---|"
    if with_claim:
        head += " What it shows |"
        rule += "---|"
    rows = [head, rule]
    for p in sorted(papers, key=lambda x: (-x["year"], x["id"])):
        src = "/".join(p.get("source") or [])
        mth = ", ".join(p.get("method") or []) or "—"
        row = f"| {p['year']} | {md_link(p)} | {p['venue']} | {src} | {mth} |"
        if with_claim:
            row += f" {p.get('key_claim', '')} |"
        rows.append(row)
    return "\n".join(rows)


def bibtex(papers: list[dict]) -> str:
    out = []
    for p in sorted(papers, key=lambda x: x["id"]):
        first = p["authors"].split(",")[0].strip()
        kind = "article" if p.get("doi") else "misc"
        fields = [
            ("title", p["title"]),
            ("author", p["authors"]),
            ("year", str(p["year"])),
            ("journal", p["venue"]),
        ]
        if p.get("doi"):
            fields += [("doi", p["doi"])]
        if p.get("arxiv"):
            fields += [("eprint", p["arxiv"]), ("archivePrefix", "arXiv")]
        body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields if v)
        out.append(f"@{kind}{{{first}{p['year']}{p['id'].split(str(p['year']))[-1]},\n{body}\n}}")
    return "\n\n".join(out) + "\n"


def write_generated(papers: list[dict]) -> None:
    README.write_text(render_readme(papers), encoding="utf-8")
    BIB.parent.mkdir(exist_ok=True)
    BIB.write_text(bibtex(papers), encoding="utf-8")
    DOCS.mkdir(exist_ok=True)
    DOCS.joinpath("by-method.md").write_text(render_by_method(papers), encoding="utf-8")
    DOCS.joinpath("timeline.md").write_text(render_timeline(papers), encoding="utf-8")
    print(f"rendered {len(papers)} papers -> README.md, bib/xgi.bib, docs/")


def render_readme(papers: list[dict]) -> str:
    by_id = {p["id"]: p for p in papers}
    core = [by_id[i] for i in MUST_READ if i in by_id]
    return f"""# X-ray Ghost Imaging

> A method map, a paper index and runnable reference implementations for **X-ray ghost
> imaging (XGI)** — imaging with penetrating radiation where a single bucket detector
> replaces a pixelated camera.

![papers](https://img.shields.io/badge/papers-{len(papers)}-blue) ![status](https://img.shields.io/badge/status-v0.1-orange)

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

{table(core, with_claim=True)}

Full index: {len(papers)} entries in [`data/papers.yaml`](data/papers.yaml) ·
[by method](docs/by-method.md) · [timeline](docs/timeline.md) · [BibTeX](bib/xgi.bib)

## 4. Landscape — four groups, four routes

| Group | Route | Representative |
|---|---|---|
| {GROUPS['latrobe']} | theory-heavy; synchrotron, phase contrast, ghost projection | Pelliccia PRL 2016 |
| {GROUPS['barilan']} | experiment-heavy; lab source, multipixel, fluorescence, Monte Carlo | Sefi 2024 |
| {GROUPS['cas']} | table-top, ultra-low dose, coding disk, deep learning | Zhang 2017 |
| {GROUPS['other']} | foundational theory and cross-wavelength context | Lane & Ratner 2019 |

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
@misc{{zby1900_xgi,
  title  = {{X-ray Ghost Imaging: method map and reference implementations}},
  author = {{ZBY1900 and contributors}},
  year   = {{2026}},
  url    = {{https://github.com/ZBY1900/xray-ghost-imaging}}
}}
```

## 9. License

Docs and data: CC0-1.0 · Code: MIT. Paper metadata is factual; **no PDFs are hosted here**.
"""


def render_by_method(papers: list[dict]) -> str:
    parts = ["# Papers by method\n"]
    for tag in sorted(VOCAB["method"]):
        sel = [p for p in papers if tag in (p.get("method") or [])]
        if sel:
            parts.append(f"## `{tag}` ({len(sel)})\n\n{table(sel)}\n")
    return "\n".join(parts)


def render_timeline(papers: list[dict]) -> str:
    parts = ["# Timeline\n"]
    for year in sorted({p["year"] for p in papers}, reverse=True):
        parts.append(f"## {year}\n")
        for p in sorted(papers, key=lambda x: x["id"]):
            if p["year"] == year:
                parts.append(f"- {md_link(p)} — *{p['venue']}*")
        parts.append("")
    return "\n".join(parts)


def main() -> int:
    papers = load()
    problems = validate(papers)
    missing_doi = [p["id"] for p in papers if not p.get("doi")]
    if problems:
        print("VALIDATION PROBLEMS:")
        for line in problems:
            print("  ✗", line)
    else:
        print(f"✓ {len(papers)} papers validated against vocabulary")
    if missing_doi:
        print(f"· {len(missing_doi)} entries without DOI (arxiv-only): {', '.join(missing_doi)}")
    if "--check" in sys.argv:
        return 1 if problems else 0
    write_generated(papers)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
