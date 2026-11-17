# TUHS utree 1BSD 页（ref10864 复用卡）

- **性质**：复用件卡（不建新 ref）。ref10864＝TUHS Unix Tree 1BSD 卷目录页，V35 线 2026-11-16 登记（原卡 `20261116_TUHS_1BSD_page_ref-new.md`；raw_source 表定 official_doc／layer3）。
- **原 claim 引用面**：V35-p2-b012 EV-SUP-002204 引页面述介段（“1BSD was Bill Joy's first Berkeley Software Distribution. Th…”）。
- **本批（supp-V12-b007）引用面**：异段异锚，零冲突——
  1. 目录列表行（1bsd-archive#dirlist）：READ_ME 6833 1977-11-23／TAPE 426 1977-11-23／UPDATE 59 1977-11-23／ashell dir／assubs dir／bin dir／…／ex-1.1 dir／…／man1 dir
  2. README 自述三段（1bsd-archive#readme）：“This tape includes sources and binaries for a quantity of UC Berkeley software.”／“The major items on this tape are the instructional Pascal system and the text editor "ex".”／“Machine readable documentation is included for all programs.”
- **考据注**：READ_ME／TAPE／UPDATE 三件档案戳 1977-11-23（1bsd.tar.gz 馈赠件元数据，经 utree 界面渲染）；1bsd.tar.gz 捐者 Keith Bostic 或 Kirk McKusick。档案戳只作“该件标注”，不用于判定首版发行时点（诸说披露见 V12 b006 批记）。页面文本经剥标签＋空白归一后逐字核验（script/_v12/_b007_tuhs_page.txt）。
- **本批落点**：V12.2.1.5／V12.2.1.6 各一块（#url）
- **考据日期**：2026-11-17（supp-V12-b007；official_doc 表定抬头／L3）

## b017 追加段（2026-11-18，supp-V12-b017）

- **本批（supp-V12-b017）引用面**：READ_ME 正文四句（utree.pl?file=1BSD/READ_ME 实取，剥标签＋空白归一，直引号与标点照录），异段异锚，零冲突——
  1. Pascal 硬件依存句（1bsd-archive#readme-dep-iandd）：“The Pascal system requires separate I/D space; that is, an 11/45 or 11/70 host. To run the Pascal stuff right away you will also need floating point hardware”
  2. ex 版本依存句（1bsd-archive#readme-ex-v6）：“The binaries in "ex" will run directly on standard or Berkeley-type version 6 UNIX systems.”
  3. install 起动面句（1bsd-archive#readme-install）：“The suggested way to bring up the software on this tape is to run the install scripts in "pi", "pxp", and "px", and to then install (some or all) of the software from "bin".”
  4. ex 数据库依存句（1bsd-archive#readme-ex-db）：“The editor "ex" can also be installed... this requires probably as much work as all the others combined as it uses some data bases which don't exist on standard UNIX relating to terminal types and capabilities.”
- **考据注**：四句均在 READ_ME 正文 .SH 小节内（Pascal／Ex／Installing the software），支撑 V12 2.7.2（依存关系）与 2.7.3（结构含义）两题两面。引文逐字照录，READ_ME 原文的省略号（"installed..."）为原文自带，非引者截断。取源时点 2026-11-18，TUHS utree 界面渲染页（页脚档案戳 1977-11-23）。
- **本批落点**：V12.2.7.2／V12.2.7.3 各两块（#url、#2）
- **考据日期**：2026-11-18（supp-V12-b017；official_doc 表定抬头／L3）

## b018 追加段（2026-11-18，supp-V12-b018）

- **本批（supp-V12-b018）引用面**：目录页捐赠者句（1bsd-archive#donor-two-claims），异段异锚，零冲突——
  1. 捐赠者两说句（1bsd-archive#donor-two-claims）：“The files here come from 1bsd.tar.gz, donated by either Keith Bostic or Kirk McKusick.”
- **考据注**：TUHS 述介对 1bsd.tar.gz 的捐赠者给出 Bostic 或 McKusick 两说（either…or 原文并列），归属归属复原止于两说披露、不择一为定。与 b017 追加段四句同为 utree 卷页文本（剥标签＋空白归一）。
- **本批落点**：V12.2.8.6 一块（#url）
- **考据日期**：2026-11-18（supp-V12-b018；official_doc 表定抬头／L3）
