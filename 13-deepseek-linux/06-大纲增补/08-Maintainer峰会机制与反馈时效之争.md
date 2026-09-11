# 08-Maintainer峰会机制与反馈时效之争.md

> 对应页面：ksummit-discuss p73（pk 347856-347905，2017-04-20/26 连续讨论 45 封 + KS2014 混档 5 封）
> 判定：50 CAND / 0 NV（本页无纯出席确认信）
> 编号：DSLXC-4078..4127 | claim 已入库（50/50，dslinux_claims.duckdb）

## 8.1 净收益阈值与文件搬移代价

**要点**：Bottomley 提出「净收益阈值」把关（接受补丁多因看似无害但无用户可见收益）；Corbet 辩护文档重组（面向受众成册手册）；Bottomley 澄清立场（成本 vs 收益先评估、refactor 自带门槛）；Dobrybn 系统调用表/drivers-net 目录 UX 实证；Ingo 修正 syscall 表只搬过一次。

**史料**：`347856、`347859、`347860、`347862、`347866

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347856 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347859 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347860 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347862 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347866 -->` 

## 8.2 CI 与测试基础设施

**要点**：Dan Williams：0day+linux-next 非充分 CI，cmock mock 化打硬件路径，测试发现/判定「干净运行」痛点；Brown：kernelci（Kevin Hilman）与 Linaro 自动化、测试 miniconf 呼声、discoverability 问题。

**史料**：`347863、`347867

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347863 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347867 -->` 

## 8.3 distro 与 semi-distro 视角

**要点**：Brown 论 longterm 与更新意愿（Debian 排期+缺意愿+业务模型）；Ledford Fedora 无痛、RHEL 才是痛并修正代言立场；Chris Mason（btrfs semi-distro）：大部分平稳、性能回归怪自己基准。

**史料**：`347861、`347864、`347865、`347891

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347861 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347864 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347865 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347891 -->` 

## 8.4 patchwork 通知标准化与维护者脚本

**要点**：Belloni 指出 MAINTAINERS B: 未被推广、patchwork 通知仅账号者；Julia 更正（无账号也收）；Sang：可配置全列表（ozlabs 先例）；Ellerman：通知应发原收信列表、便捷我也用 git-notes；Mauro：linuxtv 默认全列表、附 post-receive mailbomb Perl 脚本全文；Bottomley 附同类脚本+错误发送前科。

**史料**：`347871、`347872、`347873、`347874、`347875、`347877、`347878、`347880、`347881、`347882、`347883

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347871 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347872 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347873 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347874 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347875 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347877 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347878 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347880 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347881 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347882 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347883 -->` 

## 8.5 sub-maintainer 名单与 co-maintainership 实践

**要点**：Belloni 自荐：coccinelle 补丁泛滥之恶（devm 转换害处）与 RTC 依赖 I2C/SPI 想早被纳入讨论；Ferre（at91）：6 年 co-maintainership 教训——非万能药、有真实缺陷限制，须谈 best practice。

**史料**：`347876、`347884

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347876 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347884 -->` 

## 8.6 不可变分支与跨树协作

**要点**：Vetter 对 arm-soc 拆树批评（bisect 落 merge、启用补丁整版延迟）；Brown 指出跨子系统问题非 ARM 独有；Olof 回应 DT/ARM（绑定先 review、冲突 quiet 惯例）；Linus Walleij：immutable topic branch 与 MFD/dt-bindings 头文件 nexus；Olof：clk per-driver 分支推回「仅为数值 define」加依赖；Brown：cross-merge 只需 sign a tag；Lee Jones：MFD 1-7 个 immutable tag 实践与硬依赖门。

**史料**：`347858、`347869、`347885、`347886、`347887、`347888、`347889

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347858 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347869 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347885 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347886 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347887 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347888 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347889 -->` 

## 8.7 反馈时效、评审机制与信任因子

**要点**：Rafael：无人认领代码、review 自愿无偿「让 review 更有回报」、比例 2/3+1/3 36-45 人；Bart 实例（block/SCSI/RDMA 快、两块慢）；Brown：老议题能否爆新意——「处在新老维护者之间的新子系统无人正向」；Guenter：obscure 子系统唯一行 view 者应获宽松；Geert 反题；Carpenter 几周 OK 几月不 OK；Petersen：简单补丁立复、复杂核心需整块时间、厂商 30+ patch 全渠前；Brown 观察「人消失/无兴趣无候选」；Kosina Reviewed-by 廉价化；Lunn：netdev 模式 NACK+拆小批教学提交者；Bottomley：信任因子与 SCSI 史式 hold-until-review 实验（mixed、仍建议）。

**史料**：`347870、`347892、`347893、`347894、`347895、`347896、`347897、`347898、`347899、`347900、`347902、`347903、`347904、`347905

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347870 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347892 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347893 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347894 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347895 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347896 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347897 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347898 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347899 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347900 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347902 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347903 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347904 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347905 -->` 

## 8.8 KS2014 档案混档（2014-05-12）

**要点**：本页 KS2014 档案信 5 封（002 QR oops 防重复/043 Energy bias CPU 解析/024 Iyer Energy 调度器条件/035 QR cut-here 行数提示/046 tinification bloat-o-meter）已入 claim。

**史料**：`347857、`347868、`347879、`347890、`347901

**史料锚**：

`<!-- ROW_MINE: ksummit-discuss.messages.347857 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347868 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347879 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347890 -->` `<!-- ROW_MINE: ksummit-discuss.messages.347901 -->` 

---
注：本文件由判定表程序化生成（8.1-8.8 共 8 块，覆盖 50/50 CAND）；要点逐字取自判定表「要点」列（审读实录），史料锚与 CAND 一一对应。
