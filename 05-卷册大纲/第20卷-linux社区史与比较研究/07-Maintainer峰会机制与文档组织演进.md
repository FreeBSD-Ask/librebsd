# 07-Maintainer峰会机制与文档组织演进.md

> 对应页面：ksummit-discuss p72（pk 347806-347855，2017-04-18/20 爆发 42 封 + KS2014 混档 5 封）
> 判定：45 CAND / 5 NV（347809/347813/347821/347839/347854 纯出席确认或单句反问）
> 编号：DSLXC-4033..4077 | claim 已入库（45/45，dslinux_claims.duckdb）

## 7.1 【Linux社区】人数定调与首轮名单配比

**要点**：
1. Linus：人数必砍；「每人至少带一个 process pain-point + 改善建议，没有可自退为 happy」机制；20 维护者+10 下游/基建配比；top-10 名单只是 first round
2. Linus 核心名单展开：stable/next（Ben/Stephen）、基建（Korg/Wu/Rostedt/Shuah/KTD/Leemhuis/Corbet）、安全（Lutomirski/Kees/John disjoint）、distro（Laura/Jiri/Rom）；承认无法选出「叶子开发者」代表；点名想补 VFS/block/网络
3. Jiri：RHEL 内核维护者同样应出席（受 stable 影响不输 SLES），但不知人选
4. Jens Axboe：block 层自荐代表（初名单 top-20 已列）；Facebook 是大上游消费者且全额回馈，「不只发行商在用」
5. Lutomirski：问「规范性主题」，自评「sort-of 只维护东西」，拱体系议题可代表；security/arch 双代表
6. Geert：stable 回归统计——「fix 先入 head」策略下 stable 仍有回归，质疑是否有统计（反方平衡）
7. Linus 定调主题定义：仅过程议题（与子系统无关的跨切面），非技术解决方案讨论（那些归 mini-summit）；实例：security 披露规则、测试覆盖、基建自动化、无主维护区域、distro 互动

**史料**：`347806`、`347817`、`347823`、`347818`、`347828`、`347831`、`347830`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347806 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347817 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347823 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347818 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347828 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347831 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347830 -->`

## 7.2 【Linux社区】distro 与 stable 视角

**要点**：
1. Linus：Fedora/RHEL 对照——RHEL 有意滞后做 backport（"knows what it's doing"），Android 属同村但更值得谈；Fedora Laura 去年 KS 已谈过 stable 流程
2. Justin Forbes：Fedora/RHEL 双打——user stable 策略「fix 须先入 head 才进 stable」导致简单修复在 -next 排队到下一 merge window；痛点不同因两条线模型不同
3. Laura Abbott：Fedora 痛点（不同于 RHEL）——bug 报告引导不可扩展（bugzilla 194911 靠自建 bisection 摘要线才能推进、仅 2 人）、stable 更新时机不定用户难答「何时修」

**史料**：`347811`、`347814`、`347815`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347811 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347814 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347815 -->`

## 7.3 【Linux社区】sub-maintainer 名单与推进方式

**要点**：
1. Mauro：media 以 quilt 单树收 pull、sub-maintainer（Hans Verkuil/V4L2）不上 top-50；提出文档分组制议题（单书 vs 多主题分书）需峰会多维护者共议
2. Vetter：Sean/Jani 仅在讨论 group-maintainer 时有意义；drm userspace CI 雄心（每日百万测试含 pre-merge）；Android/SoC 不上游是大缺口（drm 长期缺 Android 视角直到上游+谷歌补上）
3. Shuah：kselftest 树与 mm/net/x86 冲突渐多（测试依赖走核心树导致冲突），提为 linux-next 见到的冲突样例
4. Arnd：ARM 分布式工作（pull 数虚高自陈）；sub-维护者推荐名单——DT（Rob/Rowand/Rutland）、CLK（Turquette/S.Boyd）、ARM 平台（sunxi/OMAP/Renesas/Broadcom/QC/飞）、arch 人（RMK/Marinas/Deacon）
5. Laurent：代表性缺失——过程出问题时代理维护者与开发者观点分叉，开发者无人代表；选代表难、不宜扩员
6. Mauro：通知邮件标准化「因树而异」——media 用 patchwork 通知免费，本议题不成压力

**史料**：`347807`、`347808`、`347810`、`347825`、`347816`、`347847`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347807 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347808 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347810 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347825 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347816 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347847 -->`

## 7.4 【Linux社区】圆桌与反馈机制之争

**要点**：
1. Laurent：匿名/聚合式维护者反馈机制提议（周期收集、去芜存菁、匿名提交）；维护者峰会决策是否启用
2. James：把「对着维护者开火」做成 LinuxCon EU kernel 轨的公开圆桌（人人可来抱怨）；内线过程问题 vs 外部问题分级
3. Josh：casual/occasional contributor 议题值得做（建议挂 LinuxCon）；框架锚「亲身遇到/观察到的议题」而非「random 过程主意」；峰会与展会先后顺序影响反馈吸收
4. Laurent：包办组织 casual-contributor 议题（愿提初步提案并主持）；扩展框架为「你或你代表的人亲身遇到」
5. Vetter：公开圆桌不现实——leaf 不敢公开怼维护者（怕报复）、家里利无提升、通常静静离场（abandon subsystem）；LinuxCon 寬泛受众带来「花生社员」
6. Laurent：先在线收集（含不参会者）多点反馈再给 LinuxCon EU 圆桌用材料（Vetter 论点延伸），组办积极

**史料**：`347819`、`347820`、`347827`、`347829`、`347842`、`347844`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347819 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347820 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347827 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347829 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347842 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347844 -->`

## 7.5 【Linux社区】议程提案与既往提案回响

**要点**：
1. James 议程提案：①patch 状态通知邮件标准化（commit-id/tree/维护者/列表/目标版本五要素）②kernel.org 托管 blessed 脚本集中化 ③「tasteful rebasing」准则整理 ④ 0day+linux-next 是否够格的 CI 讨论
2. Jiri：引用自己 2015-07 通知标准化提案（ksummit-discuss/2015-July/001287.html），当年无 traction——防止重复讨论
3. Jiri：Doc&lt;tab&gt; 补全断链实证（kernel-parameters.txt 消失）——Sphinx 迁移 UX 代价
4. Josh：symlinks 兼容方案（ln -s 旧路径→新路径），引 commit 852d21ae 先例
5. Jiri：反驳 symlink 案——kernel-parameters.rst 实为 include 占位（显示 Josh 自己也迷路）；pattern 不能普适
6. Josh：认错 commit 核查（只注意到 verbatim 改名没看 include 全文件）；细演示迁移误导面
7. Hellwig：文件搬移破坏个人工作流（lect 补充）——迁移代价实证

**史料**：`347822`、`347826`、`347833`、`347834`、`347836`、`347837`、`347838`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347822 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347826 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347833 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347834 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347836 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347837 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347838 -->`

## 7.6 【Linux社区】文档议题与 Sphinx 中期评估

**要点**：
1. Corbet：文档议题——责任归属不清多树抢收/冲突；Sphinx 转换中期评估与去向
2. Jani：pdfdocs build 绊在长预格式块，commit e52347b 为权宜拆分；无正式修复
3. Jani：bugzilla 服务依赖子系统、部分维护者直接无视；B: 条目（MAINTAINERS）已支持「偏好 bug 上报处」，应推广文档化；建议 bugzilla 按 MAINTAINERS 提示"多半被忽略"组件
4. Mauro：docs 冲突难避（补丁常代码+文档同寄）；一条维护者名单版图 + 每子系统一本书的主张（book 入 index + conf 后自带父树反冲突）
5. Jani：bug 报告期望文档化——reporting-bugs.rst 补全 + MAINTAINERS/FAQ/bug-writing 指往同一处

**史料**：`347832`、`347840`、`347843`、`347849`、`347852`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347832 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347840 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347843 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347849 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347852 -->`

## 7.7 【Linux社区】longterm/stable 生态与现状

**要点**：
1. Jani：kernel.org 现状 1 stable+8 longterm+1 eol——多家 longterm 信号「滞后也 OK」，早年鼓励用最新稳定 的力度更强
2. Greg：5 年最老 longterm 是 Debian 疯子排期；主题游说（上月亚洲巡讲、下月美国）+ LTS ★一年一个新 LTS 已三年
3. Jani：longterm 双刃剑——容纳旧内核「被解读为认可落后」；一年一 LTS 是对，但 lifetime 也应缩短？—— 与发行商冲突，may be 不受欢迎
4. Greg：SoC vendor 3M 行 diff 实况（我能向前移植反而被拒「不想要那描述」）；用户 stuck 旧内核所以 longterm 有价值；长期战线是减 diff 而非改措辞

**史料**：`347841`、`347848`、`347851`、`347853`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347841 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347848 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347851 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347853 -->`

## 7.8 【Linux社区】arm-soc 拆分与跨树协作

**要点**：
1. Vetter：arm-soc 拆分批评深论——drm 跨子系统靠 review 全员+acks合并单树 或 topic branch 双 pull；arm-soc 拆树毁 bisect、测试难、甚至最终启用补丁整版延迟；单入口缺失只见人（vacation/bikeshed 生态）
2. Arnd 辩护：arm-soc 拆分是设计（2.6 时代 mach-* 大同小异、单一平台主控的教训），已重分为 irqchip/gpio/pinctrl/clk 等独立子系统；跨树协调有 Kconfig 双义名、清晰 ack、共享 share tree 等做法；（补答例：bisect 维护 QA 难题）

**史料**：`347845`、`347850`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347845 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347850 -->`

## 7.9 【Linux社区】收束与展望

**要点**：
1. James 收束：峰会轮转美/欧/亚+绑定各自技术会议解决「没一个会议覆盖全员」；「赋能」观（大多数人会给机会参与）；民主比喻

**史料**：`347855`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347855 -->`

## 7.10 【Linux社区】KS2014 混档档案信（2014-05-02 / 2014-05-12）

**要点**：
1. John Linville（2014-05-02）：[CORE TOPIC]维护者树深度——tree too flat? 直接向 Linus 收 pull 报的浸润、「eaten by raptors」保险、无线树流向 Davem（二级树）；加层带来 merge latency 与新管理成本
2. Vetter（2014-05-12）：Device error isolation——完全关闭 IOMMU（单 child 设备时）或 driver notifier；drm/i915 用「GPU wedged」宣判：原子上下文可用、停用户提交降级软渲染、保留 modeset 抓活体信息
3. Roedel（2014-05-12）：IOMMU 隔离时设备可能风暴故障——应在 IOMMU 硬件层阻塞，否则 CPU 忙于 IOMMU-CPU 中断、隔离无意义
4. Preeti（2014-05-12）：Energy bias 接口——「performance/balanced/powersave」高层分类 vs 全墙旋钮导出用户态；维持权归内核；thermal 是平台安全机制 vs battery-low 省电是内核增强 UX

**史料**：`347812`、`347824`、`347835`、`347846`

【Linux社区】**史料锚**：

【Linux社区】`<!-- ROW_MINE: ksummit-discuss.messages.347812 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347824 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347835 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347846 -->`

---
注：本文件由判定表程序化生成（10 块，覆盖 45/45 CAND）；要点逐字采用判定表「要点」列（审读实录），史料锚与 CAND 一一对应。
