#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_gate_registry.py —— 第十六件门禁：门禁体系自身的元门禁。

设立缘由（2026-09-28）
----------------------
本项目反复出现同一失效模式：**“工具已文档化 ≠ 工具已生效”**。

- `markdownlint-cli2` 在 `AGENTS.md` 里写了运行命令、给了配置，却**长期未接入任何门禁**
  → 缺陷静默累积（2026-09-20 实测审计面 89 文件 5,487 条）。
- `_scan_blockfn_scope.py` 曾写出并解决了真实缺陷（严格模式致三个功能失效），却**未升格为门禁**，
  随 `script/` 临时目录一并消失。
- `serve_refactor2026.py` 标称“固定脚本，规则引用资源”，却**未登记进 `脚本与命令/README.md`、
  无任何规则文件引用**，且与另一份实现语义分叉、双双缺安全头——2026-09-28 才发现。

本件把“接线”本身变成可机检的不变量：登记表 ↔ 磁盘实况 ↔ 规则文档，三方须一致。

判据
----
R1 **存在性**：登记表内每个脚本在磁盘上存在
R2 **可编译性**：登记的 `.py` 可 `py_compile`；`.mjs` 跳过（需 node，本件不引入依赖）
R3 **无漏接线**：`脚本与命令/audit_*.py` 全部已登记（防“写了门禁忘了登记”）
R4 **有规则引用**：每个登记脚本名至少出现在 `流程规则.md`／`AGENTS.md`／
   `脚本与命令/README.md`／`05-卷册大纲/目录/tests/README.md` 之一（AGENTS.md 要求固定脚本须由规则文件引用）
R5 **套件清单一致**：标记 `in_tests_readme` 的登记件，其文件名须出现在 `tests/README.md`
R6 **自检覆盖**（仅报告）：无判据非空自检的登记件
R7 **未登记脚本**（仅报告）：规则目录内既不在登记表、也未在 README 索引的 `.py`
R8 **阶段映射**：每个登记件须在 `STAGE_MAP` 有合法 G0–G5 阶段；映射无悬空键；阶段覆盖仅报告

用法
----
    python audit_gate_registry.py                 # 0 一致 / 1 不一致 / 2 依赖缺失
    python audit_gate_registry.py --list          # 打印登记表（含阶段列）
    python audit_gate_registry.py --selftest      # 判据非空：造“漏登记 + 缺文件 + 缺阶段”夹具，须 FAIL

依赖：仅标准库。
"""
import argparse
import py_compile
import pathlib
import re
import shutil
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[3]
CMD = REPO / "00-编纂规则与格式规范" / "01-规则" / "脚本与命令"
TESTS = REPO / "05-卷册大纲" / "目录" / "tests"
RULE_DOCS = [
    REPO / "00-编纂规则与格式规范" / "01-规则" / "流程规则.md",
    REPO / "AGENTS.md",
    CMD / "README.md",
    TESTS / "README.md",
]

# ── 登记表（唯一真值） ────────────────────────────────────────────────────
# 字段：no 编号｜script 文件名（相对 REPO）｜kind 类别｜object 对象面｜
#       trigger 触发条件｜selftest 判据非空自检命令（None = 未提供，见 R6 待办）
REGISTRY = [
    dict(no="第一件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_data_integrity.py",
         kind="门禁", object="目录页 DATA 段", trigger="改 DATA 段后",
         selftest=None, in_tests_readme=True),
    dict(no="第二件", script="00-编纂规则与格式规范/01-规则/脚本与命令/sync_refactor2026_baseline.py",
         kind="门禁", object="口径声明（05-卷册大纲/目录/*.md + AGENTS.md + 规则目录）", trigger="目录页结构或计数变动后",
         selftest="--check", in_tests_readme=True),
    dict(no="第三件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_sequence_continuity.py",
         kind="门禁", object="节号／章号连续性 + 述评恒末", trigger="结构变动后",
         selftest=None, in_tests_readme=True),
    dict(no="第四件", script="05-卷册大纲/目录/tests/visual_regression.mjs",
         kind="浏览器套件", object="目录页视觉几何与功能（21 项）", trigger="改装配源后",
         selftest=None, in_tests_readme=True),
    dict(no="第五件", script="00-编纂规则与格式规范/01-规则/脚本与命令/xref_audit.py",
         kind="门禁", object="分工注交叉引用悬空", trigger="结构重编号后",
         selftest="--selftest", in_tests_readme=True),
    dict(no="第六件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_evidence_level_labels.py",
         kind="门禁", object="大纲注入块证据等级", trigger="向 05-卷册大纲 写回带等级块后",
         selftest=None, in_tests_readme=False),
    dict(no="第七件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_index_structure.py",
         kind="门禁", object="目录页结构静态自检 A/A2/B–O", trigger="目录页结构变动后",
         selftest=None, in_tests_readme=True),
    dict(no="第八件", script="00-编纂规则与格式规范/01-规则/脚本与命令/assemble_index.py",
         kind="装配器/门禁", object="四层装配漂移（逐字节）", trigger="改任一装配源后",
         selftest="--check", in_tests_readme=True),
    dict(no="第九件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_page_assets.py",
         kind="门禁", object="页面资产层（字体子集／品牌件／自包含／夹具）", trigger="改装配源或字体子集后",
         selftest="--selftest", in_tests_readme=True),
    dict(no="第十件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_markdown_lint.py",
         kind="门禁（文档格式类，独立计数）", object="活动 .md 文件格式", trigger="改闸面内 .md 后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第十一件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_server_contract.py",
         kind="门禁（服务器，独立计数）", object="运行中的目录页服务器（8 项 HTTP 契约）", trigger="改服务器脚本后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第十二件", script="05-卷册大纲/目录/tests/tri_structure_negtest.py",
         kind="负向自检", object="第七件结构判据的有效性（九种缺陷副本）", trigger="改第七件判据后",
         selftest=None, in_tests_readme=True),
    dict(no="第十三件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_fixture_freshness.py",
         kind="门禁（夹具新鲜度）", object="tests/*.mjs 写死值 vs 内容源派生值", trigger="改内容源或夹具后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第十四件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_note_xref.py",
         kind="门禁（分工注三判据）", object="卷/章/节题与分工注交叉引用的存在性（P1 引号节名＋P2 章号节号判 FAIL；P3 自指卷号列复核清单）",
         trigger="改 outline.txt 分工注或卷/章/节号后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第十五件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_person_bio_integrity.py",
         kind="门禁（人物库语义完整性，独立计数）", object="cross_indexes.person_bio_research 全表四判据（sources/doubt_flags 合法 JSON、check_date、priority；存量 outline-legacy 行豁免记 INFO）",
         trigger="人物库任何写入后（120 批 ★4 立）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第十七件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_renumber_guard.py",
         kind="门禁（改号同源守卫，独立计数）", object="outline.txt 章节同源（静态）＋改号映射引用残留（--renamed）",
         trigger="改章号/卷号或批量改号后（丁-1；87 号文 R-3 工程化）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第十八件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_page_version_bump.py",
         kind="门禁（版本号刷新兜底，独立计数）", object="HEAD vs 工作区 index.html——口径/注数变化而版本号未刷新即 FAIL（正则兼容 X.Y.Z 旧形与 UTC+8 时间戳新形）",
         trigger="每批收口（涉页面变更）后（2026-10-07 立，堵 116c 后执行缺口）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第十九件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_anchor_resolution.py",
         kind="门禁（锚解析审计，独立计数）", object="outline.txt 三键位锚（mat N→SRC-mat:N／CL-RM→EV-RM／CL-N→claim_id）解析率≥95%；悬空逐条登记",
         trigger="目录注新增 mat／CL 锚后（104 §2.1 ／ C-12·★56，2026-10-09 立；104“不可解析”结论已订正为查询格式错配）",
         selftest=None, in_tests_readme=False),
    dict(no="第二十件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_silent_loss_guard.py",
         kind="门禁（重构静默丢失守卫，独立计数）", object="T1（2026-09-19 index.html.prebak）↔T3（现行 outline）三时点比对：曾为章、现行零承接且未豁免即 FAIL；豁免 35 条带去向北键防腐烂",
         trigger="任一批次改 outline 章结构后（88 号文三时点比对法固化，C-12 批 T1.3 残余，2026-10-09 立）",
         selftest=None, in_tests_readme=False),
    dict(no="磁盘层·术语件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_disk_terminology.py",
         kind="门禁（磁盘层，独立计数）", object="05-卷册大纲/ 在效面：T1 精确词“基础系统”命中=0；T2 .md（含 .md.<后缀>）含 CRLF/孤立 CR 的文件=0（按字节判，git 面因 autocrlf 隐形）",
         trigger="任一批次改动 05-卷册大纲 后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第十六件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_gate_registry.py",
         kind="门禁（元门禁，独立计数）", object="门禁体系自身：登记表 ↔ 磁盘 ↔ 规则文档三方一致", trigger="新增/删除门禁脚本后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第二十一件", script="05-卷册大纲/目录/tests/outline_selfcheck.py",
         kind="自检（目录收口复核）", object="目录结构独立复核（A–J：卷序 7 锚／口径四源／章节号／迁移留痕；锚点失效逐项自报不中断）",
         trigger="目录批次收口后（另：改卷题后抽查；只读、秒级）",
         selftest=None, in_tests_readme=True),
    dict(no="第二十二件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_a11y.py",
         kind="门禁（浏览器）", object="目录页无障碍：axe 四组合扫描（critical/serious=0；moderate 记 INFO）＋exportMenu 键盘契约＋forced-colors/contrast/reduced-motion 三媒体分支非空转",
         trigger="改装配源或模板后（常备，随批实跑）",
         selftest="--selftest", in_tests_readme=True),
    dict(no="第二十三件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_js_blockscope.py",
         kind="门禁", object="行为源块作用域逃逸：function 具名声明于普通块内且块外存在引用（严格模式 ReferenceError 风险；豁免＝同名多声明遮蔽／形参绑定）",
         trigger="改 src/js 行为源或 doc.js 后（常备，随批实跑；wave5 H2 升格）",
         selftest="--selftest", in_tests_readme=True),
    dict(no="第二十四件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_md_quote_glyphs.py",
         kind="门禁", object="全库 Markdown 直角引号清零（U+300C／U+300D／U+300E／U+300F／U+FF62／U+FF63 出现即 FAIL；弯引号净差仅 INFO 披露——批前既有失衡属 OCR 档案逐字保真面，另案）",
         trigger="新增或改动任何 .md 后（常备，随批实跑；2026-10-17 全库转写批立）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第二十五件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_mirror_ingest.py",
         kind="门禁（Git 入库白名单）", object="05-卷册大纲/ 根级三件派生权威件（SUMMARY.md／chapter_keywords.json／theme_index.json）的跟踪与忽略状态：E1 存在／E2 `git ls-files --error-unmatch` 已跟踪／E3 `git check-ignore -v --no-index` 命中模式非否定式（`*.json` 全局忽略下的白名单豁免）／E4 不在 `git status --porcelain --ignored` 的 `!!` 清单（2026-10-21 镜像废除后改指根级）",
         trigger="根级三件再生或提交前",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第二十六件", script="00-编纂规则与格式规范/01-规则/脚本与命令/sync_outline_mirror.py",
         kind="同步器/门禁", object="大纲根级三件（SUMMARY 双射；主题索引委派 build_theme_index.py，含 theme-index/4 与 theme-reverse/2）", trigger="大纲结构变动后（批 8 / 后续重编号）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第二十七件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_keyword_index.py",
         kind="门禁", object="主题词索引 A–G 七组：schema／覆盖双射／词质（3–6、元节 1–3、禁用词、中文、补位、单主题占比、零使用）／侧面／对齐码／反查一致／尺寸"
         , trigger="主题索引再生或大纲结构／题面变动后（常备，随批实跑；2026-10-21 立）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第二十八件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_md_bold_spacing.py",
         kind="门禁", object="05-卷册大纲/ 树内 .md 加粗定界符外侧空格（T1 左边界／T2 右边界；段首行尾例外、P*/S* 标点豁免；畸形星号同修复器口径豁免）",
         trigger="新增或改动 05-卷册大纲/ 树内 .md 后（常备，随批实跑；2026-10-21 立）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第二十九件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_engineering_practice.py",
         kind="门禁（工程实践基线，独立计数）",
         object="ADR 必填字段／ADR 索引与编号／技术债字段／模板接线／规则登记／复审日期",
         trigger="新增或修改 ADR、技术债、工程实践规则或模板后；工程类批次收口（2026-10-22 立）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第三十件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_oaa_batch.py",
         kind="门禁（OAA 批次收口对账，独立计数）",
         object="OAA 批次三面对账：分片↔判读（同名件／行数／key 集合／JSON 合法性与重复 key）↔ledger（key 总量与重复）",
         trigger="每批 OAA 收口前（2026-10-22 立）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第三十一件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_mail2d_batch.py",
         kind="门禁（批次收口对账，独立计数）",
         object="mail2d 批次 spec↔候选↔叙述↔claim_map↔库／宿主 对账",
         trigger="每批 mail2d 收口前",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第三十二件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_task_lifecycle.py",
         kind="门禁（任务强制审计、复核与轮替，独立计数）",
         object="任务审计台账／复核台账／TG 缺口登记：L1 表头、L2 准入、L3 收口、L4 字段、L5 枚举、L6 唯一、L7 复核轮次与角色、L8 复核引用、L9 轮替阈值、L10 轮替双源、L11 接线、L12 理论适用性",
         trigger="新任务开工前、任务收口前、每季度轮替检查（2026-10-22 立）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第三十三件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_anchor_pairs.py",
         kind="门禁（成对锚配平，独立计数）",
         object="05-卷册大纲/ 树内 .md 注释锚多行感知配平：数据驱动家族模式 block（G1 全树 open==close）／begin_end（G2 全树 BEGIN==END，单标记豁免）／single（只判单标记）；T4 未闭合注释；文件级仅 INFO，ROW_MINE／DEEP_ANALYSIS 单锚豁免",
         trigger="任一批次改动 05-卷册大纲 内容后；清理批次前后差分（2026-10-22 立，ADR-0011／TD-022）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第三十四件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_anchor_pair_order.py",
         kind="门禁（BEGIN/END 章内配对，独立计数）",
         object="05-卷册大纲/ 树内 BEGIN/END 成对锚按**章**配对：排序键＝目录名／文件名节号数值序（禁相对路径字典序，`.10` 不得排在 `.9` 前）；形态覆盖 `FAM:BEGIN`／`FAM:END` 与中文 `FAM:开始`／`FAM:结束`；P1 孤儿 END／P2 未配 BEGIN／P4 未闭合注释；跨章配对拆记为一孤一未配；block 家族（含 close）交由第三十三件判平；ROW_MINE／DEEP_ANALYSIS 不参与",
         trigger="任一批次改动 05-卷册大纲 的 BEGIN/END 标记后；大纲清理批次收口（2026-10-22 立，TD-022 裁定 6 复核）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第三十五件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_outline_dup.py",
         kind="门禁（大纲重复锚与重复块，独立计数）",
         object="05-卷册大纲/ 树内 .md 重复结构：A 同一文件内同一 `ROW_MINE` 锚 ≥2 副本 FAIL（`DEEP_ANALYSIS` 单标记无唯一 ID 不参与）；B 同一文件同一小节内同锚且整块（锚行＋说明行＋正文，去尾部空行）逐字相同 FAIL；B2 同小节同锚但块内容不同仅 INFO（交人工）；C 跨文件同名锚仅 INFO 计数（各节独立引用同一史料属既有体例，P2／P3 已裁定不作删除）。判据源自 TD-023 去重线（920／247／32 三批处置后全树归零），2026-10-22 固化为常驻门禁以拦生成器等距批量追加复发",
         trigger="任一批次改动 05-卷册大纲 内容后；入纲写入后；去重批次收口（2026-10-22 立，TD-023 收尾）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="第三十六件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_sidecar_backup.py",
         kind="门禁（旁路备份残留扫描，独立计数）",
         object="全库旁路备份副本残留：命中族与 .gitignore 封禁段、git_commit_gate B5 同口径（.prebak*／.preback*／.pre／.pre-*／.pre_*／.bak*／-bak*／_bak*／.orig*／.rej／结尾 ~，及 prebak*／_bak* 备份目录下全部内容）；豁免仅 script/_bak/20261017/（AGENTS.md 记载的重写前全史备份镜像）与 12-数据库备份/ 内正式归档体（.tar.gz／.tgz／.parquet／.sql／.jsonl／.gz）；非正式命名的写前快照不豁免",
         trigger="每批收口必跑（不涉改动亦跑）；旁路备份清扫批次收口（2026-10-23 立）",
         selftest="", in_tests_readme=False),
    dict(no="第三十七件", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_outline_landing.py",
         kind="门禁（大纲落地一致性 L1–L17，独立计数）",
         object="目录真值／映射台账／磁盘落点／派生件四者自洽：L1 落点节数守恒／L2 已确认映射落地／L3 落点无多余 .md／L4 H1 与路径一致／L5 旧三段号未决／L6 落点无重复内容／L7 SUMMARY 链接齐全／L8 主题索引口径／L9 落点编码／L10 无散件／L11 布局零漂移／L12 TARGET_LOST 挂账／L13 路径合规／L14 活动复合键唯一／L15 REMAP 挂账与后继／L16 旧二段号未决／L17 节占位互斥；L2/L3/L5/L6/L7/L11/L12/L13/L15/L16 依赖 mapping.tsv 与 layout.tsv，缺失时标 SKIP 不计 FAIL；mapping 缺 status 列等表头违约 exit 2",
         trigger="05-卷册大纲/ 内容落地、映射台账写入、targets.tsv／layout.tsv 再生、节级增删改号、迁移施工与收口批；Task 11 开工前与每卷迁移收口必跑（2026-10-23 立，TD-027 偿还）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="Git 暂存门禁", script="00-编纂规则与格式规范/01-规则/脚本与命令/git_commit_gate.py",
         kind="门禁", object="Git 暂存区与提交说明：G1 新增路径命中 .gitignore（含 -f 强加）／G2 单个 >5 MB blob（5,242,880 字节）／B2 根目录新条目不在白名单／B3 备份删除／B4 文档含 U+3000／B5 旁路备份副本（无放行；状态 D 不拦＝整改删除通道）／H3 直角引号六码位／H1 提交说明质量（无放行）；批准标记 APPROVED-IGNORED:／APPROVED-BIGFILE:／APPROVED-BY-OWNER: 放行（B5 与 H1 无放行）",
         trigger="每次 git commit：pre-commit 薄壳自动改正（F1 直角引号弯化／F2 不可见字符全口径／F3 CRLF→LF·BOM，仅文档类）；commit-msg 薄壳阻断核对（G1/G2/B2/B3/B4/B5/H3/H1 + 批准标记）；hook 不入库，重建后须重装，见流程规则“Git 暂存规则”",
         selftest="--selftest", in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/embed.py",
         kind="门禁", object="catalog 与内嵌数据块一致性", trigger="改 catalog 或数据块后",
         selftest="--check", in_tests_readme=True),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/guard_source_chars.py",
         kind="写盘前守卫", object="装配源字符（直角引号／U+3000／TAB／BOM）", trigger="写装配源前",
         selftest=None, in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_databases.py",
         kind="一次性审计（**非固定脚本**）", object="12 功能库 + 15 代码库 + 4 邮件库一次性盘点（英文 docstring，绑 06 号文设计）",
         trigger="—", selftest=None, in_tests_readme=False, fixed=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_folder_db_integrity.py",
         kind="门禁（数据库类）", object="文件夹级数据库与磁盘文件清单一致性", trigger="改文件夹库后",
         selftest=None, in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_provenance_dupes.py",
         kind="门禁（数据库类，独立计数）",
         object="historical_claims.provenance_history 审计表：D1 真重复（同 source_id/event_type/at/detail 多行）FAIL；D2a 裁定前空 id 仅登记 INFO、D2b 裁定日起空 id（违反统一约定）FAIL；D3 source_id 空值率 WARN；D4 三元组重复中 detail 分歧者记 INFO（正当形态，非缺陷）；D5 id 序列冲突（同号多行）裁定后 FAIL／裁定前 WARN。只读连接，不写活库",
         trigger="provenance_history 任何写入后（2026-10-16 立：三元组判据经实测推翻——601 组重复全部 detail 分歧、真重复 0，故只判真重复；若按三元组判会把 1,690 条正当审计行全误报。同日 ykla 裁定 id 统一约定＝前向收紧不回填：实测 id 为真实全局单调序号（按 at 升序回落 0/1618）、空 id 行仍持续产生（f4_b24_dbfix 23 行为全表最新），故 8,936 行存量显式登记为债务、裁定日 2026-10-17 起新写入缺 id 即 FAIL）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/register_waterlock.py",
         kind="写库排他门禁（独立计数）",
         object="historical_claims.claim_id 号段跨会话排他：claim_id **无主键约束**（实测 information_schema.table_constraints 计数 0）⇒ 撞号静默成功。锁文件 12-数据库备份/waterlock/（O_CREAT+O_EXCL 原子创建）串行化——锁内实测 MAX 回吐本批号段，释放前断言 rows == distinct == count（无主键约束下唯一能证明号段连续的机会，不符即拒放锁）。TTL 3 小时、超 24 小时判陈旧；接管须显式 --force 且强制填写理由。只读连接，不写活库。是串行化设施，不替代 claimdb_guard.py（写前哨兵）与写前 prebak",
         trigger="任何 register 写库前（2026-10-17 升格入库：原驻 script/_db_row_mining/ 受 .gitignore *.py 排除、永久不可入库，改一轮丢一轮；迁入后 repo_root() 上行 3 层即达，路径解析不破，selftest 与活库只读 probe 均实测通过）",
         selftest="selftest", in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/rotate_guard_state.py",
         kind="写库排他门禁（独立计数）",
         object="claimdb_guard 快照多槽轮换：单槽 12-数据库备份/claimdb_guard_state.json 被每次非 FAIL 运行就地覆盖 ⇒ 污染态（2026-10-13 广播事故）被记成基线、S2/S4 从此对假水位比对。健康判定只读快照自带指标（不碰库）：fact_max_pct>0.25 或 upd_max_pct>0.50 ⇒ poisoned（＝S1/S3 FAIL 阈值），>0.05 或 distinct/rows<0.90 ⇒ suspect；实测健康 0.994/0.00017 vs 污染 0.025/0.975，差两个数量级。restore --best 取**最近的健康槽**（不是“最近槽”）、--dry-run 只报不换、prune 健康槽至少留 1",
         trigger="register／claimdb_guard 前后（2026-10-17 立；BASE 走 D:/UNC 双候选＋--base，不可解析 exit 2 不静默空转）",
         selftest="selftest", in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/font_subset_rebuild.py",
         kind="重建器（字体子集）", object="内嵌字体子集／源字体覆盖", trigger="大纲增字、改字体源或重建字体后",
         selftest=None, in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/review_v2_full.py",
         kind="复算套件（独立复算）", object="产物 index.html 与内容源", trigger="每批目录重构后",
         selftest=None, in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/serve_refactor2026.py",
         kind="服务器（固定脚本）", object="服务器白名单／压缩／缓存／安全头", trigger="服务器改动或启动前",
         selftest=None, in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/oaa_remap_claims.py",
         kind="F 线认领清单回映器（检查＋写模式）",
         object="`claims_F*.txt`（1,097 条）在目录化后字面存在率 0.00%——按“卷号＋章题＋节题去数字前缀”唯一回映现行树；`--check` 只读统计；`--write [--apply]` 就地改写（prebak、歧义/未匹配拒写、写后逐行在盘断言、幂等二跑 0 改动）；`--selftest` 判据非空",
         trigger="F 线开批前（认领清单新鲜度：存在率／唯一回映率须 100%）；大纲结构变动后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/build_theme_index.py",
         kind="生成器/门禁", object="chapter_keywords.json／theme_index.json", trigger="大纲结构变动后",
         selftest="--selftest", in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/outline_writer.py",
         kind="入纲写入器（唯一实现）", object="mail2d／OAA 入纲宿主写入（块追加面）：宿主＝小节 .md（claim_map hosts／outline_map 权威，不猜文件名；multi 由 narr 宿主列消歧）、块级锚点幂等（ROW_MINE: lib.messages.pk；扫描面默认宿主所在章节目录）、路径 commonpath 断言（写点 allow-root／读点 input-root 分层＋启动打印生效路径）、临时件→fsync→os.replace＋全或无回滚、写后断言增量＝计划数；--check-only 供 F／OAA 线核查认领清单可解析率。F 线块内整行替换仍属 apply_fixes.py（TD-016／TD-017）",
         trigger="每批 mail2d／OAA 入纲（2026-10-22 立，替代 _outline_<tag>.py 批内一次性脚本，ADR-0010；生产切换为准阶段二）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/outline_registry.py",
         kind="目标注册表与漂移机制（执行器）",
         object="由 `05-卷册大纲/目录/data/outline.txt` 派生稳定节点 ID（V-001／C-0001／S-000001）并生成 `05-卷册大纲/映射/targets.tsv`；漂移算法（同父同题→同层同题→模糊改题≥0.86→新增，未匹配旧节点退役）落 `05-卷册大纲/映射/drift/drift-report.tsv`；`--write` 生成（默认 dry-run）／`--check` 只读检测／`--sync [--write]` 同步／`--selftest` 六类场景自证",
         trigger="大纲结构变动后（改号／重排／改题／增删）；Task 3 生产版（2026-10-23 立）",
         selftest="--selftest", in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/verify_tuhs_wiki.py",
         kind="验证器（语料完整性，独立计数）",
         object="03-原始史料库/16-TUHS-Wiki史料/tuhs_wiki.duckdb 的 V1–V12 完整性与保真判据",
         trigger="TUHS Wiki 抓取或重抓后、交付前",
         selftest="--selftest", in_tests_readme=False),
    dict(no="—", script="00-编纂规则与格式规范/01-规则/脚本与命令/verify_tuhs_wiki_sql.py",
         kind="验证器（独立 SQL 复核，独立计数）",
         object="同一语料库的 V1–V5／V10／V12 独立 SQL 复算（不复用主验证器判据代码）",
         trigger="主验证器通过后，交叉复核轮",
         selftest="--selftest", in_tests_readme=False),
]

# ── 阶段映射（R8 唯一真值；键＝脚本文件名） ──────────────────────────────
# 允许单阶段或逗号分隔多阶段；阶段集合固定为 G0–G5。
# 本表由 2026-10-22 工程实践基线批首次建立（按门禁对象面判断）。
# 2026-10-22 TD-005 批逐件核实 47 件（脚本 docstring／主要判据／实际触发点），
# 修订 5 处：audit_evidence_level_labels、audit_anchor_resolution（产物→源级，G3）、
# audit_mail2d_batch、audit_oaa_batch（源级→收口对账，G5）、embed（G3→G3,G4）。
# 逐件证据见 script/_td005_verify_20261022.md，差异记录见
# 01-项目管理/02-工程决策与技术债/工程实践复审台账.md “TD-005 逐件核实（2026-10-22）”。
ALL_STAGES = {"G0", "G1", "G2", "G3", "G4", "G5"}
STAGE_MAP = {
    "audit_data_integrity.py": "G4",
    "sync_refactor2026_baseline.py": "G5",
    "audit_sequence_continuity.py": "G4",
    "visual_regression.mjs": "G4",
    "xref_audit.py": "G4",
    "audit_evidence_level_labels.py": "G3",
    "audit_index_structure.py": "G4",
    "assemble_index.py": "G3,G4",
    "outline_writer.py": "G3,G4",
    "outline_registry.py": "G3",
    "oaa_remap_claims.py": "G3",
    "audit_page_assets.py": "G4",
    "audit_markdown_lint.py": "G3",
    "audit_server_contract.py": "G4",
    "tri_structure_negtest.py": "G3",
    "audit_fixture_freshness.py": "G3",
    "audit_note_xref.py": "G3",
    "audit_person_bio_integrity.py": "G4",
    "audit_renumber_guard.py": "G3",
    "audit_page_version_bump.py": "G5",
    "audit_anchor_resolution.py": "G3",
    "audit_silent_loss_guard.py": "G3",
    "audit_disk_terminology.py": "G3",
    "audit_gate_registry.py": "G5",
    "outline_selfcheck.py": "G4",
    "audit_a11y.py": "G4",
    "audit_js_blockscope.py": "G3",
    "audit_md_quote_glyphs.py": "G3",
    "audit_mirror_ingest.py": "G5",
    "sync_outline_mirror.py": "G3",
    "audit_keyword_index.py": "G4",
    "audit_md_bold_spacing.py": "G3",
    "audit_engineering_practice.py": "G2,G5",
    "audit_task_lifecycle.py": "G1,G4,G5",
    "audit_anchor_pairs.py": "G3",
    "audit_anchor_pair_order.py": "G3,G4",
    "audit_outline_dup.py": "G3,G4",
    "audit_sidecar_backup.py": "G3,G4",
    "audit_outline_landing.py": "G3,G4",
    "audit_mail2d_batch.py": "G5",
    "audit_oaa_batch.py": "G5",
    "git_commit_gate.py": "G5",
    "embed.py": "G3,G4",
    "guard_source_chars.py": "G3",
    "audit_databases.py": "G3",
    "audit_folder_db_integrity.py": "G4",
    "audit_provenance_dupes.py": "G4",
    "register_waterlock.py": "G3",
    "rotate_guard_state.py": "G3",
    "font_subset_rebuild.py": "G3",
    "review_v2_full.py": "G4",
    "serve_refactor2026.py": "G4",
    "build_theme_index.py": "G3",
    "verify_tuhs_wiki.py": "G4",
    "verify_tuhs_wiki_sql.py": "G4",
}


def _read(p):
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def run(cmd_dir: pathlib.Path, tests_dir: pathlib.Path, registry, check_extra=True):
    rows = []

    # R1 存在性
    missing = [e["script"] for e in registry if not (REPO / e["script"]).exists()]
    rows.append(("R1", "登记脚本全部存在", not missing,
                 "登记 %d 件；缺失 %s" % (len(registry), ", ".join(missing) or "无")))

    # R2 可编译性
    bad = []
    for e in registry:
        p = REPO / e["script"]
        if p.suffix != ".py" or not p.exists():
            continue
        try:
            py_compile.compile(str(p), cfile=str(pathlib.Path(tempfile.gettempdir())
                                                 / "_grc.pyc"), doraise=True)
        except py_compile.PyCompileError as ex:
            bad.append("%s：%s" % (p.name, str(ex).splitlines()[0][:80]))
    rows.append(("R2", "登记脚本可编译（.py）", not bad,
                 "不通过 %d 件%s" % (len(bad), "：" + "；".join(bad) if bad else "")))

    # R3 无漏接线
    on_disk = {p.name for p in cmd_dir.glob("audit_*.py")}
    registered = {pathlib.Path(e["script"]).name for e in registry}
    unreg = sorted(on_disk - registered)
    rows.append(("R3", "脚本与命令/audit_*.py 全部已登记", not unreg,
                 "磁盘 %d 件、登记 %d 件；未登记 %s"
                 % (len(on_disk), len(registered & on_disk), ", ".join(unreg) or "无")))

    # R4 有规则引用（仅对固定脚本；非固定脚本见 R7）
    docs = "".join(_read(p) for p in RULE_DOCS if p.exists())
    noref = [pathlib.Path(e["script"]).name for e in registry
             if e.get("fixed", True) and pathlib.Path(e["script"]).name not in docs]
    rows.append(("R4", "每个**固定**脚本至少被一处规则／索引文档引用", not noref,
                 "无引用 %s" % (", ".join(noref) or "无")))

    # R5 套件清单一致
    tr = _read(tests_dir / "README.md")
    tbad = [pathlib.Path(e["script"]).name for e in registry
            if e["in_tests_readme"] and pathlib.Path(e["script"]).name not in tr]
    rows.append(("R5", "标记 in_tests_readme 者出现在 tests/README.md", not tbad,
                 "未出现 %s" % (", ".join(tbad) or "无")))

    # R6 自检覆盖（仅报告，不判 FAIL —— 存量多件无自检，属既有债）
    no_st = [e["no"] + " " + pathlib.Path(e["script"]).name
             for e in registry if not e["selftest"]]
    rows.append(("R6", "（仅报告）无判据非空自检的登记件", True,
                 "%d/%d 件：%s" % (len(no_st), len(registry),
                                   "、".join(no_st) if no_st else "无")))

    # R7 未登记脚本（仅报告）：规则目录内既不在登记表、也未在 README 索引者
    readme = _read(cmd_dir / "README.md")
    loose = sorted(p.name for p in cmd_dir.glob("*.py")
                   if p.name not in registered and p.name not in readme)
    rows.append(("R7", "（仅报告）规则目录内既未入登记表、也未入 README 索引的 .py", True,
                 "共 %d 件：%s" % (len(loose), "、".join(loose) if loose else "无")))

    # R8 阶段映射（2026-10-22 立）：登记件须有合法 G0–G5 阶段；映射无悬空键
    reg_names = {pathlib.Path(e["script"]).name for e in registry}
    missing_stage = sorted(n for n in reg_names if n not in STAGE_MAP)
    extra_stage = sorted(k for k in STAGE_MAP if k not in reg_names) if check_extra else []
    bad_stage = sorted(
        "%s=%s" % (k, STAGE_MAP[k])
        for k in reg_names & set(STAGE_MAP)
        if not set(STAGE_MAP[k].split(",")) <= ALL_STAGES
    )
    coverage = []
    for st in sorted(ALL_STAGES):
        count = sum(1 for n in reg_names if st in STAGE_MAP.get(n, "").split(","))
        coverage.append("%s:%d" % (st, count))
    rows.append(("R8", "每个登记件有合法 G0–G5 阶段归属", not (missing_stage or extra_stage or bad_stage),
                 "缺阶段 %s；悬空键 %s；非法值 %s；覆盖 %s"
                 % (", ".join(missing_stage) or "无",
                    ", ".join(extra_stage) or "无",
                    ", ".join(bad_stage) or "无",
                    "／".join(coverage))))
    return rows


def _report(rows, title):
    print("=" * 72)
    print(title)
    print("=" * 72)
    fails = 0
    for code, name, ok, detail in rows:
        print("  [%s] %-4s %s" % ("PASS" if ok else "FAIL", code, name))
        print("           %s" % detail)
        if not ok:
            fails += 1
    print("-" * 72)
    print("  合计 %d 项，FAIL %d 项" % (len(rows), fails))
    return fails


def cmd_selftest():
    """判据非空：造“登记了但文件不存在”＋“磁盘有 audit_*.py 未登记”＋“缺阶段”三类缺陷，须 FAIL。"""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="gatereg_"))
    try:
        cmd = tmp / "cmd"
        cmd.mkdir()
        (cmd / "audit_unregistered.py").write_text("x = 1\n", encoding="utf-8")
        reg = [
            # T1 指向真实存在的脚本（R1 应通过该项）
            dict(no="T1",
                 script="00-编纂规则与格式规范/01-规则/脚本与命令/audit_server_contract.py",
                 kind="t", object="t", trigger="t", selftest=None,
                 in_tests_readme=False),
            # T2 登记了但磁盘不存在（R1 必 FAIL）
            dict(no="T2", script="___missing___/audit_absent.py",
                 kind="t", object="t", trigger="t", selftest=None,
                 in_tests_readme=False),
        ]
        rows = run(cmd, tmp, reg, check_extra=False)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    fails = _report(rows, "判据非空自检：登记缺失 + 磁盘漏登记 + 缺阶段（预期 R1/R3/R8 FAIL）")
    got = {c for c, _n, ok, _d in rows if not ok}
    if {"R1", "R3", "R8"} <= got:
        print("  ✅ 判据非空：R1（文件缺失）、R3（漏登记）与 R8（缺阶段）均命中")
        return 0
    print("  ❌ 判据可能为空：未同时命中 R1/R3/R8（实际 %s）" % (sorted(got) or "空"),
          file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(description="门禁体系元门禁（第十六件）")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()

    if args.list:
        print("%-8s %-42s %-10s %-14s %s" % ("编号", "脚本", "阶段", "类别", "对象面"))
        for e in REGISTRY:
            name = pathlib.Path(e["script"]).name
            print("%-8s %-42s %-10s %-14s %s" % (e["no"], name,
                                                 STAGE_MAP.get(name, "?"),
                                                 e["kind"], e["object"]))
        print("\n合计 %d 件（其中 %d 件未提供判据非空自检）"
              % (len(REGISTRY), sum(1 for e in REGISTRY if not e["selftest"])))
        return 0

    for p, what in ((CMD, "脚本与命令目录"), (TESTS / "README.md", "tests/README.md")):
        if not p.exists():
            print("依赖缺失：%s（%s）" % (p, what), file=sys.stderr)
            return 2
    rows = run(CMD, TESTS, REGISTRY)
    return 1 if _report(rows, "门禁体系元门禁（第十六件）") else 0


if __name__ == "__main__":
    sys.exit(main())
