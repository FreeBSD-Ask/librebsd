# local-skills：本项目自建技能（入库源）

Spec Kit 的上游技能由 `specify init` 装到 `--commands-dir` 指定的技能目录。本技能包在此**入库保存**，运行时副本同步到用户级技能目录（WorkBuddy AI 或 ZCode）。

## 现有技能

| 技能 | 用途 |
| ---- | ---- |
| `speckit-spec-tasks-check` | 一条命令出 Spec 式产物：`spec.md`（规格）→ `plan.md`（计划，超集必需件）→ `tasks.md`（任务）→ `checklist.md`（验收检查点）。跳过 implement／converge，不建分支 |

## 目录结构

每个技能是一个**自包含目录**（可直接整包搬走）：

```text
speckit-spec-tasks-check/
├── SKILL.md        技能本体（含环境探测：项目未装 Spec Kit 时自动安装，再走上游管道）
└── INSTALL.md      安装说明（前置条件、自动安装行为、手工命令、验证步骤）
```

包内**不含模板**——四件的骨架来自 Spec Kit 上游 `.specify/templates/`；技能会自动把 Spec Kit 装到目标项目（`uv tool install specify-cli` ＋ `specify init --here --integration generic --integration-options="--commands-dir .workbuddy-ai/skills/ --skills"`，WorkBuddy AI 原生落点）。

## 安装到运行时（一律全局／用户级）

**WorkBuddy AI（2026-10-09 起主目标）**：

```sh
cp -r .specify/local-skills/speckit-spec-tasks-check ~/.workbuddy-ai/skills/
```

**ZCode（向后兼容，同一份技能正文）**：

```sh
cp -r .specify/local-skills/speckit-spec-tasks-check ~/.zcode/skills/
```

**口径（2026-09-30 主理人定，2026-10-09 扩 WorkBuddy AI）**：一律全局安装到**用户级**技能目录，装一次所有项目可用。同名技能用户级优先于项目级，故**不再保留项目级副本**（2026-09-30 已移除 `D:\librebsd\.zcode\skills\speckit-spec-tasks-check`）。改完源后重新 `cp`，并新开宿主会话才生效（技能在会话启动时扫描）。

**双落点与回落（2026-10-09）**：技能步骤 0 的就绪判据按优先级探测**项目级**技能目录——①`.workbuddy-ai/skills/`（WorkBuddy AI 原生落点）②`.zcode/skills/`（ZCode 回落）。本项目 `.specify/integration.json` 既有整合为 `zcode`，按技能内置的「整合冲突守卫」**只复用、不重装**，故本项目实际走候选 ②。

## 打包分发（搬去其他电脑）

源目录本身即安装包，另在 `.specify/exports/` 留有 zip 副本便于传输：

```sh
# 解压到目标机对应技能目录：
#   WorkBuddy AI → ~/.workbuddy-ai/skills/
#   ZCode        → ~/.zcode/skills/
```

改完源后须重建 zip（Python `zipfile`，保持目录顶名）：

```sh
python -c "import zipfile,os;src=r'.specify/local-skills/speckit-spec-tasks-check';out=r'.specify/exports/speckit-spec-tasks-check-20261009.zip';z=zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED);[z.write(os.path.join(r,f),os.path.relpath(os.path.join(r,f),os.path.dirname(src)).replace('\\\\','/')) for r,d,fs in os.walk(src) for f in fs];z.close()"
```

## 为什么必须有 plan.md（超集件）

Spec Kit 的 `setup-tasks.ps1` 与 `check-prerequisites.ps1` 对 `plan.md` 是**硬依赖**（实测：缺失即 `ERROR: plan.md not found` 并 exit 1），故封装把 plan 列为必需前置。

## 为什么不做成上游技能

上游 `speckit-specify`／`speckit-plan`／`speckit-tasks` 由 `specify integration upgrade` 管理，直接改会被升级覆盖。故封装**只做引用与串接**（指示 agent 读取并执行上游 SKILL.md），不复制其逻辑——上游升级后行为自动跟随。项目未装 Spec Kit 时，封装先自动安装它（`uv tool install specify-cli` ＋ `specify init`，2026-09-30 主理人令：不再自带模板兜底），安装失败即停止报告，不用替代方案糊过去。
