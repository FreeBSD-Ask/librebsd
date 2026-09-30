# speckit-spec-tasks-check —— 便携安装说明

一条命令出 Trae Spec 式产物：**spec.md → plan.md → tasks.md → checklist.md**（落到 `specs/NNN-<slug>/`）。

## 包内容

```text
speckit-spec-tasks-check/
├── SKILL.md     技能本体
└── INSTALL.md   本文件
```

包内**不含模板**——四件的骨架全部来自 Spec Kit 上游（`.specify/templates/`）。技能在目标项目未装 Spec Kit 时**会自动安装它**（见下节）。

## 安装技能（全局，装一次所有项目可用）

```sh
mkdir -p ~/.zcode/skills/speckit-spec-tasks-check
cp -r speckit-spec-tasks-check/* ~/.zcode/skills/speckit-spec-tasks-check/
```

Windows 上 `~/.zcode/skills/` 即 `C:\Users\<你>\.zcode\skills\`；也可直接用资源管理器把整个 `speckit-spec-tasks-check` 文件夹拖进去。

**注意**：①同名技能**用户级优先**于项目级，全局装过就不必再装项目级；②**技能改动需新开 ZCode 会话才生效**（技能在会话启动时扫描）。

## 前置条件（供技能自动安装 Spec Kit 用）

| 条件 | 说明 |
| ---- | ---- |
| 网络 | 首次在某个项目使用时需联网装 CLI 与模板 |
| uv | `specify-cli` 用 uv 安装；无 uv 时先 `pip install uv` |
| Python 3.11+ | specify-cli 的运行环境 |

装了技能但缺上述条件时，技能会**停止并报告失败原因**，不会用自造模板糊过去。

## 技能会自己做的事（无需手工）

在**尚未装 Spec Kit 的项目**里第一次使用本技能时，它会自动执行：

```sh
uv tool install specify-cli
specify init --here --integration zcode --non-interactive --force --ignore-agent-tools
```

随后在该项目生成 `.specify/`（模板、workflow、PowerShell 脚本）与 `.zcode/skills/` 下的 10 个上游 `speckit-*` 技能，然后继续出四件产物。项目已装过 Spec Kit 时这一步直接跳过。

想手工预装（可选，等价）：

```sh
uv tool install specify-cli
cd <你的项目>
specify init --here --integration zcode --non-interactive --force --ignore-agent-tools
```

三个参数都是必需：`--here` 与项目名互斥；目录非空时非交互必须 `--force`；`--ignore-agent-tools` 跳过「检测不到 zcode 可执行文件」的检查（该检查只影响自检提示，不影响功能）。

## 验证安装

1. 新开 ZCode 会话。
2. 敲一条测试需求：

   ```text
   /speckit-spec-tasks-check 做一个测试功能：支持导出用户列表为 CSV
   ```

3. 检查项目下生成了 `specs/001-<slug>/`，内含 `spec.md`／`plan.md`／`tasks.md`／`checklist.md`（新项目同时会看到 `.specify/` 被建出来）。
4. 确认 `checklist.md` 每条都可判定（含具体条件／数量／路径），且全部为未勾选 `[ ]`。

## 卸载

删掉 `~/.zcode/skills/speckit-spec-tasks-check` 目录即可（技能本身无副作用）。技能在各项目里装出的 `.specify/` 与 `specs/` 属项目自身内容，按项目需要自行保留或删除。

## 与 Trae Spec 的对应关系

| Trae | 本技能 |
| ---- | ------ |
| spec.md | `spec.md`（用户故事＋可判定需求＋成功判据） |
| tasks.md | `tasks.md`（按故事分组、`[P]` 并行、依赖图） |
| checklist.md（可判定验收单） | `checklist.md`（四层组织、逐条追溯到 spec／task、生成时不勾选） |
| — | `plan.md`（超集；同时也是 Spec Kit 脚本的硬依赖，不可省） |

差异说明：不设 Trae 的「审批闸门」——本技能按需求一口气出四件，中间不停；如需中途确认（如 spec 写完后停下等你过目），可在需求描述里写明「写完 spec 先停下等我确认」。
