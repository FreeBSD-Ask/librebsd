# usenet 行级挖掘（7 组）·长线归档

> **归档**：2026-10-18。本线已收官，其登记层内容由《长线任务总登记表》§二 迁入本目录独立存档（**逐字保留**）；总登记表对应节已改写为指针，**本件是该线章节全文的唯一载体**。归档口径与操作规则见 `00-编纂规则与格式规范/01-规则/长线任务归档规则.md`。
>
> | 项 | 内容 |
> | -- | ---- |
> | **登记表线号** | #1 |
> | **终态** | CLOSED —— 七组 169,055/169,055（100.00%）；usenet 全库 43 组 234,573/234,573 亦 100%（2026-10-17 台账实测） |
> | **归档前权威源（唯一真值）** | `script/_db_row_mining/long_task_state.json`（`usenet7.progress`）＋ `_PROGRESS_AUDIT_7GROUPS_20260915.json`（机读源留原处未迁） |
> | **登记表原位置** | 总登记表 §二（现仅存指针） |
> | **线级任务书／交接书** | `usenet任务书与交接书/`（`_RESUME.md`、长期计划与收官交接书等，2026-10-17 迁入，见《任务书迁移登记.md》） |
> | **变更记录** | 总登记表 §十五（编年日志保留不迁，含本线收官条目） |

## 一、登记表 §一 总览表行（归档快照，逐字）

| 1 | **usenet 行级挖掘（7 组）** | `CLOSED` | 七组已读 **169,055/169,055（100.00%）**｜剩余段 **0**｜开放组 **无**（2026-10-17 台账实测；usenet 全库 43 组 234,573/234,573 亦 100%） | `script/_db_row_mining/long_task_state.json`（`usenet7.progress`）＋ `_PROGRESS_AUDIT_7GROUPS_20260915.json` | 读 `01-项目管理/01-编纂规划与报告归档/usenet任务书与交接书/_RESUME.md` → `script/_db_row_mining/_resume.py`（线级任务书 2026-10-17 已迁，机读源留原处） | `_progress_audit_7groups.py --check-state` |

## 二、登记表章节全文（归档快照，逐字）

## 二、usenet 行级挖掘（7 组）

- **范围**：`comp.sys.sun`(11)、`comp.unix.questions`(20)、`comp.unix.wizards`(23)、`unix.bsd.bsdi.misc`(38)、`unix.bsd`(40)、`unix.bsd.misc`(41)、`unix.bsd.openbsd.misc`(44)，共 169,055 头。
- **状态**：11／20／23／38／40／41 **六组已 100% 收官**；**仅 list 44 开放**（48,720 头，剩 60 段）。
- **真值源**：`long_task_state.json` 的 `usenet7.progress.by_list`，由 `_progress_audit_7groups.py --sync-state` **唯一计算**（四源实读：源库／claim 库／大纲 ROW_MINE／staging）。**禁手工编辑派生字段**。
- **续跑**：`_RESUME.md`（一页纸）→ `_resume.py`（一屏快照）→ 按【④ 下一步建议】执行。
- **健康检查**：`_progress_audit_7groups.py --check-state`（无漂移 PASS）。
- **作业规范**：`script/_db_row_mining/_SINGLE_ROUND_SOP.md`（单轮作业手册）；技能 `usenet-row-mining`。
- **组级收官门禁**：10 项，见技能 §五。
- **🔴 list 44 专用长线入口（2026-09-19 dakuD 会话建；同日拆为双线分治）**：
  - **D 线（正推低端）**：`script/_db_row_mining/_LONGTERM_PLAN_dakuD_list44.md` —— s75–s98（24 段／9,600 头），波 4–7；
  - **E 线（倒推高端）**：`script/_db_row_mining/_HANDOFF_dakuE.md` —— s122–s99（24 段／9,524 头），波 E1–E4；
  - 波段驱动 `script/_db_row_mining/_wave_sop.py <K1> <K2>`（dry／`--land`／`--gates`／`--closeout`／`--commit "<msg>"`，含前置闸）。
  - 🔴 **分治进度口径**：分界 pk ＝ **`225804`**（s98 上界）；`_progress_audit_7groups.py` 与 `_plan_sync_dbtruth.py`
    已改为**双向前沿**（两处同源同值，**勿只改一处**）。E 线未开工时口径与旧值逐值一致（已验）。
  - ⚠️ **该驱动是“人在场触发”的批处理脚本，不是定时任务**（本项目禁自动化，见本表头部裁定）。
