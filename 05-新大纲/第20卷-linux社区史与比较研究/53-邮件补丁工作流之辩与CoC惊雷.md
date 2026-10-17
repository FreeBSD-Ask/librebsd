# 53 【Linux社区】邮件补丁工作流之辩与CoC惊雷

> 来源：ksummit-discuss p105（50 封全读，2018-09-17/18，夹杂 KS2014 档案信 2014-05-03/15）。
> 判定：50 CAND / 0 NV。主题分布：communication 28、distro-bugzilla 7、coc 6、KS2014 6、EXPORT_SYMBOL_GPL 1、stable-ml 1、Banbury 1。

## 【Linux社区】零、体例说明

本文件系 ksummit-discuss p105（pk 349456-349505）的逐封提取（50 CAND / 0 NV），全 6 块采用**导语＋带锚条目体例**：每块由“## 53.x 【Linux社区】题名”＋导语段＋“- 【Linux社区】… ROW_MINE 来源坐标”条目构成，不逐块展开要点、史料、史观、辨析、文献五字段。取舍依据：本层为页面级逐封索引——导语段承担“要点”职能、带锚条目承担“史料”与“史料锚”职能（ROW_MINE 坐标与 claim 库 source_ref 一致，可反查去重）；史观、辨析、文献三项不在本层给出，其著录须回 claim 库逐封核对后另行落盘，本层不重复、不臆补（00-总览 §一.2 的五字段标准适用于正式入卷块）。块内叙述仅为当事人原话的转述与节选，史家判断不在本层给出。

## 53.1 【Linux社区】CoC 惊雷：仓促、阴谋论与“罐头已开”

2018-09-18 ksummit-discuss CoC 议题正式立项：五种立场同页——立项者 Airlie、牵头者 Rostedt、接受者 Bottomley、忧虑者 Vetter、程序性问责者 Geert。

- 【Linux社区】Airlie 提新议题 CoC and Linus position：Chatham House Rule 或不记录不公开的敏感场、Linus 录像后烧毁以安抚不知情维护者；“也可以把盖子钉回去” `<!-- ROW_MINE: ksummit-discuss.messages.349465 -->`
- 【Linux社区】Rostedt 支持上 Maintainer Summit、当面比邮件有效；愿牵头（“不知道我为何总这样对自己”）；“罐头已开虫已放” `<!-- ROW_MINE: ksummit-discuss.messages.349476 -->`
- 【Linux社区】Bottomley：现行列表治理已与新 CoC 相近；宁做根管也不辩论修 CoC，够用就上路 `<!-- ROW_MINE: ksummit-discuss.messages.349477 -->`
- 【Linux社区】Vetter 惊讶速度：fd.o CoC 走了数年共识、这次约 10 天；阴谋论四起；担忧过快变革压垮社区消化力 `<!-- ROW_MINE: ksummit-discuss.messages.349481 -->`
- 【Linux社区】Vetter 回 Bottomley：“多年坚持没什么可讨论”正是走到今天的原因，此策略不可持续 `<!-- ROW_MINE: ksummit-discuss.messages.349482 -->`
- 【Linux社区】Geert：Code of Conflict commit ddbd2b7ad99a418c 曾获 66 人 ack、大改动应 CC 原 ack 者“显然这次没有” `<!-- ROW_MINE: ksummit-discuss.messages.349483 -->`

## 53.2 【Linux社区】邮件工具地狱：Sony 防钓鱼重写与“附件派”之争

企业邮件环境与补丁工作流之辩的白热化：Sony URL 重写实录（proofpoint 链接原文留档）、附件派（Luck/Bird）与正文派（Torokhov/Brown）对峙、Linus 的 patchwork 语义网关构想与 Konstantin 的 web 提交流程草案。

- 【Linux社区】Brown：Outlook 把一切翻译成内部格式之脆；忆 Tim Bird 曾提企业内部部署可审计 VM 邮件服务 `<!-- ROW_MINE: ksummit-discuss.messages.349488 -->`
- 【Linux社区】Tony Luck“惊悚”提议：一次性贡献者补丁放附件即可，Outlook 通常不动附件 `<!-- ROW_MINE: ksummit-discuss.messages.349491 -->`
- 【Linux社区】Torokhov 反驳：附件补丁难按行评论，“我可不愿” `<!-- ROW_MINE: ksummit-discuss.messages.349492 -->`
- 【Linux社区】Tim Bird：Sony 防钓鱼系统重写全部邮件 URL——补丁杀手；“邮件是可靠文本投递服务”的假设越来越不成立 `<!-- ROW_MINE: ksummit-discuss.messages.349493 -->`
- 【Linux社区】Konstantin：有 kernel.org 账户可用 mail.kernel.org 出站 `<!-- ROW_MINE: ksummit-discuss.messages.349494 -->`
- 【Linux社区】Tim Bird 谢绝个人解：刻意走 IT 通用工具以体察同事障碍、找通用解 `<!-- ROW_MINE: ksummit-discuss.messages.349495 -->`
- 【Linux社区】Tim Bird：附件法正是我测试项目所用；建议 ML 软件并入附件正文或 git am 支持附件 `<!-- ROW_MINE: ksummit-discuss.messages.349497 -->`
- 【Linux社区】Tim Bird 自嘲：故意留着 proofpoint URL 重写让诸位看看我的痛 `<!-- ROW_MINE: ksummit-discuss.messages.349498 -->`
- 【Linux社区】Linus（休假中答信）：patchwork 不正是干这个的？附件解耦 charset/MUA；DKIM 使纯邮件网关不行、须高语义层网关；“trivial 是个完全用错的词” `<!-- ROW_MINE: ksummit-discuss.messages.349499 -->`
- 【Linux社区】Brown：附件可行但评论体验差、对积极参投的公司不可扩展 `<!-- ROW_MINE: ksummit-discuss.messages.349500 -->`
- 【Linux社区】Brown 回应 Woodhouse：“Outlook 是坨屎”之说对被强用 Outlook 的人是空谈 `<!-- ROW_MINE: ksummit-discuss.messages.349502 -->`
- 【Linux社区】Woodhouse 原话：“Outlook is a pile of crap, but Exchange itself works tolerably”；玩笑提 EWS 后端 `<!-- ROW_MINE: ksummit-discuss.messages.349503 -->`
- 【Linux社区】Sean Paul：chromium.org 开 DMARC 三周、邮件全进 Spam 而无人知——静默失败 `<!-- ROW_MINE: ksummit-discuss.messages.349504 -->`
- 【Linux社区】Konstantin 构想“想象中的 web 工具”：开户/验邮箱/教补丁/checkpatch/get_maintainer/代发——能解问题还是添麻烦？ `<!-- ROW_MINE: ksummit-discuss.messages.349505 -->`

## 53.3 【Linux社区】SCSI 树 rebase 之辩与 topic 分支实录

Distribution kernel bugzillas considered harmful 线程的 SCSI 技术层：rebase 动因（测试覆盖不足+整系列撤下）、topic 分支三条实践证言（Brown/Geert 提议/hch 与 Axboe 的失败史）。

- 【Linux社区】Petersen 长文：git patch-id 跨树跟踪优于 commit id；SCSI 无综合测试设施、0day 常只测 x86_64；三选项（恒 revert/scsi-staging/rc4 后不 rebase）；0day 与 linux-next 是命脉 `<!-- ROW_MINE: ksummit-discuss.messages.349475 -->`
- 【Linux社区】Geert 建议 topic 分支（core+每驱动/厂商）+ for-next 每日合并；忆 Brown“章鱼合并”遭 Linus 嫌 `<!-- ROW_MINE: ksummit-discuss.messages.349480 -->`
- 【Linux社区】Petersen 答：SCSI core 改动仅占百分之几不值分树；真有效须每驱动一支“大锤” `<!-- ROW_MINE: ksummit-discuss.messages.349484 -->`
- 【Linux社区】hch：早给 SCSI 树做过 core/drivers 分树、完全行不通——core 改动多由驱动所需 `<!-- ROW_MINE: ksummit-discuss.messages.349486 -->`
- 【Linux社区】Jens Axboe 证实：NVMe 常驱动 core 变更故分树有害；现特性依赖减少、愿重启 `<!-- ROW_MINE: ksummit-discuss.messages.349487 -->`
- 【Linux社区】Brown 自述：-next 为各 topic 分支自动合并、坏分支整个丢弃；曾因 Linus 嫌分支多而停用 `<!-- ROW_MINE: ksummit-discuss.messages.349489 -->`
- 【Linux社区】Brown：topic 分支多为每驱动一支、内嵌跨树嵌入式改动；core 改动叠同支或并入驱动支 `<!-- ROW_MINE: ksummit-discuss.messages.349496 -->`

## 53.4 【Linux社区】邮件替代方案的攻防续局

通信系统之辩的攻防续局：Mauro 的单一模型反对论、hch-ACPI 指控的澄清（ACPICA 上游实情）、moderated 数字之纠（221→32）、public-inbox/lore.kernel.org 的历史意义与企业环境三重印证。

- 【Linux社区】Mauro 回 Pinchart：需求清单未强制邮件；不应强制单一模型；高流量子系统迁移须保邮件流不破；git log 才是最持久记录 `<!-- ROW_MINE: ksummit-discuss.messages.349457 -->`
- 【Linux社区】Mauro 回 Geert：linux-arm-kernel 对自己也延时放行；get_maintainers 命中+人工放行即可 `<!-- ROW_MINE: ksummit-discuss.messages.349458 -->`
- 【Linux社区】Rafael 答 hch ACPI 指控：那是 ACPICA 独立上游、补丁应先投上游 `<!-- ROW_MINE: ksummit-discuss.messages.349459 -->`
- 【Linux社区】Rafael 补充：ACPICA 也收邮件补丁、但须针对上游代码库 `<!-- ROW_MINE: ksummit-discuss.messages.349460 -->`
- 【Linux社区】Airlie 反向提醒：git send-email 对新人不易（gmail+公司不开 smtp）、别以为邮件流程对新手简单 `<!-- ROW_MINE: ksummit-discuss.messages.349461 -->`
- 【Linux社区】Joe Perches 纠正 221 数字：去重后仅 32 条 moderated、几乎都有公开档案 `<!-- ROW_MINE: ksummit-discuss.messages.349462 -->`
- 【Linux社区】Bottomley：自己不用 git-send-email（format-patch+evolution） `<!-- ROW_MINE: ksummit-discuss.messages.349464 -->`
- 【Linux社区】Nicolas Ferre 印证：企业环境下 git send-email 部署之仗反复重打 `<!-- ROW_MINE: ksummit-discuss.messages.349466 -->`
- 【Linux社区】Geert 印证：跨公司协作也有人被企业环境挡在协作工具外 `<!-- ROW_MINE: ksummit-discuss.messages.349468 -->`
- 【Linux社区】Vetter 问 Bottomley：除裸 diff 明文邮件外还有什么方式走邮件列表 `<!-- ROW_MINE: ksummit-discuss.messages.349469 -->`
- 【Linux社区】Biederman：single point of failure 仍相关；推介 public-inbox 与 lore.kernel.org——LKML 全档进笔记本 git 库、git-grep 胜 web 搜索 `<!-- ROW_MINE: ksummit-discuss.messages.349471 -->`
- 【Linux社区】Pinchart 提议 git-send-gmail/git-send-outlook 脚本 `<!-- ROW_MINE: ksummit-discuss.messages.349472 -->`
- 【Linux社区】Bottomley 答 Vetter：format-patch+evolution 不难、指向 **email-clients.rst** `<!-- ROW_MINE: ksummit-discuss.messages.349473 -->`
- 【Linux社区】Randy Dunlap：系列用 git send-email、单补丁用邮件客户端 `<!-- ROW_MINE: ksummit-discuss.messages.349485 -->`

## 53.5 【Linux社区】EXPORT_SYMBOL_GPL 判据与 stable 机器学习与 Banbury 异步 I/O

三笔技术要点收束：_GPL 的“Linux 独有”判据、stable 树机器学习议题立项、Banbury 的文件系统异步 I/O 错误上报维度。

- 【Linux社区】Rostedt 判据：Linux 独有功能应 _GPL（trace 全系 _GPL）、跨 OS 通用功能（request_irq）可 EXPORT_SYMBOL `<!-- ROW_MINE: ksummit-discuss.messages.349474 -->`
- 【Linux社区】Sasha Levin 与 Julia Lawall 提 stable 机器学习议题：ML 识别 bug 修复提交、已向 stable 树提交逾千补丁 `<!-- ROW_MINE: ksummit-discuss.messages.349463 -->`
- 【Linux社区】Reinecke 反驳 Banbury“用户态为主”：多数文件系统无法向应用直接报 I/O 错误；建议异步上报如 DAX；次年 LSF 续议 `<!-- ROW_MINE: ksummit-discuss.messages.349470 -->`

## 53.6 【Linux社区】KS2014 档案六封

页内夹杂的 KS2014 档案信（2014-05-03/15）：ARM minisprint 提议、2038 嵌入式展望、统一资源 API 之难、QR oops 技术细节、kmemleak 开销之辩。

- 【Linux社区】Grant Likely：ARM legacy DT conversion 宜作 minisprint 不作主 summit；minisummit 易沦为纯 DT 会 `<!-- ROW_MINE: ksummit-discuss.messages.349456 -->`
- 【Linux社区】Likely 回 hpa 2038：0.25 美元 32 位 MCU 跑 Linux 且联网、“部署后永不更新”之叹 `<!-- ROW_MINE: ksummit-discuss.messages.349467 -->`
- 【Linux社区】Brown：统一资源管理 API 之难——设备与系统 PM 整合两固件体系差异大 `<!-- ROW_MINE: ksummit-discuss.messages.349478 -->`
- 【Linux社区】Kurusa：QR oops 尺寸 100x100~150x150、MicroQR 扫描 app 多不支持（NeoReader 实测）、80x50 半块字符与 U+2580-259F 之议 `<!-- ROW_MINE: ksummit-discuss.messages.349479 -->`
- 【Linux社区】Catalin Marinas：kmemleak 重启用 NACK 之由与降开销替代方案 `<!-- ROW_MINE: ksummit-discuss.messages.349490 -->`
- 【Linux社区】Jason Cooper 同意 ARM platforms minisprint `<!-- ROW_MINE: ksummit-discuss.messages.349501 -->`
