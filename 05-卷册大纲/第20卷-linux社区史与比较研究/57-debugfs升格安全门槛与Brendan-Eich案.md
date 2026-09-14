# 57 【Linux社区】debugfs升格安全门槛与Brendan-Eich案

> 来源：ksummit-discuss p109（50 封全读，2018-10-01/04，夹杂 KS2014 档案信 2014-05-03/15）。
> 判定：50 CAND / 0 NV。主题分布：debugfs 27、coc 13、KS2014 6、zufs 4。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p109（pk 349656-349705）的逐封提取（50 CAND / 0 NV），全 8 块采用**导语＋带锚条目体例**：每块由“## 57.x 【Linux社区】题名”＋导语段＋“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——导语段承担“要点”职能、带锚条目承担“史料”与“史料锚”职能（ROW_MINE 坐标与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 57.1 【Linux社区】debugfs 定位之争：tracefs 先例与“直接干”流程观

2018-10-01/02 debugfs→sysfs 迁移议题的定位之争：Rostedt 提案、Greg 的“debugfs 只属于调试”红线与电池测量事故实录、Olof 的容器命名空间升格判据。

- 【Linux社区】Rostedt 新议题：成熟 debugfs 接口在 debugfs 关闭系统上不可用——迁出流程何在？自举 tracefs 先例 `<!-- ROW_MINE: ksummit-discuss.messages.349657 -->`
- 【Linux社区】Greg KH：“技术议题别上 maintainer summit”；debugfs 东西永远不该用于真实功能；多数发行版已关 debugfs、Android 亦然；放哪个案个案定 `<!-- ROW_MINE: ksummit-discuss.messages.349658 -->`
- 【Linux社区】Greg：“流程？直接干”；脚注实录：一整条 SoC 线把电池测量逻辑放 debugfs（sysfs 明明有标准电池/电源 API），关 debugfs 手机即无法报电量 `<!-- ROW_MINE: ksummit-discuss.messages.349659 -->`
- 【Linux社区】Rostedt：“调试用的东西往往变成生产系统想要的（tracing/perf/powertop）”；debugfs 或可用作开发中接口存放处 `<!-- ROW_MINE: ksummit-discuss.messages.349661 -->`
- 【Linux社区】Olof 升格判据：命名空间与安全理顺方可毕业进 sysfs；容器想要的功能进 sysfs 却无法提供给非特权容器——应避免 `<!-- ROW_MINE: ksummit-discuss.messages.349663 -->`

## 57.2 【Linux社区】模块参数反向迁移与 probe 时序之利

Jani 的“模块参数即调试旋钮”反向提案与 Mauro 的廉价硬件用例反驳，probe 时序成为模块参数不可替代的技术根由。

- 【Linux社区】Jani 反向议题：模块参数应首先视为调试旋钮而非 ABI；但全数出现在 sysfs——纯调试选项因便利性做成模块参数（几行代码/probe 前生效/无可比拟）；求反向迁移便利法 `<!-- ROW_MINE: ksummit-discuss.messages.349660 -->`
- 【Linux社区】Rostedt：选部分参数做 debugfs 旋钮？个人没遇到此类困扰 `<!-- ROW_MINE: ksummit-discuss.messages.349662 -->`
- 【Linux社区】Mauro 反对一刀切：media 廉价硬件无 eeprom/无 ID 靠非调试类 modprobe 参数加载配置；也不动现有参数以免破坏用户空间 `<!-- ROW_MINE: ksummit-discuss.messages.349668 -->`
- 【Linux社区】Jani：调试参数无法在 probe 时生效（驱动须先注册 debugfs 文件）——正是模块参数独有便利 `<!-- ROW_MINE: ksummit-discuss.messages.349672 -->`

## 57.3 【Linux社区】debugfs 安全门槛与发行版实态

debugfs 安全门槛之辩全景：Greg 的“完全不稳→root-only 默认”时间线、Shuah 的发行版 CONFIG 实查、Brown 的“须改内核方可写”regmap 模式、SUSE 的客户排障依赖与默认挂载之辨。

- 【Linux社区】Shuah：移 sysfs 更安全但“留在 debugfs 也要讲安全”；正处理容器场景驱动、其命名空间未限制在容器范围 `<!-- ROW_MINE: ksummit-discuss.messages.349664 -->`
- 【Linux社区】Greg：“直到约一年前 debugfs 完全不安全、崩溃内核轻而易举”；“内核不知道什么是容器 :)；多数驱动子系统没有也不该有命名空间” `<!-- ROW_MINE: ksummit-discuss.messages.349665 -->`
- 【Linux社区】Greg：debugfs 仍有可致大问题的残留——别挂不可信系统；“正在好转、再给一年” `<!-- ROW_MINE: ksummit-discuss.messages.349666 -->`
- 【Linux社区】Mauro：debugfs 些东西不该上生产——泄露内存地址等有助攻破系统 `<!-- ROW_MINE: ksummit-discuss.messages.349669 -->`
- 【Linux社区】Shuah 实查发行版配置：BLK_DEBUG_FS/KVM_DEBUG_FS/DEBUG_FS 仍被启用；“需广而告之让 distros 收紧” `<!-- ROW_MINE: ksummit-discuss.messages.349670 -->`
- 【Linux社区】Greg：“幸好 debugfs 已默认仅 root、攻击面大减” `<!-- ROW_MINE: ksummit-discuss.messages.349671 -->`
- 【Linux社区】Sudeep Holla：ARM 平台 PM 补丁在 debugfs 放完整系统时钟控制、还能向远程控制处理器发指令——生产系统绝不想要 `<!-- ROW_MINE: ksummit-discuss.messages.349674 -->`
- 【Linux社区】Jan Kara：“发行版需要这些配置排客户问题——请客户开 tracepoint/看 debugfs stats 很常见” `<!-- ROW_MINE: ksummit-discuss.messages.349677 -->`
- 【Linux社区】Brown：“我一直强烈抵制 regmap/regulator debugfs 文件可写——须改内核才能启用” `<!-- ROW_MINE: ksummit-discuss.messages.349679 -->`
- 【Linux社区】Greg：“tracepoint 不该在 debugfs；依赖的 stats 就该移到稳定位置” `<!-- ROW_MINE: ksummit-discuss.messages.349680 -->`
- 【Linux社区】Shuah：“继续把 debugfs 做安全、新服务提高门槛——自担风险地启用、我们尽力做安全” `<!-- ROW_MINE: ksummit-discuss.messages.349682 -->`
- 【Linux社区】Sudeep：“下次见 debugfs 必须限制写的场合就照 Brown 的做——加个小补丁才能启用” `<!-- ROW_MINE: ksummit-discuss.messages.349686 -->`
- 【Linux社区】Jan Kara：bdi/ stats 契合 debugfs 宗旨；“不必常挂 debugfs——但必须编译进内核” `<!-- ROW_MINE: ksummit-discuss.messages.349687 -->`
- 【Linux社区】Iwai：“问题是 debugfs 默认挂载在我们系统上；想在生产系统收集调试数据故禁编译 no-go；禁挂载是另一回事” `<!-- ROW_MINE: ksummit-discuss.messages.349690 -->`

## 57.4 【Linux社区】HID debugfs 实例之辩

HID debugfs 的去留实例战：verbatim 描述符与解析后呈现之别、usbfs 对称设想——debugfs 合法用例的最具体呈现。

- 【Linux社区】Kosina：HID debugfs 条目——读描述符+分析解析后事件；契合 debugfs 用途、远程调试正需要这些数据 `<!-- ROW_MINE: ksummit-discuss.messages.349681 -->`
- 【Linux社区】Greg：“描述符 USB/PCI 都有常在途径——HID 或可同样做；hidfs 或许需要来配 usbfs :)” `<!-- ROW_MINE: ksummit-discuss.messages.349683 -->`
- 【Linux社区】Greg：“为何不放 sysfs？你已有 report_descriptor；为何还要 debugfs 版？” `<!-- ROW_MINE: ksummit-discuss.messages.349684 -->`
- 【Linux社区】Kosina：“sysfs 是从设备读的 verbatim 二进制、debugfs 是内核解析器理解后的呈现——两回事；events 无 sysfs 对应物” `<!-- ROW_MINE: ksummit-discuss.messages.349688 -->`

## 57.5 【Linux社区】ZUFS 用户态文件系统提案

ZUFS（零拷贝用户态文件系统）一周年进展提案与“该在哪讨论”的轨道归位问答。

- 【Linux社区】Harrosh 新议题：ZUFS one year later——完整 VFS API（dax/mmap/IOCTL/xattrs/ACL，缺 quota）、IO API 改版、ASYNC、pmem+常规块设备、私有内存池、ZT 多通道动态分配 `<!-- ROW_MINE: ksummit-discuss.messages.349673 -->`
- 【Linux社区】Greg：“为什么不在文件系统专门会议讨论？今年开过了吗？” `<!-- ROW_MINE: ksummit-discuss.messages.349675 -->`
- 【Linux社区】Harrosh：已过 LSF 全场讨论（半年前远未 ready）；现代码完整稳定、技术超越纯 FS——用户态服务器通信新方式、cpu-locality 与 NUMA aware；“实为我睡岗错过 Plumbers 截止” `<!-- ROW_MINE: ksummit-discuss.messages.349676 -->`
- 【Linux社区】Boaz 重发 ZUFS 提案（个人 gmail 版） `<!-- ROW_MINE: ksummit-discuss.messages.349685 -->`

## 57.6 【Linux社区】Brendan Eich 案引入与法务暴露之辩

2018-10-04 Brendan Eich 案例引入：CoC 的诉讼暴露论（2000 万期权假设案）、LF 出资法律顾问倡议、Zephyr 去 enforcement 先例与 Pinchart 的程序/代表性两问。

- 【Linux社区】jonsmirl 新话题：请 Linux 社区律师评审新 CoC；在 Ksummit 讨论 Brendan Eich 局面——须预案、不当回应招法律挑战；附 4 篇 Mozilla CEO 辞职事件文章 `<!-- ROW_MINE: ksummit-discuss.messages.349691 -->`
- 【Linux社区】Bottomley FYI：Zephyr 项目收录 contributor covenant CoC（去掉 enforcement 条款）——标准 github PR 流程；“等社区共识再加执行细节” `<!-- ROW_MINE: ksummit-discuss.messages.349692 -->`
- 【Linux社区】Pinchart：“教科书级案例、激辩概率不低于 100%”；两问——暴民等在庭外时如何留足时间冷静思考（程序保证）+ representation：TAB 授权是否延伸至代表社区、如何让分歧者保留异议仍感属于社区 `<!-- ROW_MINE: ksummit-discuss.messages.349693 -->`
- 【Linux社区】jonsmirl：“有人因被指控违反 CoC 被解雇、损失 2000 万美元期权怎么办？CoC 给所有维护者制造了诉讼暴露——真需要内核法务团队审查” `<!-- ROW_MINE: ksummit-discuss.messages.349694 -->`
- 【Linux社区】Vivi 驳：“因公开场合不尊重他人被解雇恐怕早已在全世界发生；后果源于言论本身、而非渠道” `<!-- ROW_MINE: ksummit-discuss.messages.349695 -->`
- 【Linux社区】Pinchart：“LF 或其代表 TAB 咨询社区+获取法律建议才合理——个人各请律师无法 scale；需要汇集关切的论坛+有人出资法律顾问” `<!-- ROW_MINE: ksummit-discuss.messages.349696 -->`
- 【Linux社区】jonsmirl：“被解雇者很可能起诉维护者在指控中的角色——维护者从此背上法律辩护负担” `<!-- ROW_MINE: ksummit-discuss.messages.349697 -->`

## 57.7 【Linux社区】“封禁 Alice”思想实验：被禁贡献者的有效修复

Al Viro 的“封禁 Alice”思想实验及四方回应：Viro/Triplett/Tim Bird 的处理路径（代提交/自修整/类比失效邮箱）、tglx 的列表封禁-CC 送达漏洞、Corbet 的“过渡人”机制——CoC 执行论最锋利的一组推演。

- 【Linux社区】Al Viro 思想实验：Alice 被封禁→发出技术上有效的 roothole 修复→Bob 验证 bug 真修复对来源被封——Bob 该怎么办？“‘提交不提 Alice’不可行、‘换实现不提’更糟、‘送 Alice 去革命广场’亦非选项——TAB 不是 CSP、断头台也退役了” `<!-- ROW_MINE: ksummit-discuss.messages.349698 -->`
- 【Linux社区】Corbet：“没听说有人要禁止接受任何人的补丁；CoC 常见的是封禁特定场所——不触发上述场景”（忆马甲发信前例） `<!-- ROW_MINE: ksummit-discuss.messages.349699 -->`
- 【Linux社区】Josh Triplett：封禁非流程第一步；“补丁修真 bug 但不合其他要求？见过自己修整也见过拒绝+他人清理——参见 grsecurity”；“验证有效/许可/签名→作为修复合入”；类比失效邮箱情形 `<!-- ROW_MINE: ksummit-discuss.messages.349702 -->`
- 【Linux社区】tglx 驳 Corbet：“Alice 被封出列表但仍按规则发修复 CC 维护者；LKML 丢弃但维护者仍收到——忘了加 **/dev/null** 过滤就得无视它？” `<!-- ROW_MINE: ksummit-discuss.messages.349703 -->`
- 【Linux社区】Corbet：“没人设想禁止维护者接受补丁；常见做法是让当事人经由愿意与其打交道的人过渡——全面拒收我从未见过” `<!-- ROW_MINE: ksummit-discuss.messages.349704 -->`
- 【Linux社区】Tim Bird：“辩论假想情形不太有生产力——低概率；维护者可清理提交信息——一直这么干；补丁上游后没人该在乎来自谁——CoC 不是 witch hunt” `<!-- ROW_MINE: ksummit-discuss.messages.349705 -->`

## 57.8 【Linux社区】KS2014 档案六封

页内夹杂的 KS2014 档案信（2014-05-03/15）：提名名录勘误、DT bindings 活文档设想、QR oops 的 hpa 三连与 mailman 收件人上限。

- 【Linux社区】Shuah 确认提名邮箱（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349656 -->`
- 【Linux社区】Rob Herring：ARM legacy DT 积压大半=需要 DT bindings；todo list 应成活文档“否则就 bit rot”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349667 -->`
- 【Linux社区】hpa：QR 讨论已远超技术对话、该去 LKML（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349678 -->`
- 【Linux社区】hpa 论 QR 去寄存器：“HELL NO.”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349689 -->`
- 【Linux社区】Kerrisk 求解除 mailman“Too many recipients”审核扣信限制（2014-05-03 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349700 -->`
- 【Linux社区】hpa：QR 整点是对付没有合理上网路径的设备；“（突然想到 modem 音调+声卡的邪念）”（2014-05-15 档案信） `<!-- ROW_MINE: ksummit-discuss.messages.349701 -->`
