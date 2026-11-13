# wg(8) — FreeBSD 配置工具手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=wg&sektion=8
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.9.1“WireGuard 的接口设计”补证（D2 块）：配置工具的子命令面（D2 块，ref_id 见库）

## 抓取正文（节选）

```
WG(8)				    WireGuard				   WG(8)

NAME
     wg - set and retrieve configuration of WireGuard interfaces


SYNOPSIS
     wg [ COMMAND ] [ OPTIONS ]... [ ARGS ]...


DESCRIPTION
     wg  is  the configuration utility for getting and setting the configuration
     of WireGuard tunnel interfaces. The interfaces themselves can be added  and
     removed  using  ip-link(8) and their IP addresses and routing tables can be
     set using ip-address(8) and ip-route(8).  The wg utility provides a  series
     of sub-commands for changing WireGuard-specific aspects of WireGuard inter-
     faces.

     If  no  COMMAND  is specified, COMMAND defaults to show.  Sub-commands that
     take an INTERFACE must be passed a WireGuard interface.


COMMANDS
     show { <interface> | all | interfaces } [public-key | private-key | listen-
     port | fwmark | peers | preshared-keys | endpoints | allowed-ips | latest-
     handshakes | persistent-keepalive | transfer | dump]
	    Shows current WireGuard configuration  and	runtime  information  of
	    specified  <interface>.  If no <interface> is specified, <interface>
	    defaults to all.  If interfaces is specified, prints a list  of  all
```

## 引文摘录（空白已归一，供逐字核对）

WG(8) WireGuard WG(8) NAME wg - set and retrieve configuration of WireGuard interfaces SYNOPSIS wg [ COMMAND ] [ OPTIONS ]... [ ARGS ]... DESCRIPTION wg is the configuration utility for getting and setting the configuration of WireGuard tunnel interfaces. The interfaces themselves can be added and removed using ip-link(8) and their IP addresses and routing tables can be set using ip-address(8) and ip-route(8). The wg utility provides a series of sub-commands for changing WireGuard-specific aspects of WireGuard inter- faces. If no COMMAND is specified, COMMAND defaults to show. Sub-commands that take an INTERFACE must be passed a WireGuard interface. COMMANDS show { <interface> | all | interfaces } [public-key | private-key | listen- port | fwmark | peers | preshared-keys | endpoints | allowed-ips | latest- handshakes | persistent-keepalive | transfer | dump] Shows current WireGuard configuration and runtime information of specified <interface>. If no <interface> is specified, <interface> defaults to all. If interfaces is specified, prints a list of all
