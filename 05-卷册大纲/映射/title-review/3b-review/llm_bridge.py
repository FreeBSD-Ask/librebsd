# -*- coding: utf-8 -*-
"""3B 标题审定 · LLM 桥（本会话半实时建议的取件与回填）。

页面点“获取建议”后，请求进入服务端队列；本脚本供会话侧使用：

    python llm_bridge.py --list                    # 列出待处理请求（含上下文）
    python llm_bridge.py --result results.json     # 回填候选（JSON 数组）
    python llm_bridge.py --status s1234567890abcd # 查看单条

results.json 形如：
    [{"id": "s1234abcd", "candidates": [
        {"candidate_id": "c1", "new_title": "……", "rationale": "……"}, …]}]
    [{"id": "s1234abcd", "error": "无法生成的原因"}]

服务端地址默认 http://127.0.0.1:8899，可用 --base 覆盖。
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request

DEFAULT_BASE = "http://127.0.0.1:8899"


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


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="3B 实时建议队列桥")
    parser.add_argument("--base", default=DEFAULT_BASE)
    parser.add_argument("--list", action="store_true", help="列出待处理请求")
    parser.add_argument("--status", metavar="ID", help="查看单条请求")
    parser.add_argument("--result", metavar="JSON", help="回填候选结果")
    args = parser.parse_args(argv)
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
