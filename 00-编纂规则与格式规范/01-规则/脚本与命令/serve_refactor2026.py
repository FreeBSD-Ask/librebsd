#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重构2026 目录页局域网服务器（固定脚本，规则引用资源）—— **唯一实现**。

2026-09-28 归一重写：本脚本是重构2026 目录页的**唯一服务器实现**。
此前并存两份（本脚本旧版 0.0.0.0:8090 多线程；`08-核查报告与多轮复核/重构2026/
server/serve_index.py` 0.0.0.0:80 单线程），二者**语义分叉**且**均缺压缩、均缺安全
响应头、均开启目录列表**。旧 `serve_index.py` 已归档至 `script/_archive/`。

设计要点
--------
1. **docroot 白名单**：只服务显式清单（`/`、`/index.html`、`/favicon.ico`），
   其余一律 404。不继承 `SimpleHTTPRequestHandler`，**目录列表能力在结构上不存在**
   （父类为 `BaseHTTPRequestHandler`，无 `list_directory`）。
2. **传输压缩 + 新鲜度**：按需读盘并预压 gzip 缓存；**mtime 变即重读**，故
   `assemble_index.py` 重装配后**无需重启服务**即可拿到新版（与压缩缓存两者兼得）。
   实测 1,583,076 B → 890,469 B（-43.8%）。
3. **缓存语义**：`Cache-Control: no-cache`（允许存储、强制再验证）。**不用 no-store**
   ——no-store 禁止存储会使条件请求无从发起，每次刷新全量重传；改用 no-cache 后
   磁盘未变即回 304、正文 0 字节，而重装配后 mtime 变则自动回 200，新鲜度语义不变。
4. **安全响应头**：补 62 号文 §7/§8 声明而现存实现均未发送者。HTTP 下 HSTS 不适用，
   不发送并在 README 注明原因。
5. **只读**：仅 GET/HEAD；其余方法 501。
6. **幂等**：端口被占用即静默退出（退出码 0），重复拉起不产生重复实例。

用法
----
    python serve_refactor2026.py                       # 0.0.0.0:8090（局域网可达）
    python serve_refactor2026.py --port 18080
    python serve_refactor2026.py --bind 127.0.0.1      # 仅本机（门禁用）
    python serve_refactor2026.py --root D:\\某目录 --port 8080
    python serve_refactor2026.py --port 80 --pidfile D:\\librebsd\\_tmp\\senseindex_80.pid

停止：Ctrl+C；或用 PID 文件（默认 `%LOCALAPPDATA%\\senseindex\\serve_refactor2026_<port>.pid`，
`--pidfile` 可改路径）精确结束。

修订（2026-10-03）：文档自始宣称支持 `--pidfile`，argparse 却未定义该参数（实测传参即
usage error，文档与实现不符）。本次补齐 `--pidfile PATH`：仅覆盖 PID 文件**路径**，
默认路径与既有行为不变；`--no-pidfile` 语义不变。
"""
import argparse
import email.utils
import gzip
import http.server
import io
import os
import socket
import sys
import time

# 必须在其它导入之前：不写 __pycache__、不加载用户站点包
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
os.environ.setdefault("PYTHONNOUSERSITE", "1")

DEFAULT_ROOT = r"D:\librebsd\08-核查报告与多轮复核\重构2026"
DEFAULT_PORT = 8090
DEFAULT_BIND = "0.0.0.0"

# ── docroot 白名单 ────────────────────────────────────────────────────────
# 请求路径 → 相对 docroot 的磁盘路径。**只列此处**，其余一律 404。
ALLOW = {
    "/": "index.html",
    "/index.html": "index.html",
    "/favicon.ico": "assets/favicon.ico",   # 浏览器兜底请求；不列会留控制台 404
}

# ── 响应头 ────────────────────────────────────────────────────────────────
CACHE_HEADERS = (
    ("Cache-Control", "no-cache"),          # 允许存储 + 强制再验证 → 可 304
    ("Pragma", "no-cache"),
)
SECURITY_HEADERS = (
    ("X-Content-Type-Options", "nosniff"),
    ("Referrer-Policy", "no-referrer"),
    ("X-Frame-Options", "DENY"),
    ("Permissions-Policy",
     "geolocation=(), microphone=(), camera=(), payment=(), usb=()"),
    ("Cross-Origin-Opener-Policy", "same-origin"),
    ("Cross-Origin-Resource-Policy", "same-origin"),
    # HSTS 仅在 HTTPS 下有意义，本服务为 HTTP，**刻意不发送**。
)

MIME = {
    ".html": "text/html; charset=utf-8",
    ".ico": "image/x-icon",
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".svg": "image/svg+xml",
    ".json": "application/json; charset=utf-8",
}


class _Asset:
    """一份磁盘资产的只读快照（含预压缩体）。"""

    __slots__ = ("path", "raw", "gzb", "mtime", "ctype")

    def __init__(self, path: str):
        self.path = path
        with open(path, "rb") as f:
            self.raw = f.read()
        self.mtime = os.path.getmtime(path)
        self.ctype = MIME.get(os.path.splitext(path)[1].lower(),
                              "application/octet-stream")
        # 预压缩：mtime=0 保证确定性（同内容 → 同字节）
        buf = io.BytesIO()
        with gzip.GzipFile(fileobj=buf, mode="wb", compresslevel=6, mtime=0) as gz:
            gz.write(self.raw)
        self.gzb = buf.getvalue()


class Handler(http.server.BaseHTTPRequestHandler):
    """白名单只读处理器。父类无 list_directory，**目录列表结构上不可能**。"""

    server_version = "senseindex/2.0"
    sys_version = ""
    protocol_version = "HTTP/1.1"       # keep-alive；Content-Length 必发
    root = DEFAULT_ROOT
    _cache = {}                          # 路径 → _Asset

    # 不派生子进程、不回显命令行；日志静默，避免产生持续增长的文件
    def log_message(self, fmt, *args):
        pass

    # ── 内部 ─────────────────────────────────────────────────────────────
    @classmethod
    def _asset(cls, rel):
        """按需读盘 + 预压缓存；**mtime 变了就重读**，故重装配后无需重启服务。"""
        p = os.path.join(cls.root, rel)
        try:
            mt = os.path.getmtime(p)
        except OSError:
            return None
        a = cls._cache.get(rel)
        if a is None or a.mtime != mt:
            a = _Asset(p)
            cls._cache[rel] = a
        return a

    def _emit_headers(self, code, ctype, length, extra=()):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(length))
        for k, v in CACHE_HEADERS:
            self.send_header(k, v)
        for k, v in SECURITY_HEADERS:
            self.send_header(k, v)
        for k, v in extra:
            self.send_header(k, v)
        self.end_headers()

    def _respond(self, head_only=False):
        rel = ALLOW.get(self.path)
        if rel is None:
            body = b"HTTP 404\n"
            self._emit_headers(404, "text/plain; charset=utf-8", len(body))
            if not head_only:
                self.wfile.write(body)
            return
        a = self._asset(rel)
        if a is None:
            body = b"HTTP 500\n"
            self._emit_headers(500, "text/plain; charset=utf-8", len(body))
            if not head_only:
                self.wfile.write(body)
            return

        # 条件请求：磁盘未变 → 304（正文 0 字节）
        # ⚠️ 必须用 email.utils.parsedate_to_datetime：它返回带时区的 aware datetime。
        # 用 time.strptime(..., "%Z") + time.mktime 会把 GMT 当**本地时间**解释，
        # 在 UTC+8 上产生 -8h 偏移，使 mtime <= ims 恒为假 → 304 永不触发
        # （2026-09-28 实测：本件门禁 C 项即抓出此缺陷）。
        ims = self.headers.get("If-Modified-Since")
        if ims and "If-None-Match" not in self.headers:
            try:
                ims_t = email.utils.parsedate_to_datetime(ims).timestamp()
            except (TypeError, IndexError, OverflowError, ValueError):
                ims_t = None
            if ims_t is not None and int(a.mtime) <= int(ims_t):
                self.send_response(304)
                for k, v in CACHE_HEADERS:
                    self.send_header(k, v)
                self.end_headers()
                return

        want_gz = "gzip" in self.headers.get("Accept-Encoding", "")
        body = a.gzb if want_gz else a.raw
        extra = []
        if want_gz:
            extra.append(("Content-Encoding", "gzip"))
            extra.append(("Vary", "Accept-Encoding"))
        extra.append(("Last-Modified",
                      self.date_time_string(int(a.mtime))))
        self._emit_headers(200, a.ctype, len(body), extra)
        if not head_only:
            self.wfile.write(body)

    # ── 方法 ─────────────────────────────────────────────────────────────
    def do_GET(self):
        self._respond(head_only=False)

    def do_HEAD(self):
        self._respond(head_only=True)

    def _unsupported(self):
        body = b"HTTP 501\n"
        self.send_response(501)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    do_POST = do_PUT = do_DELETE = do_PATCH = do_OPTIONS = _unsupported


class Server(http.server.ThreadingHTTPServer):
    """多线程：keep-alive 下单线程会被慢客户端阻塞（旧版单线程为省内存的取舍）。"""

    daemon_threads = True
    # 必须为 False：Windows 上 SO_REUSEADDR 语义是“允许多个进程共享同一地址:端口”
    # （不是 Linux 的“越过 TIME_WAIT”），开着会让“端口被占用即静默退出”的幂等
    # 守卫失效，开出多个实例同时监听。
    allow_reuse_address = False


def lan_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def write_pid(port: int, path: str = "") -> str:
    """写 PID 文件；`path` 为空时用默认位置（%LOCALAPPDATA%\\senseindex）。"""
    try:
        if not path:
            d = os.path.join(os.environ.get("LOCALAPPDATA", ""), "senseindex")
            os.makedirs(d, exist_ok=True)
            path = os.path.join(d, "serve_refactor2026_%d.pid" % port)
        else:
            parent = os.path.dirname(os.path.abspath(path))
            if parent and not os.path.isdir(parent):
                os.makedirs(parent, exist_ok=True)
        with open(path, "w", encoding="ascii") as f:
            f.write("%d\n" % os.getpid())
        return path
    except OSError:
        return ""


def report_failure(exc: BaseException) -> None:
    """pythonw.exe 无控制台，启动失败时把原因落一份文件，否则无从排查。"""
    try:
        d = os.path.join(os.environ.get("LOCALAPPDATA", ""), "senseindex")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "serve_refactor2026.err.log"), "a",
                  encoding="utf-8") as f:
            from datetime import datetime, timezone
            f.write(datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                    + " " + repr(exc) + "\n")
    except OSError:
        pass


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="重构2026 目录页局域网服务器（唯一实现）")
    ap.add_argument("--root", default=DEFAULT_ROOT, help="docroot（默认仓库内 重构2026）")
    ap.add_argument("--port", type=int, default=DEFAULT_PORT)
    ap.add_argument("--bind", default=DEFAULT_BIND,
                    help="监听地址；局域网用 0.0.0.0，门禁/本机用 127.0.0.1")
    ap.add_argument("--no-pidfile", action="store_true")
    ap.add_argument("--pidfile", default="",
                    help="PID 文件路径（默认 %%LOCALAPPDATA%%\\senseindex\\"
                         "serve_refactor2026_<port>.pid）")
    args = ap.parse_args(argv)

    Handler.root = os.path.abspath(args.root)
    Handler._cache = {}

    # 启动即校验白名单资产可读，并预热压缩体（把首次请求的压缩成本前移）
    for rel in sorted(set(ALLOW.values())):
        p = os.path.join(Handler.root, rel)
        if not os.path.isfile(p):
            print("白名单资产缺失：%s" % p, file=sys.stderr)
            return 2
    t0 = time.time()
    for rel in sorted(set(ALLOW.values())):
        Handler._asset(rel)
    warm = time.time() - t0

    try:
        srv = Server((args.bind, args.port), Handler)
    except OSError as e:
        code = getattr(e, "winerror", None) or (e.args[0] if e.args else None)
        if code in (10048, 10013):       # WSAEADDRINUSE / WSAEACCES
            print("port %d busy; an instance is already up" % args.port,
                  file=sys.stderr)
            return 0
        raise

    pid = "" if args.no_pidfile else write_pid(args.port, args.pidfile)
    print("senseindex/2.0 listening on %s:%d" % (args.bind, args.port))
    print("  docroot : %s" % Handler.root)
    print("  本机    : http://127.0.0.1:%d/" % args.port)
    if args.bind == "0.0.0.0":
        print("  局域网  : http://%s:%d/" % (lan_ip(), args.port))
    print("  白名单  : %s" % ", ".join(sorted(ALLOW)))
    print("  预热    : %.0f ms（gzip 预压缩已缓存）" % (warm * 1000))
    if pid:
        print("  pid     : %d（%s）" % (os.getpid(), pid))
    print("Ctrl+C 停止")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
    finally:
        srv.server_close()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:              # noqa: BLE001 - 顶层兜底
        report_failure(e)
        sys.exit(1)
