<!-- 网页存档｜来源：https://man.netbsd.org/veriexec.4｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# veriexec.4 — NetBSD 手册页（Veriexec fingerprint pseudo-device）

## 抓取正文（NAME 至 SEE ALSO 前，节选）

```
VERIEXEC(4) NetBSD Kernel Interfaces Manual VERIEXEC(4)
 NAME 
 veriexec -- Veriexec pseudo-device
 SYNOPSIS 
 pseudo-device veriexec 
 DESCRIPTION 
 Veriexec verifies the integrity of specified executables and files before
 they are run or read. This makes it much more difficult to insert a tro-
 jan horse into the system and also makes it more difficult to run bina-
 ries that are not supposed to be running, for example, packet sniffers,
 DDoS clients and so on.
 The veriexec pseudo-device is used to load and delete entries to and from
 the in-kernel Veriexec databases, as well as query information about
 them. It can also be used to dump the entire database.
 Kernel-userland interaction 
 Veriexec uses proplib(3) for communication between the kernel and user-
 land.
 VERIEXEC_LOAD
 Load an entry for a file to be monitored by Veriexec .
 The dictionary passed contains the following elements:
 Name Type Purpose 
 file string filename for this entry
 entry-type uint8 entry type (see below)
 fp-type string fingerprint hashing algorithm
 fp data the fingerprint
 keep-filename bool whether or not to retain the entry's
 filename
 ``entry-type'' can be one or more (binary-OR'd) of the following:
 Type Effect 
 VERIEXEC_DIRECT can execute directly
 VERIEXEC_INDIRECT can execute indirectly (interpreter, mmap(2) )
 VERIEXEC_FILE can be opened
 VERIEXEC_UNTRUSTED located on untrusted storage
 VERIEXEC_DELETE
 Removes either an entry for a single file or entries for an entire
 mount from Veriexec .
 The dictionary passed contains the following elements:
 Name Type Purpose 
 file string filename or mount-point
 VERIEXEC_DUMP
 Dump the Veriexec monitored files database from the kernel.
 Only files for which the filename was kept will be dumped. The
 returned array contains dictionaries with the following elements:
 Name Type Purpose 
 file string filename
 fp-type string fingerprint hashing algorithm
 fp data the fingerprint
 entry-type uint8 entry type (see above)
 VERIEXEC_FLUSH
 Flush the Veriexec database, removing all entries.
 This command has no parameters.
 VERIEXEC_QUERY
 Queries Veriexec about a file, returning information that may be
 useful about it.
 The dictionary passed contains the following elements:
 Name Type Purpose 
 file string filename
 The dictionary returned contains the following elements:
 Name Type Purpose 
 entry-type uint8 entry type (see above)
 status uint8 entry status
 fp-type string fingerprint hashing algorithm
 fp data the fingerprint
 ``status'' can be one of the following:
 Status Meaning 
 FINGERPRINT_NOTEVAL not evaluated
 FINGERPRINT_VALID fingerprint match
 FINGERPRINT_MISMATCH fingerprint mismatch
 Note that the requests VERIEXEC_LOAD, VERIEXEC_DELETE, and VERIEXEC_FLUSH
 are not permitted once the strict level has been raised past 0.
```

## 用途注记

Task 8.2 G5-P2 · V41《NetBSD 技术专题史》第 9 章安全机制联网补证（D2 块；官方手册页，collection=NetBSD-current）。
