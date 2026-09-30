# local-skills：本项目自建技能（入库源）

Spec Kit 的 `zcode` 集成把上游技能装到 `.zcode/skills/`，但该目录被根 `.gitignore` 忽略（`/.zcode`）——**入库的源放在这里**，运行时副本同步到 `.zcode/skills/`。

## 现有技能

| 技能 | 用途 |
| ---- | ---- |
| `speckit-spec-tasks-check` | 一条命令出 Trae Spec 式产物：`spec.md`（规格）→ `plan.md`（计划，超集必需件）→ `tasks.md`（任务）→ `checklist.md`（验收检查点）。跳过 implement／converge，不建分支 |

## 同步到运行时（新技能或改完源后执行）

```sh
cp -r .specify/local-skills/<skill-name> .zcode/skills/<skill-name>
```

ZCode 在工作区会话启动时扫描 `.zcode/skills/`，改完需新开会话才生效。

## 为什么必须有 plan.md（超集件）

Spec Kit 的 `setup-tasks.ps1` 与 `check-prerequisites.ps1` 对 `plan.md` 是**硬依赖**（实测：缺失即 `ERROR: plan.md not found` 并 exit 1），故封装把 plan 列为必需前置。

## 为什么不做成上游技能

上游 `speckit-specify`／`speckit-tasks` 由 `specify integration upgrade` 管理，直接改会被升级覆盖。故封装技能只做**引用与串接**（指示 agent 读取并执行上游两个 SKILL.md），不复制其逻辑——上游升级后行为自动跟随。
