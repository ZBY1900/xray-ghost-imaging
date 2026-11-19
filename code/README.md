# Reference code

Numbered by execution order, not by topic.

| Dir | What | Depends on |
|---|---|---|
| `00_simulate/` | Synthesise speckle, masks, phantom, forward model | numpy only |
| `10_reconstruct/` | Recover an image from bucket signals | `00_simulate` output |
| `20_tomography/` | Rotate + reconstruct (ghost CT) | `10_reconstruct` |

**Rule:** everything here must run on synthetic data with no downloads.
If a module needs experimental data, it belongs in `benchmarks/`, not here.
