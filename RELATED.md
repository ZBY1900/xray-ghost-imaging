# Related work outside X-rays

**Why this file exists.** XGI borrowed almost everything from optical ghost imaging:
correlation reconstruction, Hadamard bases, compressive sensing, deep-learning priors.
Those tools are mature in the optical regime and nearly absent in the X-ray one.
We therefore do *not* index them here, but we point to them as method references.

## Optical / visible single-pixel imaging

| Repo | Stars | What to steal |
|---|---|---|
| [`openspyrit/spyrit`](https://github.com/openspyrit/spyrit) | ~69 | Reconstruction framework: plug any forward model + any solver |
| [`cbasedlf/single_pixel_demo`](https://github.com/cbasedlf/single_pixel_demo) | ~38 | Minimal MATLAB+Python pair; clearest code to read first |
| [`zibangzhang/Fourier-single-pixel-imaging`](https://github.com/zibangzhang/Fourier-single-pixel-imaging) | ~76 | FSI: sinusoidal patterns, 4-step phase shifting |
| [`williamdelacruz/Single-Pixel-Imaging`](https://github.com/williamdelacruz/Single-Pixel-Imaging) | ~48 | Hadamard ordering and fast transform |
| [`nducros/SPIRIT`](https://github.com/nducros/SPIRIT) | ~41 | MATLAB toolbox; good for cross-checking our Python |

## Other probes

- **Electrons** — Lane & Ratner's multiplexing framework applies unchanged
- **Neutrons** — same correlation mathematics, much longer exposure
- **XUV / THz** — see the multi-wavelength review (Tian 2025)

## Reading order for a newcomer

1. Kingston 2021 (dose) — understand *why* before *how*
2. Lane & Ratner 2019 (multiplexing) — the general theory
3. Pelliccia 2016 (first experiment) — what the hardware looks like
4. `cbasedlf/single_pixel_demo` — run something today