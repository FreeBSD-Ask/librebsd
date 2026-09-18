#!/usr/bin/env python3
"""重构2026 目录页局域网服务器（固定脚本，规则引用资源）。

用途：以 0.0.0.0 监听，向局域网提供 index.html 访问。
启动：python serve_refactor2026.py [端口]（默认 8090）
访问：http://<本机IP>:8090/  （手机/其他设备连同一 Wi-Fi）
停止：Ctrl+C 或结束进程。
"""
import http.server
import socket
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8090
ROOT = r"D:\librebsd\08-核查报告与多轮复核\重构2026"


def lan_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        # 禁缓存：每次访问拉取最新版（开发/审阅场景）
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Expires", "0")
        super().end_headers()


class ReusableTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with ReusableTCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"重构2026 目录页服务器已启动（0.0.0.0:{PORT}）")
        print(f"  本机访问:   http://localhost:{PORT}/")
        print(f"  局域网访问: http://{lan_ip()}:{PORT}/")
        print("Ctrl+C 停止")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")
