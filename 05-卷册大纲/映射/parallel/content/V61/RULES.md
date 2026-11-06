# Task 8.4 判读规程卡（V61“BSD 分支的安全工程：防线、漏洞与响应”卷批）

> 本卡是本会话（主代理，单写者，**不使用子代理**）的判据来源。目标、非目标、验收判据见同目录
> `00-意图确证.md`，不得改写；手段可自选。
> 批次：Task 8.4（V61 全卷 7 章 88 节 440 题；料域 59 件、1,509 块，分五片）。
> 生成：2026-11-06。

## 一、你在做什么

旧树 59 件子节（POSIX／C／RFC 标准遵守史、FIPS-140、合规争议等料域，见 `parts.tsv`）共
1,509 个机器块。这些块是**语料**，不是小节。逐块判读，判定它归入 440 个已批论题中的哪一个；
不能归入者按阶梯处置（§四）。

**禁止由史料反推结构**（J0）：440 题已由标题线批准并落纲（`approved/V61.title.ok`，
`ledger_sha256=f4ba994d…` 与 `title-design/V61.tsv` 现字节一致），只做归属，
不改题、不增题、不并题、不拆分节。

## 二、输入

| 件 | 路径（相对仓库根） | 用法 |
| --- | --- | --- |
| 440 题清单 | `05-卷册大纲/映射/parallel/content/V61/titles.tsv` | `subsection_id／title／thesis／source_count／sources／order`；thesis 是归属第一判据 |
| 分片清单 | `05-卷册大纲/映射/parallel/content/V61/parts.tsv` | 按 `part` 列筛出本件；`block_count` 为该件块数 |
| 块档 | `05-卷册大纲/映射/parallel/content/V61/part<K>.blocks.jsonl` | 每行一块：`rowmine_id／source_file／block_seq／kind／evidence_level／bytes／sha256／text` |

块形态：`<!-- ROW_MINE: … -->` 头＋“**当事人自述**（证据等级：Lx，来源：…）”样板行＋摘要正文；
另有 `MAIL_INSIGHT`、`DEEP_ANALYSIS`、`NEWREF`、`DB_REF`、`DB_POINTS` 块，同样逐块处置。

## 三、七章论题边界（归属的硬边界）

| 章 | 章题 | 收什么 | 不收什么 |
| --- | --- | --- | --- |
| 1 | UNIX 网络化与现代安全工程的形成（1988–1995） | 超级用户／UID-GID／setuid／受信主机／口令文件；联网攻击面；sendmail／fingerd／rsh 漏洞；Morris 蠕虫事件与技术解剖；早期信任缺陷；CERT／CC 与响应制度；披露制度（全披露／协调／CVE）；BSD 进入现代安全体系 | 具体标准合规流程（V62）、法律条文（V72） |
| 2 | BSD 安全工程共同基础 | UID-GID 权限、chroot、securelevel、ACL、MAC、rlimit、内存保护、审计日志、文件完整性、磁盘加密、随机数与 PKI、软件签名 | 安全模型理论（第 3 章）、跨 BSD 比较（第 5 章）、具体漏洞案例（第 6 章） |
| 3 | 安全模型理论 | Bell–LaPadula、Biba、Clark–Wilson、Chinese Wall、参考监视器／TCB、DAC-MAC-RBAC、能力模型与最小权限 | 具体实现（Ch2／Ch4）、BSD 分支差异（Ch5） |
| 4 | 现代防护机制 | jail／sandbox、内存安全与执行保护、W^X／ASLR、CFI、模糊测试、形式化验证、安全启动、CHERI／BERI、编译期缓解、Capsicum／CloudABI、后量子迁移 | 纯理论（Ch3）、历史事件（Ch1） |
| 5 | 跨 BSD 比较 | DAC-MAC、能力、jail／sandbox、pf／ipfw／NPF、W^X、完整性、密码设施、供应链、安全默认、pledge-unveil vs Capsicum、历史原因、FreeBSD／NetBSD／OpenBSD／DragonFly 路线、安全文化、与 Linux／Windows／Solaris／macOS 比较 | 单一分支实现细节（Ch2／Ch4） |
| 6 | 漏洞与响应 | 权限提升、内核内存破坏、用户空间、信息泄露、网络协议（含 TCP SACK 2019）、文件系统、隔离边界、虚拟化、认证、第三方组件与供应链事件、补丁与回归、安全公告体系、第三方库响应 | 披露制度史（Ch1）、史料形态（Ch7） |
| 7 | 安全史料与史学 | 公告体例、CVE 与漏洞数据库、提交历史、补丁与版本树、安全官团队记录、审计报告、数量统计局限、用户规模与暴露面、目标与实际、证据边界、连续性与分化 | 具体漏洞技术细节（Ch6）、制度形成（Ch1） |

**歧义裁决顺序**：①块的主对象属于哪一类（制度／机制／理论／比较／漏洞／史料）；②该对象在
440 题中的唯一归属；③仍歧义看块的时代与场合（哪年、哪个邮件列表、哪次公告），取最贴近者；
④实在无法归属按 §四 处置并在 reason 写明，**不得硬塞**。

## 四、处置阶梯（逐块择一）

| 处置 | 含义 | 何时用 |
| --- | --- | --- |
| `归入` | 进入对应论题小节 | 默认；块主题与该题 thesis 同类 |
| `辑存` | 同件多个低价值同质块合为一件，不逐块设小节 | reason 写“辑存组：<组名>” |
| `移出` | 确属他卷／他节论题 | reason 须写建议宿主（如 `V62-2.1`、`V72-1.3`） |
| `挂账` | 该小节容量已满（≤12 块），或暂无法定位 | reason 写“容量已满（第 N 块）”或“待定位：<理由>” |
| `删除` | 仅限零内容块（空块、纯签名、退订启事、纯转载无内容） | reason 写“零内容：<类型>”，并抄 bytes 与 sha256 前 12 位 |

**容量规则**：同一 `subsection_id` 收到超过 12 块时，第 13 块起一律 `挂账`。
**同类率**：同一小节的 `归入` 块须主题同类（J1 ≥80%）；异质块改 `移出`／`挂账`，不得凑数。

## 五、输出

`05-卷册大纲/映射/parallel/content/V61/part<K>.tsv`（本会话由决定清单 `script/_dec_V61_P<K>.txt`
经 `_t8_mkledger.py` 生成，不由人手抄表）：

```
rowmine_id	subsection_id	title	action	reason
```

行数守恒：每片输出行数＝该片块数，每块出现且仅出现一次（合并器 `_t8_merge.py` 硬验）。

## 六、硬约束

1. 不撰写正文；`reason` 只写判据，不写赏析。
2. 不新拟题名；`title` 只能逐字取自 `titles.tsv`。
3. 不改 `title-design／title-evidence／approved` 任何文件。
4. 禁直角引号（U+300C／U+300D／U+300E／U+300F）；引文用弯引号；禁不可见字符。
5. 块内容涉及技术结论时只判“主题归属”，不判“结论真伪”。
6. 不跑 `git add`／提交（提交由卷批收口统一做）；不写其他卷目录。
