# B 类存疑联网核验报告（2026-08-04）

> 核验方式：WebSearch + WebFetch（官方一手源优先）
> 核验日期：2026-08-04 14:45

## 一、核验通过（大纲表述正确，可 resolved）9 项

| 存疑 id | 大纲主张 | 一手/权威来源 | 结论 |
|---------|---------|--------------|------|
| 1744 | FreeBSD Foundation 商标条款最新版 2025-05-13 | freebsdfoundation.org/legal/trademark-usage-terms-and-conditions/ 页面明确 "Updated May 13, 2025" | **完全一致** |
| 1748 | 2004-06 IEEE/Open Group 授权 FreeBSD 使用 1400 余个 POSIX 接口 | The Open Group 官网新闻稿（opengroup.org/comm/press/01jun04.htm，2004-06-01）原文："permissions for reuse of material covering **over 1400 interfaces**" | **完全一致**（日期 06-01 亦核实） |
| 1750 | Common Criteria v3.1 R5 发布日期 2017-04 | 多份 CC 官方评估报告引用 "Version 3.1 Revision 5, April 2017, CCMB-2017-04-001" | **完全一致** |
| 1752 | GDPR 生效日 2018-05-25 | 前轮已多源交叉确认（EUR-Lex 正文 JS 无法直核不阻碍结论） | 生效日确认 |
| 1753 | CCPA 签署日期 2018-06-28 | NatLawReview/Ice Miller/InsidePrivacy 多源一致 "June 28, 2018, Gov. Jerry Brown signed" | **完全一致** |
| 1755 | DPDPA Act No. 22 of 2023，通过日 2023-08-11 | indiacode.nic.in 官方 PDF（一手）："ACT NO. 22 OF 2023 [11th August, 2023]" | **完全一致** |
| 1756 | LGPD art65 2020-09-18 生效、2021-08-01 制裁生效 | Demarest/Kincaid/cfmv.gov.br 多源一致 | **完全一致** |
| 1757 | PIPEDA 生效日 2001-01-01、S.C. 2000, c. 5 | laws.justice.gc.ca 官方（一手）：Assented 2000-04-13，Part 1 in force 2001-01-01 | **完全一致** |
| 1861 | OpenBSD 首次 hackathon 1999-06 Calgary | openbsd.org/hackathons.html 官网一手："In June of 1999, OpenBSD held the first hackathon... a house in Calgary" | **完全一致** |

## 二、需订正大纲（5 项）

| 存疑 id | 大纲现状 | 核验结果 | 订正建议 |
|---------|---------|---------|---------|
| 1751 | "ISO/IEC/IEEE 9945:2017(POSIX.1-2017)" | POSIX.1-2017 的 ISO 正式编号为 **ISO/IEC/IEEE 9945:2009**（+Cor 1:2012 + Cor 2:2017，Cor 2 于 2017-03 发布）；ISO 官网无 "9945:2017" 编号（新版本为 9945:2026） | 改为"ISO/IEC/IEEE 9945:2009（Cor 2:2017）对应 IEEE Std 1003.1-2017" |
| 1754 | CPRA 实施细则最终强制执行日 2024-03-29 | 2024-03-29 系 Sacramento Superior Court 判决（2023-06-30）的日期，但 **2024-02-09 加州上诉法院（Cal. Priv. Protection Agency v. Sup. Ct. of Sac. Cty., C099130）已推翻**，CPRA 法规实际立即生效 | 订正为"2024-02-09 上诉法院裁定生效（原 2024-03-29 中止令被推翻）" |
| 1762 | FreeBSD® 商标 USPTO 注册号 1916233 | **USPTO TSDR 实证：1916233 = "ICEFIELDS"（ISIS Imaging Corp，1995-09-05 注册，2006 已取消）**；FREEBSD 正确注册号 = **1955727**（serial 74546171，1994-07-06 申请，1996-02-13 注册，2016-04-04 续展有效，Live） | 注册号改为 1955727 |
| 1763 | FreeBSD Foundation "2000.3.19 提交 Articles of Incorporation" | 多个官方来源仅证明 March 2000 注册、Justin Gibbs 为 incorporator；具体 3 月 19 日未获一手确认（Colorado SOS 数据库未检索到日期级记录） | 按存疑建议标注"约 2000 年 3 月"（或加存疑脚注） |
| 1691 | Linus Torvalds 2001 年发言 | **实证：Linus "masturbating monkeys"/"security circus" 发言系 2008-07-15 gmane.linux.kernel 帖**（ZDNet 2008-07/Linux Journal 2008-08/CSO Online 多源印证） | 年份 2001 → **2008**（并补 ZDNet 转述 URL） |

## 三、保持登记（2 项，超出联网核验能力）

| 存疑 id | 内容 | 处置 |
|---------|------|------|
| 1770 | 银河麒麟早期版本与 FreeBSD 代码承袭比例/合规判定 | 保留 [存疑脚注]，须公开源码与许可证文本逐文件比对（正文阶段执行） |
| 1881 | Netflix Open Connect 单服务器 800 Gbps | 保留 [存疑脚注]，性能宣称无独立复核基准，随硬件而异 |

## 四、方法学备注

- 法规日期类以政府官方域名（laws.justice.gc.ca / indiacode.nic.in / planalto / eur-lex）为一手，律所简报为交叉印证
- USPTO TSDR 动态检索通过 tsdr.uspto.gov/statusview/rnXXXX 直接查询（实证注册号对应关系）
- 1754 是本次核验最重要的发现：大纲引用了已被上诉法院推翻的一审判决日期
