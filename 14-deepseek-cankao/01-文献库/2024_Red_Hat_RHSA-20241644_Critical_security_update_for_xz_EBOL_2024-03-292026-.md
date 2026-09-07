---
title: "Hat_RHSA-20241644_Critical_security_update_for_xz_EBOL_2024-03-292026-"
source_url: https://access.redhat.com/errata/RHSA-2024:1644
download_date: 2026-09-07
---

# Hat_RHSA-20241644_Critical_security_update_for_xz_EBOL_2024-03-292026-

来源: https://access.redhat.com/errata/RHSA-2024:1644

 

      -->
      -->
      -->
      -->
      -->
      -->

        -->
        -->
        -->
        -->
        -->
        -->

      Note: Our personalized web services require that your browser be enabled for JavaScript and cookies  

             Skip to navigation 
             Skip to main content 

          Utilities

              Subscriptions

              Downloads

              Red Hat Console

              Get Support

                Subscriptions

                Downloads

                Red Hat Console

                Get Support

                Products

                    Top Products

                        Red Hat Enterprise Linux

                        Red Hat OpenShift

                        Red Hat Ansible Automation Platform

                      All Products

                    Downloads and Containers

                        Downloads

                        Packages

                        Containers

                    Top Resources

                        Documentation

                        Product Life Cycles

                        Product Compliance

                        Errata

                Knowledge

                      Red Hat Knowledge Center

                        Knowledgebase Solutions

                        Knowledgebase Articles

                        Customer Portal Labs

                        Errata

                    Top Product Docs

                        Red Hat Enterprise Linux

                        Red Hat OpenShift

                        Red Hat Ansible Automation Platform

                      All Product Docs

                      Training and Certification

                        About

                        Course Index

                        Certification Index

                        Skill Assessment

                Security

                      Red Hat Product Security Center

                        Security Updates

                        Security Advisories

                        Red Hat CVE Database

                        Errata

                    References

                        Security Bulletins

                        Severity Ratings

                        Security Data

                    Top Resources

                        Security Labs

                        Backporting Policies

                        Security Blog

                Support

                      Red Hat Support

                        Support Cases

                        Troubleshoot

                        Get Support

                        Contact Red Hat Support

                      Red Hat Community Support

                        Customer Portal Community

                        Community Discussions

                        Red Hat Accelerator Program

                                            Contribute

                                        -->

                    Top Resources

                        Product Life Cycles

                        Customer Portal Labs

                        Red Hat JBoss Supported Configurations

                        Red Hat Lightspeed

                                Or  troubleshoot an issue .

                        English

                            Select Your Language

                              English  
                              Français  
                              한국어  
                              日本語  
                              中文 (中国)  

                            Infrastructure and Management

                                    Red Hat Enterprise Linux

                                    Red Hat Satellite

                                    Red Hat Subscription Management

                                    Red Hat Lightspeed

                                    Red Hat Ansible Automation Platform

                            Cloud Computing

                                    Red Hat OpenShift

                                    Red Hat OpenStack Platform

                                    Red Hat OpenShift

                                    Red Hat OpenShift AI

                                    Red Hat OpenShift Dedicated

                                    Red Hat Advanced Cluster Security for Kubernetes

                                    Red Hat Advanced Cluster Management for Kubernetes

                                    Red Hat Quay

                                    Red Hat OpenShift Dev Spaces

                                    Red Hat OpenShift Service on AWS

                            Storage

                                    Red Hat Gluster Storage

                                    Red Hat Hyperconverged Infrastructure

                                    Red Hat Ceph Storage

                                    Red Hat OpenShift Data Foundation

                            Runtimes

                                    Red Hat Runtimes

                                    Red Hat JBoss Enterprise Application Platform

                                    Red Hat Data Grid

                                    Red Hat JBoss Web Server

                                    Red Hat build of Keycloak

                                    Red Hat support for Spring Boot

                                    Red Hat build of Node.js

                                    Red Hat build of Quarkus

                            Integration and Automation

                                    Red Hat Application Foundations

                                    Red Hat Fuse

                                    Red Hat AMQ

                                    Red Hat 3scale API Management

                                All Products

                You are using an unsupported web browser. Update to a supported browser for the best experience.  Read the announcement .

                As of March 1, 2016, the Red Hat Customer Portal will no longer support Internet Explorer 9. See our new  browser support policy  for more information.

           Red Hat Product Errata 
        RHSA-2024:1644 - Security Advisory

 Issued: 
 2024-04-02 
 Updated: 
 2024-04-02 

 RHSA-2024:1644 - Security Advisory 

  Overview  
  Updated Packages  

 Synopsis 
 Important: grafana-pcp security and bug fix update 

 Type/Severity 
 Security Advisory: Important 

 Red Hat Lightspeed patch analysis 

 Identify and remediate systems affected by this advisory. 

 View affected systems 

 Topic 
 An update for grafana-pcp is now available for Red Hat Enterprise Linux 8.   'Red Hat Product Security has rated this update as having a security impact of Important. A Common Vulnerability Scoring System (CVSS) base score, which gives a detailed severity rating, is available for each vulnerability from the CVE link(s) in the References section. 

 Description 
 The Grafana plugin for Performance Co-Pilot includes datasources for scalable time series from pmseries and Redis, live PCP metrics and bpftrace scripts from pmdabpftrace, as well as several dashboards.   Security Fix(es):     golang-fips/openssl: Memory leaks in code encrypting and decrypting RSA payloads (CVE-2024-1394)  
  Bug Fix(es):     TRIAGE CVE-2024-1394 grafana-pcp: golang-fips/openssl: Memory leaks in code encrypting and decrypting RSA payloads (JIRA:RHEL-30544)  

 Solution 
 For details on how to apply this update, which includes the changes described in this advisory, refer to:    https://access.redhat.com/articles/11258  

 Affected Products 

Red Hat Enterprise Linux for x86_64 8 x86_64

Red Hat Enterprise Linux for IBM z Systems 8 s390x

Red Hat Enterprise Linux for Power, little endian 8 ppc64le

Red Hat Enterprise Linux for ARM 64 8 aarch64

Red Hat Enterprise Linux for x86_64 - Extended Life Cycle 8.10 x86_64

Red Hat Enterprise Linux for ARM 64 - Extended Life Cycle 8.10 aarch64

Red Hat Enterprise Linux for Power, little endian - Extended Life Cycle 8.10 ppc64le

Red Hat Enterprise Linux for IBM z Systems - Extended Life Cycle 8.10 s390x

 Fixes 

 BZ - 2262921 
- CVE-2024-1394 golang-fips/openssl: Memory leaks in code encrypting and decrypting RSA payloads

 CVEs 

  CVE-2024-1394  

 References 

  https://access.redhat.com/security/updates/classification/#important  

  Note:

  More recent versions of these packages may be available.
  Click a package name for more details.

 Red Hat Enterprise Linux for x86_64 8 

       SRPM 

          grafana-pcp-5.1.1-2.el8_9.src.rpm

         SHA-256: 25d2d6b0e28cfd3fa8f07d24075a2e0dcac09d581b343468aac2f1d553c4d133 

       x86_64 

          grafana-pcp-5.1.1-2.el8_9.x86_64.rpm

         SHA-256: 8fd0e9918c334229a1a7e4271899a965232e238a2299e0bed73abb08ef8c51e0 

          grafana-pcp-debuginfo-5.1.1-2.el8_9.x86_64.rpm

         SHA-256: f001860343136207b42f842d2b521a29613232dfc9699bafbfd99f23df242f96 

          grafana-pcp-debugsource-5.1.1-2.el8_9.x86_64.rpm

         SHA-256: ca12d31ad699bdc1637a380aed63b0799c8c6068b015dbd7065528e061f76641 

 Red Hat Enterprise Linux for IBM z Systems 8 

       SRPM 

          grafana-pcp-5.1.1-2.el8_9.src.rpm

         SHA-256: 25d2d6b0e28cfd3fa8f07d24075a2e0dcac09d581b343468aac2f1d553c4d133 

       s390x 

          grafana-pcp-5.1.1-2.el8_9.s390x.rpm

         SHA-256: 149e48bc4e5744bf8094def2322faa8403ac9b150c55c09a1e9d744d286eabfb 

          grafana-pcp-debuginfo-5.1.1-2.el8_9.s390x.rpm

         SHA-256: 74a0d985461eb1d5c27bbdd6aecd86082037c82a3f340a42dde445994ebdb28c 

          grafana-pcp-debugsource-5.1.1-2.el8_9.s390x.rpm

         SHA-256: 8503f921bc6c2f735bc3820d09c7551f1ed8767995f9f011b784cfc893d0b432 

 Red Hat Enterprise Linux for Power, little endian 8 

       SRPM 

          grafana-pcp-5.1.1-2.el8_9.src.rpm

         SHA-256: 25d2d6b0e28cfd3fa8f07d24075a2e0dcac09d581b343468aac2f1d553c4d133 

       ppc64le 

          grafana-pcp-5.1.1-2.el8_9.ppc64le.rpm

         SHA-256: 5eef83e67c3f36de6d462874f6c053160d68c2ec407ef62563da7ee39775e67d 

          grafana-pcp-debuginfo-5.1.1-2.el8_9.ppc64le.rpm

         SHA-256: 84aa2ec411b43ada65ee717e2f2950872da383c67189462e9232e10b3c5a4b6a 

          grafana-pcp-debugsource-5.1.1-2.el8_9.ppc64le.rpm

         SHA-256: d827e9b2ab0235e4e990b6131a636e2371e0c815bebe89e89f03a1b75a0b5c96 

 Red Hat Enterprise Linux for ARM 64 8 

       SRPM 

          grafana-pcp-5.1.1-2.el8_9.src.rpm

         SHA-256: 25d2d6b0e28cfd3fa8f07d24075a2e0dcac09d581b343468aac2f1d553c4d133 

       aarch64 

          grafana-pcp-5.1.1-2.el8_9.aarch64.rpm

         SHA-256: 8afbc0dc0c181db5bbd61e1b466b6c9911b9350476a4ef0ef11ccd0f2c919a9e 

          grafana-pcp-debuginfo-5.1.1-2.el8_9.aarch64.rpm

         SHA-256: 354a01bc23b65f8856048b16f0bb476694a425dd1bdb6cdfc9d1d20cf2661129 

          grafana-pcp-debugsource-5.1.1-2.el8_9.aarch64.rpm

         SHA-256: 18274b960aecfcb2968cb43e8e8c3ee41b3734b4dfd41bd2ae716f8157d76347 

 Red Hat Enterprise Linux for x86_64 - Extended Life Cycle 8.10 

       SRPM 

          grafana-pcp-5.1.1-2.el8_9.src.rpm

         SHA-256: 25d2d6b0e28cfd3fa8f07d24075a2e0dcac09d581b343468aac2f1d553c4d133 

       x86_64 

          grafana-pcp-5.1.1-2.el8_9.x86_64.rpm

         SHA-256: 8fd0e9918c334229a1a7e4271899a965232e238a2299e0bed73abb08ef8c51e0 

          grafana-pcp-debuginfo-5.1.1-2.el8_9.x86_64.rpm

         SHA-256: f001860343136207b42f842d2b521a29613232dfc9699bafbfd99f23df242f96 

          grafana-pcp-debugsource-5.1.1-2.el8_9.x86_64.rpm

         SHA-256: ca12d31ad699bdc1637a380aed63b0799c8c6068b015dbd7065528e061f76641 

 Red Hat Enterprise Linux for ARM 64 - Extended Life Cycle 8.10 

       SRPM 

          grafana-pcp-5.1.1-2.el8_9.src.rpm

         SHA-256: 25d2d6b0e28cfd3fa8f07d24075a2e0dcac09d581b343468aac2f1d553c4d133 

       aarch64 

          grafana-pcp-5.1.1-2.el8_9.aarch64.rpm

         SHA-256: 8afbc0dc0c181db5bbd61e1b466b6c9911b9350476a4ef0ef11ccd0f2c919a9e 

          grafana-pcp-debuginfo-5.1.1-2.el8_9.aarch64.rpm

         SHA-256: 354a01bc23b65f8856048b16f0bb476694a425dd1bdb6cdfc9d1d20cf2661129 

          grafana-pcp-debugsource-5.1.1-2.el8_9.aarch64.rpm

         SHA-256: 18274b960aecfcb2968cb43e8e8c3ee41b3734b4dfd41bd2ae716f8157d76347 

 Red Hat Enterprise Linux for Power, little endian - Extended Life Cycle 8.10 

       SRPM 

          grafana-pcp-5.1.1-2.el8_9.src.rpm

         SHA-256: 25d2d6b0e28cfd3fa8f07d24075a2e0dcac09d581b343468aac2f1d553c4d133 

       ppc64le 

          grafana-pcp-5.1.1-2.el8_9.ppc64le.rpm

         SHA-256: 5eef83e67c3f36de6d462874f6c053160d68c2ec407ef62563da7ee39775e67d 

          grafana-pcp-debuginfo-5.1.1-2.el8_9.ppc64le.rpm

         SHA-256: 84aa2ec411b43ada65ee717e2f2950872da383c67189462e9232e10b3c5a4b6a 

          grafana-pcp-debugsource-5.1.1-2.el8_9.ppc64le.rpm

         SHA-256: d827e9b2ab0235e4e990b6131a636e2371e0c815bebe89e89f03a1b75a0b5c96 

 Red Hat Enterprise Linux for IBM z Systems - Extended Life Cycle 8.10 

       SRPM 

          grafana-pcp-5.1.1-2.el8_9.src.rpm

         SHA-256: 25d2d6b0e28cfd3fa8f07d24075a2e0dcac09d581b343468aac2f1d553c4d133 

       s390x 

          grafana-pcp-5.1.1-2.el8_9.s390x.rpm

         SHA-256: 149e48bc4e5744bf8094def2322faa8403ac9b150c55c09a1e9d744d286eabfb 

          grafana-pcp-debuginfo-5.1.1-2.el8_9.s390x.rpm

         SHA-256: 74a0d985461eb1d5c27bbdd6aecd86082037c82a3f340a42dde445994ebdb28c 

          grafana-pcp-debugsource-5.1.1-2.el8_9.s390x.rpm

         SHA-256: 8503f921bc6c2f735bc3820d09c7551f1ed8767995f9f011b784cfc893d0b432 

The Red Hat security contact is  secalert@redhat.com .
More contact details at  https://access.redhat.com/security/team/contact/ .

                     LinkedIn 

                     YouTube 

                     Facebook 

                     X, formerly Twitter 

                 Quick Links 

                      Downloads  
                      Subscriptions  
                      Support Cases  
                      Customer Service  
                      Product Documentation  

                 Help 

                      Contact Us  
                      Customer Portal FAQ  
                      Log-in Assistance  

                 Site Info 

                      Trust Red Hat  
                      Browser Support Policy  
                      Accessibility  
                      Awards and Recognition  
                      Colophon  

                 Related Sites 

                      redhat.com  
                      developers.redhat.com  
                      connect.redhat.com  
                      cloud.redhat.com  

                     Red Hat legal and privacy
                        links 

                          About Red Hat  

                          Jobs  

                          Events  

                          Locations  

                          Contact Red Hat  

                          Red Hat Blog  

                          Inclusion at Red Hat  

                          Cool Stuff Store  

                          Red Hat Summit  

                      © 2026 Red Hat 

                     Red Hat legal and
                        privacy links 

                          Privacy statement  
                          Terms of use  
                          All policies and guidelines  
                          Digital accessibility  


