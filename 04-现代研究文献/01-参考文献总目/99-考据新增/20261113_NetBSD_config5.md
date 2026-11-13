<!-- 网页存档｜来源：https://man.netbsd.org/config.5｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# config.5 — NetBSD 手册页（config -- kernel configuration file syntax）

## 抓取正文（NAME 至 SEE ALSO 前，节选）

```
CONFIG(5) NetBSD File Formats Manual CONFIG(5)
 NAME 
 config -- kernel configuration file syntax
 DESCRIPTION 
 The kernel configuration file specifies the way the kernel should be com-
 piled by the rest of the toolchain. It is processed by config(1) to pro-
 duce a number of files that will allow the user to compile a possibly
 customised kernel. One compilation can issue several kernel binaries,
 with different root and dump devices configurations, or with full debug-
 ging information.
 This manual page is intended to serve as a complete reference of all
 aspects of the syntax used in the many files processed by config(1) . The
 novice user will prefer looking at the examples given in
 config.samples(5) in order to understand better how the default configu-
 ration can be changed, and how all of its elements interact with each
 other.
 The kernel configuration file actually contains the description of all
 the options, drivers and source files involved in the kernel compilation,
 and the logic that binds them. The machine statement, usually found in
 the std.${MACHINE} file, hides this from the user by automatically
 including all the descriptive files spread all around the kernel source
 tree, the main one being conf/files .
 Thus, the kernel configuration file contains two parts: the description
 of the compilation options, and the selection of those options. However,
 it begins with a small preamble that controls a couple of options of
 config(1) , and a few statements belong to any of the two sections.
 The user controls the options selection part, which is located in a file
 commonly referenced as the main configuration file or simply the kernel 
 configuration file . The developer is responsible for describing the
 options in the relevant files from the kernel source tree.
 Statements are separated by new-line characters. However, new-line char-
 acters can appear in the middle of a given statement, with the value of a
 space character.
 OBJECTS AND NAMES 
 config(1) is a rather complicated piece of software that tries to comply
 with any configuration the user might think of. Quite a few different
 objects are manipulated through the kernel configuration file, therefore
 some definitions are needed.
 Options and attributes 
 The basic objects driving the kernel compilation are options , and are
 called attributes in some contexts. An attribute usually refers to a
 feature a given piece of hardware might have. However, the scope of an
 attribute is rather wide and can just be a place holder to group some
 source files together.
 There is a special class of attribute, named interface attribute , which
 represents a hook that allows a device to attach to (i.e., be a child of)
 another device. An interface attribute has a (possibly empty) list of
 locators to match the actual location of a device. For example, on a PCI
 bus, devices are located by a device number that is fixed by the wiring
 of the motherboard. Additionally, each of those devices can appear
 through several interfaces named functions. A single PCI device entity
 is a unique function number of a given device from the considered PCI
 bus. Therefore, the locators for a pci(4) device are `dev' (for device),
 and `function'.
 A locator can either be a single integer value, or an array of integer
 values. It can have a default value, in which case it can be wildcarded
 with a `?' in the options selection section of the configuration file. A
 single locator definition can take one of the following forms:
 � locator 
 � locator = value 
 � [ locator = value ]
 � locator [ length ]
 � locator [ length ]={ value , ... }
 � [ locator [ length ]={ value , ... }]
 The variants that specify a default value can be enclosed into square
 brackets, in which case the locator will not have to be specified later
 in the options selection section of the configuration file.
 In the options selection section, the locators are specified when declar-
 ing an instance as a space-separated list of ``< locator > < value >''
 where value can be the `?' wildcard if the locator allows it.
 Devices, instances and attachments 
 The main benefit of the kernel configuration file is to allow the user to
 avoid compiling some drivers, and wire down the configuration of some
 others. We have already seen that devices attach to each other through
 interface attributes, but not everything can attach to anything. Fur-
 thermore, the user has the ability to define precise instances for the
 devices. An instance is simply the reality of a device when it is probed
 and attached by the kernel.
 Each driver has a name for its devices. It is called the base device 
 name and is found as `` base '' in this documentation. An instance is the
 concatenation of a base device name and a number. In the kernel configu-
 ration file, instances can sometimes be wildcarded (i.e., the number is
 replaced by a `*' or a `?') in order to match all the possible instances
 of a device.
 The usual `*' becomes a `?' when the instance name is used as an
 attachment name . In the options selection part of the kernel configura-
 tion files, an attachment is an interface attribute concatenated with a
 number or the wildcard `?'.
 Pseudo-devices 
 Some components of the kernel behave like a device although they don't
 have any actual reality in the hardware. For example, this is the case
 for special network devices, such as tun(4) and tap(4) . They are inte-
 grated in the kernel as pseudo-devices , and can have several instances
 and even children, just like normal devices.
 Dependencies 
 The options description part of the kernel configuration file contains
 all the logic that ties the source files together, and it is done first
 through writing down dependencies between config(1) objects.
 In this documentation, the syntax for dependencies is a comma-separated
 list of options and attributes .
 For example, the use of an Ethernet network card requires the source
 files that handle the specificities of that protocol. Therefore, all
 Ethernet network card drivers depend on the `ether' attribute.
 Conditions 
 Finally, source file selection is possible through the help of
 conditionals , referred to as `` condition '' later in this documentation.
 The syntax for those conditions uses well-known operators (`&', `|', and
 `!') to combine options and attributes .
 CONTEXT NEUTRAL STATEMENTS 
 version yyyymmdd 
 Indicates the syntax version used by the rest of the file, or
 until the next version statement. The argument is an ISO
 date. A given config(1) binary might only be compatible with
 a limited range of version numbers.
 include path 
 Includes a file. The path is relative to the top of the ker-
 nel source tree, or the inner-most defined prefix .
 cinclude path 
 Conditionally includes a file. Contrary to include , it will
 not produce an error if the file does not exist. The argu-
 ment obeys the same rules as for include .
 prefix [ path ]
 If path is given, it pushes a new prefix for file , include 
 and cinclude . prefix statements act like a stack, and an
 empty path argument has the latest prefix popped out. The
 path argument is either absolute or relative to the current
 defined prefix, which defaults to the top of the kernel
 source tree.
 buildprefix [ path ]
 If path is given, it pushes a new build prefix for file .
 buildprefix statements act like a stack, and an empty path 
 argument has the latest prefix popped out. The path argument
 is relative to the current defined buildprefix, which
 defaults to the top of the kernel build directory. When pre-
 fix is either absolute or relative out of the kernel source
 tree ( ../ ), buildprefix must be defined.
 ifdef attribute 
 ifndef attribute 
 elifdef attribute 
 elifndef attribute 
 else 
 endif Conditionally interprets portions of the current file. Those
 statements depend on whether or not the given attribute has
 been previously defined, through define or any other state-
 ment that implicitly defines attributes such as device .
 PREAMBLE 
 In addition to include , cinclude , and prefix , the preamble may contain
 the following optional statements:
 build path Defines the build directory for the compilation of the ker-
 nel. It replaces the default of ../compile/ < config-file > and
 is superseded by the -b parameter of config(1) .
 source path 
 Defines the directory in which the source of the kernel
 lives. It replaces the default of ../../../.. and is super-
 seded by the -s parameter of config(1) .
 OPTIONS DESCRIPTION 
 The user will not usually have to use descriptive statements, as they are
 meant for the developer to tie a given piece of code to the rest of the
 kernel. However, third parties may provide sources to add to the kernel
 compilation, and the logic that binds them to the NetBSD kernel will have
 to be added to the user-edited configuration file.
 devclass class 
 Defines a special attribute, named device class . A given
 device cannot belong to more than one device class.
 config(1) translates that property by the rule that a device
 cannot depend on more than one device class, and will prop-
 erly fill the configuration information file it generates
 according to that value.
 defflag [ file ] option [ option [ ... ]] [ : dependencies ]
 Defines a boolean option , that can either be selected or be
 un-selected by the user with the options statement. The
 optional file argument names a header file that will contain
 the C pre-processor definition for the option. If no file
 name is given, it will default to opt_< option >.h. config(1) 
 will always create the header file, but if the user choose
 not to select the option, it will be empty. Several options
 can be combined in one header file, for convenience. The
 header file is created in the compilation directory, making
 them directly accessible by source files.
 defparam [ file ] option [ = value ] [ := lint-value ] [ option [ ... ]]
 [ : dependencies ]
 Behaves like defflag , except the defined option must have a
 value. Such options are not typed: they can have either a
 numeric or a string value. If a value is specified, it is
 treated as a default, and the option is always defined in the
 corresponding header file. If a lint-value is specified,
 config(1) will use it as a value when generating a lint con-
 figuration with -L , and ignore it in all other cases.
 deffs name ... 
 Defines a file-system name . It is no more than a regular
 option, as defined by defflag , but it allows the user to
 select the file-systems to be compiled in the kernel with the
 file-system statement instead of the options statement.
 obsolete defflag [ file ] option ... 
 obsolete defparam [ file ] option ... 
 Those two statements are identical and mark the listed option
 names as obsolete. If the user selects one of the listed
 options in the kernel configuration file, config(1) will emit
 a warning and ignore the option. The optional file argument
 should match the original definition of the option.
 mkflagvar option ... 
 Specifies that an option previously defined with defflag 
 should have a variable created in the kernel Makefile if the
 option is selection with an options statement. No variable
 is created if the option is not selected. The Makefile vari-
 able will have the name KERNEL_OPT_< option > and, because
 options defined with defflag are boolean, the variable will
 have the value ``1''.
 define attribute [ { locators } ] [ : dependencies ]
 Defines an attribute . The locators list is optional, and can
 be empty. If the pair of braces are present, the locator
 list is defined and the declared attribute becomes an
 interface attribute , on which devices can attach.
 maxpartitions number 
 Defines the maximum number of partitions the disklabels for
 the considered architecture can hold. This statement cannot
 be repeated and should only appear in the std.${ARCH} file.
 maxusers min default max 
 Indicates the range of values that will later be accepted by
 config(1) for the maxusers statement in the options selection
 part of the configuration file. In case the user doesn't
 include a maxusers statement in the configuration file, the
 value default is used instead.
 device base [ { locators } ] [ : dependencies ]
 Declares a device of name base . The optional list of
 locators , which can also be empty, indicates the device can
 have children attached directly to it. Internally, that
 means base becomes an interface attribute . For every device
 the user selects, config(1) will add the matching
 CFDRIVER_DECL () statement to ioconf.c . However, it is the
 responsibility of the developer to add the relevant
 CFATTACH_DECL_NEW () line to the source of the device's
 driver.
 attach base at attr [ , attr [ , ... ]] [ with name ] [ : dependencies ]
 All devices must have at least one declared attachment. Oth-
 erwise, they will never be found in the autoconf(9) process.
 The attributes on which an instance of device base can attach
 must be interface attributes, or root in case the device is
 at the top-level, which is usually the case of e.g.,
 mainbus(4) . The instances of device base will later attach
 to one interface attribute from the specified list.
 Different attach definitions must use different names using
 the with option. It is then possible to use the associated
 name as a conditional element in a file statement.
 defpseudo base [ : dependencies ]
 Declares a pseudo-device. Those devices don't need an
 attachment to be declared, they will always be attached if
 they were selected by the user.
 defpseudodev base [ { locators } ] [ : dependencies ]
 Declares a pseudo-device. Those devices don't need an
 attachment to be declared, they will always be attached if
 they were selected by the user. This declaration should be
 used if the pseudodevice uses autoconf(9) functions to manage
 its instances or attach children. As for normal devices, an
 optional list of locators can be defined, which implies an
 interface attribute named base , allowing the pseudo-device to
 have children. Interface attributes can also be defined in
 the dependencies list.
 file path [ condition ] [ needs-count ] [ needs-flag ] [ compile with rule ]
 Adds a source file to the list of files to be compiled into
 the kernel, if the condition is met. The needs-count option
 indicates that the source file requires the number of all the
 countable objects it depends on (through the condition ) to be
 defined. It is usually used for pseudo-devices whose number
 can be specified by the user in the pseudo-device statement.
 Countable objects are devices and pseudo-devices. For the
 former, the count is the number of declared instances. For
 the latter, it is the number specified by the user, default-
 ing to 1. The needs-flag options requires that a flag indi-
 cating the selection of an attribute to be created, but the
 precise number isn't needed. This is useful for source files
 that only partly depend on the attribute, and thus need to
 add pre-processor statements for it.
 Both needs-count and needs-flag produce a header file for
 each of the considered attributes. The name of that file is
 < attribute > .h . It contains one pre-processor definition of
 NATTRIBUTE set to 0 if the attribute was not selected by the
 user, or to the number of instances of the device in the
 needs-count case, or to 1 in all the other cases.
 The rule argument specifies the make(1) rule that will be
 used to compile the source file. If it is not given, the
 default rule for the type of the file will be used. For a
 given file, there can be more than one file statement, but
 not from the same configuration source file, and all later
 statements can only specify a rule argument, and no condition 
 or flags. This is useful when a file needs special consider-
 ation from one particular architecture.
 The path is relative to the top of the kernel source tree, or
 the inner-most defined prefix .
 object path [ condition ]
 Adds an object file to the list of objects to be linked into
 the kernel, if the conditions are met. This is most useful
 for third parties providing binary-only components.
 The path is relative to the top of the kernel source tree, or
 the inner-most defined prefix .
 device-major base [ char number ] [ block number ] [ condition ]
 Associates a major device number with the device base . A
 device can be a character device, a block device, or both,
 and can have different numbers for each. The condition indi-
 cates when the relevant line should be added to ioconf.c , and
 works just like the file statement.
 makeoptions condition name += value [ , condition name += value [ , ... ]]
 Appends to a definition in the generated Makefile .
 This variant of makeoptions belongs to the options descrip-
 tion section. The condition is mandatory and only += can be
 used. Not to be confused with the confusingly similar vari-
 ant of makeoptions used in the selections section.
 OPTIONS SELECTION 
 machine machine [ arch [ subarch [ ... ]]]
 The machine statement should appear first in the kernel con-
 figuration file, with the exception of context-neutral state-
 ments. It makes config(1) include, in that order, the fol-
 lowing files:
 1. conf/files 
 2. arch/${ARCH}/conf/files.${ARCH} if defined
 3. arch/${SUBARCH}/conf/files.${SUBARCH} for each defined
 sub-architecture
 4. arch/${MACHINE}/conf/files.${MACHINE} 
 It also defines an attribute for the machine , the arch and
 each of the subarch .
 ioconf name 
 Used instead of machine in config file snippets for kernel
 modules to generate just the ioconf.c definitions. The gen-
 erated file contains subtrees that start with attachments
 declared with pseudo-root .
 package path 
 Simpler version of:
 prefix DIR
 include FILE
 prefix
 ident string 
 Defines the identification string of the kernel. This state-
 ment is optional, and the name of the main configuration file
 will be used as a default value.
 no ident Deletes any pre-existing identification string of the kernel.
 maxusers number 
 Despite its name, this statement does not limit the maximum
 number of users on the system. There is no such limit, actu-
 ally. However, some kernel structures need to be adjusted to
 accommodate with more users, and the maxusers parameter is
 used for example to compute the maximum number of opened
 files, and the maximum number of processes, which itself is
 used to adjust a few other parameters.
 options name [ = value ][ , name [ = value ][ , ... ]]
 Selects the option name , affecting it a value if the options
 requires it (see the defflag and defparam statements).
 If the option has not been declared in the options descrip-
 tion part of the kernel configuration machinery, it will be
 added as a pre-processor definition when source files are
 compiled. If the option has previously been selected, the
 statement produces a warning, and the new options statement
 replaces the original.
 no options name [ , name [ , ... ]]
 Un-selects the option name . If option name has not previ-
 ously been selected, the statement produces a warning.
 file-system name [ , name [ , ... ]]
 Adds support for all the listed file-systems.
 no file-system name [ , name [ , ... ]]
 Removes support for all the listed file-systems.
 config name root on device [ type fs ] [ dumps on device ]
 Adds name to the list of kernel binaries to compile from the
 configuration file, using the specified root and dump devices
 information.
 Any of the device and fs parameters can be wildcarded with
 `?' to let the kernel automatically discover those values.
 The device can also be specified as a quoted specification
 string. The kernel interprets this string like the console
 input when prompting for a root device. E.g., ``wedge: NAME ''
 specifies a named disk wedge.
 At least one config statement must appear in the configura-
 tion file.
 no config name 
 Removes name from the list of kernel binaries to compile from
 the configuration file.
 pseudo-root instance 
 Used in conjunction with ioconf in kernel modules. Declares
 an instance of a device that serves as the root for a subtree
 described in the module config. The declared instance can
 then be used as an attachment for devices in the kernel mod-
 ule. Multiple such attachment points may be declared in the
 config file. instance may name a device (e.g. `pci*') an
 interface attribute (e.g. `audiobus*')
 instance at attachment [ locator-specifications ... ]
 Configures an instance of a device attaching at a specific
 location in the device tree. All parameters can be wild-
 carded, with a `*' for instance , and a `?' for attachment and
 the locators.
 no instance [ at attachment ]
 Removes the previously configured instances of a device that
 exactly match the given specification. If two instances dif-
 fer only by their locators, both are removed. If no
 attachment is specified, all matching instances are removed.
 If instance is a bare device name, all the previously defined
 instances of that device, regardless of the numbers or wild-
 card, are removed.
 no device at attachment 
 Removes all previously configured instances that attach to
 the specified attachment. If attachment ends with a `*', all
 instances attaching to all the variants of attachment are
 removed.
 pseudo-device device [ number ]
 Adds support for the specified pseudo-device. The parameter
 number is passed to the initialisation function of the
 pseudo-device, usually to indicate how many instances should
 be created. It defaults to 1, and some pseudo-devices ignore
 that parameter.
 no pseudo-device name 
 Removes support for the specified pseudo-device.
 makeoptions name = value [ , name += value [ , ... ]]
 Adds or appends to a definition in the generated Makefile . A
 definition cannot be overridden, it must be removed before it
 can be added again. Optionally, if an option
 makeoptions_< name > is defined with defparam , the value is
 defined as an option too.
 This variant of makeoptions belongs to the options selection
 section. Both = and += can be used. Not to be confused with
 the confusingly similar variant of makeoptions used in the
 descriptions section.
 no makeoptions name [ , name [ , ... ]]
 Removes one or more definitions from the generated Makefile .
 select name 
 Adds the specified attribute and its dependencies.
 no select name 
 Removes the specified attribute and all the attributes which
 depend on it.
 FILES 
 The files are relative to the kernel source top directory (e.g.,
 /usr/src/sys ).
 arch/${MACHINE}/conf/std.${MACHINE}
 Standard configuration for the given architecture. This file
 should always be included.
 arch/${MACHINE}/conf/GENERIC
 Standard options selection file for the given architecture.
 Users should always start changing their main kernel configu-
 ration file by editing a copy of this file.
 conf/files Main options description file.
 EXAMPLES 
 config.samples(5) uses several examples to cover all the practical
 aspects of writing or modifying a kernel configuration file.
```

## 用途注记

Task 8.2 G5-P2 · V41《NetBSD 技术专题史》联网补证（D2 块；官方手册页，collection=NetBSD-current）。
