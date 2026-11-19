# Announcing NetBSD 9.0（exa 实取快照，Security/Quality Assurance 段全文）

fetched: 2026-11-19 via exa web_fetch（curl SSL exit 35，同 b012 预备件口径）
url: https://netbsd.org/releases/formal-9/NetBSD-9.0.html
published: 2020-02-14

---

### Security, Quality Assurance

- Support for Kernel ASLR, on x86 64-bit, via the new GENERIC_KASLR kernel configuration file. This implementation is one of the most advanced available to date. The default GENERIC configuration is also shipped with a partial Kernel ASLR enabled by default. Find out more on this page.
- Support for KLEAK, a new feature able to detect kernel memory disclosures, with initial support for amd64. It allowed to find and fix more than 25 bugs in the kernel. Find out more in this paper.
- Support for Kernel Address Sanitizer (KASAN), on amd64 and aarch64. This feature allows the kernel to detect illegal memory accesses, such as buffer overflows, stack overflows and use-after-frees. KASAN plays an important role in assuring kernel code quality.
- Support for Kernel Undefined Behavior Sanitizer (KUBSAN), this feature allows the kernel to detect several classes of undefined behavior. KUBSAN also plays an important role in assuring kernel code quality.
- Support for Kernel Coverage (KCOV), on amd64. This drivers allows fuzzers to collect kernel coverage to improve fuzzing inputs.
- Support for userland sanitizers, with new configurations allowing to run the entire userland stack with sanitizers.
- Kernel Heap Hardening, making it harder to exploit several classes of memory bugs.
- Audited network stack, bringing more confidence in the networking components of the kernel. Find out more on this blog entry.
- Many bug fixes and enhancements for the ptrace(2) debugger framework.
- Removal of numerous old and unmaintained components. This results in a code base that is much cleaner, smaller, and easier to work on. The removed items include NETISDN and related drivers (daic, iavc, ifpci, ifritz, iwic, isic), NETNATM and the related midway driver, several compatibility layers (NDIS, SVR3, SVR4), the n8 driver, vm86, ipkdb, among others.

> 存证注记：KCOV 行原文笔误 “This drivers allows…” 逐字照录（预备件 §6.2）；本段为 9.9 节四题与 9.3.4 的证据载体段，引文以此件为准。
