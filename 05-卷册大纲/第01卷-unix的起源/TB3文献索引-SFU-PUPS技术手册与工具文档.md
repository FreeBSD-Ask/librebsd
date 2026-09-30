# TB3 文献索引——SFU PUPS 技术手册、工具与安全文献（重 OCR 转录）

> **转录批次**：TB3（GLM 视觉重 OCR，2026-09-29）
> **覆盖范围**：ref 3666–3718（共 53 件，1246 页）
> **转录方法**：GLM-4.6V 视觉逐页转录，替代原 rapidocr_onnx
> **数据库状态**：**44/53 件入库**，`fulltext.extraction_method='glm_vision_20260924'`；余 9 件仍为 `rapidocr_onnx`（转录未完成）
> **key_facts**：**271 条**（id 前缀 `kf-tb3-`；technology 247 + person 24；`confidence='0.7'`；`related_chapter='第01卷-unix的起源'`）

本文件为**卷级文献索引**，按 TB4 先例（`TB4文献索引-早期UNIX文档与工具.md`）体例。
不改动任何章节正文、不引入新锚点格式、不修改 `SUMMARY.md` 与 `chapter_keywords.json`。
每条「说明」均依已入 `key_facts` 的逐字可回验引文撰写（`source_quote` 全为转录页原文精确子串）。

> **与 TB2+TB3 首批接线的关系**：3693、3698、3699、3707 四件已先期收入同卷
> `TB2+TB3文献索引-早期UNIX手册与516-TSS技术文档.md`（该文件主体为 TB2 的 516-TSS 文档）。
> 本文件给出 TB3 全批书目视图；该四件在两文件中均有条目，说明可互参。

## 文献清单

### 手册与参考指南

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3666 | 06-man4 | 26 | — | Bell Telephone Laboratories 出品。设备与驱动级手册（第四节）：收录 dp0／hp／ht／MEM(4)／rp(4)／tty(4)／KL-11 等设备条目，含 kmem 与 I/O 页地址约定（I/O 页始于 kmem 0160000） |
| 3669 | D.1.1_C_Reference_Manual | 31 | — | Dennis M. Ritchie 撰。C 语言参考手册：标识符前 8 字符有效、lvalue 定义与赋值表达式、求值顺序、赋值运算符族、条件编译与命名文件包含 |
| 3670 | D.1.2_A_Guide_to_the_C_Library | 20 | — | C. D. Perez 撰。标准 I/O 库使用指南：`fopen` 取外部名做协商后返回内部名，模式仅 r／w／a；`getc`／`putc` 等在头文件中以宏定义，不可重新声明 |
| 3674 | D.3.1_Unix_Programming | 22 | — | Brian W. Kernighan 与 Dennis M. Ritchie 撰。UNIX 编程入门：标准 I/O、预开描述符 0／1／2、`open`／`creat` 系统入口、`errno` 与 `perror`、`fork`、`pipe`、`system` 实现（`SIGINT` 置忽略以独占终端） |
| 3678 | 01_Annotated_Table_of_Contents | 10 | — | UNIX 文档卷注释目录：A 至 F 各节所列表文均适用 UNIX Release 4.0，标题后另有说明者除外；各文页数标于作者名后 |
| 3698 | F.1.1_UNIX_Operations_Manual | 26 | — | A. G. Petruccelli 撰。PDP-11/45 与 PDP-11/70 控制台操作手册（署址 Piscataway）。**此件已属 TB2+TB3 首批接线** |
| 3704 | F.5.1_UNIX_Implementation | 10 | — | Ken Thompson 撰。UNIX 实现说明，含 triple indirect 手法 |
| 3706 | F.5.3_UNIX_on_the_PDP_11_34 | 7 | 1978 | T. J. Kowalski 撰。UNIX 在 PDP-11/34 上的运行：supervisor 相关 |

### 语言与文本处理工具

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3667 | B.4.1_UNIX_Shell_Tutorial | 38 | — | G. A. Snyder 与 J. R. Mashey 撰。shell 入门教程：`sh` 是以 C 编写的普通用户程序；shell procedure 即命令文件；文件描述符 2 承载诊断输出 |
| 3668 | C.3.1_Tbl | 18 | — | M. E. Lesk 撰。troff 表格预处理程序 tbl 用户指南，含文本块语法与致谢（Gimpel、Ossanna） |
| 3671 | D.1.3_Lint | 11 | — | S. C. Johnson 撰。C 程序检查器 lint 说明：`-p`／`-h`／`-hp` 选项与 `.lnt` 库描述文件 |
| 3672 | D.2.2_Ratfor | 12 | — | Brian W. Kernighan 撰。Ratfor —— Fortran 子集预处理器：把 Fortran 子集转译为 C，`rc` 提供命令行接口 |
| 3673 | D.2.3_EFL | 36 | — | S. I. Feldman 撰。EFL（Extended Fortran Language）：过程为基本单位、六字符外部名限制、`**` 幂运算 |
| 3675 | D.4.1_Make | 9 | — | S. I. Feldman 撰。GNU make 前身：对依赖图做深度优先搜索、宏 `$*`／`$@`／`$?`／`$<`、`-i` 与 `.IGNORE`、默认后缀表（.y／.yr／.ye／.?）、命令行 `make CC=newcc` 可替换编译器 |
| 3676 | D.4.2_An_Augmented_Version_of_Make | 16 | — | S. I. Feldman 撰。扩展版 make：新增 `MAKEFLAGS`、含 `$(MAKE)` 的命令行即使设 `-n` 也执行、`.a` 库构建规则、`lib(time.o):` 成员依赖、`$%` 宏、`include` 嵌套约 16 层 |
| 3677 | D.5.1_Sdb | 9 | — | H. P. Katseff 撰。PDP-11 源级调试器 sdb：`b`／`h`／`l` 长度修饰、结构与一维数组访问、绝对地址显示、断点 `12b`／`proc:12b`、`s` 单步与 `S` 不进入被调过程 |
| 3679 | E.1.1_Lex | 19 | — | 词法分析器 LEX：由正则表达式规格生成自动机与识别器 |
| 3680 | E.2.1_M4 | 6 | — | Brian W. Kernighan 与 Dennis M. Ritchie 撰。宏处理器 m4 说明，含 `eval` 在 UNIX 上 32 位的精度约定 |
| 3681 | E.3.1_Awk | 8 | — | Alfred V. Aho、Brian W. Kernighan、Peter J. Weinberger 撰。Awk —— 为文本处理填补缺口的语言，正则表达式形式与字符串／数值一体化 |
| 3682 | E.4.1_SCCS_Users_Guide | 27 | — | L. E. Bonanni 与 C. A. Salemi 撰。SCCS 用户指南：delta／g-file／p-file／x-file 存储格式、SID 决定规则、校验和与 `what` 命令 |
| 3683 | E.4.2_SCCS_Interface_Program | 3 | 1978 | L. E. Bonanni 与 A. Guyton 撰。SCCS 接口程序说明 |
| 3684 | E.5.1_Bc | 14 | — | Lorinda Cherry 与 Robert Morris 撰。`bc` 任意精度计算器，含函数 `a(x,y)=x*y` 之例 |
| 3685 | E.5.2_Dc | 8 | — | `dc` —— `bc` 的反波兰记法调试器说明 |

### 图形与数据工具

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3686 | E.6.1_UNIX_Graphics_Overview | 7 | — | A. R. Feuer 撰。UNIX 图形系统总览 |
| 3687 | E.6.2_Graphics_Editor_Tutorial | 17 | — | A. R. Feuer 撰。图形编辑器教程；`gex` 由 D. J. Jackowski 编写 |
| 3688 | E.6.3_Stat_A_Tool_for_Analyzing_Data | 20 | — | A. R. Feuer 与 A. Guyton 撰。`Stat` —— 数据分析工具，含 `Prof` 分类 |
| 3689 | E.6.4_Administrative_Information_for_Graphics | 6 | — | R. L. Chen、D. E. Pinkston 与 A. Guyton 撰。图形系统的管理信息 |

### 远地执行与联网

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3690 | E.7.1_UNIX_RJE_Users_Guide | 7 | — | A. L. Sabsevitz 与 K. A. Kelleman 撰。UNIX 远地作业执行（RJE）用户指南：RJE 是设计为无需人工值守的自主设施 |
| 3691 | E.7.2_UNIX_RJE_Administrators_Guide | 20 | 1980 | M. J. Fitton 撰。RJE 管理指南：已安装的 RJE 子系统要求远地线登记于 `/usr/rje/lines` |
| 3692 | E.7.3_VPM_Release_1.0 | 7 | — | P. F. Long 与 C. Mee, III 撰。VPM 1.0 —— KMC11 挂接 PDP-11 或 VAX-11/780 的 UNIBUS，可成为 UNIBUS 主控 |
| 3693 | E.7.4_VPM_Release_2.0 | 20 | — | DEC 出品。VPM 2.0：在 1.0 的面向字节半双工 BISYNC 类协议之上新增面向位的全双工协议（IBM SDLC 与国际标准化 HDLC）。**此件已属 TB2+TB3 首批接线，详见同卷 `TB2+TB3文献索引-早期UNIX手册与516-TSS技术文档.md`** |
| 3694 | E.8.1_UUCP_Network | 10 | — | D. A. Nowitz 与 M. E. Lesk 撰。UUCP 网络说明 |
| 3695 | E.8.2_UUCP_Implementation | 15 | — | M. E. Lesk 撰。UUCP 实现说明：登录信息以字段与子字段序列给出 |
| 3696 | E.9.1_LP_Implementation | 13 | — | J. R. Kliegman 撰。`lp` 行式打印机守护进程实现：`lpsched` 交叉锁顺序、`-c` 选项语义 |
| 3697 | E.9.2_LP_Administrators_Guide | 12 | — | J. R. Kliegman 撰。LP 管理指南，含硬接线设备配置 |

### 文件系统、运维与安全

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3699 | F.1.2_Fsck | 20 | — | T. J. Kowalski 撰。`fsck` 文件系统检查程序：利用文件系统内冗余结构信息，依更新请求的处理次序恢复被破坏的文件系统。**此件已属 TB2+TB3 首批接线** |
| 3700 | F.2.1_UNIX_Accounting_System | 19 | — | John Mashey 撰。UNIX 记账系统：`wtmpfix` 与 `tacct` 修补，汇总记账数据为报表 |
| 3701 | F.2.2_UNIX_System_Activity_Package | 8 | — | Tsyh-Wen Pao 撰。UNIX 系统活动包：`sadc`／`sadp` 采样与快照 |
| 3702 | F.3.1_Stand_Alone_IO_Library | 11 | — | S. R. Eisen 撰。独立运行 I/O 库：`iob` 与 `mtab` 结构定义 |
| 3703 | F.4.1_ETP_Operational_Procedures | 24 | — | A. L. Chellis 与 T. J. Kowalski 撰。ETP（Error Trap Program）运行规程：错误捕获、转储与恢复 |
| 3705 | F.5.2_The_UNIX_IO_System | 7 | — | Dennis M. Ritchie 撰。UNIX I/O 系统说明 |
| 3707 | F.5.4_UNIX_Assembler | 12 | — | Dennis M. Ritchie 撰。PDP-11 汇编器 `as` 参考手册，语法大体与 DEC PAL-11R 相似但内部机制与输出格式无关。**此件已属 TB2+TB3 首批接线** |
| 3710 | F.7.1_On_the_Security_of_UNIX | 3 | — | Dennis M. Ritchie（转录署名）撰。UNIX 安全论文：挂载点与 `.mail` 符号链接类攻击面 |
| 3711 | F.7.2_Password_Security | 6 | — | Robert Morris 与 Ken Thompson（转录署名）撰。`Password Security — A Case History`：密码安全案例史 |

### 待转录（DB 内仍为 `rapidocr_onnx`，正文未替换）

| Ref | 标题 | 页数 | 年代 | 说明 |
|-----|------|------|------|------|
| 3708 | F.6.1_A_Tour_Through_the_Portable_C_Compiler | 25 | 1973 | 磁盘已转录 8/25 页，余 17 页未转录 |
| 3709 | F.6.2_A_Tour_Through_the_UNIX_C_Compiler | 15 | — | 磁盘已转录 6/15 页，余 9 页未转录 |
| 3712 | AUUGN-V01.5 | 58 | — | 磁盘已转录 2/58 页，余 56 页未转录 |
| 3713 | AUUGN-V01.6 | 84 | — | 磁盘已转录 2/84 页，余 82 页未转录 |
| 3714 | AUUGN-V02.3 | 84 | — | 磁盘已转录 2/84 页，余 82 页未转录 |
| 3715 | AUUGN-V02.4 | 84 | — | 磁盘已转录 2/84 页，余 82 页未转录 |
| 3716 | AUUGN-V03.1 | 24 | 1981 | 磁盘已转录 2/24 页，余 22 页未转录 |
| 3717 | AUUGN-V03.2 | 110 | 1981 | 磁盘已转录 0/110 页，余 110 页未转录 |
| 3718 | AUUGN-V03.3 | 112 | 1981 | 磁盘已转录 0/112 页，余 112 页未转录 |

**分页口径**：已入库 44 件共 650 页已转录替换；待转录 9 件共 596 页。

## 章节关联

本批文献主要关联以下章节（**仅为卷级索引建议，未写入 `chapter_matches` 与 `chapter_reviews`**——
后两表全库自 2026-08-15 起冻结，与 TB4 同样未接线）：

- **第 6 章 C 语言的诞生**／**第 15 章 早期编程语言与 C 语言诞生**：3669、3670、3671、3672、3673、3674、3675、3676
- **第 11 章 操作系统的谱系**：3666、3678、3698、3704、3705、3706、3707
- **第 16 章 CPP-Shell 家族与脚本语言生态**：3667、3668、3677、3679、3680、3681、3682、3683、3684、3685
- **第 18 章 小型机的诞生与 DEC-PDP 谱系**：3706（PDP-11/34）、3707（PDP-11 汇编器）
- **第 7 章 UNIX 的传播**：3690–3695（RJE／VPM／UUCP 网络化）、3696／3697（LP）
- **第 8 章 贝尔实验室的黄金时代**：3693–3707 全部为 Bell Labs 内部技术备忘录
- **安全主题（尚无独立章节）**：3710《On the Security of UNIX》与 3711《Password Security — A Case History》是本批最高价值的 L1 一手安全文献
- **待转录的 AUUGN 通讯（3712–3718）**拟落**第 18 卷**「大洋洲 BSD 社区」，见该卷「SFU PUPS 存档增补清单（待迁移）」

## 转录质量说明

- 已入库 44 件共 650 页经 GLM-4.6V 视觉逐页转录，替换原 rapidocr_onnx 结果
- 全部 271 条 `source_quote` 已逐条程序回验为所引页 `.txt` 的**精确子串**（库内行与磁盘转录逐字节一致）
- 原印件笔误照录未修（如 3670 `followes`、3671 `for various stupid reasons!`、3673 `niggleing restrictions`、3680 `GCOGS`、3685 `designed for used by`）
- 转录件在图元处插入 `[图：…]` 行内描述，属转录层附注、不属原始文档内容
- **⚠ 同卷 `TB2+TB3…md` 的 `key_facts` 计数已过期**：该文件记「154 条 `fact_category='periodical_primary'`、`confidence='2'`」，
  但活库实测 `periodical_primary` 全库仅 58 行、涉 TB3 **0 行**——原行已被 2026-09-29 19:45–19:47 的批量写入替换。

## 数据库留痕

- `fulltext`：44 件更新为 `glm_vision_20260924`（3666–3702 全 37 件 + 3704／3705／3706／3707／3710／3711）
- `fulltext_blocks`：`block_type='ocr_glm_vision'`，逐页块数与 worklist 页数一一对应
- `references.ocr_status`：44 件置 `glm_vision_reocr_20260929`（余 9 件仍 `needs_review`）；该列**不由 `merge_reocr.py` 写入**——全库 `*.py`／`*.sql` grep `glm_vision_reocr` **0 命中**，TB4 为一次性手改，本批照做并补记 `reference_update_log`（`update_type='ocr_status'`）44 行，比 TB4 多一层可追溯留痕
- `key_facts`：新增 271 条 `kf-tb3-` 行（technology 247 + person 24）；`source_block_id` 全 NULL（glm 块 id 全库为 NULL）；`related_chapter='第01卷-unix的起源'`
- `reference_update_log`：本批 96 条留痕记录 —— `fulltext_reocr` 52 条（`merge_reocr.py` 每写入一件记一条）＋ `ocr_status` 44 条
- **本文件未改动** `chapter_matches`、`chapter_reviews`、`SUMMARY.md`、`chapter_keywords.json` 与任何章节正文

## 已知缺陷与待裁定

1. ~~**`references.ocr_status` 未更新**~~ **已闭环（2026-09-29 21:xx）**：44 件已置 `glm_vision_reocr_20260929`，补记 `reference_update_log` 44 行（`update_type='ocr_status'`）。
   余 9 件（3708／3709／3712–3718）因转录未完成，仍 `needs_review`。
2. **⚠ 词频垃圾行并置**：同一批 ref 另存 735 条 `kf-batch-` 行（`fact_text` 形如 `file mentioned (30 times)`，
   `related_chapter` 全 NULL），实测 **645/735 的 `source_quote` 不是任何一页原文的精确子串**（固定字符窗从关键词首现处硬切，
   跨页窗必然落空，且窗内为半截词）。未经主理人裁决未删除。
3. **⚠ 作者署名与通行史实不符（照录未改）**：3710 转录署「Dennis M. Ritchie」，而《On the Security of UNIX》通行作者为 Morris 与 Kleiner；
   3711 转录署「Robert Morris; Ken Thompson」，而通行作者为 Thompson 与 Ritchie。转录照录所见、**未按常识改字**，待回原图裁定。
4. **转录待裁定积压**：3703 `8FD00CA1` vs `9FD00CA1`、3704 p0005 多处 hyphen、3707 p0011 `sist`／`strt`、3699 选项 hyphen vs em dash、
   3700 p0015 `pwba`／`pwn` 与 MINUTES 列求和差 1、3702 p0003 `i_flygs`、3698 p0021／22 破折号字形、3693 花括号、3695 `●` vs `*`
5. **6 处 `BLANKRUN4+`（3 空行）未闭合**：`3699_p0020`、`3701_p0008`、`3708_p0001`、`3709_p0001`、`3714_p0001`、`3715_p0001`
6. **跨行重排存量约 54 页**（3669 最集中）未清

---

**生成日期**：2026-09-29  
**转录批次**：TB3（任务书 3 / OCR3）  
**总件数**：53（已入库 44／待转录 9）  
**总页数**：1246（已转录替换 650／待转录 596）
