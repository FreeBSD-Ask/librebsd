# 189. Rust 参考驱动提案、峰会邀请机制披露与不可验证代码政策后果（ks p53）

> 来源：ksummit 独有 p53（50 封全读，2021-04 至 2026-08：Miguel Ojeda 于 Rust 合入主线近一年之际提出 Rust 参考驱动方案系统回应无重复驱动与无树内用户死结；Ted Ts'o 唯一完整披露 Maintainers Summit 邀请机制 Linus 名单脚本初筛程序委员会 5-1 打分与 30 人上限；Dave Chinner 以 buffer_head/iomap 实测数据叠加 EU 网络弹性法案压力论证不可验证代码将被迫删除的政策后果；Sasha Levin 指出 LLM 时代修复提交可被快速转成 exploit 且 security@k.o 与 vulns.git 实为公开漏洞库；Bugzilla 存废争论与 linus-next 流程各四封）
> 判定：39 CAND / 11 NV。主题分布：面板驱动现代化 2、Rust与GPIO竞态 1、UMN伪补丁争议 1、AI生成内容准则 1、文件系统维护危机 1、驱动probe失败语义 1、AI补丁审查分级 2、linus-next流程 3、AI标注与版权 2、安全披露流程之争 2、AI审查提示词方法 1、Bugzilla存废争论 2、C安全标注语法 1、HIGHMEM淘汰审计 1、Coverity任务资源 1、Link标签语义之争 2、kernel.org信任网改版 1、峰会邀请流程 1、LLM内核流程提案 1、LLM与贡献信任 1、THE REST列表迁移 1、维护者心理健康 1、疫情与峰会办会 1、public-inbox镜像工具 1、Bugzilla替代方案 2、Rust参考驱动提案 1、稳定版回归窗口 1、Rust与驱动开发模式 1、Rust构建环境痛点 1、Rust引用计数安全 1。

## 189.1 面板驱动现代化

- 【Linux社区】面板支持牵涉DDIC与玻璃厂商双重NDA，面板IC商无上游提交记录，高通以超通用驱动加复杂DT描述面板，举安卓vendor树为例。 `<!-- ROW_MINE: ksummit.messages.8246 -->`
- 【Linux社区】Packett指面板多模式切换需经DCS写配置寄存器，而现行API无法按模式定义prepare序列，其让prepare访问CRTC的补丁陷入空指针困境。 `<!-- ROW_MINE: ksummit.messages.8311 -->`

## 189.2 Rust与GPIO竞态

- 【Linux社区】Wedson为写Rust GPIO抽象读代码，指出gpiochip移除时“numbing”未同步，gpio_ioctl判空后下游lineinfo_get仍可能用空指针，存在UAF竞态。 `<!-- ROW_MINE: ksummit.messages.8248 -->`

## 189.3 UMN伪补丁争议

- 【Linux社区】Brauner比较“伪君子提交”与2003年uid=0木马提交，认为即便一条问题提交入树已令UMN研究伦理可疑，各子系统审查强度差异巨大。 `<!-- ROW_MINE: ksummit.messages.8250 -->`

## 189.4 AI生成内容准则

- 【Linux社区】Lorenzo反对弱化措辞，坚持全自动生成补丁须“接受额外审查”，提交者须能解释并捍卫每行代码，否则维护者可直接拒绝整个系列。 `<!-- ROW_MINE: ksummit.messages.8254 -->`

## 189.5 文件系统维护危机

- 【Linux社区】Chinner引buffer_head在Debian为104字节、iomap用摘要位图更可扩展，警告EU网络弹性法案与虚假CVE将迫使删除不可验证的旧文件系统。 `<!-- ROW_MINE: ksummit.messages.8256 -->`

## 189.6 驱动probe失败语义

- 【Linux社区】Shuah报告2005年起probe失败仍注册驱动并留sysfs接口，Laurent指probe失败未必是驱动之过，如何区分驱动bug与设备故障尚无方案。 `<!-- ROW_MINE: ksummit.messages.8263 -->`

## 189.7 AI补丁审查分级

- 【Linux社区】Arnaldo提议CI对补丁做测试、LLM与lint后加盖“合格章”并分类，让维护者早晨优先读“好补丁”，并盼perf构建与测试纳入自动化。 `<!-- ROW_MINE: ksummit.messages.8264 -->`
- 【Linux社区】Lunn介绍netdev CI强制跑checkpatch并公开失败，脏补丁直接拒审，长期促使提交者自跑工具；维护者也需运行工具，大子系统已自动化。 `<!-- ROW_MINE: ksummit.messages.8336 -->`

## 189.8 linus-next流程

- 【Linux社区】Bartosz告知Laurent其树可入linux-next，但媒体子系统cherry-pick其PR将致重复提交，Rothwell的机器人会自动发重复警告邮件。 `<!-- ROW_MINE: ksummit.messages.8267 -->`
- 【Linux社区】Jiri分享自身实践：维护for-N+1/topic与for-N/fixes分支并自动合并为for-next供Stephen拉取，不必另开紧急修复分支。 `<!-- ROW_MINE: ksummit.messages.8293 -->`
- 【Linux社区】Linus反对自动拦截越界改动：ABI变更必然波及全树、向每个维护者索要ack不现实，且误报会让人习惯性忽视真正该在意的警告。 `<!-- ROW_MINE: ksummit.messages.8321 -->`

## 189.9 AI标注与版权

- 【Linux社区】Mauro称AI出现前就常收到雷同补丁、通用算法本就高度相似，本地ollama可保隐私；Paul坚持AI问答非私密且版权法风险不容忽视。 `<!-- ROW_MINE: ksummit.messages.8270 -->`
- 【Linux社区】Bottomley类比signed-off-by源于SCO诉讼溯源，引美国版权局对生成式AI的立场，主张AI使用与否影响补丁版权状态，标签须留存。 `<!-- ROW_MINE: ksummit.messages.8307 -->`

## 189.10 安全披露流程之争

- 【Linux社区】Sasha指用LLM可从修复提交快速生成可用exploit，security@k.o修复公开加syzkaller面板与vulns.git CVE库实为庞大公开漏洞库。 `<!-- ROW_MINE: ksummit.messages.8272 -->`
- 【Linux社区】Jiri双帽表态：开发者角度看CVE处理是灾难；发行版角度看linux-distros仍是SUSE安全团队首轮筛出安全修复的关键渠道，不宜全弃。 `<!-- ROW_MINE: ksummit.messages.8322 -->`

## 189.11 AI审查提示词方法

- 【Linux社区】Mason用约300个带已知bug的Fixes补丁迭代Claude审查提示词：漏报就让AI改提示，误报则追问成因并增补假阳性指南。 `<!-- ROW_MINE: ksummit.messages.8273 -->`

## 189.12 Bugzilla存废争论

- 【Linux社区】Artem回应Linus怒斥，称从未指点他人工作方式，只求bugzilla允许CC愿意参与的开发者，并称曾借bugzilla解决严重bug。 `<!-- ROW_MINE: ksummit.messages.8274 -->`
- 【Linux社区】Geert晒十年仅收到3封bugzilla邮件且均低质，而邮件渠道修复的bug报告多出数个数量级，主张MAINTAINERS文件才是权威指引。 `<!-- ROW_MINE: ksummit.messages.8373 -->`

## 189.13 C安全标注语法

- 【Linux社区】Linus主张C的安全与不安全标注应像属性一样绑定具体代码块并随块作用域嵌套，反对_Pragma式safe on与off全局开关模型。 `<!-- ROW_MINE: ksummit.messages.8279 -->`

## 189.14 HIGHMEM淘汰审计

- 【Linux社区】Arnd逐平台核查kmap_high_get去留：ARMv7与多数ARMv6缓存不混叠可关，AST2500仅512MB，ARMv5 VIVT仍依赖，新型SAM9x7限256MB。 `<!-- ROW_MINE: ksummit.messages.8280 -->`

## 189.15 Coverity任务资源

- 【Linux社区】Gustavo指linux-next每周Coverity扫描项目可认领审计任务，并附其在Kernel Recipes 2017至2019修复Coverity议题的演讲稿与视频。 `<!-- ROW_MINE: ksummit.messages.8283 -->`

## 189.16 Link标签语义之争

- 【Linux社区】Geert指v6.18-rc1提交944df7a31452删除tip文档中patch.msgid.link的Link:指引，改用不可点击的Message-ID:标签，质疑其通用性。 `<!-- ROW_MINE: ksummit.messages.8286 -->`
- 【Linux社区】Desnoyers指Link:已成无所不装的万能袋，主张将补丁来源从URL域名隐含语义升为显式标签如Link-Origin或Origin，使语义人人可辨。 `<!-- ROW_MINE: ksummit.messages.8374 -->`

## 189.17 kernel.org信任网改版

- 【Linux社区】Bottomley批评kernel.org与OpenSSF的新信任网方案拖延公开，违背“尽早发布”开源规范，并称这削弱其在企业内推动开源倡导的立场。 `<!-- ROW_MINE: ksummit.messages.8287 -->`

## 189.18 峰会邀请流程

- 【Linux社区】Ted详述峰会邀请机制：Linus点名约10至12人、脚本筛年度活跃者、程序委员会按5至1打分取均值划线，30人上限难兼顾各方平衡。 `<!-- ROW_MINE: ksummit.messages.8291 -->`

## 189.19 LLM内核流程提案

- 【Linux社区】Lorenzo提议峰会确立AI提交基本规则与选择加入或退出机制，警告媒体一旦渲染“Linux接受AI补丁”将引发提交激增，并提按子系统红绿灯分级。 `<!-- ROW_MINE: ksummit.messages.8292 -->`

## 189.20 LLM与贡献信任

- 【Linux社区】Linus称开源最大问题是贡献信任：熟人或凭补丁本身取信，陌生人侵入式补丁默认难被接受，AI既是威胁也可经Sashiko类工具增信。 `<!-- ROW_MINE: ksummit.messages.8299 -->`

## 189.21 THE REST列表迁移

- 【Linux社区】Joe Perches自称THE REST条目的责任人之一，表态支持Konstantin提案，将F:*默认收件由LKML改为patches@lists.linux.dev。 `<!-- ROW_MINE: ksummit.messages.8308 -->`

## 189.22 维护者心理健康

- 【Linux社区】Pinchart指开发者群体缺乏处理心理问题的技能，社区规模足以引入专业帮助，定向培训亦比要求所有维护者修学位更现实。 `<!-- ROW_MINE: ksummit.messages.8330 -->`

## 189.23 疫情与峰会办会

- 【Linux社区】David反驳“接种即可线下办会”：德国许多人9月前难接种首针，峰会安排必须顾及当年无法出行的维护者，不能只满足已接种者。 `<!-- ROW_MINE: ksummit.messages.8343 -->`

## 189.24 public-inbox镜像工具

- 【Linux社区】Wong说明public-inbox-clone与public-inbox-fetch可镜像单个收件箱，开发中的2.0版可借grokmirror清单一次镜像多个inbox。 `<!-- ROW_MINE: ksummit.messages.8351 -->`

## 189.25 Bugzilla替代方案

- 【Linux社区】Konstantin提出git-bug加b4 bugs方案：邮件讨论可转为bug条目持续同步、cgit在线查看，新报告经LLM预筛垃圾与发行版内核后分流。 `<!-- ROW_MINE: ksummit.messages.8355 -->`
- 【Linux社区】Weinberger构想网页界面：输入源文件、模块名甚至Oops即可获得应发列表与报告内容、纯文本格式等建议，辅助新人正确上报。 `<!-- ROW_MINE: ksummit.messages.8361 -->`

## 189.26 Rust参考驱动提案

- 【Linux社区】Miguel提议“Rust参考驱动”：允许维护者选择加入，在树内为范式C驱动写等价Rust实现，以破“无重复驱动”与抽象无用户的死结并量化评估。 `<!-- ROW_MINE: ksummit.messages.8357 -->`

## 189.27 稳定版回归窗口

- 【Linux社区】Sasha说明上游会在合并窗口后继续维护旧内核数周，用户可在Y-1版本驻留，故新内核X.Y实际约有五周暴露期供用户发现回归。 `<!-- ROW_MINE: ksummit.messages.8362 -->`

## 189.28 Rust与驱动开发模式

- 【Linux社区】Leon称新驱动开发以复制粘贴为主流模式，C驱动基数远大于Rust故更易抄，Rust化将使“路过式”开发者更难产出可用驱动。 `<!-- ROW_MINE: ksummit.messages.8371 -->`

## 189.29 Rust构建环境痛点

- 【Linux社区】Behrens称其Nix开发壳PR已可用clang构建内核并跑kunit，呼应Jarkko“Rust难在运行环”、内核文档缺BuildRoot与Yocto指引的观点。 `<!-- ROW_MINE: ksummit.messages.8375 -->`

## 189.30 Rust引用计数安全

- 【Linux社区】Wedson向Greg论证Ref<T>无需锁：借用不得长于被借内存，编译期保证引用计数只从n增至n+1、永无0到1，并举E0597生命周期错误为例。 `<!-- ROW_MINE: ksummit.messages.8379 -->`
