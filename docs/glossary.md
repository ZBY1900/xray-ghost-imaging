# 术语中英对照 / Glossary

> 中文译名采用国内光学界通行说法；括号内为文献中出现的其它译法。
> 排序按概念簇，不按字母。

## 一、成像体制

| 中文 | English | 一句话 |
|---|---|---|
| 鬼成像（关联成像） | ghost imaging (GI) | 用两路关联测量，从桶信号里"算"出图像 |
| 经典鬼成像 | classical ghost imaging (CGI) | 用经典光/热光的强度关联实现，不依赖纠缠 |
| 计算鬼成像 | computational ghost imaging | 照明图案已知，只需一路桶探测器 |
| 单像素成像 | single-pixel imaging (SPI) | 计算鬼成像的同义/上位说法，无"鬼"的含义 |
| 鬼投影 | ghost projection | CGI 的逆向用法：用静态掩模平移"合成"任意图案 |
| 鬼层析 | ghost tomography | 鬼成像 + 旋转扫描 + 层析重建 |
| 傅里叶单像素成像 | Fourier single-pixel imaging (FSI) | 用正弦条纹作基，直接在频域采样 |
| 多像素鬼成像 | multipixel ghost imaging | 桶探测器换成少量像素，换取分辨率 |
| 相位敏感鬼成像 | phase-sensitive GI | 利用相位衬度而非吸收成像 |
| X 射线荧光鬼成像 | X-ray fluorescence GI (XRF-GI) | 桶信号取自荧光光子，做元素分布 |

## 二、信号与重建

| 中文 | English | 一句话 |
|---|---|---|
| 桶探测器 | bucket detector | 无空间分辨、只输出一个数的探测器 |
| 单像素探测器 | single-pixel detector | 同上；X 射线常用光电二极管/闪烁体+PMT |
| 散斑 | speckle | 空间上随机起伏的强度分布，是关联的来源 |
| 赝热光 | pseudothermal light | 用激光+旋转毛玻璃模拟热光统计 |
| 二阶关联函数 | second-order correlation function | ⟨I₁I₂⟩−⟨I₁⟩⟨I₂⟩，鬼成像的数学核心 |
| 桶信号 | bucket signal | 每个图案对应的一个标量测量值 |
| 照明图案 | illumination pattern / mask | 已知的空间强度分布 |
| 编码孔径 | coded aperture | 固定图案的透射掩模 |
| 编码盘 | coding disk | 旋转的图案盘，用于高速序列成像 |
| 空间光调制器 | spatial light modulator (SLM) | 光波段可编程图案器件；硬 X 射线难以实现 |
| 差分鬼成像 | differential ghost imaging (DGI) | 减去背景项，显著提高信噪比 |
| 归一化鬼成像 | normalized ghost imaging (NGI) | 对桶信号归一化，抗光源涨落 |
| 压缩感知 | compressive sensing (CS) | 欠采样 + 稀疏先验重建 |
| 哈达玛图案 | Hadamard pattern | ±1 正交基，可用快速变换 O(N log N) 重建 |
| 采样率 | sampling ratio | 测量数 / 像素数 |
| 峰值信噪比 / 结构相似度 | PSNR / SSIM | 重建质量的两种标准度量 |

## 三、X 射线物理

| 中文 | English | 一句话 |
|---|---|---|
| 同步辐射 | synchrotron radiation | 高亮度、可调谐、准单色的 X 射线源 |
| 波荡器 | undulator | 同步辐射中产生准单色高亮度光束的插入件 |
| 弯铁 | bending magnet | 另一种同步辐射光源，谱更宽 |
| 自由电子激光 | X-ray free-electron laser (XFEL) | 单脉冲极强、脉冲间涨落大（正适合鬼成像） |
| 单束团 | isolated electron bunch | 分离的电子束团，其时域散斑可被相机分辨 |
| 填充模式 | fill pattern | 储存环中束团的填充时序 |
| 劳厄几何 | Laue (transmission) geometry | 晶体透射衍射，用于把一束 X 射线分成两束相干拷贝 |
| 衰减系数 | linear attenuation coefficient (μ) | 决定透射强度的核心量 |
| 光电吸收 | photoelectric absorption | 低能区主导的相互作用 |
| 康普顿散射 | Compton scattering | 高能区主导；XGI 中既是噪声也可作信号 |
| X 射线荧光 | X-ray fluorescence (XRF) | 元素特征谱线，用于元素映射 |
| 相位衬度 | phase contrast | 利用折射率实部而非虚部成像 |
| 传播相位衬度 | propagation-based phase contrast | 靠传播距离把相位转成强度 |
| 闪烁体 | scintillator | 把 X 射线转成可见光的间接探测介质 |
| 像元尺寸 | pixel pitch | 传统 X 射线成像的分辨率上限来源 |
| 视场 | field of view (FOV) | 单次成像覆盖范围 |

## 四、剂量与评价

| 中文 | English | 一句话 |
|---|---|---|
| 剂量 | radiation dose | XGI 的主要卖点；单位 Gy |
| 剂量分次 | dose fractionation | 把总剂量分摊到多次测量 |
| 复用测量 | multiplexing | 一次测量同时编码多个自由度 |
| 调制传递函数 | modulation transfer function (MTF) | 分辨率的频域刻画 |
| 光子计数 | photon counting | 单光子量级的探测模式 |
| 桌面源 | table-top / laboratory source | 微焦斑 X 射线管，成本低、亮度低 |