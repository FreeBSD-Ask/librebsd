---
title: "2022_LWN_Rust_in_61_kernel.md"
source_url: https://lwn.net/Articles/913857/
download_date: 2026-09-08
note: manual_direct
---

# 2022_LWN_Rust_in_61_kernel.md

来源: https://lwn.net/Articles/913857/

         

          rcu: Add RCU stall diagnosis information [LWN.net] 

             LWN .net 
             News from the source  

           Content     Weekly Edition    Archives    Search    Kernel    Security    Events calendar    Unread comments       LWN FAQ    Write for us    
   Edition     Return to the Announcements page    

          User:     
		  Password:          |

             |

                 Log in   /
                 Subscribe   /
                 Register  

 rcu: Add RCU stall diagnosis information 

   From : 
                 Zhen Lei &lt;thunder.leizhen-AT-huawei.com&gt;  
   To : 
                 "Paul E . McKenney" &lt;paulmck-AT-kernel.org&gt;,        Frederic Weisbecker &lt;frederic-AT-kernel.org&gt;,        Neeraj Upadhyay &lt;quic_neeraju-AT-quicinc.com&gt;,        "Josh Triplett" &lt;josh-AT-joshtriplett.org&gt;,        Steven Rostedt &lt;rostedt-AT-goodmis.org&gt;,        Mathieu Desnoyers &lt;mathieu.desnoyers-AT-efficios.com&gt;,        Lai Jiangshan &lt;jiangshanlai-AT-gmail.com&gt;,        Joel Fernandes &lt;joel-AT-joelfernandes.org&gt;, &lt;rcu-AT-vger.kernel.org&gt;,        &lt;linux-kernel-AT-vger.kernel.org&gt;  
   Subject : 
                 [PATCH v4 0/4] rcu: Add RCU stall diagnosis information  
   Date : 
                 Fri, 04 Nov 2022 10:12:19 +0800  
   Message-ID : 
                 &lt;20221104021224.102-1-thunder.leizhen@huawei.com&gt;  
   Cc : 
                 Zhen Lei &lt;thunder.leizhen-AT-huawei.com&gt;,        Robert Elliott &lt;elliott-AT-hpe.com&gt;  
   Archive-link : 
                  Article   

v3 --&gt; v4:
1. Rename rcu_cpu_stall_deep_debug to rcu_cpu_stall_cputime.

v2 --&gt; v3:
1. Fix the return type of kstat_cpu_irqs_sum()
2. Add Kconfig option CONFIG_RCU_CPU_STALL_DEEP_DEBUG and boot parameter
   rcupdate.rcu_cpu_stall_deep_debug.
3. Add comments and normalize local variable name

v1 --&gt; v2:
1. Fixed a bug in the code. If the rcu stall is detected by another CPU,
   kcpustat_this_cpu cannot be used.
@@ -451,7 +451,7 @@ static void print_cpu_stat_info(int cpu)
        if (r-&gt;gp_seq != rdp-&gt;gp_seq)
                return;

-       cpustat = kcpustat_this_cpu-&gt;cpustat;
+       cpustat = kcpustat_cpu(cpu).cpustat;
2. Move the start point of statistics from rcu_stall_kick_kthreads() to
   rcu_implicit_dynticks_qs(), removing the dependency on irq_work.

v1:
In some extreme cases, such as the I/O pressure test, the CPU usage may
be 100%, causing RCU stall. In this case, the printed information about
current is not useful. Displays the number and usage of hard interrupts,
soft interrupts, and context switches that are generated within half of
the CPU stall timeout, can help us make a general judgment. In other
cases, we can preliminarily determine whether an infinite loop occurs
when local_irq, local_bh or preempt is disabled.

Zhen Lei (4):
  genirq: Fix the return type of kstat_cpu_irqs_sum()
  sched: Add helper kstat_cpu_softirqs_sum()
  sched: Add helper nr_context_switches_cpu()
  rcu: Add RCU stall diagnosis information

 .../admin-guide/kernel-parameters.txt         |  5 +++
 include/linux/kernel_stat.h                   | 14 ++++++++-
 kernel/rcu/Kconfig.debug                      | 10 ++++++
 kernel/rcu/rcu.h                              |  1 +
 kernel/rcu/tree.c                             | 16 ++++++++++
 kernel/rcu/tree.h                             | 17 ++++++++++
 kernel/rcu/tree_stall.h                       | 31 +++++++++++++++++++
 kernel/rcu/update.c                           |  2 ++
 kernel/sched/core.c                           |  5 +++
 9 files changed, 100 insertions(+), 1 deletion(-)

-- 
2.25.1

            Copyright &copy; 2022, Eklektix, Inc. 

            Comments and public postings are copyrighted by their creators. 
            Linux  is a registered trademark of Linus Torvalds 


