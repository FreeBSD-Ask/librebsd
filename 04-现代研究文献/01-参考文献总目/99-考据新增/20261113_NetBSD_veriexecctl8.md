<!-- 网页存档｜来源：https://man.netbsd.org/veriexecctl.8｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# veriexecctl.8 — NetBSD 手册页（Veriexec control utility）

## 抓取正文（NAME 至 SEE ALSO 前，节选）

```
VERIEXECCTL(8) NetBSD System Manager's Manual VERIEXECCTL(8)
 NAME 
 veriexecctl -- manage the Veriexec subsystem
 SYNOPSIS 
 veriexecctl [ -ekv ] load [ file ]
 veriexecctl delete file | mount_point 
 veriexecctl dump 
 veriexecctl flush 
 veriexecctl query file 
 DESCRIPTION 
 The veriexecctl command is used to manipulate Veriexec , the NetBSD file
 integrity subsystem.
 Commands 
 load [ file ]
 Load the fingerprint entries contained in file , if specified, or
 the default signatures file otherwise.
 This operation is only allowed in learning mode (strict level
 zero).
 The following flags are allowed with this command:
 -e Evaluate fingerprint on load, as opposed to when the file
 is accessed.
 -k Keep the filenames in the entry for more accurate logging.
 -v Enable verbose output.
 delete file | mount_point 
 Delete either a single entry file or all entries on mount_point 
 from being monitored by Veriexec .
 dump Dump the Veriexec database from the kernel. Only entries that have
 the filename will be presented.
 This can be used to recover a lost database:
 # veriexecctl dump > /etc/signatures
 flush 
 Delete all entries in the Veriexec database.
 query file 
 Query Veriexec for information associated with file : Filename,
 mount, fingerprint, fingerprint algorithm, evaluation status, and
 entry type.
 FILES 
 /dev/veriexec Veriexec pseudo-device
 /etc/signatures default signatures file
```

## 用途注记

Task 8.2 G5-P2 · V41《NetBSD 技术专题史》第 9 章安全机制联网补证（D2 块；官方手册页，collection=NetBSD-current）。
