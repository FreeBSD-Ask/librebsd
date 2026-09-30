# speckit-spec-tasks-check —— 便携安装说明

一条命令出 Trae Spec 式产物：**spec.md → plan.md → tasks.md → checklist.md**（落到 `specs/NNN-<slug>/`）。

## 包内容

```text
speckit-spec-tasks-check/
├── SKILL.md              技能本体（含环境探测与两条执行路径）
├── INSTALL.md            本文件
└── assets/
    ├── spec-template.md      规格模板
    ├── plan-template.md      计划模板
    ├── tasks-template.md     任务模板
    └── checklist-template.md 检查点模板
```

模板取自 GitHub Spec Kit（MIT 许可）。

## 安装（两种装法，选一）

**用户级＝全局安装（推荐，装一次所有项目可用，本机现状即此）**

```sh
mkdir -p ~/.zcode/skills/speckit-spec-tasks-check
cp -r speckit-spec-tasks-check/* ~/.zcode/skills/speckit-spec-tasks-check/
```

Linux／macOS／Git Bash 同用此路径写法；Windows 上 `~/.zcode/skills/` 即 `C:\Users\<你>\.zcode\skills\`。

**项目级（备选，仅该项目可用、随项目走）**

```sh
mkdir -p <你的项目>/.zcode/skills/speckit-spec-tasks-check
cp -r speckit-spec-tasks-check/* <你的项目>/.zcode/skills/speckit-spec-tasks-check/
```

也可直接用资源管理器把整个 `speckit-spec-tasks-check` 文件夹拖进目标 `.zcode/skills/` 下。

**注意**：①同名技能**用户级优先**于项目级（ZCode 口径），故全局装过就不必再装项目级，免得两份漂移；②**技能改动需新开 ZCode 会话才生效**（技能在会话启动时扫描）；③全局安装后技能在任何项目可用——项目里没有 Spec Kit 时自动走模式 B。

## 两条执行路径（技能自动判断，无需配置）

| 环境 | 走哪条 | 行为 |
| ---- | ------ | ---- |
| 项目里已有 `.specify/templates/` 且 `.zcode/skills/` 下有上游 `speckit-specify`／`-plan`／`-tasks` | 模式 A | 复用 Spec Kit 上游技能与脚本完整执行，上游升级自动跟随 |
| 只有 ZCode | 模式 B | 用本包 `assets/` 模板直出，**不依赖 Spec Kit、不依赖 PowerShell 脚本** |

也就是说：装不装 Spec Kit 都能用，四件产物一样。

## 验证安装

1. 新开 ZCode 会话（在装了技能的项目目录下）。
2. 敲一条测试需求：

   ```text
   /speckit-spec-tasks-check 做一个测试功能：支持导出用户列表为 CSV
   ```

3. 检查项目下生成了 `specs/001-<slug>/`，内含 `spec.md`／`plan.md`／`tasks.md`／`checklist.md`。
4. 确认 `checklist.md` 每条都是可判定的（含具体条件／数量／路径），且全部为未勾选 `[ ]`。

## 可选：装完整 Spec Kit（想用上游其余能力时）

模式 A 才需要。目标机需 Python 3.11+ 与 uv：

```sh
uv tool install specify-cli
cd <你的项目>
specify init --here --integration zcode --non-interactive --force --ignore-agent-tools
```

`--ignore-agent-tools` 用于跳过「检测不到 zcode 可执行文件」的告警（官方集成清单含 ZCode，仅检测器认不出 CLI 名，功能不受影响）。装完会在项目里生成 `.specify/`（模板、workflow、脚本）与 `.zcode/skills/` 下的 10 个上游 `speckit-*` 技能。

## 卸载

删掉对应的 `speckit-spec-tasks-check` 目录即可（技能无副作用，不写注册表、不改全局配置）。

## 与 Trae Spec 的对应关系

| Trae | 本技能 |
| ---- | ------ |
| spec.md | `spec.md`（用户故事＋可判定需求＋成功判据） |
| tasks.md | `tasks.md`（按故事分组、`[P]` 并行、依赖图） |
| checklist.md（可判定验收单） | `checklist.md`（四层组织、逐条追溯到 spec／task、生成时不勾选） |
| — | `plan.md`（超集；模式 A 下是脚本硬依赖，不可省） |

差异说明：不设 Trae 的「审批闸门」——本技能按需求一口气出四件，中间不停；如需中途确认（如 spec 写完后停下等你过目），可在需求描述里写明「写完 spec 先停下等我确认」。
