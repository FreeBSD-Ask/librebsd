---
title: "Project_HardenedBSD_Features_Documentation_EBOL_2026-07-22"
source_url: https://hardenedbsd.org/
download_date: 2026-09-07
---

# Project_HardenedBSD_Features_Documentation_EBOL_2026-07-22

来源: https://hardenedbsd.org/

 

 HardenedBSD 

     Skip to main content 

                                    HardenedBSD  

           Verifying Build Artifacts 

              Submitted by  Shawn Webb  on  Fri, 10/27/2023 - 14:43   

        The HardenedBSD build artifacts are signed with an SSH key. SSH keys are used so that artifacts can be validated using only tools included in the base operating system. 
 First, download the SSH public key:  

$ fetch https://installers.hardenedbsd.org/pub/keys/ssh.pub.txt 

 Then download the build artifact. For purposes of this documentation, the 
compressed memstick installation image for HardenedBSD 14-STABLE will be used. 

$ fetch https://installers.hardenedbsd.org/pub/14-stable/amd64/amd64/installer/LATEST/memstick.img.xz 
$ fetch https://installers.hardenedbsd.org/pub/14-stable/amd64/amd64/installer/LATEST/memstick.img.xz.sig 

 Next, generate an `allowed_signers` file which contains the SSH public key:  

$ echo "hbsd-os-build-01 $(cat ssh.pub.txt)" &gt; allowed_signers 

 Now the signature file can be verified: 

$ ssh-keygen -Y verify -f allowed_signers -I hbsd-os-build-01 -n file -s memstick.img.xz.sig &lt; memstick.img.xz 

          Read more  about Verifying Build Artifacts     

           HardenedBSD installers 

              Submitted by  op  on  Tue, 11/03/2015 - 15:32   

                        16-CURRENT

                                                git

                                                git clone  https://rad.hardenedbsd.org/z2HLHXgL1xevBNQsf8BmQW7MpJmtm.git  HardenedBSD-current

                                                Radicle

                                                rad clone rad:z2HLHXgL1xevBNQsf8BmQW7MpJmtm; cd HardenedBSD-src

                                                installers

                                                 https://installers.hardenedbsd.org/pub/current/ 

                        15-STABLE

                                                git

                                                git clone  --single-branch --branch hardened/15-stable/main  https://rad.hardenedbsd.org/z2HLHXgL1xevBNQsf8BmQW7MpJmtm.git  HardenedBSD-15-stable

                                                Radicle

                                                rad clone rad:z2HLHXgL1xevBNQsf8BmQW7MpJmtm; cd HardenedBSD-src; git checkout -b hardened/15-stable/main rad/hardened/15-stable/main

                                                installers

                                                 https://installers.hardenedbsd.org/pub/15-stable/ 

                        PORTS

                                                git

                                                git clone  https://rad.hardenedbsd.org/z2XrdvALg77ycnuZRXgScb27yb3wM.git  HardenedBSD-ports

                                                tar.gz

                                                 fetch -o hardenedbsd-ports.tar.gz  https://rad.hardenedbsd.org/raw/rad:z2XrdvALg77ycnuZRXgScb27yb3wM/archiv... 

          Read more  about HardenedBSD installers     

           HardenedBSD June / July 2026 Status Report 

              Submitted by  Shawn Webb  on  Fri, 07/31/2026 - 19:07   

        This status report covers both June and July 2026. It has been a rather chaotic couple of months for me. 
 I am going to use quite the number of backticks (`) in this status report. I apologize in advance. Think of then as used in Markdown to convey a command or static text. 
 In my  announcement  about force pushing the ports branch: I neglected to clarify the underlying issue and who is impacted. So, a non-malicious less-than-desireable commit made its way to the FreeBSD ports tree. FreeBSD needed to effectively remove the offending commit from the history due to licensing issues (there could be additional factors to which I am not privvy.) Since further commits made it to the tree, this made recovering from that state 
a bit more difficult. 
 This naturally caused a chain reaction downstream for us. In addition to FreeBSD's commits, I had made multiple commits to migrate some of our ports entries to Radicle. This means that, we, too, have to break git commit history. 
 Those downstream from HardenedBSD, even, could be further impacted in a similar fashion. Those impacted primarily are those who maintain their own patches atop our ports tree. HardenedBSD uses a merge-based workflow for bringing in changes from upstream. I recognize that there may be downstream users who use a different workflow. I cannot advise you in that case--I'm most familiar with a merge-based workflow and haven't been sufficiently motivated to try others. 
 What I did was `git reset --hard` the tree back to the HardenedBSD auto-sync merge commit just prior to the offending commit from upstream.  Afterwards, I merged the new freebsd main HEAD commit to our hardenedbsd/main branch. 
 If the last time you updated your ports tree was in the period we accepted the bad commit and our subsequent rollback, but you do NOT carry patches, you might find yourself in a weird state. I'm unsure what to tell users who use `git pull`, since I use a `git fetch &amp;&amp; git merge` model. So, if you use the same, you can simply `git reset --hard rad/hardenedbsd/main` (after fetching `rad` of course). 
 I did run into issues with Radicle: primarily issues with mental models for this kind of situation. Previously, I consdiered the `rad` remote (which Radicle sets up by default) to be okay to use for both fetching and pushing. I used it like I would any normal git remote with push access. 
 Instead, I really should have considered the `rad` remote as read-only: use it only for fetching. I instructed Radicle to create a new remote, pointed to my own Radicle node: `rad remote add --name self $(rad self --did)`. I should push to this new remote, named `self`. For a more nuanced discussion, please see Appendix A below. 
 I haven't forgotten about re-establishing our GitHub mirror. I have other higher priority tasking at the moment, but I just wanted to say it is not forgotten. (And, I'm somewhat glad that our GitHub mirror hasn't been updated, since it hasn't been updated in so long, it didn't see the bad ports commit.) 
  In src:  

 Robert set the default VMSIZE to 80gb for release VM images 
 Shawn Webb: Harden the new security.bsd.allow_tiocsti sysctl node 
 Shawn Webb: rc.conf(5): Support custom values for KLD prohibition value (hbsd_late_kld_prohibition_value, default: 1) 
 Shawn Webb: Harden security.bsd.unprivileged_kenv_read 
 Shawn Webb: Enable stack auto-init to zero for the linuxulator 
 Shawn Webb: jail(8): Use safer memory management APIs 
 Shawn Webb: Enable -ftrivial-var-auto-init=zero for linuxkpi_{hdmi,video} 

		Shawn Webb: HBSD: Harden new sysctl nodes and reorganize PTrace hardening

 Harden vm.phys_fictitious_segs sysctl node with CTLFLAG_ROOTONLY 
 Harden ptrace(PT_SET_SC_RET) in the same fashion as ptrace(PT_SC_REMOTE) 

 Shawn Webb: Enable trivial var auto-init for uvideo(4) 
 Shawn Webb: Enable -ftrivial-var-auto-init=zero for opensolaris.ko 
 Shawn Webb: Garbage collect unused sysctl node 
 Shawn Webb: Harden the GEOM and related control interfaces 

  In ports:  

 Robert added a new port: misc/robert 
 Robert migrated misc/robert to Radicle 
 Robert updated the misc/robert port a few times, currently sitting at version 0.10.0. 
 Robert migrated hardenedbsd/ctrl to Radicle 

		Shawn Webb disabled COMPAT32 for the following ports:

 misc/compat13x 
 misc/compat14x 
 misc/compat15x 

 Shawn Webb fixed the build of graphics/mesa-libs 
 Shawn Webb fixed the build of graphics/mesa-dri 
 Shawn Webb fixed the python version used with net-p2p/reticulum 
 Shawn Webb fixed the build of lang/zig015 (which has, as of this writing, is broken again and on my queue to figure out.) 
 Default devel/wasi-libc to llvm 21 
 Migrate the default llvm version to 21 globally now that 15-STABLE LLVM in base has been updated to llvm 21 
 Update ports-mgmt/pkg to 2.8.1 
 Migrate hardenedbsd/liblattutil to Radicle 
 Migrate hardenedbsd/hbsdmon to Radicle 
 Migrate net/libpushover to Radicle 
 Migrate sysutils/vm-bhyve-hbsd to Radicle and update to 1.7.4 (from 1.5.0) 

  Appendix A  
 Note:  Relevant Zulip discussion  
 It is suggested that if you plan to contribute to a repository, you create a new remote called `self`: `rad remote add --name self $(rad self --did)`. Fetch from `rad`, push to `self`. 
 Treat `rad` as a virtual peer/contributor that tracks the network consensus and `self` is where you do all your own work. 
 Your `self` is what others see when they `rad remote add` you, and vice versa, so they're good for ad-hoc sharing. `rad` looks around at everybody and gathers up the crefs that satisfy sig requirements, so it's where you fetch canonical state from. As a convenience, `rad` also gathers up all the open patches so you don't have to hunt them down in the specific remote they came from. 

          Read more  about HardenedBSD June / July 2026 Status Report     

           HardenedBSD May 2026 Status Report 

              Submitted by  Shawn Webb  on  Mon, 06/01/2026 - 11:16   

        These past two months have been incredibly busy. I didn't publish a status report for April 2026, so this status report will cover that, too. 
 We have mostly completed the migration from our self-hosted GitLab Enterprise instance to Radicle. There's still further work to be done, but the most crucial bits have made it over. We're also still working on ironing out some kinks in learning "the Radicle way". I hope soon to write an article chronicling our journey thus far. 
 I wrote  documentation  on how to bootstrap Radicle's local storage directory with src and ports. If you hope to someday submit issues and/or patches, following these bootstrap instructions will certainly ease the initial pain. I plan to include an export of these Radicle storage bootstrap archives with each official build. The current exports are not signed. I'm going to include the hashes in this signed email. I am working on a candidate patch to our build scripts to perform this export. The archives exported by our builder VMs will be signed with our normal ssh key-based signing method. 
 Fully fixing the release image generation (chiefly fixing generation of disc1.iso) is my first priority. Radicle bootstrap archive generation is my second priority. Radicle integration in our auto-sync is my third priority. Our commit emails came from GitLab. I need to replicate that functionality but with "the Radicle way." For now, I'm performing the sync myself when time permits (usually multiple times per day.) 
 The past couple months have also seen a number of FreeBSD security advisories, so we've published new builds for 16-CURRENT and 15-STABLE. Installer image generation is still somewhat broken, though I've seen some success with memstick.img. I plan to continue working on this until we're 100% fixed, though it will take time. It takes quite the number of hours to test even the smallest of changes. I get pretty much at most two attempts at testing fixes per day. 
 I spent some time studying Reticulum's code. I'm in the process of writing a shim to abstract how its backbone interface implementation uses select and friends. Back when I last looked at it, it required use of epoll. Simultaenously while I was working on that, I did notice the Reticulum project was working on a more portable backbone interface implementation. So I need to restart that research when the time comes. 
 I also spent a little bit of time with hbsdfw. I started work on forward-porting our 14-stable hbsdfw-specific patches to 15-STABLE. Then GitLab died, and my priorities switched to the Radicle migration. So I need to restart this research, too, when the time comes. I think I might target -CURRENT rather than 15-STABLE. That way, we don't have to periodically forward-port patches: we just maintain our patches against the naturally-evvolving hardened/current/master. 
 We completed the ISP account migration. Some pain is left to resolve. We lost support for our tunneled IPv6 (via Hurricane Electric's Tunnel Broker). I need to schedule a part of my day to capture some packets and get on the phone with some tech support folks on the side of both my ISP and HE. Until then, I've removed the AAAA DNS records for the relevant bits of infrastructure. 
  In src:  

 FreeBSD merged llvm 21 into base. We needed to fix one compilation error in HardenedBSD's code caught by llvm 21 
 Replace FreeBSD's README.md with our main wiki-based documentation. 
 Drop the -HBSD suffix in newvers.sh 
 Migrate hbsd-update-build to Radicle 
 Revert the release/ subdirectory to a known good-ish commit. This brought back generation of memstick.img 
 The hardening.pax.kmod_load_disable sysctl node logic was enhanced 
 Fix MK_LLVM_LINK_STATIC_LIBRARIES in src.opts.mk 

  In ports:  

 multimedia/ffmpeg build was fixed 
 ports-mgmt/pkg was updated to 2.7.5 
 ports-mgmt/poudriere-hbsd was updated to 3.4.8 
 A patch was brought in to fix the graphics/hdr_histogram port 
 hardenedbsd/secadm was updated to account for recent MAC hook changes by FreeBSD 
 Some incredibly basic support was implemented for downloading distfiles via Radicle HTTP 
 ports-mgmt/pkg was migrated to Radicle 
 The default llvm version was bumped to 21 for latest 16-CURRENT users 
 ports-mgmt/poudriere-hbsd was migrated to Radicle 
 COMPAT32 was disable for misc/compat{14,15} 
 PIE was disabled for devel/ccache4 
 net-p2p/reticulum was migrated to Radicle 
 hardenedbsd/secadm was migrated to Radicle 

 I want to say a heartfelt thank you to the Radicle folks. You've spent a lot of time in helping out. You didn't have to, but you chose to. And for that, I'm incredibly grateful. It's fun to see the Radicle network evolve. 

==== BEGIN ARTIFACT HASHES ====
$ sha256 ports.tar.xz
SHA256 (ports.tar.xz) = b12f303b96b02b16744c1286868726ab4df43a06f6d28de3c247d4d1598f743b
$ wc -c ports.tar.xz
1472685664 ports.tar.xz
$ sha256 src.tar.xz
SHA256 (src.tar.xz) = 00301a70910127f4fd9564dca1be948e6b9909e864053a76b9197565768345cf
$ wc -c src.tar.xz
2069117660 src.tar.xz
==== END ARTIFACT HASHES ====

          Read more  about HardenedBSD May 2026 Status Report     

           HardenedBSD Officially on Radicle 

              Submitted by  Shawn Webb  on  Sun, 04/26/2026 - 18:19   

        Over the past week, I have been working on bringing HardenedBSD's code repositories on Radicle (as most/all of you already know by now.) We are now at the point where Radicle is usable for us. There are still some sharp edges and some things to work out, but the core functionality is working. 
 I have done some very basic/naive integration in the ports tree for downloading project distfiles from a radicle-httpd instance, similar in scope to USE_GITHUB/USE_GITLAB. This integration still needs a lot of work, but it works well enough to build ports-mgmt/pkg. 
 Radicle does still have some issues with regards to performance. You will want to configure Radicle explicitly to support larger repos. You may need to edit the Radicle config at ~/.radicle/config.json and set the node.limits.fetchPackReceive setting to at least 3GB. 
 You can browse our repos at:  https://radicle.network/nodes/rad.hardenedbsd.org  
 Here are our current repos. I plan to migrate 100% of our repos over time.  secadm will likely be next. 

 rad:z2HLHXgL1xevBNQsf8BmQW7MpJmtm: HardenedBSD-src 
 rad:z2XrdvALg77ycnuZRXgScb27yb3wM: HardenedBSD-ports 
 rad:z3QDZAW2FAfuLvihrhiyDC9fAD8G9: HardenedBSD-pkg 

 These are the steps I've found to be the most reliable: 

 Connect to the HardenedBSD seed vm: 
 rad node connect z6MknwwMpmZET1PcvQjPYhA6hGY7wkYzxb9YtSRh5j2qSQdG@rad.hardenedbsd.org:8776  
 Seed the src tree (repeat for ports): 
 rad seed --from z6MknwwMpmZET1PcvQjPYhA6hGY7wkYzxb9YtSRh5j2qSQdG rad:z2HLHXgL1xevBNQsf8BmQW7MpJmtm  
 Watch ~/.radicle/storage/rad:z2HLHXgL1xevBNQsf8BmQW7MpJmtm.tmp to move to ~/.radicle/storage/rad:z2HLHXgL1xevBNQsf8BmQW7MpJmtm. When this happens, you now have the src tree stored in Radicle's local storage. This will take a long while. Grab a pizza and a root beer. 
 Clone the repo: rad clone rad:z2HLHXgL1xevBNQsf8BmQW7MpJmtm 

 Thank you everyone for your patience, support, and help. This has been a rather wild ride (and it's technically not over). As I make progress on further Radicle integration, I will keep everyone informed. 

          Read more  about HardenedBSD Officially on Radicle     

           HardenedBSD March 2026 Status Report 

              Submitted by  Shawn Webb  on  Sun, 03/29/2026 - 19:15   

        Before I get into the bulk of the status report, I want to give a heads up about ISP changes coming in April 2026. On 23 Apr 2026, I will disconnect internet service at our home and on 24 Apr 2026, internet service will be restored. This is to migrate the account from my personal finances to being under the HardenedBSD Foundation umbrella. This switch will save us $30 USD/month with no changes in bandwidth capacity (symmetric and uncapped 940Mbps). 
 In March 2026, I focused on Reticulum. I started studying its code and started work on the BackboneInterface code, porting it to HardenedBSD. I'm almost complete with my initial work-in-progress patch. 
 I also fixed the build issues for both 15-STABLE and 16-CURRENT. pkgbase support is still broken in our installers, so that will be a topic for this coming quarter. 
 As I write this report on the 29th of March, I am preparing the next quarterly branches and build. 
  In src:  

 Disable retpolines for the bootloader 
 Make sure the kinfo_file struct always gets zeroed 

  In ports:  

 0x1eef's hardenedbsd/sourcezap and hardenedbsd/portzap were updated to 2.3.0. 
 Fix the build of security/snowflake-tor 
 ports-mgmt/pkg was updated to 2.6.2_1 

          Read more  about HardenedBSD March 2026 Status Report     

           HardenedBSD February 2026 Status Report 

              Submitted by  Shawn Webb  on  Sun, 03/01/2026 - 15:37   

        February saw a few changes in HardenedBSD. The majority of my time was spent chasing down the kernel crash in HardenedBSD 15-STABLE that has been plaguing our users. I worked on narrowing down to a three-day window during which a commit was made that causes the crash. 
 As I write this, I'm narrowing that down further to the specific commit. I'm hoping to have this resolved this month. If I find and fix the problem this week, I will create new builds for folks to use. Otherwise, the next scheduled regular quarterly build is for 01 Apr 2026. 
 I appreciate everyone's patience on this. This has been a tricky bug (at times, it fit the description of a "heisenbug"). My spare time is limited (I have a rather large amount of tasks/obligations in everyday ${LIFE} right now), so it has naturally taken a long while to get to this point. 
 While inbetween clients at my dayjob, I have been granted the opportunity to research meshtastic and other mesh networking projects. I'm getting a lot closer in my censorship- and surveillance-resistant mesh network proof-of-concept. I'm now at the point where I need to port Linux-specific code to HardenedBSD. I'm hoping to get normal tcp/ip packets flowing through Reticulum nodes on the inside of six months. This project,  announced  in partnership with Protectli one-and-a-half years ago[1], is starting to move along at a nice pace. I will have more to share on that by the next status report. 
 On Saturday, 28 Feb 2026, I had given my local Hackers N' Hops chapter a little show &amp; tell of Meshtastic, Reticulum, and HardenedBSD. I met with a bunch of really cool hacckers there, and demoed two Reticulum RNodes backed by Reticulum instances on two HardenedBSD laptops. I demoed an exec-over-meshtastic Python script I wrote the day prior. The script is available on Radicle as rad:z44pvAJS7SiQf2CGtpn8hY44GDMyu. 
 Speaking of Radicle, I plan to migrate some of my personal repos away from our self-hosted GitLab and onto the Radicle network. With time, I'm hoping to migrate us completely towards Radicle. Now would be a good time for those who want to contribute to HardenedBSD to start playing around and experimenting with Radicle. 
  In src:  

 Contributor "gmg" hardened the kernel crashdump interface. 
 Opt zlib kernel module into -ftrivial-var-auto-init=zero. 
 bsdinstall(8): Align us more closely with FreeBSD. 

  In ports:  

 net-p2p/reticulum was updated to 1.1.3_2 
 Disable PaX PAGEEXEC and PaX NOEXEC for science/zotero 
 Bring in candidate patch to fix dns/unbound 
 Hook hardenedbsd/ctrl into the build 
 0x1eef added a new port: hardenedbsd/ctrl 
 Bump ports-mgmt/pkg to 3.5.1_1 
 0x1eef updated a port: portzap v2.1.1 
 0x1eef updated a port: sourcezap v2.1.1 

 Once I have figured out what's going on with the 15-STABLE panic and have a proper fix in place, I plan to quickly switch gears towards hbsdfw. I haven't produced a working hbsdfw build in a long time, and it's far past due. After that, I plan to switch right back to the Reticulum research and development. 
 I'll make sure to keep the community informed of the 15-STABLE findings and fixes. 

          Read more  about HardenedBSD February 2026 Status Report     

           HardenedBSD January 2026 Status Report 

              Submitted by  Shawn Webb  on  Mon, 02/02/2026 - 10:44   

        January was a busy month with regards to infrastructure. With both OpenSSL and FreeBSD announcing security fixes, we published new builds just weeks after our new quarterlies dropped. :-) 
 Now that we have the new quarterlies, I plan to "MFC" (old FreeBSD CVS/SVN term for "Merge From Current".) Kids these days call it `git cherry-pick`. MFC is shorter to type, so that's what I'll use. I plan to MFC a number of commits made in hardened/current/master to the hardened/15-stable/main branch this week. 
 I've also received multiple reports of crashes with the 15-STABLE installer. I haven't been able to work on this just yet, but am hoping to in the next two weeks. It is almost my current first priority (the MFCs being first.) I figure that if testing the cherry-picked code proves successful, I could cherry-pick those commits into the relevant quarterly branch. Kind of a "thank you" gesture for being patient with me. :-) 
 I applied relevant updates across the entire infrastructure. I migrated the package repos from being served by a leased server with limited storage to out of my home with plenty of storage. My next goal is to fully automate the build, including syncing. This will mark a good next step to eventually supporting mirroring our package repos. It's much easier to transfer a 140GB package repo over a local 2.5Gbps LAN than a 150Mbps link upstream. 
 I spent some time experimenting with Meshtastic and Reticulum. I'm getting a better picture from a user's perspective on the current state of mesh networking. My next goal is to teach Reticulum's BackboneInterface implementation how to work on FreeBSD/HardenedBSD. 
 Two of the four donated Protectli devices are providing the testing lab for this Meshtastic and Reticulum research. Even though the timeframe has shifted pretty dramatically, I'm grateful for their donations and their support. 
  In src:  

 Opt ipfw into -ftrivial-var-auto-init=zero 
 Remove our old MAC hook for jail/prison destruction (this commit breaks building secadm. I'm waiting on upstream to implement a specific MAC hook, and a patch for (for src, not for secadm) is being worked on by FreeBSD's Kyle Evans.) 
 Disable WITNESS' checking of vnode locks by default. FreeBSD changed some vnode locking semantics and not all filesystem code paths have been updated. As such, we are seeing vnode locking-related panics. I need to get a consequtive block of time to dive in. I'm not a filesytems developer, so this one might take a while to figure out unless someone beats me to it. 
 rc.subr: Ignore required_modules failures in jails (patch submission by leper4{ _AT_ }protnmail.com.) 

  In ports:  

 Bump ftp/curl to 8.18.0
  Update Reticulum to latest git HEAD 
 Disable HARDCFLAGS for devel/avr-gcc 
 Enable ZEROREG for security/openssl3*. This could induce a noticeable performance hit. Please let me know if you have any serious performance issues after this next package build. 

          Read more  about HardenedBSD January 2026 Status Report     

           Welcome 0x1eef (Robert) to the HardenedBSD Development Team! 

              Submitted by  Shawn Webb  on  Wed, 01/21/2026 - 11:24   

        Multi-year HardenedBSD community member  0x1eef (Robert)  has been sending in good quality patches over the past few years. I reached out on behalf of the HardenedBSD Core Team to 0x1eef, asking if he would like to become an official HardenedBSD developer. He accepted! Welcome to the team, 0x1eef! Thank you for the hard work! 
 A little bio about 0x1eef: I’m a systems-focused programmer working primarily with hardenedBSD for the past few years and I generally appreciate (and often use) all flavors of BSD. In the hardenedBSD space I have written portzap(8), sourcezap(8), ctrl(8) among a few other small contributions. 

          Read more  about Welcome 0x1eef (Robert) to the HardenedBSD Development Team!     

           HardenedBSD December 2025 Status Report 

              Submitted by  Shawn Webb  on  Sun, 12/28/2025 - 15:58   

        This status report is going to be a lengthy one. Due to scheduling conflicts, I was unable to get out the November status report, this one will cover the two months November - December 2025. 
 A large portion of my focus has been on the infrastructure, getting a build environment for the recently-created hardened/15-stable/main branch. As discussed in a previous mailing list thread[1], the 14-STABLE build infrastructure has now been migrated to 15-STABLE. We have archived the last 14-STABLE package build, which last completed on 24 Dec 2025. 
 We self-host nearly the entirety of our infrastructure out of my home. We have only one leased server, from the fine folks at NetActuate (previously RootBSD).  This leased server hosts our main website, the hbsd-update build artifacts, and the package repos. Our package repos, naturally, grow over time. Back when we started this, each package repo was at most 75GB in size. Now we're encroaching 135GB. 
 We now have a 30TB NAS in the home-based infrastructure. In order to support the growth, we will be migrating the package repo to the home infra. The package repos themselves have already been migrated. The only thing left to do is adjust the various DNS entries. I plan to do that once we have a usable 15-STABLE package repo. We will update this[2] mailing list thread when the migration has completed, DNS records and all. There will likely be a little blip in HTTPS/TLS connections as we regenerate LetsEncrypt certs. There's a delicate dance here. I plan to keep everyone informed as to when I begin and complete the process. 
 The 14-STABLE build server (which is now being migrated to 15-STABLE) housed two VMs: 

 The OS installer/update build VM. This builds the artifacts published at  https://installers.hardenedbsd.org/  and mirrors. 
 The package build VM. 

 When we deployed that (stupendously) slow server to test its capabilities as a build server for 15-STABLE, we followed the same pattern: two separate VMs. We are going to keep the 15-STABLE OS installer/update build VM on that slow server. We're going to power off the 14-STABLE OS build VM and increase the resources to the package build VM. This means we should be able to decrease the time it takes for that server to produce a usable package repo. Naturally, this comes at a cost of a slow build time for the OS installer/updates, but that process can tolerate **a lot** of slowness. So long as it can produce its build artifacts in less than 48 hours, I'm satisfied. It's the package building (36,000+ packages) that takes the most resources. 
 I spent a lot of time in the ports tree over the past couple months. The focus was on fixing ports broken by the various hardening techniques we employ. The introduction of -Werror=format-security caused a large amount of fallout, which I have been addressing. While addressing those, I figured I might as well fix ports broken by the other techniques. 
 I'm working on enhancing libhbsdcontrol with better error handling. I'm hoping to have that work committed in early January 2026. 
 I'm hoping in January to spend some time on hbsdfw. The VM I've been using to build hbsdfw has been panicking when the Poudriere build finishes when building the hbsdfw packages. In Q1 2026, I plan to migrate hbsdfw from HardenedBSD 14-STABLE to 16-CURRENT. Following the hardened/current/master src branch will lighten my load in maintaining this little hobby subproject. 
 I need to file a bug report upstream in FreeBSD/OpenZFS to track this kernel panic. The panic happens when something during the build checks whether PaX PAGEEXEC is enabled through looking up a filesystem extended attribute. OpenZFS recently changed how filesystem extended attributes work, so it's possible we're hitting a unique edge case. 
 In January, I'm going to get two lab environments set up: 

 Internal Reticulum nodes to test the Reticulum protocol and its potential for use with our censorship- and surveillance-resistant mesh network R&amp;D. 
 Internal Radicle nodes to start concerted testing to eventually replace GitLab with Radicle. 

 I feel somewhat down for not making more progress this year on the censorship- and surveillance-resistant networks. I'm hoping to place more emphasis on this in 2026. 
  In src:  

 Always build elftc-nm and elft-ar 
 TPE: Ensure user-owned vnodes are unwritable 
 ASLR: Use VMFS_NO_SPACE to map the stack 
 Add various C/C++ hardening flags:

 -fno-delete-null-pointer-checks 
 -Werror=format-security 

 Unlock the sound mutex on error 
 Fix branch detection in release 
 Disable SafeStack for the Unbound daemon 
 Some pkgbase-related work 

  In ports (this is gonna be a long list (our longest to date)):  

 Disable LINUX for x11/nvidia-kmod 
 ftp/curl: Fixup .onion patch 
 Add "general compilation hardening" USES 
 Delete unneeded patch for databases/redis 
 Fix archivers/zip 
 Disable hardcflags for devel/m4 
 Disable hardcflags for lang/gcc13 
 Disable HARDCFLAGS for devel/t1lib 
 Fix HARDCFLAGS errors for devel/ctags 
 Disable HARDCFLAGS for archivers/unzip 
 Fix HARDCFLAGS for net-mgmt/libsmi 
 Disable HARDCFLAGS for x11-toolkits/open-motif 
 Disable HARDCFLAGS for devel/expect 
 Fix the devel/ivykis port 
 Fix HARDCFLAGS for multimedia/webcamd 
 Disable HARDCFLAGS for lang/gcc12 
 Disable HardenedBSD features for lang/gcc14 
 Disable HardenedBSD features for lang/gcc15 
 Disable HardenedBSD features for lang/gcc16-devel 
 Fix HARDCFLAGS for multimedia/smpeg 
 Disable HARDCFLAGS for devel/elfutils 
 Fix HARDCFLAGS for converters/recode 
 Disable fortifysource for graphics/netpbm 
 Fix hardcflags for devel/fortytwo-encore 
 Fix HARDCFLAGS for graphics/libvisual04 
 Disable HARDCFLAGS for devel/kBuild 
 Fix HARDCFLAGS for devel/libbegemot 
 Fix HARDCFLAGS for games/pmars-sdl 
 Disable FORTIFYSOURCE for security/signify 
 Disable HARDCFLAGS for mail/mailutils 
 Fix HARDCFLAGS for devel/ta-lib 
 Fix HARDCFLAGS for math/spooles 
 Fix HARDCFLAGS for textproc/wv 
 Fix HARDCFLAGS for databases/sqlite2 
 Disable HARDCFLAGS for graphics/lensfun 
 Fix HARDCFLAGS for devel/rlwrap 
 Disable fortifysource for mail/opensmtpd 
 Fix HARDCFLAGS for x11-toolkits/unique 
 Fix HARDCFLAGS for devel/efivar 
 Fix HARDCFLAGS for lang/f2c 
 Fix HARDCFLAGS for textproc/scim-table-imengine 
 Disable FORTIFYSOURCE and HARDCFLAGS for sysutils/fwupd-efi 
 Fix HARDCFLAGS for games/libmt_client 
 Disable HARDCFLAGS for games/gnugo 
 Fix HARDCFLAGS for comms/rxtx 
 Disable PIE and RELRO for databases/redis 
 Fix build for devel/omniORB 
 Fix build of security/rubygem-bcrypt_pbkdf 
 Fix HARDCFLAGS for math/grace 
 Fix HARDCFLAGS for audio/libbs2b 
 Disable HARDCFLAGS for graphics/plotutils 
 Fix HARDCFLAGS for emulators/libretro-reicast 
 Add -Wformat for HARDCFLAGS 
 Disable HARDCFLAGS for graphics/gracula 
 Fix HARDCFLAGS for mail/spmfilter 
 Add cheat support in games/ioquake3 
 Fix HARDCFLAGS for print/catdvi 
 Fix HARDCFLAGS for graphics/seom 
 Fix HARDCFLAGS for deskutils/presage 
 Fix HARDCFLAGS for graphics/alpng 
 Enable SLH for games/ioquake3 
 Fix -Werror=format-security bug in games/ioquake3 
 Fix HARDCFLAGS for x11-toolkits/fox16 
 Disable HARDCFLAGS for graphics/glslang 
 Re-enable PIE and RELRO for databases/redis 
 Fix HARDCFLAGS for converters/uudeview 
 Fix HARDCFLAGS for textproc/gdome2 
 Disable FORTIFYSOURCE for misc/mbuffer 
 Disable HARDCFLAGS for archivers/unarj 
 Disable FORTIFYSOURCE for misc/amanda-{client,server} 
 Disable FORTIFYSOURCE for net/dante 
 Fix HARDCFLAGS for archivers/sharutils 
 Fix HARDCFLAGS for lang/squeak 
 Disable FORTIFYSOURCE for devel/socket_wrapper 
 Fix HARDCFLAGS for net/pvm 
 Fix HARDCFLAGS for audio/snack 
 Fix HARDCFLAGS for textproc/sgmlformat 
 Fix HARDCFLAGS for cad/iverilog 
 Fix HARDCFLAGS for sysutils/genisoimage 
 Disable HARDCFLAGS for games/libretro-boom3 
 Fix HARDCFLAGS for math/testu01 
 Disable FORTIFYSOURCE for devel/pcc-libs 
 Disable PIE for security/cryptlib 
 Fix HARDCFLAGS for mail/addresses-goodies 
 Fix build of devel/ivykis on 14-stable 
 Disable HARDCFLAGS for security/pgpin 
 (0x1eef) Fix grub2-bhyve build error 
 Disable HARDCFLAGS for devel/cunit 
 Disable FORTIFYSOURCE for editors/dte 
 Disable FORTIFYSOURCE for mail/akpop3d 
 Disable HARDCFLAGS for emulators/x48 
 Fix HARDCFLAGS for net/osrtspproxy 
 Fix HARDCFLAGS for mail/qmailmrtg7 
 Fix HARDCFLAGS for print/transfig 
 Disable PIE for graphics/nsxiv 
 Disable FORTIFYSOURCE for devel/uid_wrapper 
 Disable HARDCFLAGS for devel/cweb 
 Fix FORTIFYSOURCE for multimedia/ffmpeg 
 Fix build of lang/gcc14 
 Fix FORTIFYSOURCE for devel/tex-libtexluajit 
 Disable FORTIFYSOURCE and HARDCFLAGS for security/barnyard2 
 Fix build of lang/gcc12 
 Fix build of databases/arrow 

 [1]:  https://groups.google.com/a/hardenedbsd.org/g/users/c/51IARO8noYo/m/asRq...  
[2]:  https://groups.google.com/a/hardenedbsd.org/g/users/c/G6HbsE8DA5w/m/I4ou...  

          Read more  about HardenedBSD December 2025 Status Report     

 Pages    1   2    3    4    5    6    7    8    9   …   next ›    last »    

       Donate to HardenedBSD 

  GitHub Sponsors  
 Fidelity Charitable  
 BTC: 
1FmbSRvZK4yC1b6aj 
eZWSvYXV2nmvwdWQq 
 BCH: 
1PbGHPPmdNqSmh4L 
3SbvPdaPzSL9kZ5H6f 
 ETH: 
0x9Ea8E44736AC8Ed 
806ef57f7F174a14D93689775 
 LTC: 
LQsiWawAU9saQi4mK 
AyW8LBY97WXaTPi9m

       2021 Donation Status 

Contributions raised: $19,369.02 out of target of $15,000 USD.

       Navigation 

      Home    About HardenedBSD    Latest Builds    HardenedBSD Infrastructure    Mirrors    Easy Feature Comparisons    Donors    HardenedBSD Wiki    Mailing Lists    Roadmap    Meet The Team    Projects    In media    

       Search form 

   Search  

       Links 

     HardenedBSD at GitHub  
 HardenedBSD Signal Group  
 HardenedBSD on Mastodon  
 HardenedBSD via Tor Onion Service v3  
 HardenedBSD on DEF CON Forums  
 HardenedBSD on Matrix  
#hardenedbsd at Libera Chat IRC 

Copyright © 2014-2024 The HardenedBSD Project. 
The mark FreeBSD is a registered trademark of The FreeBSD Foundation and is used by HardenedBSD with the permission of The FreeBSD Foundation.   
Logo proudly designed by  Hyper6 . 
 SoldierX  is a sponsor of the HardenedBSD project.


