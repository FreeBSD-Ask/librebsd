<!-- 网页存档｜来源：https://man.netbsd.org/cgdconfig.8｜抓取：2026-11-18｜curl 直取成功，HTML 标签剥离与空白归一 -->
# cgdconfig.8 — NetBSD 手册页（configuration utility for the cryptographic disk driver）

## 抓取正文（DESCRIPTION 节选，空白已归一） ``` cgdconfig is used to configure and unconfigure cryptographic disk devices (cgds) ```
## 抓取正文（选项节选，空白已归一） ``` -C Configure all the devices listed in the cgd configuration file. -e Echo the passphrase. -f configfile Specify the configuration file explicitly, rather than using the default configuration file /etc/cgd/cgd.conf . -o outfile When generating a paramsfile , store it in outfile . If -o is not given, any paramsfile content is written to stan- dard output. -k kgmeth Specify the key generation method (default: pkcs5_pbkdf2/sha1). ```
## 抓取正文（Verification Method 节选，空白已归一） ``` The verification method is how cgdconfig determines if the generated key is correct. If the newly configured disk fails to verify, then cgdconfig will regenerate the key and re-configure the device. It only makes sense to specify a verification method if at least one of the key generation methods is error prone, e.g., uses a user-entered passphrase. ```
## 用途注记 Task 8.2 V41—V45 五卷线 · V41《NetBSD 技术专题史》9.7.1（密钥派生与存放——pkcs5_pbkdf2 缺省×paramsfile 存放）与 9.7.3（启动挂钩——-C 组列×口令验证流程）联网补证（D2 块；官方手册页，collection=NetBSD-current）。
