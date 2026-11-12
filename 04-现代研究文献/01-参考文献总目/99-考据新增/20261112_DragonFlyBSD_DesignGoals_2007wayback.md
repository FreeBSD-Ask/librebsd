<!-- 网页存档（节录）｜来源：https://web.archive.org/web/20070318041530/http://www.dragonflybsd.org/docs/goals.shtml｜抓取：2026-11-12（经 exa 服务端取回）｜仅存本次引用所需段落，其余段落未收录 -->

# DragonFly Design Goals（2007-03-18 存档）

DragonFly is going to be a multi-year project. It will take a lot of groundwork to even approach the goals we outline here. By checking our various goal links, you can bring up position papers on various nitty-gritty aspects of kernel and system design which the project hopes to accomplish.

First and foremost among all of our goals is a desire to be able to implement them in small bite-sized chunks, while at the same time maintaining good stability for the system as a whole. While the goals are not listed in any particular order, there is a natural order to things which should allow us to advance piecemeal without compromising the stability of the system as a whole. It's a laudable goal that will sit foremost in our minds, even though we know it is probably not 100% achievable. The messaging system is going to be key to the effort. If we can get that in-place we will have an excellent (and debuggable) API on top of which the remainder of the work can be built.

Our goal is to create a flexible dual-purpose caching infrastructure which mimics the well known and mature MESI (Modified Exclusive Shared Invalid) model over a broad range of configurations. The primary purpose of this infrastructure will be to protect I/O operations and live memory mappings. For example, a range-based MESI model would allow multiple processes to simultaneously operate both reads and writes on different portions of a single file. If we implement the infrastructure properly we can extend it into a networked-clustered environment, getting us a long ways towards achieving a single-system-image capability.

## The Port/Messaging Model

DragonFly will have a lightweight port/messaging API to go along with its lightweight kernel threads. The port/messaging API is very simple in concept; You construct a message, you send it to a target port, and at some point later you wait for a reply on your reply port. On this simple abstraction, we intend to build a high level of capability and sophistication. To understand the capabilities of the messaging system, you must first understand how a message is dispatched.

## The Light Weight Kernel Threading Model

DragonFly employs a light weight kernel threading (LWKT) model at its core. Each process in the system has an associated thread, and most kernel-only processes are in fact just pure threads. For example, the pageout daemon is a pure thread and has no process context.

The LWKT model has a number of key features that can be counted on no matter the architecture. These features are designed to remove or reduce contention between cpus.
