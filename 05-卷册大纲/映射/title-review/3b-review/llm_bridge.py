# -*- coding: utf-8 -*-
"""3B 标题审定 · LLM 桥（Python 侧轮询，主代理实时回填）。

页面点“获取建议”后，请求进入服务端队列；本脚本提供两种用法：

    python llm_bridge.py --watch                   # 常驻轮询：新请求写入收件箱，自动投递回执
    python llm_bridge.py --list                    # 一次性列出待处理请求（含上下文）
    python llm_bridge.py --result results.json     # 一次性回填候选（JSON 数组）
    python llm_bridge.py --status s1234567890abcd  # 查看单条

--watch 的运行方式：
    每 2 秒轮询 /api/suggest?pending=1；发现新请求即追加到
    data/suggest/inbox.jsonl 并打印 [NEW] 行；同时扫描
    data/suggest/outbox/*.json，发现回执即 POST /api/suggest/result，
    成功后移入 outbox/sent/，打印 [SENT] 行。主代理只需读收件箱、写回执。

results.json 形如：
    [{"id": "s1234abcd", "candidates": [
        {"candidate_id": "c1", "new_title": "……", "rationale": "……"}, …]}]
    [{"id": "s1234abcd", "error": "无法生成的原因"}]

服务端地址默认 http://127.0.0.1:8899，可用 --base 覆盖。
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_BASE = "http://127.0.0.1:8899"
DEFAULT_DATA = Path(__file__).resolve().parent / "data" / "suggest"


def call(base: str, method: str, path: str, payload=None, timeout=20):
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(base + path, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        raise SystemExit(f"HTTP {exc.code} {path}：{detail}")
    except urllib.error.URLError as exc:
        raise SystemExit(f"无法连接 {base}：{exc.reason}")
    return json.loads(body.decode("utf-8")) if body else None


def cmd_list(base: str) -> int:
    data = call(base, "GET", "/api/suggest?pending=1")
    pending = data.get("pending", [])
    if not pending:
        print("待处理 0 条")
        return 0
    print(f"待处理 {len(pending)} 条：")
    for item in pending:
        print(
            json.dumps(
                {
                    "id": item["id"],
                    "unit_key": item["unit_key"],
                    "level": item.get("level"),
                    "vol": item.get("vol"),
                    "chapter_no": item.get("chapter_no"),
                    "section_no": item.get("section_no"),
                    "title": item.get("title"),
                    "thesis": item.get("thesis"),
                    "tags": item.get("tags"),
                    "merge_target": item.get("merge_target"),
                    "created_at": item.get("created_at"),
                },
                ensure_ascii=False,
            )
        )
    return 0


def cmd_status(base: str, rid: str) -> int:
    print(json.dumps(call(base, "GET", "/api/suggest?id=" + rid), ensure_ascii=False, indent=2))
    return 0


def cmd_result(base: str, path: str) -> int:
    with open(path, encoding="utf-8-sig") as handle:
        results = json.load(handle)
    if isinstance(results, dict):
        results = results.get("results", [results])
    data = call(base, "POST", "/api/suggest/result", {"results": results})
    print(json.dumps(data, ensure_ascii=False))
    return 0 if not data.get("errors") else 1


def cmd_watch(base: str, data_dir: Path, interval: float) -> int:
    """常驻轮询：新请求入收件箱，outbox 回执自动投递。"""
    data_dir.mkdir(parents=True, exist_ok=True)
    inbox = data_dir / "inbox.jsonl"
    outbox = data_dir / "outbox"
    sent = outbox / "sent"
    outbox.mkdir(parents=True, exist_ok=True)
    sent.mkdir(parents=True, exist_ok=True)
    heartbeat = data_dir / "watch.heartbeat"

    seen = set()
    if inbox.exists():
        for line in inbox.read_text(encoding="utf-8-sig").splitlines():
            try:
                seen.add(json.loads(line)["id"])
            except (ValueError, KeyError):
                continue
    print(f"[WATCH] base={base} interval={interval}s inbox={inbox}", flush=True)

    offline = False
    while True:
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            pending = call(base, "GET", "/api/suggest?pending=1", timeout=8).get("pending", [])
            if offline:
                print(f"[ONLINE] {now} 服务恢复", flush=True)
                offline = False
            for item in pending:
                rid = item["id"]
                if rid in seen:
                    continue
                seen.add(rid)
                record = {
                    "seen_at": now,
                    **{k: item.get(k) for k in (
                        "id", "unit_key", "level", "vol", "chapter_no", "section_no",
                        "title", "thesis", "tags", "merge_target", "created_at",
                    )},
                }
                with inbox.open("a", encoding="utf-8") as handle:
                    handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                print(f"[NEW] {rid} {item.get('unit_key')} tags={'+'.join(item.get('tags') or [])}"
                      f" title={item.get('title')}", flush=True)

            for path in sorted(outbox.glob("*.json")):
                try:
                    with path.open(encoding="utf-8-sig") as handle:
                        payload = json.load(handle)
                except (OSError, ValueError) as exc:
                    print(f"[BAD] {path.name}：{exc}", flush=True)
                    shutil.move(str(path), str(sent / path.name))
                    continue
                results = payload.get("results") if isinstance(payload, dict) else payload
                if not isinstance(results, list):
                    results = [payload]
                try:
                    reply = call(base, "POST", "/api/suggest/result", {"results": results}, timeout=20)
                except SystemExit as exc:
                    print(f"[FAIL] {path.name}：{exc}", flush=True)
                    shutil.move(str(path), str(sent / path.name))
                    continue
                print(f"[SENT] {path.name} applied={reply.get('applied')} "
                      f"errors={reply.get('errors')}", flush=True)
                shutil.move(str(path), str(sent / path.name))

            heartbeat.write_text(now, encoding="utf-8")
        except SystemExit:
            if not offline:
                print(f"[WAIT] {now} 服务不可达，{interval}s 后重试", flush=True)
                offline = True
        except Exception as exc:  # noqa: BLE001 - 常驻进程不因单次异常退出
            if not offline:
                print(f"[WAIT] {now} {exc}", flush=True)
                offline = True
        time.sleep(interval)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="3B 实时建议队列桥")
    parser.add_argument("--base", default=DEFAULT_BASE)
    parser.add_argument("--list", action="store_true", help="列出待处理请求")
    parser.add_argument("--watch", action="store_true", help="常驻轮询（Python 侧）")
    parser.add_argument("--interval", type=float, default=2.0, help="轮询间隔秒，默认 2")
    parser.add_argument("--data", default=str(DEFAULT_DATA), help="收件箱与 outbox 目录")
    parser.add_argument("--status", metavar="ID", help="查看单条请求")
    parser.add_argument("--result", metavar="JSON", help="回填候选结果")
    args = parser.parse_args(argv)
    if args.watch:
        return cmd_watch(args.base, Path(args.data), args.interval)
    if args.list:
        return cmd_list(args.base)
    if args.status:
        return cmd_status(args.base, args.status)
    if args.result:
        return cmd_result(args.base, args.result)
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
