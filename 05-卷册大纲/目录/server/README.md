# 重构2026 目录页 · 服务器说明

> **2026-09-28 归一重写。** 本目录此前另有一份服务器实现 `serve_index.py`（`0.0.0.0:80`，单线程），
> 与固定脚本 `00-编纂规则与格式规范/01-规则/脚本与命令/serve_refactor2026.py`（`0.0.0.0:8090`，多线程）
> **语义分叉**：端口不同、并发模型不同、`allow_reuse_address` 取值相反、一份有幂等守卫一份没有。
> 二者**均缺传输压缩、均缺安全响应头、均开启目录列表**，而本 README 旧版却声称“不给目录列表”。
> 现已**归一为唯一实现**——固定脚本 `serve_refactor2026.py`；旧 `serve_index.py` 归档于
> `script/_archive/20260928/serve_index.py.superseded-20260928`
> （5,886 B，sha256 `0424dd0b3d35071520c70794b20249fbd72e33116948eaf7c32693af80cbab9c`；保留留痕，不再维护）。
> 本目录自此只保留本说明文件。

## 启动

```bat
C:\Python314\python.exe D:\librebsd\00-编纂规则与格式规范\01-规则\脚本与命令\serve_refactor2026.py
```

默认 `0.0.0.0:8090`（局域网可达）。常用变体：

```bat
:: 换端口
python serve_refactor2026.py --port 8080
:: 仅本机（不暴露局域网）
python serve_refactor2026.py --bind 127.0.0.1
:: 换 docroot
python serve_refactor2026.py --root D:\某个其他目录
:: 不写 pid 文件
python serve_refactor2026.py --no-pidfile
```

用 `pythonw.exe` 启动则**不弹任何窗口**（GUI 子系统）；用 `python.exe` 会占一个控制台，关窗即停。

## 停止

```bat
:: 精确停止（推荐）：pid 写在
::   %LOCALAPPDATA%\senseindex\serve_refactor2026_8090.pid
taskkill /F /PID <pid>
```

> **不要**用 `taskkill /F /IM pythonw.exe`——它会杀掉本机**所有** `pythonw` 进程。

## 访问

- 本机：`http://127.0.0.1:8090/`
- 局域网：`http://<本机IP>:8090/`（启动时脚本会打印实际 IP）

局域网需先放行入站（管理员命令行，一次即可）：

```bat
netsh advfirewall firewall add rule name=senseindex-8090 dir=in action=allow protocol=TCP localport=8090
```

删除该规则：

```bat
netsh advfirewall firewall delete rule name=senseindex-8090
```

> 本说明**不写死具体 IP 与网卡名**（旧版写死 `192.168.5.4`／“以太网 2”，换网即失效）。
> 查本机 IP：`ipconfig`，或直接看启动时脚本打印的那一行。

## 行为契约

由**第十一件门禁** `00-编纂规则与格式规范/01-规则/脚本与命令/audit_server_contract.py`
逐项核验（八项断言，全部走真实 HTTP）：

| 项 | 行为 |
| --- | --- |
| **docroot 白名单** | 只服务 `/`、`/index.html`、`/favicon.ico`；其余一律 404。`data/`、`tests/`、`script/`、`_prep_*`、备份件、`catalog.json` **均不可获取** |
| **目录列表** | **结构上不存在**——父类为 `BaseHTTPRequestHandler`，没有 `list_directory` 可被继承 |
| **传输压缩** | 按需读盘并预压 gzip 缓存；`Accept-Encoding: gzip` 时发送。1,583,076 B → 890,469 B（−43.8%） |
| **缓存** | `Cache-Control: no-cache`（允许存储 ＋ 强制再验证）。磁盘未变 → **304、正文 0 字节** |
| **新鲜度** | 资产 **mtime 变即重读重压** → `assemble_index.py` 重装配后**无需重启服务**即拿到新版 |
| **安全响应头** | `X-Content-Type-Options: nosniff`／`Referrer-Policy: no-referrer`／`X-Frame-Options: DENY`／`Permissions-Policy`／`COOP: same-origin`／`CORP: same-origin` |
| **方法** | 仅 GET/HEAD；POST/PUT/DELETE/PATCH/OPTIONS → 501 |
| **幂等** | 端口被占用即静默退出（退出码 0），重复拉起不产生重复实例 |

### 两处刻意的取舍

1. **HSTS 不发送**：`Strict-Transport-Security` 仅在 HTTPS 下有意义，本服务为 HTTP。
   62 号文 §8 曾把它列为应设头，前提是当时的 HTTPS 服务器 `serve_https.py`——该脚本已不存在。
2. **`allow_reuse_address = False`**：Windows 上 `SO_REUSEADDR` 的语义是“允许多个进程共享同一
   地址:端口”（不是 Linux 那种“越过 TIME_WAIT”），开着它幂等守卫就形同虚设，会开出多个实例
   同时监听。监听 socket 在 `close()` 后不进入 TIME_WAIT，故此处不需要复用地址。

### 相对旧版的取舍变化

| 项 | 旧 `serve_index.py` | 现版 |
| --- | --- | --- |
| 并发 | 单线程 `HTTPServer`（省内存） | `ThreadingHTTPServer`（HTTP/1.1 keep-alive 下单线程会被慢客户端阻塞） |
| 协议 | `HTTP/1.0`（每请求关连接） | `HTTP/1.1`（keep-alive；`Content-Length` 必发） |
| docroot | 整棵树 | 白名单三路径 |
| 端口 | 80 | 8090（80 需管理员权限，且与 IIS／其他服务冲突面大） |

## 排错

| 现象 | 处置 |
| --- | --- |
| 启动没反应 | 端口被占用时脚本**静默退出（退出码 0）**——先确认是否已有实例在跑：`netstat -ano \| findstr :8090` |
| 启动报“白名单资产缺失” | docroot 下缺 `index.html` 或 `assets/favicon.ico`；用 `--root` 指定正确目录 |
| 无控制台看不到错误 | 用 `python.exe`（而非 `pythonw.exe`）启动，或看 `%LOCALAPPDATA%\senseindex\serve_refactor2026.err.log` |
| 想验证行为契约 | `python 00-编纂规则与格式规范/01-规则/脚本与命令/audit_server_contract.py`（自动起临时实例、绑 127.0.0.1、跑完即杀） |
