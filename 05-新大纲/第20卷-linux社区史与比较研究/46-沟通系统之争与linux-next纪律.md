# 46 【Linux社区】沟通系统之争与linux-next纪律

> 对应页面：ksummit-discuss p100（pk 349206-349255，2018 沟通系统/patchwork-linux-next 纪律多线程 + 2014 档案）
> 判定：50 CAND / 0 NV
> 编号：DSLXC-5929..5978 | claim 已入库（50/50，dslinux_claims.duckdb）

## 46.1 【Linux社区】沟通系统与 patchwork／gitlab 之争（12 例）

**要点（判定表逐字）**：Daniel Vetter 称 drm 不会从 freedesktop 迁往 kernel.org，因与 mesa、X11、wayland 等用户态项目交互面更大，弃用内核 bugzilla 改用 fd.o 的；Laurent Pinchart 请 Daniel Vetter 说明迁往 gitlab 具体指开发流程哪部分受影响、为何现有方式不足，质疑自动追踪 patch 系列的可行性；Laurent Pinchart 指出 patch 系列生命周期内边界不固定、常被拆分合并，不信任能自动全程追踪的系统，但主张在常见情形让追踪信息易取已是进步；Laurent Pinchart 忧各子系统若分别采用 gitlab、gerrit 等会令跨子系统改动成噩梦，主张新工具可选且须与邮件双向兼容；Laurent Pinchart 主张需全子系统共用的沟通系统，今日即邮件；列出三要素：推送式、可脚本化审阅与拉取、可离线，邮件皆满足；Daniel Vetter 请求把 gitlab 讨论移到线程别处，此处仅就 cregit 提问，自承提及 gitlab 已分散注意力；Daniel Vetter 列痛点为 patchwork 的 CI 集成、首贡献者流程、patch 系列演进追踪，计划 LPC 用 igt gpu 测试仓库做演示；Sean Paul 视各子系统规则差异为特性而非缺陷，但承认跨子系统改动（如 Kees 的树-wide 修改）会因此剧痛，认有中间地带；Theodore Y. Ts'o 增补要求：消息须存档且具一流检索，凭提交号可溯及整串讨论，觅得某改动的立法史至关重要；Konstantin Ryabitsev 推介 pagure.io，乃架于 gitolite 之上、可经 ssh 与邮件运作的 Web 界面，由红帽背书且无社区版商业版分裂；Josh Triplett 称有可改编的工具与算法做 patch 系列跨版本比对、检测重排并示 interdiff，扩展至系列间匹配不难；Laurent Pinchart 称若有人造出兼具邮件优点的沟通系统必乐见，认同 patchwork 辅助邮件流程的理念，主张保持其哲学

**史料**：`349207`、`349208`、`349209`、`349211`、`349213`、`349215`、`349217`、`349218`、`349219`、`349220`、`349222`、`349224`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349207 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349208 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349209 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349211 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349213 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349215 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349217 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349218 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349219 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349220 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349222 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349224 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Daniel Vetter 的“drm 不会从 freedesktop 迁往 kernel.org，因与 mesa、X11、wayland 等用户态项目交互面更大”与 Laurent Pinchart 的“主张需全子系统共用的沟通系统，今日即邮件”并置，未替任一方定论）；经验优先（总纲第 9 条——经验优先：以 Laurent Pinchart 的“patch 系列生命周期内边界不固定、常被拆分合并，不信任能自动全程追踪的系统”、Theodore Y. Ts'o 的“凭提交号可溯及整串讨论，觅得某改动的立法史至关重要”为判据）
**辨析**：Laurent Pinchart 的“忧各子系统若分别采用 gitlab、gerrit 等会令跨子系统改动成噩梦”与 Sean Paul 的“视各子系统规则差异为特性而非缺陷，但承认跨子系统改动会因此剧痛，认有中间地带”构成两说并置；Daniel Vetter 的“请求把 gitlab 讨论移到线程别处，自承提及 gitlab 已分散注意力”为当事人自反留痕；Konstantin Ryabitsev 的“推介 pagure.io，乃架于 gitolite 之上、可经 ssh 与邮件运作的 Web 界面，由红帽背书且无社区版商业版分裂”为工具提案；Josh Triplett 的“称有可改编的工具与算法做 patch 系列跨版本比对”为其可行性主张。本页未见决议。
**文献**：DSLXC-5930、DSLXC-5931、DSLXC-5932、DSLXC-5934、DSLXC-5936、DSLXC-5938、DSLXC-5940、DSLXC-5941、DSLXC-5942、DSLXC-5943、DSLXC-5945、DSLXC-5947（`ksummit-discuss.messages.349207`、`ksummit-discuss.messages.349208`、`ksummit-discuss.messages.349209`、`ksummit-discuss.messages.349211`、`ksummit-discuss.messages.349213`、`ksummit-discuss.messages.349215`、`ksummit-discuss.messages.349217`、`ksummit-discuss.messages.349218`、`ksummit-discuss.messages.349219`、`ksummit-discuss.messages.349220`、`ksummit-discuss.messages.349222`、`ksummit-discuss.messages.349224`，2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10），全文见 `raw_source.raw_json`

## 46.2 【Linux社区】沟通系统续论与架构清理（10 例）

**要点（判定表逐字）**：Laurent Pinchart 称各子系统虽自由定制流程，但终归集成于同一内核，靠共同沟通工具维系；若用 gerrit 恐失多数开发者；Arnd Bergmann 述删八无维护架构的经过，unicore32 被维护者临末挽回；归类服务器架构（alpha、parisc、ia64、sparc）与多机架构中已死平台；Guenter Roeck 指 unicore32 因私有工具链过旧（gcc 低于四点六）已无法在主线程构建，或可重议保留决定；Daniel Vetter 称 patchwork 是边缘附加件、gitlab 有即时状态指示与合并请求集成；喻 CI 应如老虎机令人上瘾以提升开发者关注；Laurent Pinchart 自陈用词失当，澄清新人常驻贡献者非对立双方而是连续谱系，目标在兼顾各群体减痛；Laurent Pinchart 称 Josh Triplett 的系列比对工具可补 patchwork，靠启发式难达百分之百但能显著改善现状；Laurent Pinchart 赞同 Ted 的检索要求，并进一步希望系统保留消息间关系、自动侦测同系列新版本；Daniel Vetter 问 Josh Triplett 的系列比对工具是否基于 git range-diff 概念，抑或另辟实现；Josh Triplett 答 Daniel：工具与 git range-diff 同概念、异实现，类 tbdiff 之算法；Linus Walleij 论 ARMv4 困境：FA526 与 EP93xx 有逾十五年 IoT 部署、MOXA ART 仍在铺，移除属不负责；IoT 生命周期可达二十至三十年

**史料**：`349225`、`349226`、`349228`、`349230`、`349231`、`349232`、`349236`、`349240`、`349252`、`349255`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349225 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349226 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349228 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349230 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349231 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349232 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349236 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349240 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349252 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349255 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Linus Walleij 的“论 ARMv4 困境：FA526 与 EP93xx 有逾十五年 IoT 部署、MOXA ART 仍在铺，移除属不负责；IoT 生命周期可达二十至三十年”与 Arnd Bergmann 的“述删八无维护架构的经过，归类服务器架构与多机架构中已死平台”对撞，未替任一方定论）；分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：删架构与保留平台之争、unicore32 被维护者临末挽回，正是树内分合的相位）
**辨析**：Guenter Roeck 的“指 unicore32 因私有工具链过旧（gcc 低于四点六）已无法在主线程构建，或可重议保留决定”为可核之技术实况；Laurent Pinchart 的“自陈用词失当，澄清新人常驻贡献者非对立双方而是连续谱系”为当事人自反留痕；Daniel Vetter 的“喻 CI 应如老虎机令人上瘾以提升开发者关注”为戏喻，非史家判断；Josh Triplett 的“工具与 git range-diff 同概念、异实现，类 tbdiff 之算法”为技术澄清。
**文献**：DSLXC-5948、DSLXC-5949、DSLXC-5951、DSLXC-5953、DSLXC-5954、DSLXC-5955、DSLXC-5959、DSLXC-5963、DSLXC-5975、DSLXC-5978（`ksummit-discuss.messages.349225`、`ksummit-discuss.messages.349226`、`ksummit-discuss.messages.349228`、`ksummit-discuss.messages.349230`、`ksummit-discuss.messages.349231`、`ksummit-discuss.messages.349232`、`ksummit-discuss.messages.349236`、`ksummit-discuss.messages.349240`、`ksummit-discuss.messages.349252`、`ksummit-discuss.messages.349255`，2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-11、2018-09-11），全文见 `raw_source.raw_json`

## 46.3 【Linux社区】linux-next 纪律与后期 -rc 质量（11 例）

**要点（判定表逐字）**：Sasha Levin 认同后期 -rc 补丁更易引入 bug 但认为原因不重要；对 stable 树可推迟更久再收 -rc5 以后的补丁，但会离 Linus 主干更远，主张这不是 WONTFIX；Tony Lindgren 称以 linux-next 每周测数次并上报回归效果良好，常在 -rc6 后见意外回归，主张应争取无回归的 -rc1；Steven Rostedt 认为后期 -rc 引入的是更微妙难触发的 bug，称 CANTFIX，最佳做法是改进 linux-next 自动化测试以减少 -rc5 补丁；Steven Rostedt 主张 Linus 应斥责破坏 linux-next 的维护者，未通过测试的分支应移出并致函，除非是两冲突提交所致集成破裂；Eduardo Valentin 反问难道大家不都该先在 linux-next 跑通测试再推送，原以为入 next 即等同可送 Linus；Steven Rostedt 指 selftest 已存于 tools/testing/selftests，含 ftrace 用例；称强制各子系统测试向来无效，且缺硬件的测试无助；Steven Rostedt 答 Eduardo：入 linux-next 本应等同可送 Linus 却未总能做到，故主张 Linus 该斥责未达标者；Stephen Rothwell 疑 next-20180910 多数失败源自 mount api 改动，问 Guenter 是否已上报；Stephen Rothwell 称 Linus 不跟 linux-next，自嘲不善斥责；此次系运行时测试失败且自己少量运行未触；Stephen Rothwell 列 linux-next 参与者须知：GPL v2 许可、Signed-off-by、贴列表、经审阅、单元测试、指向当次或下次合并窗口；Al Viro 纠 Stephen 措辞：真实检验是兼容 GPL v2 而非 v2 或更高，自陈默认 v2 仅授权、不允再分发于更宽版本

**史料**：`349206`、`349210`、`349214`、`349227`、`349235`、`349238`、`349239`、`349247`、`349248`、`349249`、`349250`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349206 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349210 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349214 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349227 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349235 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349238 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349239 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349247 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349248 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349249 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349250 -->` 

**史观**：本体论上各方平等（总纲第 8 条——本体论上各方平等：Sasha Levin 的“认同后期 -rc 补丁更易引入 bug 但认为原因不重要”与 Steven Rostedt 的“认为后期 -rc 引入的是更微妙难触发的 bug，称 CANTFIX，最佳做法是改进 linux-next 自动化测试”并置，未替任一方定论）；法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：Al Viro 的“真实检验是兼容 GPL v2 而非 v2 或更高，自陈默认 v2 仅授权、不允再分发于更宽版本”正是许可证条款边界的精确划分）
**辨析**：Stephen Rothwell 的“称 Linus 不跟 linux-next，自嘲不善斥责”“列 linux-next 参与者须知：GPL v2 许可、Signed-off-by、贴列表、经审阅、单元测试、指向当次或下次合并窗口”为可核之流程实况；Steven Rostedt 的“主张 Linus 应斥责破坏 linux-next 的维护者，未通过测试的分支应移出并致函”与 Eduardo Valentin 的“反问难道大家不都该先在 linux-next 跑通测试再推送，原以为入 next 即等同可送 Linus”相对，属规则执行之争；Al Viro 之纠为对 Stephen 措辞的法律性更正，属当事人自纠。
**文献**：DSLXC-5929、DSLXC-5933、DSLXC-5937、DSLXC-5950、DSLXC-5958、DSLXC-5961、DSLXC-5962、DSLXC-5970、DSLXC-5971、DSLXC-5972、DSLXC-5973（`ksummit-discuss.messages.349206`、`ksummit-discuss.messages.349210`、`ksummit-discuss.messages.349214`、`ksummit-discuss.messages.349227`、`ksummit-discuss.messages.349235`、`ksummit-discuss.messages.349238`、`ksummit-discuss.messages.349239`、`ksummit-discuss.messages.349247`、`ksummit-discuss.messages.349248`、`ksummit-discuss.messages.349249`、`ksummit-discuss.messages.349250`，2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-11、2018-09-11、2018-09-11、2018-09-11），全文见 `raw_source.raw_json`

## 46.4 【Linux社区】selftest 与硬件测试提议（6 例）

**要点（判定表逐字）**：Guenter Roeck 报 next-20180910 构建一百三十五通过一百三十三、qemu 三百一十五仅通过一百一十二，质疑 linux-next 可否用于回归测试；Eduardo Valentin 以 thermal 类比相机测试之难，称受控环境方可隔离变量；CI 对定向团队价值高、对大项目 prohibitive，局部自动化仍值得；Eduardo Valentin 建议要求开发者附 selftest 供机器人于 stable 回移植时执行，并强制各子系统有健全检查以提升机器人结果可靠性；Eduardo Valentin 认 selftest 难全覆盖但可捕子集，kernelCI 等已有硬件机架；thermal 真实问题多在温箱与终端用户处方显；Sasha Levin 主张 -rc8 关键复杂修复须先测，宜要求 Tested-by、送 lkml、至少一 Reviewed-by 或 Acked-by；Guenter Roeck 提议以 qemu 模拟环境触发系统响应，比温箱廉价，可解部分 thermal 等受控测试难题

**史料**：`349221`、`349229`、`349233`、`349242`、`349243`、`349244`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349221 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349229 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349233 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349242 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349243 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349244 -->` 

**史观**：动手者创造历史（总纲第 10 条——动手者创造历史：以 Eduardo Valentin 的“建议要求开发者附 selftest 供机器人于 stable 回移植时执行”、Guenter Roeck 的“提议以 qemu 模拟环境触发系统响应，比温箱廉价”为分析单位）；经验优先（总纲第 9 条——经验优先：以 Guenter Roeck 实测的“next-20180910 构建一百三十五通过一百三十三、qemu 三百一十五仅通过一百一十二”为判据）
**辨析**：Eduardo Valentin 的“以 thermal 类比相机测试之难，称受控环境方可隔离变量”“认 selftest 难全覆盖但可捕子集”“thermal 真实问题多在温箱与终端用户处方显”为其实务之陈；Sasha Levin 的“主张 -rc8 关键复杂修复须先测，宜要求 Tested-by、送 lkml、至少一 Reviewed-by 或 Acked-by”为其门槛提案；Guenter Roeck 的“质疑 linux-next 可否用于回归测试”为待答之问。
**文献**：DSLXC-5944、DSLXC-5952、DSLXC-5956、DSLXC-5965、DSLXC-5966、DSLXC-5967（`ksummit-discuss.messages.349221`、`ksummit-discuss.messages.349229`、`ksummit-discuss.messages.349233`、`ksummit-discuss.messages.349242`、`ksummit-discuss.messages.349243`、`ksummit-discuss.messages.349244`，2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10、2018-09-10），全文见 `raw_source.raw_json`

## 46.5 【Linux社区】NDA 之辩与 CVE 标注改进（4 例）

**要点（判定表逐字）**：Dave Hansen 论 NDA：企业实仅需掌控信息之感，社区正示其非唯一工具，望 Intel 等非 NDA 方共享方法，LF 或可居间；Eduardo Valentin 论 vendor 树令回移植更噩梦，顶级开发者亦避旧内核、最新 LTS 最可信，而前端摄像头多跑旧 vendor 树；Eduardo Valentin 新开线程倡改进 CVE 补丁标注：信息游离树外、有无 CVE 参差、需合入后补注、预备系列难辨所需补丁；Jiri Kosina 认 SSBD／L1TF 本次沟通良好，痛在难纳入他人（如 BPF 方、GregKH 耗时两月），问是否因披露方与其无 NDA

**史料**：`349237`、`349241`、`349251`、`349254`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349237 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349241 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349251 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349254 -->` 

**史观**：法律与道德是利益分配（总纲第 13 条——法律与道德是利益分配：Dave Hansen 的“论 NDA：企业实仅需掌控信息之感，社区正示其非唯一工具，望 Intel 等非 NDA 方共享方法，LF 或可居间”与 Jiri Kosina 的“认 SSBD／L1TF 本次沟通良好，痛在难纳入他人（如 BPF 方、GregKH 耗时两月），问是否因披露方与其无 NDA”并置，实为信息掌控权与协作成本的分配）；知识注定过时（总纲第 22 条——知识注定过时：Eduardo Valentin 的“新开线程倡改进 CVE 补丁标注：信息游离树外、有无 CVE 参差、需合入后补注、预备系列难辨所需补丁”，正是对抗安全知识散失的机制设计）
**辨析**：Eduardo Valentin 的“论 vendor 树令回移植更噩梦，顶级开发者亦避旧内核、最新 LTS 最可信，而前端摄像头多跑旧 vendor 树”为其经验归因；Jiri Kosina 的“问是否因披露方与其无 NDA”为待答之问，本页未见答复。本块例数少而议题跨度大，四封各开一面，未作汇总裁断。
**文献**：DSLXC-5960、DSLXC-5964、DSLXC-5974、DSLXC-5977（`ksummit-discuss.messages.349237`、`ksummit-discuss.messages.349241`、`ksummit-discuss.messages.349251`、`ksummit-discuss.messages.349254`，2018-09-10、2018-09-10、2018-09-11、2018-09-11），全文见 `raw_source.raw_json`

## 46.6 【Linux社区】staging 之弊、API 弃用检查与 2014 档案四封（7 例）

**要点（判定表逐字）**：Laurent Pinchart 论 staging 之弊：Intel 一次性倾泻 atomisp 大驱动后弃之腐化，git show 显示九百二十文件二十万余行新增，社区无力代劳；Mauro Chehab 析 staging 之 atomisp：提交者本欲维护，然 Spectre 与 Meltdown 事后转岗；主张入 staging 者须有人愿循上游规则否则可弃；Guenter Roeck（2014 档案）以 make C=1 跑 sparse 再跑 smatch（内核项目）做静态检查，说明个人用法；Mark Brown（2014 档案）就 PM 依赖指出核心设备探测被延至依赖就绪后才挂起，而异步挂起会破坏此假设；Wolfram Sang（2014 档案）用 C=1 CHECK 指向 ninja-check 包装调用多静态分析器，建议把 sparse 与 smatch 自动纳入 C=1；Laurent Pinchart（2014 档案）论 V4L 以显式电源管理 API 供子设备（slave）调用，但主从与 inter-slave 依赖仍未妥善解决；Jani Nikula 就 API 替换／弃用提议藉 make W=n 启用额外 gcc 检查，类比 allmodconfig 与 allyesconfig 目标容纳额外维护者逻辑

**史料**：`349216`、`349246`、`349212`、`349223`、`349234`、`349245`、`349253`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.349216 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349246 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349212 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349223 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349234 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349245 -->` `<!-- ROW_MINE: ksummit-discuss.messages.349253 -->` 

**史观**：分离聚合是永恒规律（总纲第 4 条——分离聚合是永恒规律：Laurent Pinchart 的“论 staging 之弊：Intel 一次性倾泻 atomisp 大驱动后弃之腐化”与 Mauro 的“主张入 staging 者须有人愿循上游规则否则可弃”同向，正是暂存树与子系统之间的分合相位）；一切真历史都是古代史（总纲第 1 条——一切真历史都是古代史：2014 年的静态检查用法、PM 依赖、V4L 电源管理三线档案被 2018 年讨论重提，正见旧议题的当代性）
**辨析**：Laurent Pinchart 的“git show 显示九百二十文件二十万余行新增，社区无力代劳”为可核之规模实况；Mauro 的“析 staging 之 atomisp：提交者本欲维护，然 Spectre 与 Meltdown 事后转岗”为对腐化成因的归因；Guenter Roeck 的“以 make C=1 跑 sparse 再跑 smatch 做静态检查”、Wolfram Sang 的“用 C=1 CHECK 指向 ninja-check 包装调用多静态分析器，建议把 sparse 与 smatch 自动纳入 C=1”均为个人用法之陈；Jani Nikula 的“藉 make W=n 启用额外 gcc 检查，类比 allmodconfig 与 allyesconfig 目标容纳额外维护者逻辑”为其机制提案。本块含 2014 年档案四封，与 2018 年主线不同期，属跨期并置。
**文献**：DSLXC-5939、DSLXC-5969、DSLXC-5935、DSLXC-5946、DSLXC-5957、DSLXC-5968、DSLXC-5976（`ksummit-discuss.messages.349216`、`ksummit-discuss.messages.349246`、`ksummit-discuss.messages.349212`、`ksummit-discuss.messages.349223`、`ksummit-discuss.messages.349234`、`ksummit-discuss.messages.349245`、`ksummit-discuss.messages.349253`，2018-09-10、2018-09-11、2014-05-14、2014-05-14、2014-05-14、2014-05-14、2018-09-11），全文见 `raw_source.raw_json`

---
注：本文件由判定表程序化生成（6 块，覆盖 50/50 CAND，两遍计数核对通过）；要点逐字取自判定表“要点”列（主代理全读审读实录），史料锚与 CAND 一一对应，全文以 raw_source.raw_json 为准。
