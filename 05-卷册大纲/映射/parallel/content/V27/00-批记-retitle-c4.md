# 批记：retitle-V27-c4（第 4 章改题面，G3 全责线，2026-11-25）

> 范围：V27 第 4 章“DragonFly BSD 的再分叉（2003–2005）”8 节 40 题全改（指纹 33＋未命中 7 人判）。改题面与填充面（supp-V27-b014）分列提交（162 §15.4 允许）。意图确证＝`00-意图确证-c4-b014-20261125.md`；呈审件＝`title-design/retitle/V27-c4-呈审-20261125.md`。

## 一、题面拟定与机器自检

1. **40 题全改**：拟题依六规则（v4.1 免批）＋同期经典著作参照件（实义锚／年代锚／题长不齐／平行递进）；机器自检 `script/_g3_v27c4_titlecheck.py` **FAIL 0**——题长 8—16（极差 8）、的题 0/40、冒号 0、问句 0、逐节极差 ≥6（4.1:6／4.2:6／4.3:6／4.4:7／4.5:7／4.6:8／4.7:7／4.8:6）、构式族逐节 ≥3（5/4/3/4/5/5/5/5）。
2. **题面—thesis 预核（0 信任，ykla ch2 质量信号）**：一手锚＝DragonFly 官方 1.0 公告（Matthew Dillon 署名，2004-07-12，dragonflybsd.org mailarchive/kernel/2004-07/msg00143.html）——原文“One year after starting the project as a fork off the FreeBSD-4.x tree … our 1.0 release!”、“LWKT … separate from the dynamic userland scheduler … IPI messaging”、“retain 4.x's vaunted stability”、“start removing the BGL … threading the VFS subsystem”。三处预核：4.7.2 thesis“约两年”无一手支撑（公告为 one year），题不写死年数；4.3.1 以“二〇〇三年中自四版另立代码基”承载可考两端；4.2.3／4.4.x 限定语随填充批核。thesis 字段一律不动，缺口随填充批披露。

## 二、迁移链

1. **三台账各改 40 行**：`title-design/V27.tsv`、`design/V27.tsv`、`design/fragments/V27.tsv`；键文本一致。
2. **title.ok 重签**：`ledger_sha256=662dae6fea06ba0379934ca13ac85b41e9c11c6d44bf9639cdf2aefb1c2fc17d`（＝改后 title-design/V27.tsv 的 sha256，实测一致），`approved_at=2026-11-25`；approvals 追加 c4 行（去重防线通过，supersedes 85085b7cebc07）。
   > 历史披露：approvals 尾行 c3 记 sha 5e5914dc 为前批遗留值（已收口历史），本线不改；本批按正确语义写新 sha。
3. **40 树件改名＋H1 同步**：dry-run 与 apply 均验证节目录定位唯一、树件无重名、H1 命中 1 次、新旧不同题。
4. **outline 再生**：`premerge_keyguard.py --vol 27` PASS（键集全库一致）→ `merge_subsections.py --vols 27 --write`（40 题改、无他卷误剪；outline sha ff90df0e→f523d9ac）。
5. **SUMMARY 定点再生 40/40**：`script/_g3_v27c4_summary_patch.py`（再生器与卷根 00-总览.md 冲突沿 c3 预案，定点替换）。
6. **装配**：`assemble_index.py` 8,121,772→8,123,214 B；版本戳 `2026.11.25-14:13`；口径 75/539/3,918/19,363；`--check` 无漂移。

## 三、门禁（2026-11-25 实跑）

- 37 件 L1—L19 **19/19**（三向双射 outline=tree=summary=19,363、summary_diff=0、h1/path mismatch=0、duplicate hash=0）。
- 38 件 **3/3**（D1 vols=75 ghost=0 orphan=0；D2 mismatch=0；L land.ok 齐）。
- 39 件 **47 项 FAIL 0**（J1/J2/J3/J4 全 PASS）。
- 34 件 PASS（P1/P2 无失效、P4 著录完备、P5 主体误配 0）。
- 35 件：全库 11 处块头等级与库中真值不符（并发窗口内由 8 增至 11，属他线活跃写入）——错标文件 `3-10-3.md`／`3.10.3-*`／`3.11.1-*`（V75 样式）与 `2.2.1-*`／`2.2.4-*`／`2.5.4-*`，均非 V27 第 4 章（本线树件为 4.x.x-*），本批零新增块、V27 0 命中。
- 卷级回归 V27 **6/6**（bun；深链 top=24）。
- 题面自检 FAIL 0；assemble `--check` 无漂移；keyguard PASS。

## 四、披露

1. 35 件全库 11 处块头等级与库真值不符（并发窗口内由 8 增至 11），错标文件均非 V27 第 4 章，本批零新增块、V27 0 命中（详见 §三）。
2. 工作树他线在途（V41／V50／V61／V74／V75／outline 前 staged 改动等）一律不碰；本批 pathspec 限定提交。
3.  SUMMARY 再生器与卷根 00-总览.md 冲突属跨线议题，沿 c3 定点替换预案，未改共享脚本。
4. 填充面 supp-V27-b014（23 题 open）另批提交，章级验收合并请求。

## 五、下一站

- supp-V27-b014：第 4 章 23 题 open（4.1.3／4.1.4／4.2.2／4.2.5／4.3.2／4.3.5／4.4.2—4.4.5／4.5.4／4.5.5／4.6.1—4.6.5／4.7.4／4.7.5／4.8.1／4.8.2／4.8.4／4.8.5）联网补证落块，四账守恒后与 c4 合并提请验收。
