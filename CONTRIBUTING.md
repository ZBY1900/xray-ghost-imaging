# Contributing

## 收录标准

一条记录要进 `data/papers.yaml`，必须同时满足：

1. **有稳定标识符**：DOI 或 arXiv id，二选一
2. **与 X 射线鬼成像直接相关**：只做可见光的不要
3. **至少一个受控词表标签**（`source` 必填）
4. **有 `key_claim`**：一句话说清这篇做了什么，不能只抄标题

`verified` 字段由维护者填。**未核实的条目欢迎，无出处的条目不收。**

## 提交流程

1. 开 issue（选 `new-entry` 模板）——先讨论再写代码
2. Fork → 改 `data/papers.yaml` → 本地跑 `python scripts/render.py`
3. 把 `README.md`、`bib/xgi.bib`、`docs/` 的变更一并提交
4. PR 描述里贴一段「为什么这篇值得收」

## 改词表

`method` / `source` / `modality` / `detector` 的合法值定义在 `scripts/render.py`
的 `VOCAB` 字典里。**新增值必须单独开 PR 并说明为什么现有值不够用** ——
词表膨胀比缺值更致命。

## 代码贡献

- Python ≥ 3.9，只用 numpy / scipy / matplotlib / pyyaml
- 每个新算法必须配一个能跑的 notebook 和一个 `tests/`
- 不要提交论文 PDF