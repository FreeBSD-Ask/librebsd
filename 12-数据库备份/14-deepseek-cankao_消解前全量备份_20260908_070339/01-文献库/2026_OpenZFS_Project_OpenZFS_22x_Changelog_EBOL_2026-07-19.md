---
title: "Project_OpenZFS_22x_Changelog_EBOL_2026-07-19"
source_url: https://github.com/openzfs/zfs/releases
download_date: 2026-09-07
---

# Project_OpenZFS_22x_Changelog_EBOL_2026-07-19

来源: https://github.com/openzfs/zfs/releases



   Releases · openzfs/zfs · GitHub 

       Skip to content 

      Navigation Menu                         Sign in                Appearance settings          Platform          AI CODE CREATION            GitHub Copilot  Write better code with AI            GitHub Copilot app  Direct agents from issue to merge              MCP Registry  Integrate external tools          DEVELOPER WORKFLOWS          Actions  Automate any workflow              Codespaces  Instant dev environments              Issues  Plan and track work            Code Review  Manage code changes              Code Quality  Enforce quality at merge          APPLICATION SECURITY          GitHub Advanced Security  Find and fix vulnerabilities            Code security  Secure your code as you build            Secret protection  Stop leaks before they start          EXPLORE     Why GitHub      Documentation          Blog          Changelog          Marketplace          View all features               Solutions          BY COMPANY SIZE     Enterprises      Small and medium teams      Startups      Nonprofits         BY USE CASE     App Modernization      DevSecOps      DevOps      CI/CD      View all use cases               BY INDUSTRY     Healthcare      Financial services      Manufacturing      Government      View all industries                View all solutions               Resources          EXPLORE BY TOPIC     AI      Software Development      DevOps      Security      View all topics               EXPLORE BY TYPE     Customer stories      Events &amp; webinars      Ebooks &amp; reports      Business insights      GitHub Skills             SUPPORT &amp; SERVICES     Documentation          Customer support          Community forum      Trust center      Partners          View all resources               Open Source          COMMUNITY          GitHub Sponsors  Fund open source developers          PROGRAMS     Security Lab          Maintainer Community          GitHub Stars          Archive Program             REPOSITORIES     Topics      Trending      Collections             Enterprise          ENTERPRISE SOLUTIONS          Enterprise platform  AI-powered developer platform          AVAILABLE ADD-ONS          GitHub Advanced Security  Enterprise-grade security features              Copilot for Business  Enterprise-grade AI features            Premium Support  Enterprise-grade 24/7 support             Pricing               Search  /            Sign in       Sign up                Appearance settings          

         You signed in with another tab or window.  Reload  to refresh your session. 
         You signed out in another tab or window.  Reload  to refresh your session. 
         You switched accounts on another tab or window.  Reload  to refresh your session. 

  Dismiss alert 

       {{ message }} 

               Uh oh!

                There was an error while loading.  Please reload this page . 

        openzfs

     / 

       zfs 

       Public 

 Notifications
      You must be signed in to change notification settings 

 Fork
     2k 

          Star
            12.4k 

         Code 

         Issues 
           1.5k 

         Pull requests 
           210 

         Discussions 

         Actions 

         Projects 

         Wiki 

         Security and quality 
           1 

         Insights 

  Additional navigation options 

          Code

          Issues

          Pull requests

          Discussions

          Actions

          Projects

          Wiki

          Security and quality

          Insights

 Releases: openzfs/zfs 

   Releases 
   Tags 

            -->   

   Releases · openzfs/zfs 

   Release list 

          zfs-2.4.4

          zfs-2.3.9

          zfs-2.2.11

          zfs-2.4.3

          zfs-2.3.8

          zfs-2.2.10

          zfs-2.4.2

          zfs-2.3.7

          zfs-2.4.1

          zfs-2.3.6

          Previous   Next  

     Jump to release 

          zfs-2.4.4

          zfs-2.3.9

          zfs-2.2.11

          zfs-2.4.3

          zfs-2.3.8

          zfs-2.2.10

          zfs-2.4.2

          zfs-2.3.7

          zfs-2.4.1

          zfs-2.3.6

        Previous   Next  

         zfs-2.4.4 

          zfs-2.4.4  

          Latest  

        Latest  

     Compare 

        Choose a tag to compare

                   Sorry, something went wrong. 

        Filter

      Loading 

                           Sorry, something went wrong. 

               Uh oh!

                There was an error while loading.  Please reload this page . 

               No results found 

                       View all tags 

       tonyhutter 

    released this

        21 Aug 23:34

                zfs-2.4.4

                This tag was signed with the committer’s  verified signature .

             tonyhutter 
            Tony Hutter

             GPG key ID:  6AD860EED4598027  

             Verified

           Learn about vigilant mode .

               71a9f95            

          Supported Platforms 

  Linux : compatible with 4.18 - 7.2 kernels 
  FreeBSD : compatible with releases starting from 13.3+, 14.0+ 

 Changes 

 [zfs-2.4.4] Add 'capsh' to commands.cfg 
 ZTS: device access tests  #18960  
 vdev_disk: use calling cred to check for device access  #18960  
 vdev_file: use calling cred to check for device access  #18960  
 zfs_file_open: add cred arg, use it to check access  #18960  
 vdev_open: pass credential to check for permission to open device  #18960  
 secpolicy_zfs: add a note about the power of CAP_SYS_ADMIN  #18959  
 secpolicy_sys_config: only permit a global zone credential  #18959  
 secpolicy_zinject: only permit a global zone credential  #18959  
 secpolicy_nfs: remove, not used  #18959  
 ZTS: test secpolicy_zinject correctly limits namespace access  #18959  
 ZTS: test secpolicy_sys_config correctly limits namespace access  #18959  
 config: detect idmap method via generic_permission test  #18769  
 mmp: tell a failed uberblock claim apart from remote activity  #18892  
 ZTS: add coverage for zhack mmp reclaim  #18892  
 zhack: add "mmp reclaim" to recover a pool stranded by MMP  #18892  
 Make systemd-udev-settle optional for the import units  #18832  
 Linux 7.2 compat: META  #18941  
 Fix negative time overflows in DDT pruning  #18886  
 nvpair: i_get_value_size() string array handling tweak  #18877  
 nvpair: Improve native handling of unterminated strings  #18876  
 CodeQL: Flag implicit compare-then-assign in branch conditions  #18899  
 Linux 5.19/6.17: handle differences in how to flush delay workqueue  #18847  
 Linux 6.3: follow_down() gains flags arg  #18847  
 Linux 6.18 compat: vfs_parse_fs_string() takes 3 args  #18847  
 nvpair: Fix operator precedence  #18874  
 ZTS: don't read a command's exit status as a missing binary  #18726   #18882  
 build: Fix release detection when build dir is not source dir  #18891  
 CI: don't fail a passing job when a log reader has already exited  #18885  
 CI: publish the per-VM test counter atomically  #18885  
 man: zvol_request_sync is not ignored under blk-mq  #18887  
 libzfs: don't read a dataset handle after closing it in resume send  #18870   #18883  
 ZTS: add coverage for the MMP claim on a degraded mirror  #18855  
 mmp: do not require writes to mirror legs the config marks absent  #18855  
 libzfs: String trimming should not operate out of bounds  #18868  
 libzfs: don't truncate a resolved vdev path in zpool_vdev_name()  #18851   #18871  
 libzfs: Do not call munmap() when mmap() fails  #18869  
 Add missing checks to zfs_clone_range_replay()  #18867  
 Fix DMU bonus hold leak on I/O error  #18865  
 zfs: fix stale POSIX ACL cache after rollback  #18837  
 zed: let autoexpand see capacity changes on partitioned disks  #12505   #18833  
 zpool export: return EBUSY when zvol minors are in use  #18841  
 ZTS: make file_check actually compare the resume test results  #18834  
 ZTS: save ZAP_MICRO_MAX_SIZE before the large microzap tests change it  #18834  
 dmu_recv: Avoid potential null deref  #18848  
 DDT: Fix several bugs in pruning  #18838  
 cstyle: better tolerance for struct literals 
 libspl: Implement VERIFY_IMPLY and VERIFY_EQUIV  #18822  
 mmp: skip non-writeable vdevs during activity check  #18823   #18835  
 zdb: output refcounts from verify_spacemap_refcounts()  #18809  
 L2ARC: bound the rebuild by the write hand on a first sweep  #3114   #3400   #5583   #10224   #12779   #18827  
 ZTS: make zpool_iostat_interval_all teardown deterministic  #18273   #18776  
 libzfs: fallback VDEV_UPATH to VDEV_PATH for non-DM devices  #18439   #18802  
 Fix reads for blocks freed after being cloned  #18421   #18724  
 Rate limit Direct I/O verify zevents  #18795  
 CI: Update Alpine Linux runner to 3.24.1  #18790  
 Remove libuutil from the pull request template and fix headings  #18791  
 ZTS: fix zpool_initialize_multiple_pools suspend race  #18777  
 CI: Fix race caused by shared ctr file updates  #18778  
 zpl_inode: remove zpl_rename no-flags variants  #18769  
 ZTS: stop zpool_initialize tests racing initialize to completion  #11948   #17311   #18771  
 ZTS: migration/setup: clear stale zfs_member label before new_fs  #18492   #18753  
 Fix receive of split large blocks with a short trailing chunk  #18749  
 Fix receive -x according to comment  #18737   #18738  
 Add SECURITY.md policy file  #18766  
 linux: batch DMU reads of non-resident pages in mappedread()  #16031   #18741  
 Linux: fix zfs_write() infinite loop on unfaultable buffer  #17129   #18740  
 build: Fix for building dist target outside of project root  #18744  
 ZTS: ctime_001_pos increase tolerance  #18733  
 libzfs: fix MS_CRYPT/MS_OVERLAY collision with umount2(2) flags  #18713  
 Fix insufficient locking in dedup verify  #17960   #18712   #18720  
 zpl_ctldir: remove comments describing ancient kernel behaviour  #18722  
 Linux 7.2: zpl_super: convert to sget_fc()  #18677  
 linux/abd: remove BIO support functions  #18719  
 Using net/cloud-init to unpin specific python  #18717  
 linux: handle mmap read beyond file size  #18715  
 Fix race between device removal completion and pool export  #18657  
 CI: Increase default watchdog NMI timeout on Linux  #18704  
 ddt_log: Fix refcount tagging for begin/commit  #18706  
 Update mtime/ctime when fallocate grows a file  #18573  
 honor file argument in file_wait_event  #18700  
 README: update supported FreeBSD release to 15.1  #18696  
 Clean up embedded slog metaslab across txgs  #18693  
 initramfs-zfs should not try to copy directories  #18582   #18686  
 CI: Re-allow workflow_dispatch on zfs-qemu  #18680  
 zfs_ioctl: fix EBUSY race between quota queries and mount  #18611  
 Fix handling of _PC_HAS_HIDDENSYSTEM for FreeBSD  #18688  
 Linux 7.1 compat: META ( #18682 ) 
 Update our CI runners to the newest FreeBSD 15.1 RELEASE ( #18667 ) 
 CI: Have zfs-build-packages workflow build tarballs on Alma ( #18662 ) 
 arc: add a few invariant checks in release builds  #18840  
 zbookmark_compare: handle "marker" bookmarks with negative levels  #14777   #18652  
 delegate: add 'send:encrypted' permission  #18673  
 zfs_secpolicy_send: lift checks to common function for both  #18673  
 ZTS: delegate: test send:encrypted  #18673  
 ZTS: delegate: check send permissions on encrypted datasets  #18673  
 ZTS: delegate: add encryption option for test fixture datasets  #18673  
 ZTS: remove send_delegation tests  #18672  
 ZTS: delegate: add test for send sub-permissions  #18672  
 ZTS: statx_dioalign.ksh update to stride_dd  #18547  
 ZTS: Pass dec instead of hex to mknod  #18547  
 zio_ddt_write: compute have_dvas after taking dde_io_lock  #18366   #18544  
 freebsd: set mnt_time on the rootfs at mountroot time 
 Add dbrrd_latest_time() to grab the latest timestamp in the db 
 Constify some rrd_*() functions 

       Assets 
       5 

      Loading 

               Uh oh!

                There was an error while loading.  Please reload this page . 

      -->     

                👍 
             15 
    m-ueberall, chrislongros, allddd, Safari77, stevleibelt, arakus, finn-braun, congzhangzh, manticoreroko, AllKind, and 5 more reacted with thumbs up emoji 
                🎉 
             14 
    ncoder-1, genjitran, BirMa, whoschek, chrislongros, aosan, allddd, gh4rib, vowstar, finn-braun, and 4 more reacted with hooray emoji 
                ❤️ 
             17 
    ooonea, gg7, brookiestein, kr0leg, chrislongros, andrey-podko, allddd, KrzysztofMaciejewski, finn-braun, congzhangzh, and 7 more reacted with heart emoji 
                🚀 
             14 
    kylemanna, Sieboldianus, chrislongros, allddd, davidetogni, arakus, finn-braun, congzhangzh, chaudis, manticoreroko, and 4 more reacted with rocket emoji 
                👀 
             1 
    xplosionmind reacted with eyes emoji 

     All reactions 

                 👍 
                   15 reactions 

                 🎉 
                   14 reactions 

                 ❤️ 
                   17 reactions 

                 🚀 
                   14 reactions 

                 👀 
                   1 reaction 

      40 people reacted 

         zfs-2.3.9 

          zfs-2.3.9  

     Compare 

        Choose a tag to compare

                   Sorry, something went wrong. 

        Filter

      Loading 

                           Sorry, something went wrong. 

               Uh oh!

                There was an error while loading.  Please reload this page . 

               No results found 

                       View all tags 

       tonyhutter 

    released this

        21 Aug 23:33

                zfs-2.3.9

                This tag was signed with the committer’s  verified signature .

             tonyhutter 
            Tony Hutter

             GPG key ID:  6AD860EED4598027  

             Verified

           Learn about vigilant mode .

               4c0eb72            

          Supported Platforms 

  Linux : compatible with 4.18 - 7.2 kernels 
  FreeBSD : compatible with releases starting from 13.3+, 14.0+ 

 Changes 

 [zfs-2.3.9] Add workaround for device_access ZTS test 
 [zfs-2.3.9] Add 'capsh' to commands.cfg 
 ZTS: device access tests  #18960  
 vdev_disk: use calling cred to check for device access  #18960  
 vdev_file: use calling cred to check for device access  #18960  
 zfs_file_open: add cred arg, use it to check access  #18960  
 vdev_open: pass credential to check for permission to open device  #18960  
 secpolicy_zfs: add a note about the power of CAP_SYS_ADMIN  #18959  
 secpolicy_sys_config: only permit a global zone credential  #18959  
 secpolicy_zinject: only permit a global zone credential  #18959  
 secpolicy_nfs: remove, not used  #18959  
 ZTS: test secpolicy_zinject correctly limits namespace access  #18959  
 ZTS: test secpolicy_sys_config correctly limits namespace access  #18959  
 config: detect idmap method via generic_permission test  #18769  
 mmp: tell a failed uberblock claim apart from remote activity  #18892  
 ZTS: add coverage for zhack mmp reclaim  #18892  
 zhack: add "mmp reclaim" to recover a pool stranded by MMP  #18892  
 Make systemd-udev-settle optional for the import units  #18832  
 Fix ddtprune causing space leak  #17982   #17983  
 Linux 7.2 compat: META  #18941  
 nvpair: i_get_value_size() string array handling tweak  #18877  
 nvpair: Improve native handling of unterminated strings  #18876  
 CodeQL: Flag implicit compare-then-assign in branch conditions  #18899  
 Linux 5.19/6.17: handle differences in how to flush delay workqueue  #18847  
 Linux 6.3: follow_down() gains flags arg  #18847  
 Linux 6.18 compat: vfs_parse_fs_string() takes 3 args  #18847  
 nvpair: Fix operator precedence  #18874  
 ZTS: don't read a command's exit status as a missing binary  #18726   #18882  
 build: Fix release detection when build dir is not source dir  #18891  
 CI: don't fail a passing job when a log reader has already exited  #18885  
 CI: publish the per-VM test counter atomically  #18885  
 man: zvol_request_sync is not ignored under blk-mq  #18887  
 libzfs: don't read a dataset handle after closing it in resume send  #18870   #18883  
 ZTS: add coverage for the MMP claim on a degraded mirror  #18855  
 mmp: do not require writes to mirror legs the config marks absent  #18855  
 libzfs: String trimming should not operate out of bounds  #18868  
 libzfs: don't truncate a resolved vdev path in zpool_vdev_name()  #18851   #18871  
 libzfs: Do not call munmap() when mmap() fails  #18869  
 Add missing checks to zfs_clone_range_replay()  #18867  
 zfs: fix stale POSIX ACL cache after rollback  #18837  
 zed: let autoexpand see capacity changes on partitioned disks  #12505   #18833  
 ZTS: make file_check actually compare the resume test results  #18834  
 dmu_recv: Avoid potential null deref  #18848  
 DDT: Fix several bugs in pruning  #18838  
 cstyle: better tolerance for struct literals 
 libspl: Implement VERIFY_IMPLY and VERIFY_EQUIV  #18822  
 mmp: skip non-writeable vdevs during activity check  #18823   #18835  
 zdb: output refcounts from verify_spacemap_refcounts()  #18809  
 L2ARC: bound the rebuild by the write hand on a first sweep  #3114   #3400   #5583   #10224   #12779   #18827  
 libzfs: fallback VDEV_UPATH to VDEV_PATH for non-DM devices  #18439   #18802  
 Fix reads for blocks freed after being cloned  #18421   #18724  
 Rate limit Direct I/O verify zevents  #18795  
 CI: Update Alpine Linux runner to 3.24.1  #18790  
 Remove libuutil from the pull request template and fix headings  #18791  
 CI: Fix race caused by shared ctr file updates  #18778  
 zpl_inode: remove zpl_rename no-flags variants  #18769  
 ZTS: migration/setup: clear stale zfs_member label before new_fs  #18492   #18753  
 Fix receive -x according to comment  #18737   #18738  
 Add SECURITY.md policy file  #18766  
 linux: batch DMU reads of non-resident pages in mappedread()  #16031   #18741  
 Linux: fix zfs_write() infinite loop on unfaultable buffer  #17129   #18740  
 build: Fix for building dist target outside of project root  #18744  
 ZTS: ctime_001_pos increase tolerance  #18733  
 libzfs: fix MS_CRYPT/MS_OVERLAY collision with umount2(2) flags  #18713  
 zpl_ctldir: remove comments describing ancient kernel behaviour  #18722  
 Linux 7.2: zpl_super: convert to sget_fc()  #18677  
 Using net/cloud-init to unpin specific python  #18717  
 linux: handle mmap read beyond file size  #18715  
 Fix race between device removal completion and pool export  #18657  
 CI: Increase default watchdog NMI timeout on Linux  #18704  
 ddt_log: Fix refcount tagging for begin/commit  #18706  
 Update mtime/ctime when fallocate grows a file  #18573  
 honor file argument in file_wait_event  #18700  
 README: update supported FreeBSD release to 15.1  #18696  
 Clean up embedded slog metaslab across txgs  #18693  
 initramfs-zfs should not try to copy directories  #18582   #18686  
 CI: Re-allow workflow_dispatch on zfs-qemu  #18680  
 Linux 7.1 compat: META ( #18682 ) 
 Update our CI runners to the newest FreeBSD 15.1 RELEASE ( #18667 ) 
 CI: Have zfs-build-packages workflow build tarballs on Alma ( #18662 ) 
 zbookmark_compare: handle "marker" bookmarks with negative levels  #14777   #18652  
 ZTS: Pass dec instead of hex to mknod  #18547  

       Assets 
       5 

      Loading 

               Uh oh!

                There was an error while loading.  Please reload this page . 

      -->     

                👍 
             3 
    m-ueberall, AllKind, and little-sparkleeesss reacted with thumbs up emoji 
                ❤️ 
             1 
    davidetogni reacted with heart emoji 
                🚀 
             1 
    kylemanna reacted with rocket emoji 

     All reactions 

                 👍 
                   3 reactions 

                 ❤️ 
                   1 reaction 

                 🚀 
                   1 reaction 

      5 people reacted 

         zfs-2.2.11 

          zfs-2.2.11  

     Compare 

        Choose a tag to compare

                   Sorry, something went wrong. 

        Filter

      Loading 

                           Sorry, something went wrong. 

               Uh oh!

                There was an error while loading.  Please reload this page . 

               No results found 

                       View all tags 

       tonyhutter 

    released this

        21 Aug 23:33

                zfs-2.2.11

                This tag was signed with the committer’s  verified signature .

             tonyhutter 
            Tony Hutter

             GPG key ID:  6AD860EED4598027  

             Verified

           Learn about vigilant mode .

               f2d87f5            

          Supported Platforms 

  Linux : compatible with 4.18 - 6.17 kernels 
  FreeBSD : compatible with releases starting from 13.3+, 14.0+ 

 Changes 

 [zfs-2.2.11] Add workaround for device_access ZTS test 
 [zfs-2.2.11] Add 'capsh' to commands.cfg 
 ZTS: device access tests  #18960  
 vdev_disk: use calling cred to check for device access  #18960  
 vdev_file: use calling cred to check for device access  #18960  
 zfs_file_open: add cred arg, use it to check access  #18960  
 vdev_open: pass credential to check for permission to open device  #18960  
 secpolicy_zfs: add a note about the power of CAP_SYS_ADMIN  #18959  
 secpolicy_sys_config: only permit a global zone credential  #18959  
 secpolicy_zinject: only permit a global zone credential  #18959  
 secpolicy_nfs: remove, not used  #18959  
 ZTS: test secpolicy_zinject correctly limits namespace access  #18959  
 ZTS: test secpolicy_sys_config correctly limits namespace access  #18959  
 config: detect idmap method via generic_permission test  #18769  
 libzfs: fallback VDEV_UPATH to VDEV_PATH for non-DM devices  #18439   #18802  
 CodeQL: Flag implicit compare-then-assign in branch conditions  #18899  
 CI: don't fail a passing job when a log reader has already exited  #18885  
 CI: publish the per-VM test counter atomically  #18885  
 CI: Update Alpine Linux runner to 3.24.1  #18790  
 Remove libuutil from the pull request template and fix headings  #18791  
 CI: Fix race caused by shared ctr file updates  #18778  
 Using net/cloud-init to unpin specific python  #18717  
 CI: Increase default watchdog NMI timeout on Linux  #18704  
 CI: Re-allow workflow_dispatch on zfs-qemu  #18680  
 Update our CI runners to the newest FreeBSD 15.1 RELEASE ( #18667 ) 
 CI: Have zfs-build-packages workflow build tarballs on Alma ( #18662 ) 
 zts: test syncfs() behaviour when pool suspends  #17420  
 zpl_sync_fs: work around kernels that ignore sync_fs errors  #17420  
 zfs_sync: return error when pool suspends  #17420  
 zfs_sync: remove support for impossible scenarios  #17420  
 Fix aarch64 build failure by removing earlyclobber ( #18532 ) 

       Assets 
       5 

      Loading 

               Uh oh!

                There was an error while loading.  Please reload this page . 

      -->     

                ❤️ 
             2 
    davidetogni and little-sparkleeesss reacted with heart emoji 
                🚀 
             1 
    kylemanna reacted with rocket emoji 

     All reactions 

                 ❤️ 
                   2 reactions 

                 🚀 
                   1 reaction 

      3 people reacted 

         zfs-2.4.3 

          zfs-2.4.3  

     Compare 

        Choose a tag to compare

                   Sorry, something went wrong. 

        Filter

      Loading 

                           Sorry, something went wrong. 

               Uh oh!

                There was an error while loading.  Please reload this page . 

               No results found 

                       View all tags 

       tonyhutter 

    released this

        12 Jun 21:02

                zfs-2.4.3

                This tag was signed with the committer’s  verified signature .

             tonyhutter 
            Tony Hutter

             GPG key ID:  6AD860EED4598027  

             Verified

           Learn about vigilant mode .

               83020cf            

          Supported Platforms 

  Linux : compatible with 4.18 - 7.0 kernels 
  FreeBSD : compatible with releases starting from 13.3+, 14.0+ 

 Changes 

 abd: Fix stats asymmetry in case of Direct I/O  #18390  
 ZVOL: Add encryption key check for block cloning  #18315  
 Fix log vdev removal issues  #18277  
 Remove parent ZIO from dbuf_prefetch()  #18214  
 Simplify dnode_level_is_l2cacheable()  #18212  
 When reading a vdev label skip libzfs_core_init()  #18606  
 dsl_scan: close errorscrub cursor on pause  #18603  
 enforce exact decompressed length for lz4, gzip, and zstd  #18599  
 FreeBSD: Make it possible to build openzfs.ko with sanitizers  #18596  
 spl_kvmalloc: remove __GFP_COMP before calling vmalloc()  #18558  
 zap_impl: use flex array field for mzap_phys_t.mz_chunks  #18550  
 arc: export additional required symbols  #18533  
 Fix double free for blocks cloned after DDT prune  #18520  
 zarcstat: detect attached L2ARC device with no data  #18499  
 zdb: detect BRT and DDT leaks during block traversal  #18494  
 sa: fix sa_add_projid lock ordering  #18503  
 zfs: annotate nested dd_lock in reservation sync accounting  #18497  
 Avoid flushing unrelated NFS exports on snapshot unmount  #18476  
 Fix off-by-one in PREVIOUSLY_REDACTED handler that drops last block  #18477  
 key lookup failure should always return EACCES  #18448  
 Fix "panic: cache_vop_rename: lingering negative entry"  #18430  
 Fix aarch64 build failure by removing earlyclobber ( #18532 ) 
 Linux 5.6 compat: fix fs_parse API mismatch  #18585  
 linux/super: properly apply ro/rw mount option to superblock  #18557   #18563  
 config: show progress output for kernel API checks  #18554  
 linux: suppress reclaim lockdep in zfs_inactive via rwlock wrappers  #18505  
 linux/zpl_super: handle 'source' option directly  #18529  
 Linux: avoid znode list lock inversion during resume  #18517  
 Linux: annotate nested xattr setattr znode locks  #18506  
 linux: verify stale znodes in legacy fallocate  #18458  
 ZTS: relax zpool_import_parallel_pos.ksh timing  #18634  
 Fix uninitialized variable warning in zil_parse()  #18633  
 Add additional verification of size fields and strings ( #18623 )  #18623  
 CI: Add alternative URLs for CentOS stream  #18628  
 CI: Increase default RCU stall timeout on Linux  #18624  
 CI: Update CodeQL actions to v4  #18629  
 CI: Re-enable CodeQL workflows on push  #18627  
 Remove /etc/sudoers.d/zfs  #18626  
 pam: use open fd instead of path  #18618  
 Extend dataset zfs_ioc_set_prop() secpolicy  #18617  
 Fix uninitialized variable warning in vdev_prop_get()  #18616  
 sharenfs: Check for invalid characters  #18613  
 Fix the integer type in zfs_ioc_userspace_many()  #18615  
 nvpair: Check for un-terminated strings in packed nvlist  #18604  
 CI: add concurrency support to zfs-arm  #18608  
 CI: apt-get update before purging host packages  #18607   #18609  
 build: add ZFS_DEBUG Kconfig for copy-builtin  #18595  
 CI: skip smatch, zloop, and zfs-arm for documentation-only changes  #18601  
 CI: Lustre 6.16 kernel compatibility fix ( #18602 ) 
 CI: Update checkstyle checkout action to v6  #18600  
 .github: update workflows README  #18590  
 CI: run full CI when a workflow YAML changes  #18577  
 CI: skip full CI runs on push events  #18571  
 CI: enable FreeBSD 15.0-RELEASE in matrix  #18561  
 CI: Build custom branch from zfs-qemu-packages  #18569  
 ZTS: zfs_unshare_006_pos.ksh enable usershares  #18547  
 CI: Fix qemu-guest-agent systemd enable  #18547  
 CI: Add Ubuntu 26.04 builder  #18547  
 CI: remove FreeBSD 13.5 (EOL April 30, 2026)  #18553  
 CI: Allow testing with a newer GCC on ARM builder  #18540  
 CI: Remove deprecated Fedora 42  #18545  
 CI: Fix 99.99 META version  #18526   #18531  
 CI: FreeBSD 15.1 STABLE  #18524  

       Assets 
       5 

      Loading 

               Uh oh!

                There was an error while loading.  Please reload this page . 

      -->     

                👍 
             24 
    m-ueberall, whoschek, atomjack, kylemanna, cdluminate, clouths, PeterFalken, allddd, Safari77, allixx, and 14 more reacted with thumbs up emoji 
                🎉 
             7 
    satmandu, gamanakis, chrislongros, ammarfaizi2, andrey-podko, firengate, and creekpld reacted with hooray emoji 
                ❤️ 
             12 
    davidetogni, gamanakis, xplosionmind, kr0leg, FireTrack, BirMa, chrislongros, dimlev, k3ssl0sh4y, firengate, and 2 more reacted with heart emoji 
                🚀 
             1 
    firengate reacted with rocket emoji 
                👀 
             4 
    xplosionmind, chrislongros, firengate, and JoaGamo reacted with eyes emoji 

     All reactions 

                 👍 
                   24 reactions 

                 🎉 
                   7 reactions 

                 ❤️ 
                   12 reactions 

                 🚀 
                   1 reaction 

                 👀 
                   4 reactions 

      34 people reacted 

         zfs-2.3.8 

          zfs-2.3.8  

     Compare 

        Choose a tag to compare

                   Sorry, something went wrong. 

        Filter

      Loading 

                           Sorry, something went wrong. 

               Uh oh!

                There was an error while loading.  Please reload this page . 

               No results found 

                       View all tags 

       tonyhutter 

    released this

        12 Jun 21:01

                zfs-2.3.8

                This tag was signed with the committer’s  verified signature .

             tonyhutter 
            Tony Hutter

             GPG key ID:  6AD860EED4598027  

             Verified

           Learn about vigilant mode .

               b4842ae            

          Supported Platforms 

  Linux : compatible with 4.18 - 7.0 kernels 
  FreeBSD : compatible with releases starting from 13.3+, 14.0+ 

 Changes 

 abd: Fix stats asymmetry in case of Direct I/O  #18390  
 ZVOL: Add encryption key check for block cloning  #18315  
 Fix log vdev removal issues  #18277  
 Remove parent ZIO from dbuf_prefetch()  #18214  
 Simplify dnode_level_is_l2cacheable()  #18212  
 Rename several printf attributes declarations to  printf   #18095  
 When reading a vdev label skip libzfs_core_init()  #18606  
 dsl_scan: close errorscrub cursor on pause  #18603  
 enforce exact decompressed length for lz4, gzip, and zstd  #18599  
 FreeBSD: Make it possible to build openzfs.ko with sanitizers  #18596  
 spl_kvmalloc: remove __GFP_COMP before calling vmalloc()  #18558  
 zap_impl: use flex array field for mzap_phys_t.mz_chunks  #18550  
 arc: export additional required symbols  #18533  
 Fix double free for blocks cloned after DDT prune  #18520  
 zarcstat: detect attached L2ARC device with no data  #18499  
 zdb: detect BRT and DDT leaks during block traversal  #18494  
 sa: fix sa_add_projid lock ordering  #18503  
 zfs: annotate nested dd_lock in reservation sync accounting  #18497  
 Fix off-by-one in PREVIOUSLY_REDACTED handler that drops last block  #18477  
 key lookup failure should always return EACCES  #18448  
 Fix "panic: cache_vop_rename: lingering negative entry"  #18430  
 Fix aarch64 build failure by removing earlyclobber ( #18532 ) 
 Linux 5.6 compat: fix fs_parse API mismatch  #18585  
 linux/super: properly apply ro/rw mount option to superblock  #18557   #18563  
 config: show progress output for kernel API checks  #18554  
 linux: suppress reclaim lockdep in zfs_inactive via rwlock wrappers  #18505  
 linux/zpl_super: handle 'source' option directly  #18529  
 Linux: avoid znode list lock inversion during resume  #18517  
 Linux: annotate nested xattr setattr znode locks  #18506  
 linux: verify stale znodes in legacy fallocate  #18458  
 ZTS: relax zpool_import_parallel_pos.ksh timing  #18634  
 Fix uninitialized variable warning in zil_parse()  #18633  
 Add additional verification of size fields and strings ( #18623 )  #18623  
 CI: Add alternative URLs for CentOS stream  #18628  
 CI: Increase default RCU stall timeout on Linux  #18624  
 CI: Update CodeQL actions to v4  #18629  
 CI: Re-enable CodeQL workflows on push  #18627  
 Remove /etc/sudoers.d/zfs  #18626  
 pam: use open fd instead of path  #18618  
 Extend dataset zfs_ioc_set_prop() secpolicy  #18617  
 Fix uninitialized variable warning in vdev_prop_get()  #18616  
 sharenfs: Check for invalid characters  #18613  
 Fix the integer type in zfs_ioc_userspace_many()  #18615  
 nvpair: Check for un-terminated strings in packed nvlist  #18604  
 CI: add concurrency support to zfs-arm  #18608  
 CI: apt-get update before purging host packages  #18607   #18609  
 CI: skip smatch, zloop, and zfs-arm for documentation-only changes  #18601  
 CI: Lustre 6.16 kernel compatibility fix ( #18602 ) 
 CI: Update checkstyle checkout action to v6  #18600  
 .github: update workflows README  #18590  
 CI: run full CI when a workflow YAML changes  #18577  
 CI: skip full CI runs on push events  #18571  
 CI: enable FreeBSD 15.0-RELEASE in matrix  #18561  
 CI: Build custom branch from zfs-qemu-packages  #18569  
 ZTS: zfs_unshare_006_pos.ksh enable usershares  #18547  
 CI: Fix qemu-guest-agent systemd enable  #18547  
 CI: Add Ubuntu 26.04 builder  #18547  
 CI: remove FreeBSD 13.5 (EOL April 30, 2026)  #18553  
 CI: Allow testing with a newer GCC on ARM builder  #18540  
 CI: Remove deprecated Fedora 42  #18545  
 CI: Fix 99.99 META version  #18526   #18531  
 CI: FreeBSD 15.1 STABLE  #18524  
 CI: skip qemu matrix for documentation-only pull requests  #18518  

       Assets 
       5 

      Loading 

               Uh oh!

                There was an error while loading.  Please reload this page . 

      -->     

                👍 
             5 
    m-ueberall, stevleibelt, drescherjm, IvanVolosyuk, and chrislongros reacted with thumbs up emoji 
                ❤️ 
             3 
    davidetogni, chrislongros, and little-sparkleeesss reacted with heart emoji 

     All reactions 

                 👍 
                   5 reactions 

                 ❤️ 
                   3 reactions 

      7 people reacted 

         zfs-2.2.10 

          zfs-2.2.10  

     Compare 

        Choose a tag to compare

                   Sorry, something went wrong. 

        Filter

      Loading 

                           Sorry, something went wrong. 

               Uh oh!

                There was an error while loading.  Please reload this page . 

               No results found 

                       View all tags 

       tonyhutter 

    released this

        12 Jun 21:01

                zfs-2.2.10

                This tag was signed with the committer’s  verified signature .

             tonyhutter 
            Tony Hutter

             GPG key ID:  6AD860EED4598027  

             Verified

           Learn about vigilant mode .

               07c1e2e            

          Supported Platforms 

  Linux : compatible with 4.18 - 6.17 kernels 
  FreeBSD : compatible with releases starting from 13.3+, 14.0+ 

 Changes 

 Rename several printf attributes declarations to __printf__  #18095  
 Fix uninitialized variable warning in zil_parse()  #18633  
 pam: use open fd instead of path  #18618  
 Extend dataset zfs_ioc_set_prop() secpolicy  #18617  
 Fix uninitialized variable warning in vdev_prop_get()  #18616  
 Fix the integer type in zfs_ioc_userspace_many()  #18615  
 Add additional verification of size fields and strings ( #18623 )  #18623  
 Remove /etc/sudoers.d/zfs  #18626  
 sharenfs: Check for invalid characters  #18613  
 nvpair: Check for un-terminated strings in packed nvlist  #18604  
 CI: Add alternative URLs for CentOS stream  #18628  
 CI: Increase default RCU stall timeout on Linux  #18624  
 CI: Update CodeQL actions to v4  #18629  
 CI: Re-enable CodeQL workflows on push  #18627  
 draid: fix cksum errors after rebuild with degraded disks  #18414  
 draid: allow seq resilver reads from degraded vdevs  #18405  
 draid: fix import failure after disks replacements  #18380  
 draid: fix data corruption after disk clear  #18286   #18294  
 test/draid: fix error return  #17551  
 CI: add concurrency support to zfs-arm  #18608  
 CI: apt-get update before purging host packages  #18607   #18609  
 CI: skip smatch, zloop, and zfs-arm for documentation-only changes  #18601  
 CI: Lustre 6.16 kernel compatibility fix ( #18602 ) 
 CI: Update checkstyle checkout action to v6  #18600  
 .github: update workflows README  #18590  
 CI: run full CI when a workflow YAML changes  #18577  
 CI: skip full CI runs on push events  #18571  
 CI: enable FreeBSD 15.0-RELEASE in matrix  #18561  
 CI: Build custom branch from zfs-qemu-packages  #18569  
 ZTS: zfs_unshare_006_pos.ksh enable usershares  #18547  
 CI: Fix qemu-guest-agent systemd enable  #18547  
 CI: Add Ubuntu 26.04 builder  #18547  
 CI: remove FreeBSD 13.5 (EOL April 30, 2026)  #18553  
 CI: Allow testing with a newer GCC on ARM builder  #18540  
 CI: Remove deprecated Fedora 42  #18545  
 CI: Fix 99.99 META version  #18526   #18531  
 CI: FreeBSD 15.1 STABLE  #18524  
 CI: skip qemu matrix for documentation-only pull requests  #18518  
 CI: FreeBSD 15.1 PRERELEASE ( #18490 ) 
 CI/GCC: Add Fedora 44, fix build errors and threadsappend  #18478  
 CI: curl fallback, print killed tests, FreeBSD URL  #18460  
 CI: Add more debugging to qemu-1-setup.sh  #18441  
 CI: tolerate missing artifacts  #18438  
 CI: Do not set scheduler in qemu-1-setup.sh  #18437  
 README: add FreeBSD 14.4-RELEASE alongside 15.0  #18304  
 README: describe specific kernels/distros we target  #18295  
 Fix capitalization typo in README.md  #17889  
 CI: Disable ZIP file artifacts, update versions  #18411  
 Fix available space accounting for special/dedup  #18222   #18367  
 Linux 6.18: convert ida_simple_* calls 
 Linux 6.18: replace write_cache_pages() 
 Linux 6.19: replace i_state access with inode_state_read_once()  #18053  
 Fix a declaration position of the nth_page.  #18034  
 Linux 6.18: replace nth_page() 
 sha256_generic: make internal functions a little more private 
 CI: Fix Ubuntu 22.01 rsend failures  #18032  
 nvpair: chase FreeBSD xdrproc_t definition  #18154  
 Linux 6.18: block_device_operations-&gt;getgeo takes struct gendisk* 
 linux/atomic: fill out API for atomic pointer ops  #17580  
 Linux 6.18: namespace type moved to ns_common 
 CI: Free 35GB of unused files on the runner  #18400  
 ci: update FreeBSD CI images from 14.3 to 14.4  #18362  
 [2.2.10-only] CI: Fix ARM builder path 
 CI: Add ARM builder  #18343  
 CI: Support repository variable override for ZTS OS selection  #18342  
 CI: Remove deprecated Fedora 41  #18261  
 CI: Test build Lustre against ZFS  #18161  
 CI: Fix qemu-1-setup failure, remove debug stuff  #18166  
 CI: Add Alpine Linux 3.23 runner to the pipeline ( #18087 ) 
 CI: Test 2.4.x in qemu-test-repo-vm.sh, quick mode  #18070  
 CI: Use Ubuntu mirrors instead of azure ( #18057 )  #18057  
 Remove the obsolete FreeBSD 14.2-RELEASE from CI  #18013  
 CI: Change timeout values  #18056  
 During CI, use  nproc  instead of  sysctl -n hw.ncpu   #18012  
 CI: zfs-test-packages: Add in new repos  #17956  
 CI: Add smatch static analysis workflow  #17935  
 ZTS: add mount_loopback to test zfs behind loop dev  #17329  
 config: Fix LLVM-21 -Wuninitialized-const-pointer warning  #17682   #17684  
 linux: use sys/stat.h instead of linux/stat.h  #17675  
 Fix nfs_truncate_shares without /etc/exports.d  #15369   #15468  

       Assets 
       5 

      Loading 

               Uh oh!

                There was an error while loading.  Please reload this page . 

      -->     

                👍 
             3 
    stevleibelt, chrislongros, and little-sparkleeesss reacted with thumbs up emoji 
                ❤️ 
             3 
    davidetogni, Bronek, and chrislongros reacted with heart emoji 

     All reactions 

                 👍 
                   3 reactions 

                 ❤️ 
                   3 reactions 

      5 people reacted 

         zfs-2.4.2 

          zfs-2.4.2  

     Compare 

        Choose a tag to compare

                   Sorry, something went wrong. 

        Filter

      Loading 

                           Sorry, something went wrong. 

               Uh oh!

                There was an error while loading.  Please reload this page . 

               No results found 

                       View all tags 

       tonyhutter 

    released this

        12 May 22:20

                zfs-2.4.2

                This tag was signed with the committer’s  verified signature .

             tonyhutter 
            Tony Hutter

             GPG key ID:  6AD860EED4598027  

             Verified

           Learn about vigilant mode .

               6330a45            

          Supported Platforms 

  Linux : compatible with 4.18 - 7.0 kernels 
  FreeBSD : compatible with releases starting from 13.3+, 14.0+ 

 Changes 

 initramfs: fix incorrect variable rename  #18442  
 Fix long POSIX_FADV_DONTNEED for single block files  #18399   #18489  
 Add support for POSIX_FADV_DONTNEED  #18399  
 Cleanup allocation class selection  #18208  
 [2.4.2-only] GCC: Fix uu_ident.c strchr() 
 libspl/mnttab: follow symlinks when resolving path via statx ( #18469 ) 
 Fix vdev_rebuild_range() tx commit  #18276  
 Fix redundant declaration of dsl_pool_t  #18263  
 CI: FreeBSD 15.1 PRERELEASE ( #18490 ) 
 CI/GCC: Add Fedora 44, fix build errors and threadsappend  #18478  
 Linux 7.1: access dentry d_alias directly  #18471  
 Initialize vr_last_txg for rebuild  #18482  
 Fix rare cksum errors after rebuild  #18307   #18319   #18473  
 ZTS: add targeted redundancy_draid_spare exception  #18436  
 build: use pax tar format for make dist 
 CI: curl fallback, print killed tests, FreeBSD URL  #18460  
 Fix 'kernel BUG at mm/usercopy.c'  #15918   #18408  
 dmu_direct: avoid UAF in dmu_write_direct_done()  #18440  
 Prevent range tree corruption race by updating dnode_sync()  #18235  
 range_tree: use zfs_panic_recover() for partial-overlap remove  #18255  
 [zfs-2.4.2] Whitelist some Makefile.am files from SPDX 
 Fix read corruption after block clone after truncate  #18412   #18421  
 Fix snapshot automount deadlock during concurrent zfs recv  #18415  
 Fix options memory leak in zfsctl_snapshot_mount  #18415  
 Fix s_active leak in zfsvfs_hold() when z_unmounted is true  #18309   #18310  
 fix memleak in spa_errlog.c  #18403  
 CI: Add more debugging to qemu-1-setup.sh  #18441  
 CI: tolerate missing artifacts  #18438  
 CI: Do not set scheduler in qemu-1-setup.sh  #18437  
 Linux 7.0 compat: META  #18435  
 deb.am: propagate build errors in native-deb targets  #18206   #18424  
 draid: fix cksum errors after rebuild with degraded disks  #18414  
 CI: Disable ZIP file artifacts, update versions  #18411  
 CI: set /etc/hostid in zloop runner  #18413  
 draid: allow seq resilver reads from degraded vdevs  #18405  
 Linux: Refactor zpl_fadvise()  #18395  
 CI: Free 35GB of unused files on the runner  #18400  
 linux/vfsops: remove zfs_mnt_t, pass directly  #18377  
 linux/super: work around kernels that enforce "forbidden" mount options  #18377  
 linux/super: implement new mount params parser  #18377  
 linux/super: match vfs_t lifetime to fs_context  #18377  
 linux/super: remove zpl_parse_monolithic  #18377  
 linux/vfsops: remove old options parser  #18377  
 linux/vfsops: add vfs_t allocator, make public  #18377  
 draid: fix import failure after disks replacements  #18380  
 Linux 7.0: ensure LSMs get to process mount options  #18376  
 ci: update FreeBSD CI images from 14.3 to 14.4  #18362  
 Linux 7.0: autoconf: Remove copy-from-user-inatomic API checks ( #18348 ) ( #18354 ) 
 CI: Add ARM builder  #18343  
 CI: Support repository variable override for ZTS OS selection  #18342  
 linux/super: flatten zpl_fill_super into zpl_get_tree  #18339  
 linux/super: flatten zpl_mount_impl into zpl_get_tree  #18339  
 linux/super: flatten mount/remount into get_tree/reconfigure  #18339  
 linux/super: remove support for old mount API  #18339  
 config: refuse to build without fs_context  #18339  
 Linux 7.0: also set setlease handler on directories ( #18331 ) 
 ZTS: Add back redundancy_draid_spare3 exception  #18320  
 ZTS: redundancy_draid_spare{1,3} exceptions  #18308  
 config: fix STATX_MNT_ID detection  #18312  
 draid: fix data corruption after disk clear  #18286   #18294  
 Fix deadlock on dmu_tx_assign() from vdev_rebuild()  #18210   #18258  
 README: describe specific kernels/distros we target  #18295  
 config: remove minimum kernel version check  #18295  
 libzfs: use mount_setattr for selective remount including legacy mounts  #18257  
 FreeBSD: Improve dmesg kernel message prefix  #18290  
 Fix check for .cfi_negate_ra_state on aarch64  #18262  
 zpl_super: prefer "new" mount API when available  #18260  
 CI: Remove deprecated Fedora 41  #18261  
 Linux 7.0: add shims for the fs_context-based mount API  #18216  
 Linux 7.0: posix_acl_to_xattr() now allocates memory  #18216  
 Linux 7.0: blk_queue_nonrot() renamed to blk_queue_rot()  #18216  
 build: get objtool from $kernelbuild  #18248   #18249  
 Linux 7.0: explicitly set setlease handler to kernel implementation  #18215  
 spdxcheck: enforce SPDX license tags on build system files  #18077  
 build: add SPDX license tags to build system files  #18077  

       Assets 
       5 

      Loading 

               Uh oh!

                There was an error while loading.  Please reload this page . 

      -->     

                👍 
             15 
    m-ueberall, finn-braun, lin72h, M4rtineski, Safari77, chrislongros, fahmirafie, allddd, ClosedPort22, xplosionmind, and 5 more reacted with thumbs up emoji 
                🎉 
             16 
    markeenmelo, atomjack, finn-braun, lin72h, orz--, M4rtineski, chrislongros, andrey-podko, allddd, li-nkSN, and 6 more reacted with hooray emoji 
                ❤️ 
             19 
    spike77453, behlendorf, atomjack, totalAldo, omarluq, finn-braun, lin72h, BirMa, M4rtineski, chrislongros, and 9 more reacted with heart emoji 
                🚀 
             14 
    vivo75, omarluq, finn-braun, lin72h, M4rtineski, chrislongros, allddd, 6rendel, davidetogni, kev009, and 4 more reacted with rocket emoji 
                👀 
             4 
    finn-braun, chrislongros, xplosionmind, and firengate reacted with eyes emoji 

     All reactions 

                 👍 
                   15 reactions 

                 🎉 
                   16 reactions 

                 ❤️ 
                   19 reactions 

                 🚀 
                   14 reactions 

                 👀 
                   4 reactions 

      39 people reacted 

         zfs-2.3.7 

          zfs-2.3.7  

     Compare 

        Choose a tag to compare

                   Sorry, something went wrong. 

        Filter

      Loading 

                           Sorry, something went wrong. 

               Uh oh!

                There was an error while loading.  Please reload this page . 

               No results found 

                       View all tags 

       tonyhutter 

    released this

        12 May 22:19

                zfs-2.3.7

                This tag was signed with the committer’s  verified signature .

             tonyhutter 
            Tony Hutter

             GPG key ID:  6AD860EED4598027  

             Verified

           Learn about vigilant mode .

               c030cc1            

          Supported Platforms 

  Linux : compatible with 4.18 - 7.0 kernels 
  FreeBSD : compatible with releases starting from 13.3+, 14.0+ 

 Changes 

 kmem: don't add __GFP_RECLAIMABLE for KM_VMEM allocations  #18107  
 kmem: don't add __GFP_COMP for KM_VMEM allocations  #18053  
 kmem: don't pass __GFP_HIGHMEM to __vmalloc  #18053  
 [2.3.7-only] GCC: Fix uu_ident.c strchr() 
 libspl/mnttab: follow symlinks when resolving path via statx ( #18469 ) 
 Fix vdev_rebuild_range() tx commit  #18276  
 Fix redundant declaration of dsl_pool_t  #18263  
 CI: FreeBSD 15.1 PRERELEASE ( #18490 ) 
 CI/GCC: Add Fedora 44, fix build errors and threadsappend  #18478  
 Linux 7.1: access dentry d_alias directly  #18471  
 Remove the obsolete FreeBSD 14.2-RELEASE from CI  #18013  
 During CI, use  nproc  instead of  sysctl -n hw.ncpu   #18012  
 Initialize vr_last_txg for rebuild  #18482  
 Fix rare cksum errors after rebuild  #18307   #18319   #18473  
 ZTS: add targeted redundancy_draid_spare exception  #18436  
 build: use pax tar format for make dist 
 CI: curl fallback, print killed tests, FreeBSD URL  #18460  
 Fix 'kernel BUG at mm/usercopy.c'  #15918   #18408  
 dmu_direct: avoid UAF in dmu_write_direct_done()  #18440  
 Prevent range tree corruption race by updating dnode_sync()  #18235  
 range_tree: use zfs_panic_recover() for partial-overlap remove  #18255  
 Fix read corruption after block clone after truncate  #18412   #18421  
 ZTS: add regression test for  #17180   #18109  
 Fix s_active leak in zfsvfs_hold() when z_unmounted is true  #18309   #18310  
 fix memleak in spa_errlog.c  #18403  
 [zfs-2.3.7] Whitelist some Makefile.am files from SPDX 
 spdxcheck: enforce SPDX license tags on build system files  #18077  
 build: add SPDX license tags to build system files  #18077  
 CI: Add more debugging to qemu-1-setup.sh  #18441  
 CI: Do not set scheduler in qemu-1-setup.sh  #18437  
 CI: tolerate missing artifacts  #18438  
 Linux 7.0 compat: META  #18435  
 ZTS: resilver_restart_001 improvements  #18434  
 deb.am: propagate build errors in native-deb targets  #18206   #18424  
 draid: fix cksum errors after rebuild with degraded disks  #18414  
 RAIDZ: Remove some excessive logging  #18059  
 CI: set /etc/hostid in zloop runner  #18413  
 draid: allow seq resilver reads from degraded vdevs  #18405  
 Linux: Refactor zpl_fadvise()  #18395  
 linux/vfsops: remove zfs_mnt_t, pass directly  #18377  
 linux/super: work around kernels that enforce "forbidden" mount options  #18377  
 linux/super: implement new mount params parser  #18377  
 linux/super: match vfs_t lifetime to fs_context  #18377  
 linux/super: remove zpl_parse_monolithic  #18377  
 linux/vfsops: remove old options parser  #18377  
 linux/vfsops: add vfs_t allocator, make public  #18377  
 draid: fix import failure after disks replacements  #18380  
 Linux 7.0: ensure LSMs get to process mount options  #18376  
 dmu_tx: break tx assign/wait when pool suspends  #17355  
 dmu_tx: make DMU_TX_* flags an enum  #17355  
 txg_wait_synced_flags: add TXG_WAIT_SUSPEND flag to not wait if pool suspended  #17355  
 Linux 7.0: autoconf: Remove copy-from-user-inatomic API checks ( #18348 ) ( #18354 ) 
 linux/super: flatten zpl_fill_super into zpl_get_tree  #18339  
 linux/super: flatten zpl_mount_impl into zpl_get_tree  #18339  
 linux/super: flatten mount/remount into get_tree/reconfigure  #18339  
 linux/super: remove support for old mount API  #18339  
 config: refuse to build without fs_context  #18339  
 Linux 7.0: also set setlease handler on directories ( #18331 ) 
 ZTS: Add back redundancy_draid_spare3 exception  #18320  
 ZTS: redundancy_draid_spare{1,3} exceptions  #18308  
 config: fix STATX_MNT_ID detection  #18312  
 draid: fix data corruption after disk clear  #18286   #18294  
 Fix deadlock on dmu_tx_assign() from vdev_rebuild()  #18210   #18258  
 dmu_tx_assign: make all VERIFY0 calls use DMU_TX_SUSPEND  #17355  
 README: describe specific kernels/distros we target  #18295  
 config: remove minimum kernel version check  #18295  
 libzfs: use mount_setattr for selective remount including legacy mounts  #18257  
 FreeBSD: Improve dmesg kernel message prefix  #18290  
 Fix check for .cfi_negate_ra_state on aarch64  #18262  
 ZTS: Adjust mmp_on_uberblocks threshold  #18280  
 ZTS: Add additional exceptions  #18274  
 zpl_super: prefer "new" mount API when available  #18260  
 Linux 7.0: add shims for the fs_context-based mount API  #18216  
 Linux 7.0: posix_acl_to_xattr() now allocates memory  #18216  
 Linux 7.0: blk_queue_nonrot() renamed to blk_queue_rot()  #18216  
 build: get objtool from $kernelbuild  #18248   #18249  
 Linux 7.0: explicitly set setlease handler to kernel implementation  #18215  
 Linux: work around use of GPL-only symbol  kasan_flag_enabled   #18009   #18040  
 test/draid: fix error return  #17551  
 CI: Disable ZIP file artifacts, update versions  #18411  
 Fix available space accounting for special/dedup ( #18222 )  #18190   #18222  
 CI: Free 35GB of unused files on the runner  #18400  
 ci: update FreeBSD CI images from 14.3 to 14.4  #18362  
 CI: Add ARM builder  #18343  
 CI: Support repository variable override for ZTS OS selection  #18342  
 CI: Remove deprecated Fedora 41  #18261  

       Assets 
       5 

      Loading 

               Uh oh!

                There was an error while loading.  Please reload this page . 

      -->     

                👍 
             9 
    m-ueberall, AllKind, totalAldo, allddd, davidetogni, xplosionmind, whoschek, chrislongros, and mightyspiky reacted with thumbs up emoji 
                ❤️ 
             2 
    xplosionmind and chrislongros reacted with heart emoji 
                👀 
             2 
    xplosionmind and chrislongros reacted with eyes emoji 

     All reactions 

                 👍 
                   9 reactions 

                 ❤️ 
                   2 reactions 

                 👀 
                   2 reactions 

      9 people reacted 

         zfs-2.4.1 

          zfs-2.4.1  

     Compare 

        Choose a tag to compare

                   Sorry, something went wrong. 

        Filter

      Loading 

                           Sorry, something went wrong. 

               Uh oh!

                There was an error while loading.  Please reload this page . 

               No results found 

                       View all tags 

       tonyhutter 

    released this

        25 Feb 01:52

                zfs-2.4.1

                This tag was signed with the committer’s  verified signature .

             tonyhutter 
            Tony Hutter

             GPG key ID:  6AD860EED4598027  

             Verified

           Learn about vigilant mode .

               1c702dd            

          Supported Platforms 

  Linux : compatible with 4.18 - 6.19 kernels 
  FreeBSD : compatible with releases starting from 13.3+, 14.0+, 15.0+ 

 Changes 

 Fix available space accounting for special/dedup ( #18222 )  #18190   #18222  
 CI: Test &amp; fix Linux ZFS built-in build  #18234  
 Linux 6.19 compat: in-tree build: fix duplicate GCM assembly functions  #18204   #18224  
 zfs_vnops_os.c: Move a vput() to after zfs_setattr_dir() 
 Fix activating large_microzap on receive  #18143   #18144  
 Improve caching for dbuf prefetches  #18160  
 Flush RRD only when TXGs contain data  #18082   #18138  
 Fix  send:raw  permission for send  -w -I   #18198   #18193  
 ZTS: Fix zed_synchronous_zedlet  #18192   #18196  
 Linux 6.19 compat: META  #18197  
 CI: Test build Lustre against ZFS  #18161  
 Include missing newline in 'man' error  #18183  
 ZTS: update the relevant mmp test cases 
 zhack: add "action idle" subcommand 
 zhack: add -G option to dump debug buffer 
 mmp: claim sequence id before final import 
 mmp: add spa_load_name() for tryimport 
 mmp: move "Starting import" log message 
 mmp: further restrict mmp exported pool check 
 Fix build for Linux 6.18 with PowerPC/RISC-V kernels. ( #18145 ) 
 Linux 6.19: handle --werror with CONFIG_OBJTOOL_WERROR=y  #18152  
 CI: Add Alpine Linux 3.23 runner to the pipeline ( #18087 ) 
 cmd/ztest: avoid  PATH_MAX  stack allocation in  ztest_get_zdb_bin()  ( #18085 ) 
 zed.d, contrib: fix shellcheck errors in scripts 
 zfs_main: cosmetic: add missing flag to the comment for create 
 CI: Test 2.4.x in qemu-test-repo-vm.sh, quick mode  #18070  
 Change shellcheck and checkbashism triggers.  #18000  
 Replace bashisms in ZFS shell function stub.  #18000  
 Make lines stay within 80 char limit.  #18000  
 Add some comments to clarify the mounting of filesystems.  #18000  
 Standardise if/then/else and for/do/done lines.  #18000  
 Add missing initrd config variables.  #18000  
 Remove unnecessary sourcing of variables.  #18000  
 Fix issue with finding degraded pool(s).  #18000  
 Prefix all variables that are local with underscore.  #18000  
 Shell script good practices changes.  #18000  
 Fix potential global variable overwrite.  #18000  
 zpool: fix conflict with -v and -o options 
 CI: Fix qemu-1-setup failure, remove debug stuff  #18166  
 CI: Use Ubuntu mirrors instead of azure ( #18057 )  #18057  
 nvpair: chase FreeBSD xdrproc_t definition  #18154  
 Make sure we can still write data to txg  #18139  
 Lock db_mtx around arc_release() in couple places  #18146  
 remove thread unsafe debug code causing FreeBSD double free panic  #18140  
 FreeBSD: Remove references to DEBUG_VFS_LOCKS  #18136  
 FreeBSD: unbreak compilation on i386  #18096  
 Fix --enable-invariants on FreeBSD  #18131  
 Fix history logging for  zpool create -t   #18118   #18102  
 DDT: Add locking for table ZAP destruction  #18115  
 Add fh_to_parent export definition  #18099  
 spl: remove a _KERNEL check  #18117  
 spl: unexport kstat_proc_entry functions  #18117  
 spl: lift 64-bit math compat out to separate file  #18117  
 spl: remove old atomic lock  #18117  
 icp: emit .note.GNU-stack section for all ELF targets  #18119  
 When receiving a stream with the large block flag, activate feature  #18105  
 Fix zfs_open() to skip zil_async_to_sync() for the snapshot  #18091  
 ZTS: add regression test for  #17180   #18109  
 Rename several printf attributes declarations to  printf   #18095  
 Add handling for STATX_CHANGE_COOKIE  #18097  
 kmem: don't add __GFP_RECLAIMABLE for KM_VMEM allocations  #18107  
 cmd/zfs: clone: accept  -u  to not mount newly created datasets  #18080  
 kmem: don't add __GFP_COMP for KM_VMEM allocations  #18053  
 kmem: don't pass __GFP_HIGHMEM to __vmalloc  #18053  
 Linux 6.19: replace i_state access with inode_state_read_once()  #18053  
 Use reduced precision for scan times  #18061  
 Reduce minimal scrub/resilver times  #18060  
 zdb: Add -O option for -r to specify object-id  #16307  
 Fix rangelock test for growing block size  #18064  
 Bypass snprintf() in quota checks if no quotas set  #18063  
 RAIDZ: Remove some excessive logging  #18059  
 Remove the obsolete FreeBSD 14.2-RELEASE from CI  #18013  
 DDT: Fix compressed entry buffer size  #18055  
 DDT: Add/use zap_lookup_length_uint64_by_dnode()  #18048  
 DDT: Switch to using ZAP _by_dnode() interfaces  #18047  
 DDT: Move logs searches out of the lock  #18044  
 Improve async destroy processing timing  #18043  
 Defer async destroys on pool import  #18033  
 ZTS: Fix zvol_misc_fua SLOG writes check  #18033  
 ZIO: ZIO_STAGE_DDT_WRITE is a blocking stage  #17981  
 ARC: Increase parallel eviction batching  #17970  
 ARC: Pre-convert zfs_arc_min_prefetch_ms  #17965  
 Reduce dataset buffers re-dirtying  #18028  
 CI: Increase setup timeout to 20min, add timestamps  #17714  

       Assets 
       5 

      Loading 

               Uh oh!

                There was an error while loading.  Please reload this page . 

      -->     

                👍 
             22 
    ClosedPort22, chrislongros, Safari77, dimlev, allddd, Nopel2020, mabod, stevleibelt, liberodark, atomjack, and 12 more reacted with thumbs up emoji 
                🎉 
             11 
    aosan, chrislongros, KrzysztofMaciejewski, mclang, dimlev, allddd, furistar, Zaczero, gamanakis, pbek, and firengate reacted with hooray emoji 
                ❤️ 
             15 
    dimlev, allddd, satmandu, atomjack, WillGreen, Ranguvar, kanna5, BirMa, gamanakis, davidetogni, and 5 more reacted with heart emoji 
                🚀 
             8 
    santiagobiali, allixx, danie-dejager, bes-internal, gamanakis, sz4bi, chrislongros, and firengate reacted with rocket emoji 
                👀 
             3 
    xplosionmind, firengate, and chrislongros reacted with eyes emoji 

     All reactions 

                 👍 
                   22 reactions 

                 🎉 
                   11 reactions 

                 ❤️ 
                   15 reactions 

                 🚀 
                   8 reactions 

                 👀 
                   3 reactions 

      42 people reacted 

         zfs-2.3.6 

          zfs-2.3.6  

     Compare 

        Choose a tag to compare

                   Sorry, something went wrong. 

        Filter

      Loading 

                           Sorry, something went wrong. 

               Uh oh!

                There was an error while loading.  Please reload this page . 

               No results found 

                       View all tags 

       tonyhutter 

    released this

        25 Feb 01:52

                zfs-2.3.6

                This tag was signed with the committer’s  verified signature .

             tonyhutter 
            Tony Hutter

             GPG key ID:  6AD860EED4598027  

             Verified

           Learn about vigilant mode .

               c840612            

          Supported Platforms 

  Linux : compatible with 4.18 - 6.19 kernels 
  FreeBSD : compatible with releases starting from 13.3+, 14.0+, 15.0+ 

 Changes 

 CI: Test &amp; fix Linux ZFS built-in build  #18234  
 chksum: run 256K benchmark on demand, preserve chksum_stat_data  #17945   #17946  
 Linux 6.19 compat: META  #18197  
 nvpair: chase FreeBSD xdrproc_t definition  #18154  
 remove thread unsafe debug code causing FreeBSD double free panic  #18140  
 FreeBSD: Remove references to DEBUG_VFS_LOCKS  #18136  
 FreeBSD: Remove HAVE_INLINE_FLSL use  #18004  
 Linux 6.19: replace i_state access with inode_state_read_once()  #18053  
 Linux 6.18: generic_drop_inode() and generic_delete_inode() renamed 
 linux/super: add tunable to request immediate reclaim of unused dentries 
 control its behaviour. By default it continues the traditional  #17746  
 linux/super: add tunable to request immediate reclaim of unused inodes  #17746  
 config: restore ZFS_AC_KERNEL_DENTRY tests  #17621  
 Fix a declaration position of the nth_page.  #18034  
 Fix build for Linux 6.18 with PowerPC/RISC-V kernels. ( #18145 ) 
 Linux 6.19: handle --werror with CONFIG_OBJTOOL_WERROR=y  #18152  
 ZTS: update the relevant mmp test cases 
 zhack: add "action idle" subcommand 
 zhack: add -G option to dump debug buffer 
 mmp: claim sequence id before final import 
 mmp: add spa_load_name() for tryimport 
 mmp: move "Starting import" log message 
 mmp: further restrict mmp exported pool check 
 spa_activity_check: narrow scope of MMP vars  #17551  
 Enable zhack to work properly with 4k sector size disks  #17576  
 Add allocation profile export and zhack subcommand for import  #17576  
 CI: Test build Lustre against ZFS  #18161  
 CI: Fix qemu-1-setup failure, remove debug stuff  #18166  
 CI: Add Alpine Linux 3.23 runner to the pipeline ( #18087 ) 
 ZTS: add mount_loopback to test zfs behind loop dev  #17329  
 CI: Test 2.4.x in qemu-test-repo-vm.sh, quick mode  #18070  
 CI: Add smatch static analysis workflow  #17935  
 ZIO: Set minimum number of free issue threads to 32  #17903  
 Suppress some ashift warnings  #17830  
 Explicit set ashift for non-leaf vdevs  #17826  
 raidz_test: Restore rand_data protection  #17977  
 raidz_test: Fix ZIO ABDs initialization  #17977  
 raidz_test: Set io_offset reasonably  #17977  
 ZFS: Enable more logs for raidz_001_neg  #17977  
 CI: Use Ubuntu mirrors instead of azure ( #18057 )  #18057  
 CI: Change timeout values  #18056  
 CI: zfs-test-packages: Add in new repos  #17956  
 CI: Fix Ubuntu 22.01 rsend failures  #18032  
 CI: exclude signed-off-by/reviewed-by from 72 char limit  #18030  
 Fix HIGHMEM/kmap API violation in zfs_uiomove_bvec_impl()  #15668   #18030  
 Preserve LIFO ordering of kmap ops in abd_raidz_gen_iterate()  #15668   #18030  
 Fix interaction of abd_iter_map()/abd_iter_unmap() with HIGHMEM  #15668   #18030  
 Linux 6.18: META 
 config/kmap_atomic: initialise test data 
 zvol_id: make array length properly known at compile time 
 Linux: bump -std to gnu11 
 sha256_generic: make internal functions a little more private 
 Linux 6.18: namespace type moved to ns_common 
 Linux 6.18: replace write_cache_pages() 
 Linux 6.18: block_device_operations-&gt;getgeo takes struct gendisk* 
 Linux 6.18: convert ida_simple_* calls 
 Linux 6.18: replace nth_page() 
 linux: use sys/stat.h instead of linux/stat.h  #17675  
 config: Fix LLVM-21 -Wuninitialized-const-pointer warning ( #17997 )  #17682   #17684  

       Assets 
       5 

      Loading 

               Uh oh!

                There was an error while loading.  Please reload this page . 

      -->     

                👍 
             7 
    stevleibelt, liberodark, danie-dejager, norohind, little-sparkleeesss, firengate, and lin72h reacted with thumbs up emoji 
                🎉 
             6 
    mclang, dimlev, allddd, IzumiRaine, firengate, and lin72h reacted with hooray emoji 
                ❤️ 
             7 
    dimlev, allddd, francoism90, norohind, xplosionmind, firengate, and lin72h reacted with heart emoji 
                🚀 
             3 
    santiagobiali, firengate, and lin72h reacted with rocket emoji 
                👀 
             2 
    xplosionmind and firengate reacted with eyes emoji 

     All reactions 

                 👍 
                   7 reactions 

                 🎉 
                   6 reactions 

                 ❤️ 
                   7 reactions 

                 🚀 
                   3 reactions 

                 👀 
                   2 reactions 

      14 people reacted 

        Previous   1   2   3   4   5   &hellip;   13   14   Next  

        Previous   Next  

   Footer 

        &copy; 2026 GitHub,&nbsp;Inc.

       Footer navigation 

             Terms 

             Privacy 

               Security 

               Status 

             Community 

             Docs 

             Contact 

      Manage cookies

        Do not share my personal information

    You can’t perform that action at this time.


