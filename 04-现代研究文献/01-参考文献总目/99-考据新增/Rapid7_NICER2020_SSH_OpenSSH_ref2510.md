# Rapid7 NICER 2020 — SSH 协议深读（OpenSSH 全网份额）

- **ref id**：2510
- **source_tier**：primary（独立全网扫描实测，与 Bitsight Groma 同级的原始测量数据）
- **format**：web
- **status**：verified
- **title**：NICER Protocol Deep Dive: Secure Shell (SSH) — National / Industry / Cloud Exposure Report (NICER) 2020
- **author**：Rapid7
- **year**：2020
- **publisher**：Rapid7
- **language**：en
- **source_url**：https://www.rapid7.com/blog/post/2020/08/28/nicer-protocol-deep-dive-secure-shell-ssh/
- **full_report_pdf**：https://www.rapid7.com/globalassets/_pdfs/research/nicer2020-full-report.pdf

## 核心数据（Sonar 全网扫描）

| Service Family | Count | Percentage |
|---|---|---|
| OpenSSH | 15,747,821 | 92.238% |
| Dropbear | 1,250,254 | 7.323% |
| SSH | 37,884 | 0.222% |
| WinSSHD | 10,408 | 0.061% |
| 其余（WeOnlyDo/iLO/VShell/libssh 等） | < 0.04% 各 | — |

- 扫描对象：全网可指纹识别的 SSH 服务（TCP/22），样本约 1,708 万。
- 结论：OpenSSH 在 2020 年占全网 SSH 服务 **92.238%**（远高于 Bitsight 2024 Q1 单窗口扫描的约 70%）。

## 考据用途（doubt 1688）

用于校准 OpenSSH 全球部署份额的口径差异：不同扫描（Rapid7 2020 全量 IPv4 / Bitsight 2024 单窗口 / TUM 2014 抽样）得出的 OpenSSH 占 SSH 服务比例在 **65%–92%** 区间波动，正文不应将任一单源比例误读为通用市占率。

## 入库说明

- 考据对象入库规则（考据规则 L180）：经联网核验的一手扫描数据须入 `references_fulltext.db`。
- 与 ref2498（Bitsight Groma 2026 持续扫描）互为独立测量交叉印证。
