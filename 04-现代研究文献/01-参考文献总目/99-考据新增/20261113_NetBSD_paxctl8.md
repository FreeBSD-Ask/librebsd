<!-- 网页存档｜来源：https://man.netbsd.org/paxctl.8｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# paxctl.8 — NetBSD 手册页（PaX flags 操作工具）

## 抓取正文（节选，空白已归一）

```
PAXCTL(8) NetBSD System Manager's Manual PAXCTL(8) NAME paxctl -- list and modify PaX flags associated with an ELF program SYNOPSIS paxctl [ -0 | flags ] program ... DESCRIPTION The paxctl utility is used to list and manipulate PaX flags associated with an ELF program. The PaX flags signify to the loader the privilege protections to be applied to mapped memory pages, and fuller explanations of the specific protections can be found in the security(7) manpage. To view existing flags on a program , execute paxctl without any flags. If -0 option is specified, all PaX flags (including reserved bits) are cleared. Otherwise, each flag can be prefixed either with a ` + ' or a ` - ' sign to add or remove the flag, respectively. The following flags are available: a Explicitly disable PaX ASLR (Address Space Layout Randomization). A Explicitly enable PaX ASLR. g Explicitly disable PaX Segvguard. G Explicitly enable PaX Segvguard. m Explicitly disable PaX MPROTECT ( mprotect(2) restrictions). M Explicitly enable PaX MPROTECT.
```

## 用途注记

Task 8.2 G5-P2 · V41《NetBSD 技术专题史》第 9 章利用缓解机制联网补证（D2 块；官方手册页，collection=NetBSD-current）。
