# TG-V40 第 40 卷 标题设计任务组

> 协议：`../README.md`；注册表：`../taskgroups.tsv`（本组数值以该行为准）。
> 状态：`pending`；波次：5（波次仅是排班提示，互不依赖）。

## 一、范围

- 卷题：可移植的执念：NetBSD 操作系统的历史（1993—2026）
- 章数 9；节数 78（V01 已含 2.3 拆节 6 节，其余卷按 `targets.tsv` 实测）；`mapping.tsv` 命中 0 行的节 54 个
- 旧料：映射件 723 件、10578568 字节（`mapping.tsv` 该卷节点命中）
- 预计标题：156—936（中位 468；J3 每节 2—12）

## 二、产出（只写这些）

- `05-卷册大纲/映射/title-design/V40.tsv`
- `05-卷册大纲/映射/title-evidence/V40.tsv`
- `05-卷册大纲/映射/title-design/exceptions/V40.tsv`（有例外才建）
- `05-卷册大纲/映射/title-design/V40-标题呈审报告.md`
- `05-卷册大纲/映射/parallel/title/V40/{claim,counts.tsv,done.json}`

## 三、禁止

- 不写他人卷台账；不写 `approvals.tsv`／`approved/`／`outline.txt`／`index.html`／树内 `.md`
- 不建旁路副本；不改本卡数值（数值由注册表再生）

## 四、作业顺序

1. `claim` 原子创建（存在即让出）。
2. 读 `data/outline.txt` 本卷段落＋`targets.tsv` 本卷节点＋`mapping.tsv` 对应件。
3. 按 `title-design/风格规范.md` 八步拟题；无史料节标题避用拉丁字母，免踩三源下限。
4. `python 00-编纂规则与格式规范/01-规则/脚本与命令/audit_title_consistency.py --check` 须 FAIL 0。
5. 写 `done.json`（titles／ledger_sha256／selftest_exit=0）→ 呈 ykla 卷级批准（合并者写 `title.ok`）。
