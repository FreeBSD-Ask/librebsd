# Managing Third-Party Applications（Juniper Networks 官方文档）引用卡

> 用途：V71.1.3.4“网络栈差异与运维接口”内容补证（G8-S2 V71 b001）。

## 一、著录

Juniper Networks. Managing Third-Party Applications[EB/OL]. Juniper Networks, （日期不详）[2026-11-12]. https://www.juniper.net/documentation/us/en/software/junos/overview-evo/topics/topic-map/evo-managing-third-party-apps.html.

- 责任者：Juniper Networks（厂商官方技术文档）
- 载体：HTML 页面；`source_tier=primary`（厂商官方文档，机构自述）
- 访问日：2026-11-12
- 说明：页面讲第三方应用在原生 Linux 上的运行方式与信息截取机制；引文照录英文原文。

## 二、逐字引文（英文，未翻译）

第三方应用取得网络信息的路径差异：

> Junos OS Evolved can run third-party applications because it runs on native Linux. There are some differences between the way Linux displays requested network topology information such as interface and route data and the way Junos OS displays this information. The CLI is designed to overcome these differences. But typically, third-party applications running on native Linux obtain this information directly from the native Linux sources using shell commands.

截取机制（libsi.so／libnli.so）：

> Junos OS Evolved uses an intercept mechanism that redirects shell requests for network topology information to a space where the information can be obtained from Junos OS. This intercept mechanism is accomplished through intercept libraries, libsi.so and libnli.so, that you preload.

接口命名不兼容的量化边界：

> One limiting factor to using this intercept mechanism is that Linux interface naming is incompatible with the Junos OS interface naming. Linux supports 15-byte interface names (15 + null-character); network interface names that exceed this limit are truncated in outputs.

## 三、考据说明

- “第三方应用直接从 Linux 源取信息、CLI 为克服呈现差异而设计”两句是 1.3.4 题面（Linux 网络栈呈现方式与 Junos CLI 不同、运维接口需额外封装）的直接来源。
- 截取库与 15 字节接口名边界给出“封装”的技术实体：libsi.so／libnli.so 预载 + jbash。
- 与《Top Differences》页的 CLI/shell 对照互为两文献（不同页面、不同章节，同一官方域但文本独立成段）。
- 厂商自述按 L3 采信。
