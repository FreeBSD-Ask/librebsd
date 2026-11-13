<!-- 网页存档｜来源：https://docs.freebsd.org/en/articles/vm-design/｜抓取：2026-11-13｜curl 直取两次 sha256 一致，HTML 标签剥离 -->

# Design elements of the FreeBSD VM system（FreeBSD 文档站；原载 DaemonNews 2000 年 1 月）

作者：Matthew Dillon（dillon at apollo.backplane.com）；文档站注明本文原载 2000 年 1 月 DaemonNews，现版本或含 Matt 及其他作者对 FreeBSD VM 实现变化的更新；文档站注记该文已过时，仅为历史目的保留。

## 抓取正文（节选）

```
The title is really just a fancy way of saying that I am going to attempt to describe the whole VM enchilada, hopefully in a way that everyone can follow.
For the last year I have concentrated on a number of major kernel subsystems within FreeBSD, with the VM and Swap subsystems being the most interesting and NFS being "a necessary chore".
I rewrote only small portions of the code. In the VM arena the only major rewrite I have done is to the swap subsystem.
Most of my work was cleanup and maintenance, with only moderate code rewriting and no major algorithmic adjustments within the VM subsystem.
The bulk of the VM subsystem’s theoretical base remains unchanged and a lot of the credit for the modernization effort in the last few years belongs to John Dyson and David Greenman.
Not being a historian like Kirk I will not attempt to tag all the various features with peoples names, since I will invariably get it wrong.
```

## 出处与署名（原文前置区节录）

```
This article was originally published in the January 2000 issue of DaemonNews. This version of the article may include updates from Matt and other authors to reflect changes in FreeBSD's VM implementation.
```

## 用途注记

Task 8.2 G5 · V50.1.1.2“FreeBSD 虚拟内存与 NFS 子系统的贡献”P2 联网补证（D2 块；官方文档站留存的当事人技术文献，作者本人自述其 FreeBSD VM／Swap／NFS 工作面）。
