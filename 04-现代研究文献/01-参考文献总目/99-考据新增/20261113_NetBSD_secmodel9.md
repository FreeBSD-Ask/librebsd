<!-- 网页存档｜来源：https://man.netbsd.org/secmodel.9｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# secmodel.9 — NetBSD 手册页（security model abstraction）

## 抓取正文（NAME 至 SEE ALSO 前，节选）

```
SECMODEL(9) NetBSD Kernel Developer's Manual SECMODEL(9)
 NAME 
 secmodel -- security model development guidelines
 SYNOPSIS 
 #include <secmodel/secmodel.h> 
 int 
 secmodel_register ( secmodel_t *sm , const char *id , const char *name ,
 prop_dictionary_t behavior , secmodel_eval_t sm_eval ,
 secmodel_setinfo_t sm_setinfo );
 int 
 secmodel_deregister ( secmodel_t sm );
 int 
 secmodel_eval ( const char *id , const char *what , void *arg , void *ret );
 static int 
 secmodel_<model>_eval ( const char *what , void *arg , void *ret );
 DESCRIPTION 
 NetBSD provides a complete abstraction of the underlying security model
 used within the operating system through a set of kauth(9) scopes and
 actions. It allows maintaining the traditional security model (based on
 a single super-user and above-super-user restrictions known as
 securelevel ) while decoupling it easily from the system.
 It is possible to modify the security model -- either slightly or using
 an entirely different model -- by attaching/detaching kauth(9) listeners.
 This can be done via the secmodel pluggable framework.
 A secmodel is typically implemented as a kernel module(9) , and can be
 either built-in statically or loaded dynamically at run-time. They base
 their decisions on available information, either directly from kernel,
 from a userspace daemon or even from a centralized network authorization
 server.
 DATA TYPES 
 The secmodel framework offers the following data types:
 secmodel_t An opaque type that describes a secmodel .
 FUNCTIONS 
 secmodel_register ( sm , id , name , behavior , sm_eval , sm_setinfo )
 Register a security model to the secmodel framework and stores
 its description inside sm .
 sm The secmodel description.
 id The unique identifier of the secmodel .
 name The descriptive human-readable name of the secmodel .
 behavior (optional) a prop_dictionary(3) that declares the
 behavior of this security model, like ``copy
 credentials on fork.''
 sm_eval (optional) the secmodel_<model>_eval () callback used
 by a secmodel to register an evaluation routine that
 can be queried later by another security model.
 sm_setinfo (optional) the secmodel_<model>_setinfo () callback
 used by a secmodel to register a routine that per-
 mits other security models to alter the secmodel 
 internals. Currently not implemented.
 secmodel_deregister ( sm )
 Deregister the secmodel described by sm .
 secmodel_eval ( id , what , arg , ret )
 Call the evaluation callback implemented by a security model.
 The return value can be either:
 - zero (0), when the call succeeded.
 - positive, when the error comes directly from the
 secmodel framework.
 - negative, when the error comes from the evaluation
 callback implemented in the targeted security model.
 The value is then implementation-defined.
 id The unique identifier of the targeted secmodel .
 what The query that will be passed down to the targeted
 secmodel .
 arg The arguments passed to the evaluation routine of the tar-
 geted secmodel .
 ret The answer of the evaluation routine.
 RETURN VALUES 
 If successful, functions return 0. Otherwise, the following error values
 are returned:
 [EEXIST] The secmodel is already registered.
 [EFAULT] An invalid address or reference was passed as parameter.
 [EINVAL] An invalid value was passed as parameter.
 [ENOENT] The targeted secmodel does not exist, or it does not implement
 an evaluation callback.
 WRITING A SECURITY MODEL 
 Before writing a security model one should be familiar with the kauth(9) 
 KPI, its limitations, requirements, and so on. See kauth(9) for details.
 A security model is based on the kernel module(9) framework, and can be
 built-in statically inside kernel or loaded dynamically at run-time. It
 is composed of (code-wise) the following components:
 1. module(9) routines, especially a MODULE () declaration and a
 secmodel_<model>_modcmd () function used to start (through
 MODULE_CMD_INIT) and stop (through MODULE_CMD_FINI) the
 secmodel .
 2. Entry routines, named secmodel_<model>_init () and
 secmodel_<model>_start (), used to initialize and start the
 security model, and another function called
 secmodel_<model>_stop (), to stop the security model in case
 the module is to be unloaded.
 3. A sysctl(9) setup routine for the model. This should create
 an entry for the model in the sysctl(7) namespace, under the
 "security.models.<model>" hierarchy.
 All "knobs" for the model should be located under the new
 node, as well as a mandatory name variable, indicating a
 descriptive human-readable name for the model.
 4. A sysctl(9) teardown routine used to destroy the sysctl(7) 
 tree associated with the model.
 5. If the model uses any private data inside credentials, listen-
 ing on the credentials scope, KAUTH_SCOPE_CRED, is required.
 6. Optionally, internal data-structures used by the model. These
 must all be prefixed with "secmodel_<model>_".
 7. A set of listeners, attached to various scopes, used to
 enforce the policy the model intends to implement.
 8. Finally, a security model should register itself after being
 initialized using secmodel_register (), and deregister itself
 before being stopped using secmodel_deregister ().
 EXAMPLES 
 Below is sample code for a kauth(9) network scope listener for the jenna 
 security model. It is used to allow users with a user-id below 1000 to
 bind to reserved ports (for example, 22/TCP):
 int
 secmodel_jenna_network_cb(kauth_cred_t cred, kauth_action_t action,
 void *cookie, void *arg0, void *arg1, void *arg2, void *arg3)
 {
 int result;
 /* Default defer. */
 result = KAUTH_RESULT_DEFER;
 switch (action) {
 case KAUTH_NETWORK_BIND:
 /*
 * We only care about bind(2) requests to privileged
 * ports.
 */
 if ((u_long)arg0 == KAUTH_REQ_NETWORK_BIND_PRIVPORT) {
 /*
 * If the user-id is below 1000, which may
 * indicate a "reserved" user-id, allow the
 * request.
 */
 if (kauth_cred_geteuid(cred) < 1000)
 result = KAUTH_RESULT_ALLOW;
 }
 break;
 }
 return (result);
 }
 There are two main issues, however, with that listener, that you should
 be aware of when approaching to write your own security model:
 1. kauth(9) uses restrictive decisions: if you attach this lis-
 tener on-top of an existing security model, even if it would
 allow the request, it could still be denied.
 2. If you attach this listener as the only listener for the net-
 work scope, there are many other requests that will be
 deferred and, eventually, denied -- which may not be desired.
 That's why before implementing listeners, it should be clear whether they
 implement an entirely new from scratch security model, or add on-top of
 an existing one.
 PROGRAMMING CONSIDERATIONS 
 There are several things you should remember when writing a security
 model:
 - Pay attention to the correctness of your secmodel implementa-
 tion of the desired policy. Certain rights can grant more
 privileges on the system than others, like allowing calls to
 chroot(2) or mounting a file-system.
 - All unhandled requests are denied by default.
 - Authorization requests can not be issued when the kernel is
 holding any locks. This is a requirement from kernel code to
 allow designing security models where the request should be
 dispatched to userspace or a different host.
 - Private listener data -- such as internal data structures -- is
 entirely under the responsibility of the developer. Locking,
 synchronization, and garbage collection are all things that
 kauth(9) does not take care of for you!
 STACKING ON AN EXISTING SECURITY MODEL 
 One of the shortcomings of kauth(9) is that it does not provide any
 stacking mechanism, similar to Linux Security Modules (LSM). This, how-
 ever, is considered a feature in reducing dependency on other people's
 code.
 To properly "stack" minor adjustments on-top of an existing security
 model, one could use one of two approaches:
 1. Register an internal scope for the security model to be used as a
 fall-back when requests are deferred.
 This requires the security model developer to add an internal scope
 for every scope the model partly covers, and register the fall-back
 listeners to it. In the model's listener(s) for the scope, when a
 defer decision is made, the request is passed to be authorized on
 the internal scope, effectively using the fall-back security model.
 Here is example code that implements the above:
 #include <secmodel/suser/suser.h>
 #include <secmodel/securelevel/securelevel.h>
 /*
 * Internal fall-back scope for the network scope.
 */
 #define JENNA_ISCOPE_NETWORK "jenna.iscope.network"
 static kauth_scope_t secmodel_jenna_iscope_network;
 /*
 * Jenna's entry point. Register internal scope for the network scope
 * which we partly cover for fall-back authorization.
 */
 void
 secmodel_jenna_start(void)
 {
 secmodel_jenna_iscope_network = kauth_register_scope(
 JENNA_ISCOPE_NETWORK, NULL, NULL);
 kauth_listen_scope(JENNA_ISCOPE_NETWORK,
 secmodel_suser_network_cb, NULL);
 kauth_listen_scope(JENNA_ISCOPE_NETWORK,
 secmodel_securelevel_network_cb, NULL);
 }
 /*
 * Jenna sits on top of another model, effectively filtering requests.
 * If it has nothing to say, it discards the request. This is a good
 * example for fine-tuning a security model for a special need.
 */
 int
 secmodel_jenna_network_cb(kauth_cred_t cred, kauth_action_t action,
 void *cookie, void *arg0, void *arg1, void *arg2, void *arg3)
 {
 int result;
 /* Default defer. */
 result = KAUTH_RESULT_DEFER;
 switch (action) {
 case KAUTH_NETWORK_BIND:
 /*
 * We only care about bind(2) requests to privileged
 * ports.
 */
 if ((u_long)arg0 == KAUTH_REQ_NETWORK_BIND_PRIVPORT) {
 if (kauth_cred_geteuid(cred) < 1000)
 result = KAUTH_RESULT_ALLOW;
 }
 break;
 }
 /*
 * If we don't have a decision, fall back to the underlying
 * security model.
 */
 if (result == KAUTH_RESULT_DEFER)
 result = kauth_authorize_action(
 secmodel_jenna_iscope_network, cred, action,
 arg0, arg1, arg2, arg3);
 return (result);
 }
 2. If the above is not desired, or cannot be used for any reason, there
 is always the ability to manually call the fall-back routine:
 int
 secmodel_jenna_network_cb(kauth_cred_t cred, kauth_action_t action,
 void *cookie, void *arg0, void *arg1, void *arg2, void *arg3)
 {
 int result;
 /* Default defer. */
 result = KAUTH_RESULT_DEFER;
 switch (action) {
 case KAUTH_NETWORK_BIND:
 /*
 * We only care about bind(2) requests to privileged
 * ports.
 */
 if ((u_long)arg0 == KAUTH_REQ_NETWORK_BIND_PRIVPORT) {
 if (kauth_cred_geteuid(cred) < 1000)
 result = KAUTH_RESULT_ALLOW;
 }
 break;
 }
 /*
 * If we don't have a decision, fall back to the suser
 * security model's behavior.
 */
 if (result == KAUTH_RESULT_DEFER)
 result = secmodel_suser_network_cb(cred, action,
 cookie, arg0, arg1, arg2, arg3);
 return (result);
 }
 AVAILABLE SECURITY MODELS 
 The following is a list of security models available in the default
 NetBSD distribution.
 secmodel_suser(9) 
 Implements the super-user (root) security policy.
 secmodel_securelevel(9) 
 Implements the securelevel security model.
 secmodel_extensions(9) 
 Implements extensions to the traditional 4.4BSD security model,
 like usermounts.
 secmodel_bsd44(9) 
 Traditional NetBSD security model, derived from 4.4BSD.
 secmodel_overlay(9) 
 Sample overlay security model, sitting on-top of
 secmodel_bsd44(9) .
 CODE REFERENCES 
 The core of the secmodel implementation is in sys/secmodel/secmodel.c .
 The header file < secmodel/secmodel.h > describes the public interface.
 To make it easier on developers to write new security models from
 scratch, NetBSD maintains an example secmodel under
 share/examples/secmodel/ .
```

## 用途注记

Task 8.2 G5-P2 · V41《NetBSD 技术专题史》第 9 章安全机制联网补证（D2 块；官方手册页，collection=NetBSD-current）。
