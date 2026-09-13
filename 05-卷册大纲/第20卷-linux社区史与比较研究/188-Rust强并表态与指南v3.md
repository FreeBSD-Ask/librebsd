# 188. Linus 强并 Rust 私下表态、工具生成内容指南 v3 与 Morton AI 红线（ks p52）

> 来源：ksummit 独有 p52（50 封全读，2022-10 至 2025-02：Hellwig 披露 Linus 私下表态将无视维护者反对强并 Rust 并预言绑定代码蔓延与多语言碎片化系重磅反方一手立场；Dave Hansen 提交 TAB 集体产出工具生成内容指南 v3 补丁全文 97 行规则文本附 8 位维护者 Reviewed-by；Ted Ts'o 提出 DCO 与 AI 生成代码四项法律问题清单含是否强制披露模型与提示词是否记录；Andrew Morton 明确 AI 找缺陷已可用写补丁尚无用并划红线任何新规不得妨碍接收 AI 缺陷报告；Bugzilla 改革四封、AI 生成内容指南四封、加速器用户态接口三封）
> 判定：43 CAND / 7 NV。主题分布：Bugzilla 改革 4、UMN 假补丁事件 1、CXL RAS 与 EDAC 1、加速器用户态接口 3、维护者峰会存废 3、cleanup.h 规则之争 3、bcachefs 治理反思 1、设备树绑定独立仓库 1、kernel.org 信任工具 1、KTODO 工具提案 1、AI 审查工具 1、AI 生成内容指南 3、补丁审阅工具 1、DCO 与 AI 披露 1、琐碎补丁收件政策 1、devres 混用检测 1、AI 照片权限方案 1、Rust 内核政策 1、Rust 测试环境 1、设备透传争论 1、ORC 栈回溯 1、C 聚合传参之争 3、io_uring BPF 议题 1、HIGHMEM 淘汰 1、LLM 测试生成 1、stable 补丁标记 1、内核文档改革 1、LKML 通配剥离 1、Sphinx 构建工具 1、TAB 选举 1。

## 188.1 Bugzilla 改革

- 【Linux社区】Slade Watkins 提议在 Bugzilla 减痛改革中设“联络人”衔接终端用户与开发者并代为分流，自称已两次表态愿承担此职，询 Leemhuis 是否采纳。 `<!-- ROW_MINE: ksummit.messages.8070 -->`
- 【Linux社区】Konstantin Ryabitsev 提议把新缺陷与评论汇入 public-inbox 数据流，可经 lore.kernel.org 与 lei 查询；战略是用可镜像的查询式订阅避免单点故障，无需全员换工作流。 `<!-- ROW_MINE: ksummit.messages.8128 -->`
- 【Linux社区】Artem 确认其提案实质：仅为出现在 MAINTAINERS 中的维护者自动创建 bugzilla 账号以便人工分流时抄送，并非设为默认指派，不会带来垃圾邮件。 `<!-- ROW_MINE: ksummit.messages.8156 -->`
- 【Linux社区】Artem 力主保留 Bugzilla：驳 GitLab 迁移（商业开源核被收购风险、单点可瘫痪），提议刷新组件、按近半年提交记录订阅开发者，或改 Discourse 八论坛；称 Linus 曾经 Bugzilla 解决其 LKML 无回应的问题。 `<!-- ROW_MINE: ksummit.messages.8198 -->`

## 188.2 UMN 假补丁事件

- 【Linux社区】Kozlowski 引明尼苏达大学计算机系 4 月 21 日官方声明，质疑其 IRB 审查有效性；指出 uwn.net 缺陷提交真伪不明，信任破坏后无法验证研究是否已停止。 `<!-- ROW_MINE: ksummit.messages.8074 -->`

## 188.3 CXL RAS 与 EDAC

- 【Linux社区】Borislav Petkov 澄清对 CXL RAS 报告系列的意见：并非要求全新设计，而是建议直接复用既有 EDAC 子系统，反问为何要另起炉灶。 `<!-- ROW_MINE: ksummit.messages.8075 -->`

## 188.4 加速器用户态接口

- 【Linux社区】Daniel Vetter 认同 AI 计算本质受限于矩阵乘，但称 BLAS 接口对可编程设备过浅；小型 SoC NPU 可用固定接口，且不应允许厂商私有扩展或旁路上传编译产物。 `<!-- ROW_MINE: ksummit.messages.8089 -->`
- 【Linux社区】Mauro 指出死锁：若新内核 API 须待发行版先收用户态实现则新 API 永难落地，他作为 Fedora 维护者即会拒绝；并以 CAN 总线与 ASIL 认证说明行业专用硬件不该挤占通用发行版。 `<!-- ROW_MINE: ksummit.messages.8200 -->`
- 【Linux社区】Leon Romanovsky 澄清主张：用户态 API 只需“已用或将用”即有公开 PR 或新包申请即可；反对为覆盖所有设备类型定通用方案，建议聚焦企业与云 AI 设备 API 的主流发行版支持。 `<!-- ROW_MINE: ksummit.messages.8222 -->`

## 188.5 维护者峰会存废

- 【Linux社区】Rafael Wysocki 提醒维护者峰会因 Documentation/process/conclave.rst 承担正式应急职能，若大幅改形式须同步修订该预案。 `<!-- ROW_MINE: ksummit.messages.8091 -->`
- 【Linux社区】Rostedt 回应 Linus 对峰会“小圈子”化的伤感：资深者主导属项目成熟常态，举 Miguel Ojeda 靠 Rust 进入核心为例；预计 5 年内 50 岁以上维护者交棒，Andrew Morton 已启动。 `<!-- ROW_MINE: ksummit.messages.8165 -->`
- 【Linux社区】Ted 说明峰会预讨论机制：ksummit 列表上的声音会实质影响场内议程；接班规划宜在 LSF/MM 等子系统场合谈，如今年 mm 接班与 FUSE 组织讨论即在 LSF/MM/BPF。 `<!-- ROW_MINE: ksummit.messages.8179 -->`

## 188.6 cleanup.h 规则之争

- 【Linux社区】James Bottomley 主张 __free 变量不初始化置于块首，混排声明规则可放宽但须注释说明必要性；强调规则应统一适用，并支持以显式作用域块界定变量生命周期。 `<!-- ROW_MINE: ksummit.messages.8094 -->`
- 【Linux社区】Rostedt 以环形缓冲代码为例，询问 __free 变量声明后紧接分配时能否把声明下移到普通声明之后，受 80 列换行影响可读性，请 Linus 定夺。 `<!-- ROW_MINE: ksummit.messages.8120 -->`
- 【Linux社区】Martin Petersen 实测 __attribute__(__cleanup__) 与 defer 方案：清理逻辑稍复杂即伤可读性，转换大型代码库后多处回退经典 goto 展开，但并非反对两者。 `<!-- ROW_MINE: ksummit.messages.8172 -->`

## 188.7 bcachefs 治理反思

- 【Linux社区】Dan Williams 反对为 bcachefs 事件过度制度化：非正式流程最终仍以项目健康为先，主张培养设定边界的成熟与勇气，引 Pat Gelsinger“少求对、多求效”。 `<!-- ROW_MINE: ksummit.messages.8100 -->`

## 188.8 设备树绑定独立仓库

- 【Linux社区】Arınç ÜNAL 自述维护 MediaTek DSA 与若干 dt-binding，主张把 dt-bindings 与 DT 源文件移出 Linux 仓库，建 Linux、U-Boot、OpenWrt 共用统一硬件描述仓库，并请求出席峰会。 `<!-- ROW_MINE: ksummit.messages.8115 -->`

## 188.9 kernel.org 信任工具

- 【Linux社区】Greg KH 回应 Bottomley 批评：kernel.org 与 OpenSSF 合作的 Web of Trust 新方案将于 2 月会议公开，可评审时即发布；Bottomley 斥其违背“早发布、常发布”开源准则。 `<!-- ROW_MINE: ksummit.messages.8123 -->`

## 188.10 KTODO 工具提案

- 【Linux社区】Dan Carpenter 澄清 KTODO 非代码注释，而是邮件列表中单行摘要式可检索标签，配合 Closes: 标记可写工具筛出未关闭项。 `<!-- ROW_MINE: ksummit.messages.8124 -->`

## 188.11 AI 审查工具

- 【Linux社区】Rostedt 表明立场：AI 审查放 CI 即可，暂不必担心专有锁定，报告同时抄送提交者与维护者双方受益；认同先做维护者侧、勿转嫁贡献者的路线。 `<!-- ROW_MINE: ksummit.messages.8130 -->`

## 188.12 AI 生成内容指南

- 【Linux社区】Dave Hansen 回应 Lorenzo：现有规则暂能抵挡 LLM 滥用但堤坝随时可能溃决；并以 checkpatch 输出可被直接拒收为例，质疑指南会鼓励维护者无理由拒稿之说。 `<!-- ROW_MINE: ksummit.messages.8131 -->`
- 【Linux社区】Dave Hansen 发布 TAB 集体起草的工具生成内容指南 v3 全文：新增 generated-content.rst 97 行，要求披露工具、提示词与测试方式，已获 Shuah、Kees、Greg、Miguel 等 8 人 Reviewed-by。 `<!-- ROW_MINE: ksummit.messages.8159 -->`
- 【Linux社区】Andrew Morton 称尚未见 LLM 产出有用内核改动，但 AI 找缺陷已可用；以补丁形式出现的 AI 缺陷报告可删补丁自修，切勿制定任何妨碍接收 AI 缺陷报告的规则。 `<!-- ROW_MINE: ksummit.messages.8166 -->`

## 188.13 补丁审阅工具

- 【Linux社区】Mauro 分享用 wdiff 审阅重命名补丁的经验，给出 diff-highlight 作 git pager 的配置；称 Fedora 33 需自改 perl 脚本，git 2.29 可用，因 RH bug 1952030 从 2.30 回退。 `<!-- ROW_MINE: ksummit.messages.8134 -->`

## 188.14 DCO 与 AI 披露

- 【Linux社区】Ted 拟咨询法律顾问四问：DCO 是否须披露 LLM 生成、需何种细节、全盘生成与局部修改是否区别对待、提示词是否如 coccinelle 脚本般记入提交说明。 `<!-- ROW_MINE: ksummit.messages.8135 -->`

## 188.15 琐碎补丁收件政策

- 【Linux社区】Martin Petersen 实证 SCSI 已在合并大量琐碎补丁：静态检查器与编译器日益严苛，拒不应用则同型修复每周重发；有人维护与无人维护的驱动已无差别，需更好流程与辅导。 `<!-- ROW_MINE: ksummit.messages.8145 -->`

## 188.16 devres 混用检测

- 【Linux社区】Dan Carpenter 就 devres 与 uapi 资源混用给出三种检测思路：直接检查、按类型推断并建 kernel.ignore_devres_types 例外表、Sparse 手工注解，建议并行实现。 `<!-- ROW_MINE: ksummit.messages.8147 -->`

## 188.17 AI 照片权限方案

- 【Linux社区】Jan Kara 认为该 AI 照片分类共享场景无需 richACL：用 AI 属主、带粘滞位的 rwxrwxrwt 目录即可实现可删己不可删人，创建限制用任意 LSM 即可施加。 `<!-- ROW_MINE: ksummit.messages.8154 -->`

## 188.18 Rust 内核政策

- 【Linux社区】Hellwig 强烈反对 Rust 政策网页：内容失实，并披露 Linus 私下称将无视子系统维护者反对强并 Rust；警告绑定代码将如癌症蔓延，多语言无序化会迫使他抽身。 `<!-- ROW_MINE: ksummit.messages.8158 -->`

## 188.19 Rust 测试环境

- 【Linux社区】Jarkko Sakkinen 展示 NixOS 构建的 TPM 驱动测试环境：docker compose 构建镜像后 QEMU 启动，计划登记进 MAINTAINERS，与 Fiona 的 nix shell 路线不同。 `<!-- ROW_MINE: ksummit.messages.8160 -->`

## 188.20 设备透传争论

- 【Linux社区】Jason Gunthorpe 反问：全开源的相机透传方案是否仅因透传形态就拒收？主张“因恐惧拒绝给用户有用的开源方案”不是 Linux 该做的事。 `<!-- ROW_MINE: ksummit.messages.8169 -->`

## 188.21 ORC 栈回溯

- 【Linux社区】Josh Poimboeuf 力挺 ORC：多年稳健、中断异常栈迹干净，唯一失效原因是无视 objtool 告警（即将默认升为编译错误）；x86-64 帧指针已实质弃用，考虑移除该 unwinder。 `<!-- ROW_MINE: ksummit.messages.8173 -->`

## 188.22 C 聚合传参之争

- 【Linux社区】comex 考据 std::string CoW 史：C++11 未明文禁 CoW，但要求 operator[] 为 O(1) 实质封杀，迫使 libstdc++ 破坏 ABI 放弃引用计数实现。 `<!-- ROW_MINE: ksummit.messages.8176 -->`
- 【Linux社区】Ralf Jung 澄清 C++ 内存模型已按程序行为而非类型系统定义，原子对象只是类型系统薄层，Rust 即绕开它；并论证把数据竞争从 UB 改为确定可见值会损害顺序代码优化。 `<!-- ROW_MINE: ksummit.messages.8185 -->`
- 【Linux社区】Linus 实测纠正 David Laight：x86 与 arm64 ABI 下两寄存器大小的结构体同样经寄存器返回（gcc 与 clang 均生成两条 movl 加 ret），超过两寄存器才走间接内存。 `<!-- ROW_MINE: ksummit.messages.8233 -->`

## 188.23 io_uring BPF 议题

- 【Linux社区】Pavel Begunkov 提交峰会议题：io_uring 拟把部分提交与控制权交给 BPF，进一步减少上下文切换与系统调用，作为提交队列轮询的替代，征集用例与 API 意见。 `<!-- ROW_MINE: ksummit.messages.8178 -->`

## 188.24 HIGHMEM 淘汰

- 【Linux社区】Richard Weinberger 报告受影响机型 MPC8343 与 QorIQ P1022：应用常假设内存布局，FPGA 树外驱动共享内核与用户态内存；Christophe 已发 powerpc 全量移除 HIGHMEM 补丁。 `<!-- ROW_MINE: ksummit.messages.8180 -->`

## 188.25 LLM 测试生成

- 【Linux社区】Mark Brown 认同 LLM 生成测试数据比测试代码安全，因后者约束更少；场景生成是否可行因运行成本而异，预示 AI 政策将更多靠“品味”而非硬规则。 `<!-- ROW_MINE: ksummit.messages.8189 -->`

## 188.26 stable 补丁标记

- 【Linux社区】Jiri Kosina 质询 stable 标记边界：既然 stable 只为修错，哪些非修错补丁应获 Cc: stable？点名硬件安全缓解、新设备 ID、quirk 一类，指 stable-kernel-rules 的定义早已不适用。 `<!-- ROW_MINE: ksummit.messages.8192 -->`

## 188.27 内核文档改革

- 【Linux社区】Vegard Nossum 系统提案：维护者条目档案加子系统评审清单并可由 kerneldoc 自动收集、HTML 侧栏按“书”重组、设“社区”卷、翻译加语言切换栏、跨架构文档按读者分流。 `<!-- ROW_MINE: ksummit.messages.8196 -->`

## 188.28 LKML 通配剥离

- 【Linux社区】Konstantin 澄清“THE REST”剥离方案是“预审”而非限权：订阅仍开放，只需说明收全部补丁的理由，高知名度维护者可订阅，并举 outlook.com 断服例证 Gmail 并非唯一故障源。 `<!-- ROW_MINE: ksummit.messages.8205 -->`

## 188.29 Sphinx 构建工具

- 【Linux社区】Mauro 解释 sphinx 检测脚本缘由：发行版 LaTeX 元包残缺致装而不能用，故脚本内置 *.sty 清单并用 kpsewhich 复核依赖；回应 openSUSE Leap 15.4 缺 tex-gyre 的问题。 `<!-- ROW_MINE: ksummit.messages.8209 -->`

## 188.30 TAB 选举

- 【Linux社区】Shuah Khan 要求公开 TAB 选举判定 3 至 49 提交档的脚本，并追问其是否也用于候选人资格核验；引选举规则：2020-21 年三项标签提交、CIVS 投票、超 50 提交自动获票。 `<!-- ROW_MINE: ksummit.messages.8219 -->`
