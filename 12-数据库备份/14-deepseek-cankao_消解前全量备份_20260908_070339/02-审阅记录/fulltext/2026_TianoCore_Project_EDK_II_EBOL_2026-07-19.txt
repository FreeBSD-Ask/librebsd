---
title: "Project_EDK_II_EBOL_2026-07-19"
source_url: https://github.com/tianocore/edk2
download_date: 2026-09-07
---

# Project_EDK_II_EBOL_2026-07-19

来源: https://github.com/tianocore/edk2



   GitHub - tianocore/edk2: EDK II · GitHub 

       Skip to content 

      Navigation Menu                         Sign in                Appearance settings          Platform          AI CODE CREATION            GitHub Copilot  Write better code with AI            GitHub Copilot app  Direct agents from issue to merge              MCP Registry  Integrate external tools          DEVELOPER WORKFLOWS          Actions  Automate any workflow              Codespaces  Instant dev environments              Issues  Plan and track work            Code Review  Manage code changes              Code Quality  Enforce quality at merge          APPLICATION SECURITY          GitHub Advanced Security  Find and fix vulnerabilities            Code security  Secure your code as you build            Secret protection  Stop leaks before they start          EXPLORE     Why GitHub      Documentation          Blog          Changelog          Marketplace          View all features               Solutions          BY COMPANY SIZE     Enterprises      Small and medium teams      Startups      Nonprofits         BY USE CASE     App Modernization      DevSecOps      DevOps      CI/CD      View all use cases               BY INDUSTRY     Healthcare      Financial services      Manufacturing      Government      View all industries                View all solutions               Resources          EXPLORE BY TOPIC     AI      Software Development      DevOps      Security      View all topics               EXPLORE BY TYPE     Customer stories      Events &amp; webinars      Ebooks &amp; reports      Business insights      GitHub Skills             SUPPORT &amp; SERVICES     Documentation          Customer support          Community forum      Trust center      Partners          View all resources               Open Source          COMMUNITY          GitHub Sponsors  Fund open source developers          PROGRAMS     Security Lab          Maintainer Community          GitHub Stars          Archive Program             REPOSITORIES     Topics      Trending      Collections             Enterprise          ENTERPRISE SOLUTIONS          Enterprise platform  AI-powered developer platform          AVAILABLE ADD-ONS          GitHub Advanced Security  Enterprise-grade security features              Copilot for Business  Enterprise-grade AI features            Premium Support  Enterprise-grade 24/7 support             Pricing               Search  /            Sign in       Sign up                Appearance settings          

         You signed in with another tab or window.  Reload  to refresh your session. 
         You signed out in another tab or window.  Reload  to refresh your session. 
         You switched accounts on another tab or window.  Reload  to refresh your session. 

  Dismiss alert 

       {{ message }} 

               Uh oh!

                There was an error while loading.  Please reload this page . 

        tianocore

     / 

       edk2 

       Public 

 Notifications
      You must be signed in to change notification settings 

 Fork
     3.3k 

          Star
            6.2k 

         Code 

         Issues 
           1.2k 

         Pull requests 
           190 

         Discussions 

         Actions 

         Projects 

         Security and quality 
           13 

         Insights 

  Additional navigation options 

          Code

          Issues

          Pull requests

          Discussions

          Actions

          Projects

          Security and quality

          Insights

                                                  master                         Branches            Tags                                          Go to file              Code                 Open more actions menu           Latest commit         History           36,681 Commits                  36,681 Commits       Folders and files      Name    Name     Last commit message      Last commit date                 .azurepipelines                .azurepipelines                              .devcontainer                .devcontainer                              .github                .github                              .mergify                .mergify                              .pytool                .pytool                              ArmPkg                ArmPkg                              ArmPlatformPkg                ArmPlatformPkg                              ArmVirtPkg                ArmVirtPkg                              BaseTools                BaseTools                              Conf                Conf                              CryptoPkg                CryptoPkg                              DynamicTablesPkg                DynamicTablesPkg                              EmbeddedPkg                EmbeddedPkg                              EmulatorPkg                EmulatorPkg                              FatPkg                FatPkg                              FmpDevicePkg                FmpDevicePkg                              IntelFsp2Pkg                IntelFsp2Pkg                              IntelFsp2WrapperPkg                IntelFsp2WrapperPkg                              ManageabilityPkg                ManageabilityPkg                              MdeModulePkg                MdeModulePkg                              MdePkg                MdePkg                              NetworkPkg                NetworkPkg                              OvmfPkg                OvmfPkg                              PcAtChipsetPkg                PcAtChipsetPkg                              PrmPkg                PrmPkg                              RedfishPkg                RedfishPkg                              SecurityPkg                SecurityPkg                              ShellPkg                ShellPkg                              SourceLevelDebugPkg                SourceLevelDebugPkg                              StandaloneMmPkg                StandaloneMmPkg                              TcgTpmPkg                TcgTpmPkg                              UefiCpuPkg                UefiCpuPkg                              UefiPayloadPkg                UefiPayloadPkg                              UnitTestFrameworkPkg                UnitTestFrameworkPkg                              contrib                contrib                              .editorconfig                .editorconfig                              .git-blame-ignore-revs                .git-blame-ignore-revs                              .gitattributes                .gitattributes                              .gitignore                .gitignore                              .gitmodules                .gitmodules                              .mailmap                .mailmap                              .markdownlint.yaml                .markdownlint.yaml                              .markdownlintignore                .markdownlintignore                              BREAKING-CHANGES.md                BREAKING-CHANGES.md                              CONTRIBUTING.md                CONTRIBUTING.md                              License-History.txt                License-History.txt                              License.txt                License.txt                              Maintainers.txt                Maintainers.txt                              ReadMe.rst                ReadMe.rst                              edksetup.bat                edksetup.bat                              edksetup.sh                edksetup.sh                              pip-requirements.txt                pip-requirements.txt                       View all files           Repository files navigation              README            Contributing            License            License           More  items                          EDK II Project        
 A modern, feature-rich, cross-platform firmware development
environment for the UEFI and PI specifications from  www.uefi.org . 

 It is recommended to install this Python version to run the full set of scripts that enable CI in the project. 
 Other Python requirements for build can be found in the  EDK II Build Instructions . 

  Core CI Build Status        

  Host Type &amp; Toolchain 
 Build Status 
 Test Status 
 Code Coverage 

   Windows_VS  

   Ubuntu_GCC  

   Windows_CLANGPDB  

   Ubuntu_CLANGPDB  

   Ubuntu_CLANGDWARF  

  More CI Build information  

  Platform CI Build Status        

  Microsoft Windows Visual Studio (VS)        

  Toolchain 
 CONFIG 
 DEBUG 
 RELEASE 
 NOOPT 

   EmulatorPkg_Win_VS  

 X64 

 X64 FULL 

   OvmfPkg_Win_VS  

 X64 

  Microsoft Windows CLANGPDB        

  Toolchain 
 CONFIG 
 DEBUG 
 RELEASE 
 NOOPT 

   EmulatorPkg_Win_CLANGPDB  

 X64 

 X64 FULL 

  Ubuntu GCC        

  Toolchain 
 CONFIG 
 DEBUG 
 RELEASE 
 NOOPT 

   ArmVirtPkg_Ubuntu_GCC  

 AARCH64 

   EmulatorPkg_Ubuntu_GCC  

 X64 

 X64 FULL 

   OvmfPkg_Ubuntu_GCC  

 X64 

     - EmulatorPkg Ubuntu GCC Segfaults during execution. 

  Ubuntu CLANGPDB        

  Toolchain 
 CONFIG 
 DEBUG 
 RELEASE 
 NOOPT 

   ArmVirtPkg_Ubuntu_CLANGPDB  

 AARCH64 

   OvmfPkg_Ubuntu_CLANGPDB  

 X64 

  Ubuntu CLANGDWARF        

  Toolchain 
 CONFIG 
 DEBUG 
 RELEASE 
 NOOPT 

   ArmVirtPkg_Ubuntu_CLANGDWARF  

 AARCH64 

   EmulatorPkg_Ubuntu_CLANGDWARF  

 X64 

 X64 FULL 

   OvmfPkg_Ubuntu_CLANGDWARF  

 X64 

  More ArmVirtPkg CI Build Information  
  More EmulatorPkg CI Build Information  
  More OvmfPkg CI Build Information  

  License Details        
 The majority of the content in the EDK II open source project uses a
 BSD-2-Clause Plus Patent License . The EDK II open
source project contains the following components that are covered by additional
licenses: 

  BaseTools/Plugin/CodeQL/analyze  
  BaseTools/Source/C/LzmaCompress  
  BaseTools/Source/C/VfrCompile/Pccts  
  CryptoPkg/Library/BaseCryptLib/SysCall/inet_pton.c  
  CryptoPkg/Library/Include/crypto/dso_conf.h  
  CryptoPkg/Library/Include/openssl/opensslconf.h  
  MdeModulePkg/Library/LzmaCustomDecompressLib  
  OvmfPkg  

 The EDK II open source project uses content from upstream projects as git submodules
that are covered by additional licenses. 

  BaseTools/Source/C/BrotliCompress/brotli  
  CryptoPkg/Library/OpensslLib/openssl  
  CryptoPkg/Library/MbedTlsLib/mbedtls  
  MdeModulePkg/Library/BrotliCustomDecompressLib/brotli  
  MdeModulePkg/Universal/RegularExpressionDxe/oniguruma  
  UnitTestFrameworkPkg/Library/CmockaLib/cmocka  
  UnitTestFrameworkPkg/Library/GoogleTestLib/googletest  
  UnitTestFrameworkPkg/Library/SubhookLib/subhook  
  RedfishPkg/Library/JsonLib/jansson  
  MdePkg/Library/BaseFdtLib/libfdt  
  MdePkg/Library/MipiSysTLib/mipisyst  
  SecurityPkg/DeviceSecurity/SpdmLib/libspdm  
  TcgTpmPkg/Library/TpmLib/TPM  

 The EDK II Project is composed of packages. The maintainers for each package
are listed in  Maintainers.txt . 

  Resources        

  TianoCore  
  EDK
II  
  Getting Started with EDK
II  
  Mailing
Lists  
  How To
Contribute  
  Release
Planning  

  Code Contributions        
 To make a contribution to a TianoCore project, follow these steps. 

 Create a change description in the format specified below to 
 use in the source control commit log. 

 Your commit message must include your  Signed-off-by  signature 

 Submit your code to the TianoCore project using the process 
 that the project documents on its web page. If the process is
not documented, then submit the code on development email list
for the project. 

 It is preferred that contributions are submitted using the same 
 copyright license as the base project. When that is not possible,
then contributions using the following licenses can be accepted: 

 Apache License, Version 2.0:  https://opensource.org/license/apache-2-0/  
 BSD (2-clause):  https://opensource.org/license/BSD-2-Clause  
 BSD (3-clause):  https://opensource.org/license/BSD-3-Clause  
 MIT:  https://opensource.org/license/MIT  
 Python-2.0:  https://opensource.org/license/Python-2.0  
 Zlib:  https://opensource.org/license/Zlib  

 For documentation: 

 FreeBSD Documentation License 
  https://www.freebsd.org/copyright/freebsd-doc-license.html  

 Contributions of code put into the public domain can also be accepted. 
 Contributions using other licenses might be accepted, but further
review will be required. 

  Developer Certificate of Origin        
 Your change description should use the standard format for a
commit message, and must include your  Signed-off-by  signature. 
 In order to keep track of who did what, all patches contributed must
include a statement that to the best of the contributor's knowledge
they have the right to contribute it under the specified license. 
 The test for this is as specified in the  Developer's Certificate of
Origin (DCO) 1.1 . The contributor
certifies compliance by adding a line saying 
 Signed-off-by: Developer Name  developer@example.org  
 where  Developer Name  is the contributor's real name, and the email
address is one the developer is reachable through at the time of
contributing. 
 Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.

  Sample Change Description / Commit Message        
 From: Contributor Name &lt;contributor@example.com&gt;
Subject: [Repository/Branch PATCH] Pkg-Module: Brief-single-line-summary

Full-commit-message

Signed-off-by: Contributor Name &lt;contributor@example.com&gt;

  Notes for sample patch email        

 The first line of commit message is taken from the email's subject
line following  [Repository/Branch PATCH] . The remaining portion
of the commit message is the email's content. 
  git format-patch  is one way to create this format 

  Definitions for sample patch email        

  Repository  is the identifier of the repository the patch applies. 
  This identifier should only be provided for repositories other than
 edk2 . For example  edk2-BuildSpecification  or  staging . 

  Branch  is the identifier of the branch the patch applies. This 
  identifier should only be provided for branches other than 

  edk2/master . 
  For example  edk2/UDK2015 , 

  edk2-BuildSpecification/release/1.27 , or 
   staging/edk2-test . 

   Module  is a short identifier for the affected code or
documentation. For example  MdePkg ,  MdeModulePkg/UsbBusDxe ,  Introduction , or 

  EDK II INF File Format . 

   Brief-single-line-summary  is a short summary of the change. 

  The entire first line should be less than ~70 characters. 

  Full-commit-message  a verbose multiple line comment describing 
  the change. Each line should be less than ~70 characters. 

  Signed-off-by  is the contributor's signature identifying them 
  by their real/legal name and their email address. 

  Submodules        
 The current submodules used in EDK II are in  .gitmodules . 
 To get a full, buildable EDK II repository, use following steps of git
command 
  git clone https://github.com/tianocore/edk2.git
 cd  edk2
git submodule update --init
 cd  ..  
 If there are updates for submodules, use the following git commands to get
the latest submodules code. 
   cd  edk2
git pull
git submodule update  
 Note: When cloning submodule repos, '--recursive' option is not
recommended. EDK II itself will not use any code or features from
submodules within the submodules listed above. So using '--recursive' adds a
dependency on being able to reach servers we do not actually want
any code from, as well as needlessly downloading code we will not
use. 

                 About   EDK II        www.tianocore.org/tianocore-wiki.github.io/     Topics    c  firmware  python  uefi    Resources         Readme          License, License licenses found       Contributing         Contributing          Activity          Custom properties     Stars         6.2k  stars    Watchers         277  watching    Forks          3.3k    forks      Report repository       Releases          Packages        Used by        Contributors        Languages                                 

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


