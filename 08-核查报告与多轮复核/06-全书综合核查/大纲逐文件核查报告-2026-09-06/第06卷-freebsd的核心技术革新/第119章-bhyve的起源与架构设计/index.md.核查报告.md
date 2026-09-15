# 核查报告：第06卷-freebsd的核心技术革新/第119章-bhyve的起源与架构设计/index.md

## 源文件
- 源文件：第06卷-freebsd的核心技术革新/第119章-bhyve的起源与架构设计/index.md
- 核查批次：C430
- 摘要行（第 7 行）：# 第119章 bhyve的起源与架构设计（第 1-5 行为 frontmatter）
- 检查方法：整文通读；核验章 index 五段、史观编号、辨析规范、消解回写残留、PODCAST_REVIEW 归属

## 概览
| 检查项 | 结果 |
| --- | --- |
| A 主题与小结自洽 | 通过——围绕 bhyve 起源与架构设计 |
| B 结构完整性 | 通过——要点/史观/辨析/文献五段齐全 |
| C 史观引据 | 存在问题——史观编号与诗意名错挂 5 处 |
| D 史料与实证 | 通过——作者归属纠正、10.0 发布修正、commit/tag 核验规范 |
| E 辨析一致 | 存在问题——dangan-20260908 消解回写块含"待核·needs_fix"残留 |
| F 文献与数据库引用 | 通过——DB_REF 区间合理，PODCAST_REVIEW 主题相关 |

## 问题清单
1. P3 | 五条史观段（第 19、21、23、25、27 行） | 史观编号与诗意名错挂：标"总纲第 2 条——实践先于理论"（2=历史是形式主义化的非存在）、"总纲第 24 条——许可证选择直接决定商业采用模式"（24=美是消解性的体验）、"总纲第 19 条——信息技术标准演进与硬件进步同步"（19=解释学循环）、"总纲第 3 条——形式主义膨胀的克制"（3=不存在进步只有权力再分配），均与权威 25 条名目不符 | 权威 25 条总纲名目 | 按权威名目统一编号与诗意名
2. P3 | 第 48-52 行 | dangan-20260908 消解回写块含"待核·needs_fix"残留——Fedora virtio-win/Pluribus Netvisor/Joyent illumos-bhyve 三条标注 DKC-2037/2040/2041→fulltext:6057/6059/6060，其"消解回写"标注与"待核·needs_fix"状态矛盾 | 0 信任原则/证据分级 | 明确核验状态或改待核标注

## 结论
- 结论：存在问题 2 项（P0 0、P1 0、P2 0、P3 2）

## 补充说明
- 正向样本：辨析规范突出——纠正"Peter Grehan 为唯一创始人"误传（commit log 与源码版权头交叉验证判 Neel Natu 为内核 vmm 模块主要初始作者）；纠正"BSD 许可证促进商业采用而 GPL 阻碍"的过度简化（KVM 随 Linux 主线获 AWS/Google/Azure 大规模采用，市场份额远超 bhyve，bhyve 未成规模生态根因非许可证）；纠正"2014.1 FreeBSD 11.0 发布 bhyve"事实错误（首次随 10.0-RELEASE 发布，经 release/10.0.0 tag 验证）；澄清 bhyve UEFI 固件与 Clover/OpenCore（Hackintosh 引导器）的区别。
- 正向样本：要点完整——bhyve 由 Neel Natu 在 NetApp 开发、内部名 BSD Hypervisor、2011 Perforce 分支开发、随 FreeBSD 10.0-RELEASE（2014-01-20）发布（SVN r245652），初始仅支持 Intel VT-x/EPT、Nehalem 及更新、64 位 FreeBSD/Linux 客户机，技术预览实验性。
- 正向样本：PODCAST_REVIEW（BSD Now 20）一手口述——Neel Natu/Peter Grehan 在 NetApp 受 KVM 先例启发、2010-11 MeetBSD 提出构想、bhyve 名称由 Joe Catterdon 命名、初期资源分区型后演进为通用实现，标注各类客户机落地时间须以 FreeBSD 官方发布记录交叉验证。
- 审阅痕迹：史观编号/诗意名、作者归属纠正、消解回写残留、10.0 发布修正逐一核验。