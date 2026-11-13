<!-- 网页存档｜来源：https://man.netbsd.org/security.7｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# security.7 — NetBSD 手册页（NetBSD security features overview）

## 抓取正文（NAME 至 SEE ALSO 前，节选）

```
SECURITY(7) NetBSD Miscellaneous Information Manual SECURITY(7)
 NAME 
 security -- NetBSD security features
 DESCRIPTION 
 NetBSD supports a variety of security features. Below is a brief
 description of them with some quick usage examples that will help you get
 started.
 Contents:
 - Veriexec (file integrity)
 - Exploit mitigation
 - Per-user /tmp directory
 - Information filtering
 - Administrative security
 See also entropy(7) .
 Veriexec 
 Veriexec is a file integrity subsystem.
 For more information about it, and a quick guide on how to use it, please
 see veriexec(8) .
 In a nutshell, once enabled, Veriexec can be started as follows:
 # veriexecgen && veriexecctl load
 Exploit mitigation 
 NetBSD incorporates some exploit mitigation features. The purpose of
 exploit mitigation features is to interfere with the way exploits work,
 in order to prevent them from succeeding. Due to that, some features may
 have other impacts on the system, so be sure to fully understand the
 implications of each feature.
 NetBSD provides the following exploit mitigation features:
 - PaX ASLR (Address Space Layout Randomization).
 - PaX MPROTECT ( mprotect(2) restrictions)
 - PaX SegvGuard
 - gcc(1) stack-smashing protection (SSP)
 - bounds checked libc functions (FORTIFY_SOURCE)
 - Protections against NULL pointer dereferences
 PaX ASLR 
 PaX ASLR implements Address Space Layout Randomization (ASLR), meant to
 complement non-executable mappings. Its purpose is to harden prediction
 of the address space layout, namely location of library and application
 functions that can be used by an attacker to circumvent non-executable
 mappings by using a technique called ``return to library'' to bypass the
 need to write new code to (potentially executable) regions of memory.
 When PaX ASLR is used, it is more likely the attacker will fail to pre-
 dict the addresses of such functions, causing the application to seg-
 fault. To detect cases where an attacker might try and brute-force the
 return address of respawning services, PaX Segvguard can be used (see
 below).
 For non-PIE (Position Independent Executable) executables, the NetBSD PaX 
 ASLR implementation introduces randomization to the following memory
 regions:
 1. The stack
 For PIE executables:
 1. The program itself (exec base)
 2. All shared libraries
 3. The data segment
 4. The stack
 While it can be enabled globally, NetBSD provides a tool, paxctl(8) , to
 enable PaX ASLR on a per-program basis.
 Example usage:
 # paxctl +A /usr/sbin/sshd
 Enabling PaX ASLR globally:
 # sysctl -w security.pax.aslr.global=1
 PaX MPROTECT 
 PaX MPROTECT implements memory protection restrictions, meant to comple-
 ment non-executable mappings. The purpose is to prevent situations where
 malicious code attempts to mark writable memory regions as executable,
 often by trashing arguments to an mprotect(2) call.
 While it can be enabled globally, NetBSD provides a tool, paxctl(8) , to
 enable PaX MPROTECT on a per-program basis.
 Example usage:
 # paxctl +M /usr/sbin/sshd
 Enabling PaX MPROTECT globally:
 # sysctl -w security.pax.mprotect.global=1
 PaX MPROTECT affects the following three uses:
 � Processes that utilize code generation (such as the JVM) might
 need to have MPROTECT disabled.
 � Miscompiled programs that have text relocations, will now core
 dump instead of having their relocations corrected. You will
 need to fix those programs (recompile them properly).
 � Debugger breakpoints: gdb(1) needs to be able to write to the
 text segment in order to insert and delete breakpoints. This
 will not work unless MPROTECT is disabled on the executable.
 PaX Segvguard 
 PaX Segvguard monitors the number of segmentation faults in a program on
 a per-user basis, in an attempt to detect on-going exploitation attempts
 and possibly prevent them. For instance, PaX Segvguard can help detect
 when an attacker tries to brute-force a function return address, when
 attempting to perform a return-to-lib attack.
 PaX Segvguard consumes kernel memory, so use it wisely. While it pro-
 vides rate-limiting protections, records are tracked for all users on a
 per-program basis, meaning that irresponsible use may result in tracking
 all segmentation faults in the system, possibly consuming all kernel mem-
 ory.
 For this reason, it is highly recommended to have PaX Segvguard enabled
 explicitly only for network services or other processes deemed as criti-
 cal to system security. Enabling PaX Segvguard explicitly works like
 this:
 # paxctl +G /usr/sbin/sshd
 However, a global knob is still provided, for use in strict environments
 with no local users (for example, some network appliances, embedded
 devices, and firewalls)
 # sysctl -w security.pax.segvguard.global=1
 Explicitly disabling PaX Segvguard is also possible:
 # paxctl +g /bin/ls
 In addition, PaX Segvguard provides several tunable options. For exam-
 ple, to limit a program to 5 segmentation faults from the same user in a
 60 second timeframe:
 # sysctl -w security.pax.segvguard.max_crashes=5
 # sysctl -w security.pax.segvguard.expiry_timeout=60
 The number of seconds a user will be suspended from running the culprit
 program is also configurable. For example, 10 minutes seem like a sane
 setting:
 # sysctl -w security.pax.segvguard.suspend_timeout=600
 GCC Stack Smashing Protection ( SSP )
 As of NetBSD 4.0, gcc(1) includes SSP , a set of compiler extensions to
 raise the bar on exploitation attempts by detecting corruption of vari-
 ables and buffer overruns, which may be used to affect program control
 flow.
 Upon detection of a buffer overrun, SSP will immediately abort execution
 of the program and send a log message to syslog(3) .
 The system (userland and kernel) can be built with SSP by using the
 ``USE_SSP'' flag in /etc/mk.conf :
 USE_SSP=yes
 You are encouraged to use SSP for software you build, by providing one of
 the -fstack-protector or -fstack-protector-all flags to gcc(1) . Keep in
 mind, however, that SSP will not work for functions that make use of
 alloca(3) , as the latter modifies the stack size during run-time, while
 SSP relies on it being a compile-time static.
 Use of SSP is especially encouraged on platforms without per-page execute
 bit granularity such as i386. As of NetBSD 6.0, SSP is used by default
 on i386 and amd64 architectures.
 FORTIFY_SOURCE 
 The so-called FORTIFY_SOURCE is a relatively simple technique to detect a
 subset of buffer overflows before these can do damage. It is integrated
 to gcc(1) together with some common memory and string functions in the
 standard C library of NetBSD.
 The underlying idea builds on the observation that there are cases where
 the compiler knows the size of a buffer. If a buffer overflow is sus-
 pected in a function that does little or no bounds checking, either a
 compile time warning can be issued or a safer substitute function can be
 used at runtime. Refer to ssp(3) for additional details.
 The FORTIFY_SOURCE is enabled by default in some parts of the NetBSD
 source tree. It is also possible to explicitly enable it by defining the
 following in mk.conf(5) :
 USE_FORT=yes
 Protections against NULL pointer dereferences 
 A certain class of attacks rely on kernel bugs that dereference NULL
 pointers. If user processes are allowed to map the virtual address 0
 with mmap(2) or by other means, there is a risk that code or data can be
 injected into the kernel address space.
 In NetBSD it is possible to restrict whether user processes are allowed
 to make mappings at the zero address. By default, address 0 mappings are
 restricted on all architectures. It is however known that some third-
 party programs may not function properly with the restriction. Such map-
 pings can be allowed either by using the USER_VA0_DISABLE_DEFAULT kernel
 configuration option or by changing the following variable at runtime:
 # sysctl -w vm.user_va0_disable=0
 Note that if securelevel (see secmodel_securelevel(9) ) is greater than
 zero, it is not possible to change the sysctl(8) variable.
 Per-user temporary storage 
 It is possible to configure per-user temporary storage to avoid potential
 security issues (race conditions, etc.) in programs that do not make
 secure usage of /tmp .
 To enable per-user temporary storage, add the following line to
 rc.conf(5) :
 per_user_tmp=YES
 If /tmp is a mount point, you will also need to update its fstab(5) entry
 to use ``/private/tmp'' (or whatever directory you want, if you override
 the default using the ``per_user_tmp_dir'' rc.conf(5) keyword) instead of
 ``/tmp''.
 Following that, run:
 # /etc/rc.d/perusertmp start
 The per-user temporary storage is implemented by using ``magic
 symlinks''. These are further described in symlink(7) .
 Note that some programs will not work correctly with the present ``magic
 symlinks'' implementation, if they invoke realpath(3) on temporary file
 paths, for example tmux(1) . In this case, resolution will fail, so this
 feature is not suited for all uses.
 Information filtering 
 NetBSD provides administrators the ability to restrict information passed
 from the kernel to userland so that users can only view information they
 ``own''.
 The hooks that manage this restriction are located in various parts of
 the system and affect programs such as ps(1) , fstat(1) , and netstat(1) .
 Information filtering is enabled as follows:
 # sysctl -w security.curtain=1
 Administrative security 
 Also certain administrative tasks are related to security. For instance,
 the daily maintenance script includes some basic consistency checks; see
 security.conf(5) for more details. In particular, it is possible to con-
 figure NetBSD to automatically audit all third-party packages installed
 via pkgsrc(7) . To audit for any known vulnerabilities on daily basis,
 set the following in /etc/daily.conf :
 fetch_pkg_vulnerabilities=YES
```

## 用途注记

Task 8.2 G5-P2 · V41《NetBSD 技术专题史》第 9 章安全机制联网补证（D2 块；官方手册页，collection=NetBSD-current）。
