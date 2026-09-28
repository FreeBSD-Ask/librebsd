#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_server_contract.py —— 第十一件门禁：重构2026 目录页服务器契约。

设立缘由（2026-09-28）
----------------------
重构2026 目录页的服务器层长期**无任何护栏**：两份实现并存（`serve_refactor2026.py`
8090 多线程 / `重构2026/server/serve_index.py` 80 单线程），二者**均缺传输压缩、
均缺安全响应头、均开启目录列表**，且 README 声称「不给目录列表」而实况相反。
页面本体的九件门禁全部以**产物**为对象，服务器**不在任何门禁的对象面内**。

本件以**运行中的服务器**为对象，逐项断言七类不变量。全部断言走真实 HTTP，
不做静态推断——「判据必须测正确性而非存在性」：压缩不仅要看 `Content-Encoding`
存在，还要**解压后与磁盘文件逐字节相等**。

断言（A–G）
-----------
A 压缩：`Accept-Encoding: gzip` 下 200 且 `Content-Encoding: gzip`，
  且**解压正文与磁盘 index.html 逐字节相等**（正确性，非存在性）
B 缓存：`Cache-Control` **不含** `no-store`（含则条件请求无从发起）
C 条件请求：带 `If-Modified-Since`（取 A 步的 `Last-Modified`）→ **304 且正文 0 字节**
D 目录列表：`/data/`、`/tests/`、`/script/` → **非 200**
E 白名单：`/index.html.bak-20260917`、`/data/outline.txt.bak83`、
  `/data/catalog.json`、`/_prep_20260915/` → **404**
F 安全头：`X-Content-Type-Options`、`Referrer-Policy`、`X-Frame-Options` 三者齐备
G 穿越：`/../CLAUDE.md`、`/%2e%2e%2fCLAUDE.md` → **404**

用法
----
    python audit_server_contract.py                 # 契约门禁（0 通过 / 1 失败）
    python audit_server_contract.py --port 18080    # 指定端口（默认自动取空闲端口）
    python audit_server_contract.py --selftest      # 判据非空自检：对内置缺陷服务器跑，
                                                    # 须 ≥4 项 FAIL（否则判据无判别力）
    python audit_server_contract.py --base URL      # 对已在跑的服务跑（不启子进程）

依赖：仅标准库。**门禁一律绑 127.0.0.1，不得绑 0.0.0.0**（避免测试期暴露工作树）。
"""
import argparse
import gzip
import http.client
import http.server
import os
import pathlib
import socket
import subprocess
import sys
import tempfile
import threading
import time

sys.stdout.reconfigure(encoding="utf-8")

REPO = pathlib.Path(__file__).resolve().parents[3]
BASE = REPO / "08-核查报告与多轮复核" / "重构2026"
SERVER = pathlib.Path(__file__).with_name("serve_refactor2026.py")
INDEX = BASE / "index.html"

HOST = "127.0.0.1"
TIMEOUT = 15


# ── HTTP 小工具 ──────────────────────────────────────────────────────────
def _req(port, path, headers=None, method="GET"):
    c = http.client.HTTPConnection(HOST, port, timeout=TIMEOUT)
    try:
        c.request(method, path, headers=headers or {})
        r = c.getresponse()
        body = r.read()
        return r.status, dict(r.getheaders()), body
    finally:
        c.close()


def free_port():
    s = socket.socket()
    s.bind((HOST, 0))
    p = s.getsockname()[1]
    s.close()
    return p


def wait_ready(port, tries=80):
    for _ in range(tries):
        try:
            _req(port, "/", {"Accept-Encoding": "identity"})
            return True
        except OSError:
            time.sleep(0.1)
    return False


# ── 断言集 ───────────────────────────────────────────────────────────────
def run_contract(port):
    """返回 [(编号, 名称, ok, detail), ...]"""
    out = []

    # A 压缩 + 正文正确性
    try:
        st, hd, body = _req(port, "/", {"Accept-Encoding": "gzip"})
        ok = st == 200 and hd.get("Content-Encoding", "").lower() == "gzip"
        detail = "status=%s encoding=%s" % (st, hd.get("Content-Encoding"))
        if ok:
            try:
                plain = gzip.decompress(body)
            except OSError as e:
                ok, detail = False, "gzip 解压失败：%r" % (e,)
            else:
                disk = INDEX.read_bytes()
                if plain == disk:
                    detail = "gzip %d B → 解压 %d B，与磁盘逐字节相等" % (
                        len(body), len(plain))
                else:
                    ok = False
                    detail = "解压正文与磁盘不符（%d vs %d 字节）" % (
                        len(plain), len(disk))
        out.append(("A", "传输压缩（gzip）且正文逐字节正确", ok, detail))
        last_mod = hd.get("Last-Modified")
    except OSError as e:
        out.append(("A", "传输压缩（gzip）且正文逐字节正确", False, repr(e)))
        last_mod = None

    # B 缓存语义
    try:
        st, hd, _ = _req(port, "/")
        cc = hd.get("Cache-Control", "")
        ok = "no-store" not in cc.lower()
        out.append(("B", "Cache-Control 不含 no-store（否则 304 不可达）", ok,
                    "Cache-Control=%r" % cc))
    except OSError as e:
        out.append(("B", "Cache-Control 不含 no-store（否则 304 不可达）", False, repr(e)))

    # C 条件请求 → 304
    try:
        h = {"If-Modified-Since": last_mod} if last_mod else {}
        st, hd, body = _req(port, "/", h)
        ok = st == 304 and len(body) == 0
        out.append(("C", "条件请求回 304 且正文 0 字节", ok,
                    "status=%s body=%d B（Last-Modified=%s）" % (st, len(body), last_mod)))
    except OSError as e:
        out.append(("C", "条件请求回 304 且正文 0 字节", False, repr(e)))

    # D 目录列表
    bad = []
    for p in ("/data/", "/tests/", "/script/", "/"):
        try:
            st, _, _ = _req(port, p)
        except OSError as e:
            bad.append("%s→%r" % (p, e))
            continue
        if p == "/":
            continue
        if st == 200:
            bad.append("%s→200" % p)
    out.append(("D", "目录列表不可枚举（/data/、/tests/、/script/ 非 200）",
                not bad, "违规：%s" % (", ".join(bad) or "无")))

    # E 白名单（备份/构建期件不可达）
    bad = []
    for p in ("/index.html.bak-20260917", "/data/outline.txt.bak83",
              "/data/catalog.json", "/_prep_20260915/", "/server/README.md"):
        try:
            st, _, _ = _req(port, p)
        except OSError as e:
            bad.append("%s→%r" % (p, e))
            continue
        if st != 404:
            bad.append("%s→%s" % (p, st))
    out.append(("E", "docroot 白名单：备份与构建期件一律 404", not bad,
                "违规：%s" % (", ".join(bad) or "无")))

    # F 安全响应头
    need = ("X-Content-Type-Options", "Referrer-Policy", "X-Frame-Options")
    try:
        _, hd, _ = _req(port, "/")
        low = {k.lower(): v for k, v in hd.items()}
        miss = [n for n in need if n.lower() not in low]
        out.append(("F", "安全响应头齐备（nosniff/Referrer-Policy/XFO）",
                    not miss, "缺失：%s" % (", ".join(miss) or "无")))
    except OSError as e:
        out.append(("F", "安全响应头齐备（nosniff/Referrer-Policy/XFO）", False, repr(e)))

    # G 路径穿越
    bad = []
    for p in ("/../CLAUDE.md", "/%2e%2e%2fCLAUDE.md", "/..%2fCLAUDE.md"):
        try:
            st, _, _ = _req(port, p)
        except OSError as e:
            bad.append("%s→%r" % (p, e))
            continue
        if st != 404:
            bad.append("%s→%s" % (p, st))
    out.append(("G", "路径穿越拦截（../ 与 %2e%2e%2f 一律 404）", not bad,
                "违规：%s" % (", ".join(bad) or "无")))

    # H 新鲜度：内容变了必须立刻生效（压缩缓存不得导致陈旧）
    #   在**临时 docroot** 上另起一台实例测，绝不触碰真实 index.html 的 mtime。
    out.append(_check_freshness())
    return out


def _check_freshness():
    """临时 docroot：写入 v1 → 请求 → 改写 v2（mtime 前进）→ 带 IMS 再请求，须回 200 + v2。"""
    port = free_port()
    root = tempfile.mkdtemp(prefix="srvfresh_")
    idx = pathlib.Path(root) / "index.html"
    idx.write_text("<html>v1</html>", encoding="utf-8")
    (pathlib.Path(root) / "assets").mkdir()
    (pathlib.Path(root) / "assets" / "favicon.ico").write_bytes(b"\x00")
    proc = subprocess.Popen(
        [sys.executable, str(SERVER), "--root", root, "--bind", HOST,
         "--port", str(port), "--no-pidfile"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        if not wait_ready(port):
            return ("H", "新鲜度：改写后立刻生效（压缩缓存不得陈旧）", False,
                    "临时实例未就绪")
        _, hd, _ = _req(port, "/", {"Accept-Encoding": "identity"})
        lm = hd.get("Last-Modified")
        # mtime 前进 2 秒（文件系统时间戳粒度）
        t = time.time() + 2
        os.utime(idx, (t, t))
        idx.write_text("<html>v2</html>", encoding="utf-8")
        os.utime(idx, (t, t))
        st, _, body = _req(port, "/", {"If-Modified-Since": lm or ""})
        ok = st == 200 and b"v2" in body
        return ("H", "新鲜度：改写后立刻生效（压缩缓存不得陈旧）", ok,
                "status=%s body=%r（期望 200 + v2；若为 304 则缓存陈旧）"
                % (st, body[:24]))
    except OSError as e:
        return ("H", "新鲜度：改写后立刻生效（压缩缓存不得陈旧）", False, repr(e))
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


# ── 内置缺陷服务器（判据非空自检用） ────────────────────────────────────
class _DefectiveHandler(http.server.SimpleHTTPRequestHandler):
    """刻意复现 2026-09-28 修复前的三类缺陷：无压缩、no-store、开目录列表、无安全头。"""

    protocol_version = "HTTP/1.0"

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, *a):
        pass


def _start_defective(port):
    """起一台「修复前形态」的服务器：SimpleHTTPRequestHandler + no-store，无压缩无安全头。"""
    root = tempfile.mkdtemp(prefix="srvbad_")
    (pathlib.Path(root) / "index.html").write_text("<html>bad</html>", encoding="utf-8")
    (pathlib.Path(root) / "data").mkdir()
    (pathlib.Path(root) / "data" / "outline.txt.bak83").write_text("x", encoding="utf-8")
    srv = http.server.ThreadingHTTPServer(
        (HOST, port),
        lambda *a, **kw: _DefectiveHandler(*a, directory=root, **kw))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, root


# ── 主流程 ───────────────────────────────────────────────────────────────
def _report(rows, title):
    print("=" * 72)
    print(title)
    print("=" * 72)
    fails = 0
    for code, name, ok, detail in rows:
        print("  [%s] %-6s %-44s %s" % ("PASS" if ok else "FAIL", code, name, detail))
        if not ok:
            fails += 1
    print("-" * 72)
    print("  合计 %d 项，FAIL %d 项" % (len(rows), fails))
    return fails


def cmd_selftest():
    """判据非空：对内置缺陷服务器跑，FAIL 集须包含 {A,B,D,F}。"""
    port = free_port()
    srv, root = _start_defective(port)
    try:
        if not wait_ready(port):
            print("自检失败：内置缺陷服务器未就绪", file=sys.stderr)
            return 2
        rows = run_contract(port)
    finally:
        srv.shutdown()
        srv.server_close()
    fails = _report(rows, "判据非空自检：内置缺陷服务器（预期 A/B/D/F 必 FAIL）")
    got = {c for c, _n, ok, _d in rows if not ok}
    need = {"A", "B", "D", "F"}
    missing = sorted(need - got)
    if not missing:
        print("  ✅ 判据非空：A/B/D/F 全部命中（共 %d 项 FAIL），判据具判别力" % fails)
        return 0
    print("  ❌ 判据可能为空：未命中 %s（实际 FAIL 集 = %s）"
          % (", ".join(missing), sorted(got) or "空"), file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(description="重构2026 服务器契约门禁（第十一件）")
    ap.add_argument("--port", type=int, default=0)
    ap.add_argument("--base", default="")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--keep", action="store_true", help="跑完不杀子进程（调试用）")
    args = ap.parse_args()

    if args.selftest:
        return cmd_selftest()

    if args.base:
        port = int(args.base.rsplit(":", 1)[-1].rstrip("/"))
        rows = run_contract(port)
        return 1 if _report(rows, "服务器契约门禁（外部目标 %s）" % args.base) else 0

    if not SERVER.is_file():
        print("依赖缺失：找不到 %s" % SERVER, file=sys.stderr)
        return 2
    if not INDEX.is_file():
        print("依赖缺失：找不到 %s" % INDEX, file=sys.stderr)
        return 2

    port = args.port or free_port()
    proc = subprocess.Popen(
        [sys.executable, str(SERVER), "--bind", HOST, "--port", str(port),
         "--no-pidfile"],
        stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    try:
        if not wait_ready(port):
            err = proc.stderr.read().decode("utf-8", "replace") if proc.stderr else ""
            print("服务器未就绪（port=%d）：\n%s" % (port, err), file=sys.stderr)
            return 2
        rows = run_contract(port)
        fails = _report(rows, "服务器契约门禁（第十一件）：127.0.0.1:%d" % port)
    finally:
        if not args.keep:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
