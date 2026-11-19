# ROADMAP

## v0.1 骨架 ✅
- [x] `data/papers.yaml` 文献库（29 条，带 arXiv id）
- [x] `scripts/render.py`：yaml → README + BibTeX + docs
- [x] 受控词表与校验
- [x] 中英术语表
- [ ] 补齐缺失 DOI（当前 20 条仅有 arXiv id）
- [ ] 给仓库加 topics
- [ ] 在个人主页 pin

## v0.2 能跑（目标：陌生人 5 分钟出图）
- [ ] `code/00_simulate/speckle.py`：赝热光/单束团散斑生成
- [ ] `code/00_simulate/masks.py`：Hadamard / 随机二值 / 正弦 / 编码盘
- [ ] `code/00_simulate/forward.py`：桶信号正向模型
- [ ] `code/00_simulate/attenuation.py`：μ/ρ 查表（NIST XCOM 精简版）
- [ ] `code/10_reconstruct/correlation.py`：DGI / NGI
- [ ] `notebooks/01_quickstart.ipynb`
- [ ] `tests/`：正向-反向可逆性测试

## v0.5 有对比
- [ ] `masks.py` 加 Huffman 序列
- [ ] `code/10_reconstruct/hadamard.py`（快速 WHT）
- [ ] `code/10_reconstruct/fsi.py`
- [ ] `notebooks/02_patterns.ipynb`：同采样率下 Hadamard vs 随机 vs 正弦
- [ ] `notebooks/03_dose_budget.ipynb`：采样率 × 光子数 × 剂量三角
- [ ] `benchmarks/results.md` 第一版

## v1.0 有用
- [ ] `code/10_reconstruct/cs.py`（TV-ADMM）
- [ ] `code/10_reconstruct/dl/`
- [ ] `code/20_tomography/ghost_ct.py`（正弦图 + FBP）
- [ ] `notebooks/04_ghost_ct.ipynb`
- [ ] `datasets/phantom/` 自造衰减体模
- [ ] `.github/workflows/arxiv-watch.yml` 每日新论文 → issue
- [ ] 生成文档站（MkDocs）

## 明确不做
- 不做"大而全的 awesome list"：全量索引放 `docs/`，首页只留 9 篇
- 不收非 X 射线波段：方法参考放 `RELATED.md`
- 不托管论文 PDF：只放 DOI/arXiv 链接（版权）
- 不做 UI 前端：notebook 就是界面