#!/bin/bash
# ============================================================
# librebsd 工作区监视器 — 单轮检查（由 _watch_git.ps1 每 5 分钟调用）
#
# 职责：
#   1. 检测工作区是否有"未暂存改动 + 未跟踪新文件 + 已暂存"
#   2. 若有：写中文提交信息草稿到 script/_commit_msg.txt
#           并把全部变更文件 git add（暂存，绝不 commit）
#   3. 若无：幂等退出（不产生任何副作用）
#
# 铁律：
#   - 绝不执行 git commit
#   - 绝不 rm 任何业务文件；trap 只清理自己的锁文件
#
# 沟通协议（文件即状态）：
#   script/_watch_git.lock    —— 锁文件，防并发双跑
#   script/_commit_msg.txt    —— 提交信息草稿（覆盖写）
#   script/_watch_last.log    —— 最近一次扫描结果（覆盖写）
#   script/_watch_history.log —— 追加式历次动作历史
#
# ⚠ 关键：PATH 必须自足（后台任务环境缺 POSIX 工具链），
#  且必须放在最顶部、任何命令解析之前。
# =========================================================
export PATH="/c/Program Files/Git/usr/bin:/c/Program Files/Git/bin:/c/Program Files/Git/cmd:/usr/bin:/bin:$PATH"
hash -r 2>/dev/null || true

# 与 ps1 保持一致：仓库绝对路径（不依赖 dirname）
REPO="/d/librebsd"
cd "$REPO" || exit 1

NOW="$(date "+%F %T")"               # 2026-09-16 01:55:00
LOG="script/_watch_last.log"
HIST="script/_watch_history.log"
MSG="script/_commit_msg.txt"
LOCK="script/_watch_git.lock"

# ---------- 0. 锁：防并发双跑（陈旧锁自动接管） ----------
if [ -f "$LOCK" ]; then
  LOCK_PID=$(cat "$LOCK" 2>/dev/null)
  if [ -n "$LOCK_PID" ] && kill -0 "$LOCK_PID" 2>/dev/null; then
    echo "[$NOW] 另一监视器实例运行中 (pid=$LOCK_PID)，退出" >> "$HIST"
    exit 0
  fi
  rm -f "$LOCK"   # 所有者失联 → 清理陈旧锁
fi
echo $$ > "$LOCK"
trap 'rm -f "$LOCK"' EXIT

# ---------- 1. 收集工作区变更（未暂存 M/T/D + 未跟踪 ?? + 已暂存） ----------
# 排除监视器自身产物（script/）与 .workbuddy-ai（记忆归会话管理）
# ⚠ 必须用 -z（NUL 分隔）解析：porcelain 对含空格/特殊字符的路径会加引号，
#   用 awk $2 分词会把路径截断（实测「采访录：Craig Federighi.md」被截断导致误报）
CHANGED=$(git status --porcelain=v1 --untracked-files=all -z | while IFS= read -r -d '' entry; do
  p="${entry:3}"                       # 跳过 "XY " 两字符状态前缀
  case "$p" in
    script/*|.workbuddy-ai/*|.workbuddy-ai) continue ;;
  esac
  printf '%s\n' "$p"
done)

NUM=$(printf '%s\n' "$CHANGED" | grep -c . )
echo "[$NOW] changed_files=$NUM" > "$LOG"

# ---------- 1.5 五分钟闸门：距上次扫描不足 300 秒则跳过（幂等） ----------
# 由循环器（90 秒心跳）高频探测，但实际扫描仍严格保持每 5 分钟一次
if [ -f "$LOG" ]; then
  LAST=$(sed -n 's/^\[\([0-9-]* [0-9:]*\)\] changed_files=.*/\1/p' "$LOG" | tail -n 1)
  if [ -n "$LAST" ] && [ "$LAST" != "$NOW" ]; then
    LAST_EPOCH=$(date -d "$LAST" +%s 2>/dev/null)
    NOW_EPOCH=$(date -d "$NOW" +%s 2>/dev/null)
    if [ -n "$LAST_EPOCH" ] && [ -n "$NOW_EPOCH" ] && [ $((NOW_EPOCH - LAST_EPOCH)) -lt 300 ]; then
      echo "[$NOW] 距上次扫描不足5分钟，跳过 (elapsed=$((NOW_EPOCH - LAST_EPOCH))s)" >> "$HIST"
      exit 0
    fi
  fi
fi

# 无改动 → 幂等退出（草稿置占位，避免旧草稿误导）
if [ -z "$CHANGED" ]; then
  echo "（当前无待提交变更）" > "$MSG"
  echo "[$NOW] 无变更，退出" >> "$HIST"
  exit 0
fi

# ---------- 2. 路径存在性校验（幽灵路径不动工） ----------
MISSING=$(printf '%s\n' "$CHANGED" | while IFS= read -r f; do [ -e "$f" ] || echo "$f"; done)
if [ -n "$MISSING" ]; then
  echo "[$NOW] ERROR 变更清单含不存在路径:" >> "$HIST"
  printf '%s\n' "$MISSING" >> "$HIST"
  exit 1
fi

# ---------- 3. 暂存（仅 add，绝不 commit；路径以正斜杠传入） ----------
{
  echo "[$NOW] git add 开始"
  printf '%s\n' "$CHANGED" | while IFS= read -r p; do
    git add -- "$p" 2>&1
  done
  echo "[$NOW] git add 结束"
} >> "$HIST"

# ---------- 4. 计算行数摘要（必须在 add 之后：此时全部已暂存，numstat 才准确） ----------
STATS=$(printf '%s\n' "$CHANGED" | while IFS= read -r f; do
  git diff --cached --numstat -- "$f" 2>/dev/null
done | awk '{a+=$1; d+=$2} END {print a "+," d "-"}')
[ -z "$STATS" ] && STATS="0+, 0-"

# ---------- 5. 撰写提交信息（中文，按卷分组、带语义） ----------
{
  echo "历史资料库 · 大纲宿主更新（$NUM 个文件，$STATS 行）"
  echo ""
  # 按卷聚合
  printf '%s\n' "$CHANGED" | sed -nE 's|^05-卷册大纲/(第[0-9]+卷-[^/]+)/.*|\1|p' | sort | uniq -c | \
    awk '{printf "  %d 个文件 | %s\n", $1, $2}'
  echo ""
  echo "变更明细："
  printf '%s\n' "$CHANGED" | sed 's/^/  - /'
  echo ""
  echo "—— 由监视器自动暂存，未提交"
  echo "生成时间：$NOW"
} > "$MSG"
echo "[$NOW] 提交信息已写 $MSG ($NUM 个文件)" >> "$HIST"

# ---------- 6. 落盘校验：暂存区新增行数 ----------
STAGED=$(git diff --cached --numstat | awk '{a+=$1} END {print a+0}')
echo "[$NOW] 暂存新增行数=$STAGED" >> "$HIST"

exit 0