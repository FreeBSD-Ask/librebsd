# local-skills：本项目自建技能（入库源）

Spec Kit 的 `zcode` 集成把上游技能装到 `.zcode/skills/`，但该目录被根 `.gitignore` 忽略（`/.zcode`）——**入库的源放在这里**，运行时副本同步到 `.zcode/skills/`。

## 现有技能

| 技能 | 用途 |
| ---- | ---- |
| `speckit-spec-tasks-check` | 一条命令出 Trae Spec 式产物：`spec.md`（规格）→ `plan.md`（计划，超集必需件）→ `tasks.md`（任务）→ `checklist.md`（验收检查点）。跳过 implement／converge，不建分支 |

## 目录结构

每个技能是一个**自包含目录**（可直接整包搬走）：

```text
speckit-spec-tasks-check/
├── SKILL.md        技能本体（含环境探测：有 Spec Kit 走上游管道，无则用 assets 模板直出）
├── INSTALL.md      安装说明（含目标机两种装法与验证步骤）
└── assets/         规格／计划／任务／检查点四份模板（取自 GitHub Spec Kit，MIT）
```

## 安装到运行时（一律全局／用户级）

```sh
cp -r .specify/local-skills/speckit-spec-tasks-check ~/.zcode/skills/
```

**口径（2026-09-30 主理人定）：一律全局安装到用户级 `~/.zcode/skills/`**，装一次所有项目可用。同名技能用户级优先于项目级，故**不再保留项目级副本**（当日已移除 `D:\librebsd\.zcode\skills\speckit-spec-tasks-check`，避免两份漂移）。改完源后重新 `cp`，并新开 ZCode 会话才生效（技能在会话启动时扫描）。

## 打包分发（搬去其他电脑的 ZCode）

源目录本身即安装包，另在 `.specify/exports/` 留有 zip 副本便于传输：

```sh
cp -r .specify/local-skills/speckit-spec-tasks-check ~/.zcode/skills/
```

或取 `.specify/exports/speckit-spec-tasks-check-<日期>.zip` 解压到目标机的 `~/.zcode/skills/` 下（该机所有项目即可用）。

改完源后须重建 zip（Python `zipfile`，保持目录顶名）：

```sh
python -c "import zipfile,os;src=r'.specify/local-skills/speckit-spec-tasks-check';out=r'.specify/exports/speckit-spec-tasks-check-20260930.zip';z=zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED);[z.write(os.path.join(r,f),os.path.relpath(os.path.join(r,f),os.path.dirname(src)).replace('\\\\','/')) for r,d,fs in os.walk(src) for f in fs];z.close()"
```

## 为什么必须有 plan.md（超集件）

Spec Kit 的 `setup-tasks.ps1` 与 `check-prerequisites.ps1` 对 `plan.md` 是**硬依赖**（实测：缺失即 `ERROR: plan.md not found` 并 exit 1），故封装把 plan 列为必需前置。无 Spec Kit 的环境（模式 B）走包内模板，不受此依赖约束。

## 为什么不做成上游技能

上游 `speckit-specify`／`speckit-plan`／`speckit-tasks` 由 `specify integration upgrade` 管理，直接改会被升级覆盖。故封装在**有 Spec Kit 时只做引用与串接**（指示 agent 读取并执行上游 SKILL.md），不复制其逻辑——上游升级后行为自动跟随；无 Spec Kit 时才启用包内模板直出。
