# Software Installation and Upgrade Overview（Junos OS Evolved 官方文档）引用卡

> 用途：V71.1.3.5“控制平面基底的更替代价”内容补证（G8-S2 V71 b001）。

## 一、著录

Juniper Networks. Software Installation and Upgrade Overview (Junos OS Evolved)[EB/OL]. Juniper Networks, （日期不详）[2026-11-12]. https://www.juniper.net/documentation/us/en/software/junos/junos-install-upgrade-evo/topics/concept/software-install-and-upgrade-overview-evo.html.

- 责任者：Juniper Networks（厂商官方技术文档）
- 载体：HTML 页面；`source_tier=primary`（厂商官方文档，机构自述）
- 访问日：2026-11-12
- 说明：升级指南的概览页，列备份、安装、重启、复核、回滚；引文照录英文原文。

## 二、逐字引文（英文，未翻译）

升级前的备份义务：

> Before installing software, you must back up the system, including the configuration. You upgrade (or downgrade) the version of the operating system on a device by copying a software installation package to your device and then use the CLI to install the new software on the device.

安装包与配置兼容性校验：

> When you upgrade or downgrade software, we recommend that you validate the configuration with the request system software add operational mode command, to check that the candidate software is compatible with the current configuration.

多版本共存与回滚：

> Junos OS Evolved stores multiple versions of software on the storage media. Junos OS Evolved also allows you to roll back to any of the releases already stored on the system with the request system software rollback operational mode command.

整机重装式的升级语义：

> During a successful upgrade, the upgrade package completely re-installs the existing operating system. It retains the juniper.conf, rescue.conf, SNMP ifIndexes, /var/home, /config/scripts, SSH files, and other filesystem files. The upgrade process removes all other information.

## 三、考据说明

- 1.3.5 题面称“代价未在官方材料中量化，只能从迁移与验证环节间接观察”。本卡三处（备份义务、配置兼容性校验、整机重装＋回滚）正是“迁移与验证环节”的官方清单；官方未在其中给出工时或费用数字，属可观察的结构性事实。
- “completely re-installs the existing operating system”为官方原文，用于说明更换底座后升级语义的变化，不作价值判断。
- 厂商自述按 L3 采信。
