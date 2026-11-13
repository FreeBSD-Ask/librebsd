<!-- 网页存档｜来源：https://man.netbsd.org/bus_space.9｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# bus_space.9 — NetBSD 手册页（bus space access functions）

## 抓取正文（NAME 至 SEE ALSO 前，节选）

```
BUS_SPACE(9) NetBSD Kernel Developer's Manual BUS_SPACE(9)
 NAME 
 bus_space , bus_space_barrier , bus_space_copy_region_1 ,
 bus_space_copy_region_2 , bus_space_copy_region_4 ,
 bus_space_copy_region_8 , bus_space_free , bus_space_handle_is_equal ,
 bus_space_is_equal , bus_space_map , bus_space_mmap , bus_space_peek_1 ,
 bus_space_peek_2 , bus_space_peek_4 , bus_space_peek_8 , bus_space_poke_1 ,
 bus_space_poke_2 , bus_space_poke_4 , bus_space_poke_8 , bus_space_read_1 ,
 bus_space_read_2 , bus_space_read_4 , bus_space_read_8 ,
 bus_space_read_multi_1 , bus_space_read_multi_2 , bus_space_read_multi_4 ,
 bus_space_read_multi_8 , bus_space_read_multi_stream_1 ,
 bus_space_read_multi_stream_2 , bus_space_read_multi_stream_4 ,
 bus_space_read_multi_stream_8 , bus_space_read_region_1 ,
 bus_space_read_region_2 , bus_space_read_region_4 ,
 bus_space_read_region_8 , bus_space_read_region_stream_1 ,
 bus_space_read_region_stream_2 , bus_space_read_region_stream_4 ,
 bus_space_read_region_stream_8 , bus_space_read_stream_1 ,
 bus_space_read_stream_2 , bus_space_read_stream_4 ,
 bus_space_read_stream_8 , bus_space_release , bus_space_reservation_addr ,
 bus_space_reservation_init , bus_space_reservation_size ,
 bus_space_reservation_map , bus_space_reservation_unmap ,
 bus_space_reserve , bus_space_reserve_subregion , bus_space_set_region_1 ,
 bus_space_set_region_2 , bus_space_set_region_4 , bus_space_set_region_8 ,
 bus_space_subregion , bus_space_tag_create , bus_space_tag_destroy ,
 bus_space_unmap , bus_space_vaddr , bus_space_write_1 , bus_space_write_2 ,
 bus_space_write_4 , bus_space_write_8 , bus_space_write_multi_1 ,
 bus_space_write_multi_2 , bus_space_write_multi_4 ,
 bus_space_write_multi_8 , bus_space_write_multi_stream_1 ,
 bus_space_write_multi_stream_2 , bus_space_write_multi_stream_4 ,
 bus_space_write_multi_stream_8 , bus_space_write_region_1 ,
 bus_space_write_region_2 , bus_space_write_region_4 ,
 bus_space_write_region_8 , bus_space_write_region_stream_1 ,
 bus_space_write_region_stream_2 , bus_space_write_region_stream_4 ,
 bus_space_write_region_stream_8 , bus_space_write_stream_1 ,
 bus_space_write_stream_2 , bus_space_write_stream_4 ,
 bus_space_write_stream_8 -- bus space manipulation functions
 SYNOPSIS 
 #include <sys/bus.h> 
 bool 
 bus_space_handle_is_equal ( bus_space_tag_t space ,
 bus_space_handle_t handle1 , bus_space_handle_t handle2 );
 bool 
 bus_space_is_equal ( bus_space_tag_t space1 , bus_space_tag_t space2 );
 void 
 bus_space_release ( bus_space_tag_t t , bus_space_reservation_t *bsr );
 int 
 bus_space_reserve ( bus_space_tag_t t , bus_addr_t bpa , bus_size_t size ,
 int flags , bus_space_reservation_t *bsrp );
 int 
 bus_space_reserve_subregion ( bus_space_tag_t t , bus_addr_t reg_start ,
 bus_addr_t reg_end , bus_size_t size , bus_size_t alignment ,
 bus_size_t boundary , int flags , bus_space_reservation_t *bsrp );
 void 
 bus_space_reservation_init ( bus_space_reservation_t *bsr , bus_addr_t addr ,
 bus_size_t size );
 bus_size_t 
 bus_space_reservation_size ( bus_space_reservation_t *bsr );
 int 
 bus_space_reservation_map ( bus_space_tag_t t ,
 bus_space_reservation_t *bsr , int flags , bus_space_handle_t *bshp );
 void 
 bus_space_reservation_unmap ( bus_space_tag_t t , bus_space_handle_t bsh ,
 bus_size_t size );
 int 
 bus_space_map ( bus_space_tag_t space , bus_addr_t address , bus_size_t size ,
 int flags , bus_space_handle_t *handlep );
 void 
 bus_space_unmap ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t size );
 int 
 bus_space_subregion ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , bus_size_t size , bus_space_handle_t *nhandlep );
 int 
 bus_space_alloc ( bus_space_tag_t space , bus_addr_t reg_start ,
 bus_addr_t reg_end , bus_size_t size , bus_size_t alignment ,
 bus_size_t boundary , int flags , bus_addr_t *addrp ,
 bus_space_handle_t *handlep );
 void 
 bus_space_free ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t size );
 void * 
 bus_space_vaddr ( bus_space_tag_t space , bus_space_handle_t handle );
 paddr_t 
 bus_space_mmap ( bus_space_tag_t space , bus_addr_t addr , off_t off ,
 int prot , int flags );
 int 
 bus_space_tag_create ( bus_space_tag_t obst , uint64_t present ,
 uint64_t extpresent , const struct bus_space_overrides *ov , void *ctx ,
 bus_space_tag_t *bstp );
 void 
 bus_space_tag_destroy ( bus_space_tag_t bst );
 int 
 bus_space_peek_1 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint8_t *datap );
 int 
 bus_space_peek_2 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint16_t *datap );
 int 
 bus_space_peek_4 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint32_t *datap );
 int 
 bus_space_peek_8 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint64_t *datap );
 int 
 bus_space_poke_1 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint8_t data );
 int 
 bus_space_poke_2 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint16_t data );
 int 
 bus_space_poke_4 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint32_t data );
 int 
 bus_space_poke_8 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint64_t data );
 uint8_t 
 bus_space_read_1 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset );
 uint16_t 
 bus_space_read_2 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset );
 uint32_t 
 bus_space_read_4 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset );
 uint64_t 
 bus_space_read_8 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset );
 void 
 bus_space_write_1 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint8_t value );
 void 
 bus_space_write_2 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint16_t value );
 void 
 bus_space_write_4 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint32_t value );
 void 
 bus_space_write_8 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint64_t value );
 void 
 bus_space_barrier ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , bus_size_t length , int flags );
 void 
 bus_space_read_region_1 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint8_t *datap , bus_size_t count );
 void 
 bus_space_read_region_2 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint16_t *datap , bus_size_t count );
 void 
 bus_space_read_region_4 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint32_t *datap , bus_size_t count );
 void 
 bus_space_read_region_8 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint64_t *datap , bus_size_t count );
 void 
 bus_space_read_region_stream_1 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , uint8_t *datap ,
 bus_size_t count );
 void 
 bus_space_read_region_stream_2 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , uint16_t *datap ,
 bus_size_t count );
 void 
 bus_space_read_region_stream_4 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , uint32_t *datap ,
 bus_size_t count );
 void 
 bus_space_read_region_stream_8 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , uint64_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_region_1 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint8_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_region_2 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint16_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_region_4 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint32_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_region_8 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint64_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_region_stream_1 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint8_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_region_stream_2 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint16_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_region_stream_4 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint32_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_region_stream_8 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint64_t *datap ,
 bus_size_t count );
 void 
 bus_space_copy_region_1 ( bus_space_tag_t space ,
 bus_space_handle_t srchandle , bus_size_t srcoffset ,
 bus_space_handle_t dsthandle , bus_size_t dstoffset ,
 bus_size_t count );
 void 
 bus_space_copy_region_2 ( bus_space_tag_t space ,
 bus_space_handle_t srchandle , bus_size_t srcoffset ,
 bus_space_handle_t dsthandle , bus_size_t dstoffset ,
 bus_size_t count );
 void 
 bus_space_copy_region_4 ( bus_space_tag_t space ,
 bus_space_handle_t srchandle , bus_size_t srcoffset ,
 bus_space_handle_t dsthandle , bus_size_t dstoffset ,
 bus_size_t count );
 void 
 bus_space_copy_region_8 ( bus_space_tag_t space ,
 bus_space_handle_t srchandle , bus_size_t srcoffset ,
 bus_space_handle_t dsthandle , bus_size_t dstoffset ,
 bus_size_t count );
 void 
 bus_space_set_region_1 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint8_t value , bus_size_t count );
 void 
 bus_space_set_region_2 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint16_t value , bus_size_t count );
 void 
 bus_space_set_region_4 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint32_t value , bus_size_t count );
 void 
 bus_space_set_region_8 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint64_t value , bus_size_t count );
 void 
 bus_space_read_multi_1 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint8_t *datap , bus_size_t count );
 void 
 bus_space_read_multi_2 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint16_t *datap , bus_size_t count );
 void 
 bus_space_read_multi_4 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint32_t *datap , bus_size_t count );
 void 
 bus_space_read_multi_8 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , uint64_t *datap , bus_size_t count );
 void 
 bus_space_read_multi_stream_1 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , uint8_t *datap ,
 bus_size_t count );
 void 
 bus_space_read_multi_stream_2 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , uint16_t *datap ,
 bus_size_t count );
 void 
 bus_space_read_multi_stream_4 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , uint32_t *datap ,
 bus_size_t count );
 void 
 bus_space_read_multi_stream_8 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , uint64_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_multi_1 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , const uint8_t *datap , bus_size_t count );
 void 
 bus_space_write_multi_2 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , const uint16_t *datap , bus_size_t count );
 void 
 bus_space_write_multi_4 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , const uint32_t *datap , bus_size_t count );
 void 
 bus_space_write_multi_8 ( bus_space_tag_t space , bus_space_handle_t handle ,
 bus_size_t offset , const uint64_t *datap , bus_size_t count );
 void 
 bus_space_write_multi_stream_1 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint8_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_multi_stream_2 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint16_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_multi_stream_4 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint32_t *datap ,
 bus_size_t count );
 void 
 bus_space_write_multi_stream_8 ( bus_space_tag_t space ,
 bus_space_handle_t handle , bus_size_t offset , const uint64_t *datap ,
 bus_size_t count );
 DESCRIPTION 
 The bus_space functions exist to allow device drivers machine-independent
 access to bus memory and register areas. All of the functions and types
 described in this document can be used by including the < sys/bus.h >
 header file.
 Many common devices are used on multiple architectures, but are accessed
 differently on each because of architectural constraints. For instance,
 a device which is mapped in one system's I/O space may be mapped in mem-
 ory space on a second system. On a third system, architectural limita-
 tions might change the way registers need to be accessed (e.g., creating
 a non-linear register space). In some cases, a single driver may need to
 access the same type of device in multiple ways in a single system or
 architecture. The goal of the bus_space functions is to allow a single
 driver source file to manipulate a set of devices on different system
 architectures, and to allow a single driver object file to manipulate a
 set of devices on multiple bus types on a single architecture.
 Not all busses have to implement all functions described in this docu-
 ment, though that is encouraged if the operations are logically supported
 by the bus. Unimplemented functions should cause compile-time errors if
 possible.
 All of the interface definitions described in this document are shown as
 function prototypes and discussed as if they were required to be func-
 tions. Implementations are encouraged to implement prototyped (type-
 checked) versions of these interfaces, but may implement them as macros
 if appropriate. Machine-dependent types, variables, and functions should
 be marked clearly in < machine/bus_defs.h > and in < machine/bus_funcs.h > to
 avoid confusion with the machine-independent types and functions, and, if
 possible, should be given names which make the machine-dependence clear.
 CONCEPTS AND GUIDELINES 
 Bus spaces are described by bus space tags, which can be created only by
 machine-dependent code. A given machine may have several different types
 of bus space (e.g., memory space and I/O space), and thus may provide
 multiple different bus space tags. Individual busses or devices on a
 machine may use more than one bus space tag. For instance, ISA devices
 are given an ISA memory space tag and an ISA I/O space tag. Architec-
 tures may have several different tags which represent the same type of
 space, for instance because of multiple different host bus interface
 chipsets.
 A range in bus space is described by a bus address and a bus size. The
 bus address describes the start of the range in bus space. The bus size
 describes the size of the range in bytes. Busses which are not byte
 addressable may require use of bus space ranges with appropriately
 aligned addresses and properly rounded sizes.
 Access to regions of bus space is facilitated by use of bus space han-
 dles, which are usually created by mapping a specific range of a bus
 space. Handles may also be created by allocating and mapping a range of
 bus space, the actual location of which is picked by the implementation
 within bounds specified by the caller of the allocation function.
 All of the bus space access functions require one bus space tag argument,
 at least one handle argument, and at least one offset argument (a bus
 size). The bus space tag specifies the space, each handle specifies a
 region in the space, and each offset specifies the offset into the region
 of the actual location(s) to be accessed. Offsets are given in bytes,
 though busses may impose alignment constraints. The offset used to
 access data relative to a given handle must be such that all of the data
 being accessed is in the mapped region that the handle describes. Trying
 to access data outside that region is an error.
 Bus space I/O operations on mappings made with BUS_SPACE_MAP_PREFETCHABLE
 or BUS_SPACE_MAP_CACHEABLE may be reordered or combined for performance
 on devices that support it, such as write-combining (a.k.a.
 `prefetchable') graphics framebuffers or cacheable ROM images. The
 bus_space_barrier () function orders reads and writes in prefetchable or
 cacheable mappings relative to other reads and writes in bus spaces.
 Barriers are needed only when prefetchable or cacheable mappings are
 involved:
 � Bus space reads and writes on non-prefetchable, non-cacheable map-
 pings at a single device are totally ordered with one another.
 � Ordering of memory operations on normal memory with bus space I/O for
 triggering DMA or being notified of DMA completion requires
 bus_dmamap_sync(9) .
 People trying to write portable drivers with the bus_space functions
 should try to make minimal assumptions about what the system allows. In
 particular, they should expect that the system requires bus space
 addresses being accessed to be naturally aligned (i.e., base address of
 handle added to offset is a multiple of the access size), and that the
 system does alignment checking on pointers (i.e., pointer to objects
 being read and written must point to properly-aligned data).
 The descriptions of the bus_space functions given below all assume that
 they are called with proper arguments. If called with invalid arguments
 or arguments that are out of range (e.g., trying to access data outside
 of the region mapped when a given handle was created), undefined behav-
 iour results. In that case, they may cause the system to halt, either
 intentionally (via panic) or unintentionally (by causing a fatal trap or
 by some other means) or may cause improper operation which is not immedi-
 ately fatal. Functions which return void or which return data read from
 bus space (i.e., functions which don't obviously return an error code) do
 not fail. They could only fail if given invalid arguments, and in that
 case their behaviour is undefined. Functions which take a count of bytes
 have undefined results if the specified count is zero.
 TYPES 
 Several types are defined in < machine/bus_defs.h > to facilitate use of
 the bus_space functions by drivers.
 bus_addr_t 
 The bus_addr_t type is used to describe bus addresses. It must be an
 unsigned integral type capable of holding the largest bus address usable
 by the architecture. This type is primarily used when mapping and unmap-
 ping bus space.
 bus_size_t 
 The bus_size_t type is used to describe sizes of ranges in bus space. It
 must be an unsigned integral type capable of holding the size of the
 largest bus address range usable on the architecture. This type is used
 by virtually all of the bus_space functions, describing sizes when map-
 ping regions and offsets into regions when performing space access opera-
 tions.
 bus_space_tag_t 
 The bus_space_tag_t type is used to describe a particular bus space on a
 machine. Its contents are machine-dependent and should be considered
 opaque by machine-independent code. This type is used by all bus_space 
 functions to name the space on which they're operating.
 bus_space_handle_t 
 The bus_space_handle_t type is used to describe a mapping of a range of
 bus space. Its contents are machine-dependent and should be considered
 opaque by machine-independent code. This type is used when performing
 bus space access operations.
 bus_space_reservation_t 
 The bus_space_reservation_t type is used to describe a range of bus
 space. It logically consists of a bus_addr_t , the first address in the
 range, and a bus_size_t , the length in bytes of the range. Machine-inde-
 pendent code creates and interrogates a bus_space_reservation_t using a
 constructor, bus_space_reservation_init (), and accessor functions,
 bus_space_reservation_addr () and bus_space_reservation_size ().
 COMPARING BUS SPACE TAGS 
 To check whether or not one bus_space_tag_t refers to the same space as
 another in machine-independent code, do not use either memcmp(9) or the C
 equals (==) operator. Use bus_space_is_equal (), instead.
 MAPPING AND UNMAPPING BUS SPACE 
 Bus space must be mapped before it can be used, and should be unmapped
 when it is no longer needed. The bus_space_map (),
 bus_space_reservation_map (), bus_space_reservation_unmap (), and
 bus_space_unmap () functions provide these capabilities.
 Some drivers need to be able to pass a subregion of already-mapped bus
 space to another driver or module within a driver. The
 bus_space_subregion () function allows such subregions to be created.
 bus_space_map ( space , address , size , flags , handlep )
 The bus_space_map () function exclusively reserves and maps the region of
 bus space named by the space , address , and size arguments. If success-
 ful, it returns zero and fills in the bus space handle pointed to by
 handlep with the handle that can be used to access the mapped region. If
 unsuccessful, it will return non-zero and leave the bus space handle
 pointed to by handlep in an undefined state.
 The flags argument controls how the space is to be mapped. Supported
 flags include:
 BUS_SPACE_MAP_CACHEABLE Try to map the space so that accesses can
 be cached by the system cache. If this
 flag is not specified, the implementation
 should map the space so that it will not
 be cached. This mapping method will only
 be useful in very rare occasions.
 This flag must have a value of 1 on all
 implementations for backward compatibil-
 ity.
 BUS_SPACE_MAP_PREFETCHABLE
 Try to map the space so that accesses can
 be prefetched by the system, and writes
 can be buffered. This means, accesses
 should be side effect free (idempotent).
 The bus_space_barrier () methods will flush
 the write buffer or force actual read
 accesses. If this flag is not specified,
 the implementation should map the space so
 that it will not be prefetched or delayed.
 BUS_SPACE_MAP_LINEAR Try to map the space so that its contents
 can be accessed linearly via normal memory
 access methods (e.g., pointer dereferenc-
 ing and structure accesses). The
 bus_space_vaddr () method can be used to
 obtain the kernel virtual address of the
 mapped range. This is useful when soft-
 ware wants to do direct access to a memory
 device, e.g., a frame buffer. If this
 flag is specified and linear mapping is
 not possible, the bus_space_map () call
 should fail. If this flag is not speci-
 fied, the system may map the space in
 whatever way is most convenient. Use of
 this mapping method is not encouraged for
 normal device access; where linear access
 is not essential, use of the
 bus_space_read/write () methods is strongly
 recommended.
 Not all combinations of flags make sense or are supported with all spa-
 ces. For instance, BUS_SPACE_MAP_CACHEABLE may be meaningless when used
 on many systems' I/O port spaces, and on some systems
 BUS_SPACE_MAP_LINEAR without BUS_SPACE_MAP_PREFETCHABLE may never work.
 When the system hardware or firmware provides hints as to how spaces
 should be mapped (e.g., the PCI memory mapping registers' "prefetchable"
 bit), those hints should be followed for maximum compatibility. On some
 systems, requesting a mapping that cannot be satisfied (e.g., requesting
 a non-prefetchable mapping when the system can only provide a prefetch-
 able one) will cause the request to fail.
 Some implementations may keep track of use of bus space for some or all
 bus spaces and refuse to allow duplicate allocations. This is encouraged
 for bus spaces which have no notion of slot-specific space addressing,
 such as ISA and VME, and for spaces which coexist with those spaces
 (e.g., EISA and PCI memory and I/O spaces co-existing with ISA memory and
 I/O spaces).
 Mapped regions may contain areas for which there is no device on the bus.
 If space in those areas is accessed, the results are bus-dependent.
 bus_space_reservation_map ( space , bsr , flags , handlep )
 The bus_space_reservation_map () function is similar to bus_space_map ()
 but it maps a region of bus space that was previously reserved by a call
 to bus_space_reserve () or bus_space_reserve_subregion (). The region is
 given by the space and bsr arguments. If successful, it returns zero and
 fills in the bus space handle pointed to by handlep with the handle that
 can be used to access the mapped region. If unsuccessful, it will return
 non-zero and leave the bus space handle pointed to by handlep in an unde-
 fined state.
 A region mapped by bus_space_reservation_map () may only be unmapped by a
 call to bus_space_reservation_unmap ().
 For more details, see the description of bus_space_map ().
 bus_space_unmap ( space , handle , size )
 The bus_space_unmap () function unmaps and relinquishes a region of bus
 space reserved and mapped with bus_space_map (). When unmapping a region,
 the size specified should be the same as the size given to
 bus_space_map () when mapping that region.
 After bus_space_unmap () is called on a handle, that handle is no longer
 valid. (If copies were made of the handle they are no longer valid,
 either.)
 This function will never fail. If it would fail (e.g., because of an
 argument error), that indicates a software bug which should cause a
 panic. In that case, bus_space_unmap () will never return.
 bus_space_reservation_unmap ( space , handle , size )
 The bus_space_reservation_unmap () function is similar to
 bus_space_unmap () but it should be called on handles mapped by
 bus_space_reservation_map () and only on such handles. Unlike
 bus_space_unmap (), bus_space_reservation_unmap () does not relinquish
 exclusive use of the bus space named by handle and size ; that is the job
 of bus_space_release ().
 bus_space_subregion ( space , handle , offset , size , nhandlep )
 The bus_space_subregion () function is a convenience function which makes
 a new handle to some subregion of an already-mapped region of bus space.
 The subregion described by the new handle starts at byte offset offset 
 into the region described by handle , with the size given by size , and
 must be wholly contained within the original region.
 If successful, bus_space_subregion () returns zero and fills in the bus
 space handle pointed to by nhandlep . If unsuccessful, it returns non-
 zero and leaves the bus space handle pointed to by nhandlep in an unde-
 fined state. In either case, the handle described by handle remains
 valid and is unmodified.
 When done with a handle created by bus_space_subregion (), the handle
 should be thrown away. Under no circumstances should bus_space_unmap ()
 be used on the handle. Doing so may confuse any resource management
 being done on the space, and will result in undefined behaviour. When
 bus_space_unmap () or bus_space_free () is called on a handle, all subre-
 gions of that handle become invalid.
 bus_space_vaddr ( tag , handle )
 This method returns the kernel virtual address of a mapped bus space if
 and only if it was mapped with the BUS_SPACE_MAP_LINEAR flag. The range
 can be accessed by normal (volatile) pointer dereferences. If mapped
 with the BUS_SPACE_MAP_PREFETCHABLE flag, the bus_space_barrier () method
 must be used to force a particular access order.
 bus_space_mmap ( tag , addr , off , prot , flags )
 This method is used to provide support for memory mapping bus space into
 user applications. If an address space is addressable via volatile
 pointer dereferences, bus_space_mmap () will return the physical address
 (possibly encoded as a machine-dependent cookie) of the bus space indi-
 cated by addr and off . addr is the base address of the device or device
 region, and off is the offset into that region that is being requested.
 If the request is made with BUS_SPACE_MAP_LINEAR as a flag, then a linear
 region must be returned to the caller. If the region cannot be mapped
 (either the address does not exist, or the constraints can not be met),
 bus_space_mmap () returns -1 to indicate failure.
 Note that it is not necessary that the region being requested by a
 bus_space_mmap () call be mapped into a bus_space_handle_t .
 bus_space_mmap () is called once per PAGE_SIZE page in the range. The
 prot argument indicates the memory protection requested by the user
 application for the range.
 bus_space_handle_is_equal ( space , handle1 , handle2 )
 Use bus_space_handle_is_equal () to check whether or not handle1 and
 handle2 refer to regions starting at the same address in the bus space
 space .
 ALLOCATING AND FREEING BUS SPACE 
 Some devices require or allow bus space to be allocated by the operating
 system for device use. When the devices no longer need the space, the
 operating system should free it for use by other devices. The
 bus_space_alloc (), bus_space_free (), bus_space_reserve (),
 bus_space_reserve_subregion (), and bus_space_release () functions provide
 these capabilities. The functions bus_space_reserve (),
 bus_space_reserve_subregion (), and bus_space_release () are not yet avail-
 able on all architectures.
 bus_space_alloc ( space , reg_start , reg_end , size , alignment , boundary ,
 flags , addrp , handlep )
 The bus_space_alloc () function allocates and maps a region of bus space
 with the size given by size , corresponding to the given constraints. If
 successful, it returns zero, fills in the bus address pointed to by addrp 
 with the bus space address of the allocated region, and fills in the bus
 space handle pointed to by handlep with the handle that can be used to
 access that region. If unsuccessful, it returns non-zero and leaves the
 bus address pointed to by addrp and the bus space handle pointed to by
 handlep in an undefined state.
 Constraints on the allocation are given by the reg_start , reg_end ,
 alignment , and boundary parameters. The allocated region will start at
 or after reg_start and end before or at reg_end . The alignment con-
 straint must be a power of two, and the allocated region will start at an
 address that is an even multiple of that power of two. The boundary con-
 straint, if non-zero, ensures that the region is allocated so that first 
 address in region / boundary has the same value as last address in region 
 / boundary . If the constraints cannot be met, bus_space_alloc () will
 fail. It is an error to specify a set of constraints that can never be
 met (for example, size greater than boundary ).
 The flags parameter is the same as the like-named parameter to
 bus_space_map , the same flag values should be used, and they have the
 same meanings.
 Handles created by bus_space_alloc () should only be freed with
 bus_space_free (). Trying to use bus_space_unmap () on them causes unde-
 fined behaviour. The bus_space_subregion () function can be used on han-
 dles created by bus_space_alloc ().
 bus_space_reserve ( t , bpa , size , flags , bsrp )
 The bus_space_reserve () function reserves, for the caller's exclusive
 use, size bytes starting at the address bpa in the space referenced by t .
 bus_space_reserve () does not map the space. The caller should use
 bus_space_reservation_map () to map the reservation. flags contains a
 hint how the caller may map the reservation, later. Whenever possible,
 callers should pass the same flags to bus_space_reserve () as they will
 pass to bus_space_reservation_map () to map the reservation.
 On success, bus_space_reserve () records the reservation at bsrp and
 returns 0. On failure, bsrp is undefined, and bus_space_reserve ()
 returns a non-zero error code. Possible error codes include
 ENOMEM There was not sufficient bus space at bpa to satisfy
 the request.
 EOPNOTSUPP bus_space_reserve () is not supported on this architec-
 ture, or flags was incompatible with the bus space rep-
 resented by t .
 bus_space_reserve_subregion ( t , reg_start , reg_end , size , alignment ,
 boundary , flags , bsrp )
 The bus_space_reserve_subregion () function reserves, for the caller's
 exclusive use, size bytes in the space referenced by t . The parameters
 reg_start , reg_end , alignment , boundary , and flags each work alike to the
 bus_space_alloc () parameters of the same names.
 On success, bus_space_reserve_subregion () records the reservation at bsrp 
 and returns 0. On failure, bsrp is undefined, and
 bus_space_reserve_subregion () returns a non-zero error code. Possible
 error codes include
 ENOMEM There was not sufficient bus space at bpa to satisfy
 the request.
 EOPNOTSUPP bus_space_reserve () is not supported on this architec-
 ture, or flags was incompatible with the bus space rep-
 resented by t .
 bus_space_release ( t , bsr )
 The bus_space_release () function releases the bus space bsr in t that was
 previously reserved by bus_space_reserve () or
 bus_space_reserve_subregion ().
 If bus_space_release () is called on a reservation that has been mapped by
 bus_space_reservation_map () without subsequently being unmapped, the
 behavior of the system is undefined.
 bus_space_free ( space , handle , size )
 The bus_space_free () function unmaps and frees a region of bus space
 mapped and allocated with bus_space_alloc (). When unmapping a region,
 the size specified should be the same as the size given to
 bus_space_alloc () when allocating the region.
 After bus_space_free () is called on a handle, that handle is no longer
 valid. (If copies were made of the handle, they are no longer valid,
 either.)
 This function will never fail. If it would fail (e.g., because of an
 argument error), that indicates a software bug which should cause a
 panic. In that case, bus_space_free () will never return.
 READING AND WRITING SINGLE DATA ITEMS 
 The simplest way to access bus space is to read or write a single data
 item. The bus_space_read_N () and bus_space_write_N () families of func-
 tions provide the ability to read and write 1, 2, 4, and 8 byte data
 items on busses which support those access sizes.
 bus_space_read_1 ( space , handle , offset )
 bus_space_read_2 ( space , handle , offset )
 bus_space_read_4 ( space , handle , offset )
 bus_space_read_8 ( space , handle , offset )
 The bus_space_read_N () family of functions reads a 1, 2, 4, or 8 byte
 data item from the offset specified by offset into the region specified
 by handle of the bus space specified by space . The location being read
 must lie within the bus space region specified by handle .
 For portability, the starting address of the region specified by handle 
 plus the offset should be a multiple of the size of data item being read.
 On some systems, not obeying this requirement may cause incorrect data to
 be read, on others it may cause a system crash.
 Read operations done by the bus_space_read_N () functions may be executed
 out of order with respect to other read and write operations if either
 are on prefetchable or cacheable mappings unless order is enforced by use
 of the bus_space_barrier () function.
 These functions will never fail. If they would fail (e.g., because of an
 argument error), that indicates a software bug which should cause a
 panic. In that case, they will never return.
 bus_space_write_1 ( space , handle , offset , value )
 bus_space_write_2 ( space , handle , offset , value )
 bus_space_write_4 ( space , handle , offset , value )
 bus_space_write_8 ( space , handle , offset , value )
 The bus_space_write_N () family of functions writes a 1, 2, 4, or 8 byte
 data item to the offset specified by offset into the region specified by
 handle of the bus space specified by space . The location being written
 must lie within the bus space region specified by handle .
 For portability, the starting address of the region specified by handle 
 plus the offset should be a multiple of the size of data item being writ-
 ten. On some systems, not obeying this requirement may cause incorrect
 data to be written, on others it may cause a system crash.
 Write operations done by the bus_space_write_N () functions may be exe-
 cuted out of order with respect to other read and write operations if
 either are on prefetchable or cacheable mappings unless order is enforced
 by use of the bus_space_barrier () function.
 These functions will never fail. If they would fail (e.g., because of an
 argument error), that indicates a software bug which should cause a
 panic. In that case, they will never return.
 PROBING BUS SPACE FOR HARDWARE WHICH MAY NOT RESPOND 
 One problem with the bus_space_read_N () and bus_space_write_N () family of
 functions is that they provide no protection against exceptions which can
 occur when no physical hardware or device responds to the read or write
 cycles. In such a situation, the system typically would panic due to a
 kernel-mode bus error. The bus_space_peek_N () and bus_space_poke_N ()
 family of functions provide a mechanism to handle these exceptions grace-
 fully without the risk of crashing the system.
 As with bus_space_read_N () and bus_space_write_N (), the peek and poke
 functions provide the ability to read and write 1, 2, 4, and 8 byte data
 items on busses which support those access sizes. All of the constraints
 specified in the descriptions of the bus_space_read_N () and
 bus_space_write_N () functions also apply to bus_space_peek_N () and
 bus_space_poke_N ().
 The return value indicates the outcome of the peek or poke operation. A
 return value of zero implies that a hardware device is responding to the
 operation at the specified offset in the bus space. A non-zero return
 value indicates that the kernel intercepted a hardware exception (e.g.,
 bus error) when the peek or poke operation was attempted. Note that some
 busses are incapable of generating exceptions when non-existent hardware
 is accessed. In such cases, these functions will always return zero and
 the value of the data read by bus_space_peek_N () will be unspecified.
 Finally, it should be noted that at this time the bus_space_peek_N () and
 bus_space_poke_N () functions are not re-entrant and should not, there-
 fore, be used from within an interrupt service routine. This constraint
 may be removed at some point in the future.
 bus_space_peek_1 ( space , handle , offset , datap )
 bus_space_peek_2 ( space , handle , offset , datap )
 bus_space_peek_4 ( space , handle , offset , datap )
 bus_space_peek_8 ( space , handle , offset , datap )
 The bus_space_peek_N () family of functions cautiously read a 1, 2, 4, or
 8 byte data item from the offset specified by offset in the region speci-
 fied by handle of the bus space specified by space . The data item read
 is stored in the location pointed to by datap . It is permissible for
 datap to be NULL, in which case the data item will be discarded after
 being read.
 bus_space_poke_1 ( space , handle , offset , value )
 bus_space_poke_2 ( space , handle , offset , value )
 bus_space_poke_4 ( space , handle , offset , value )
 bus_space_poke_8 ( space , handle , offset , value )
 The bus_space_poke_N () family of functions cautiously write a 1, 2, 4, or
 8 byte data item specified by value to the offset specified by offset in
 the region specified by handle of the bus space specified by space .
 BARRIERS 
 Devices that support prefetchable (also known as `write-combining') or
 cacheable I/O may be mapped with BUS_SPACE_MAP_PREFETCHABLE or
 BUS_SPACE_MAP_CACHEABLE for higher performance by allowing bus space read
 and write operations to be reordered, fused, torn, and/or cached by the
 system.
 When a driver requires ordering, e.g. to write to a command ring in bus
 space and then update the command ring pointer, the bus_space_barrier ()
 function enforces it.
 bus_space_barrier ( space , handle , offset , length , flags )
 The bus_space_barrier () function enforces ordering of bus space read and
 write operations for the specified subregion (described by the offset and
 length parameters) of the region named by handle in the space named by
 space .
 The flags argument controls what types of operations are to be ordered.
 Supported flags are:
 BUS_SPACE_BARRIER_READ Guarantee that any program-prior bus space
 read on any bus space has returned data
 from the device or memory before any pro-
 gram-later bus space read, bus space
 write, or memory access via
 bus_space_vaddr (), on the specified range
 in the given bus space.
 This functions similarly to
 membar_acquire(3) , but additionally orders
 bus space I/O which membar_ops(3) may not.
 BUS_SPACE_BARRIER_WRITE Guarantee that any program-prior bus space
 read, bus space write, or memory access
 via bus_space_vaddr (), on the specified
 range in the given bus space, has com-
 pleted before any program-later bus space
 write on any bus space.
 This functions similarly to
 membar_release(3) , but additionally orders
 bus space I/O which membar_ops(3) may not.
 BUS_SPACE_BARRIER_READ | BUS_SPACE_BARRIER_WRITE
 Guarantee that any program-prior bus space
 read, bus space write, or memory access
 via bus_space_vaddr () on any bus space has
 completed before any program-later bus
 space read, bus space write, or memory
 access via bus_space_vaddr () on any bus
 space.
 Note that this is independent of the spec-
 ified bus space and range.
 This functions similarly to
 membar_sync(3) , but additionally orders
 bus space I/O which membar_ops(3) may not.
 This combination is very unusual, and
 often much more expensive; most drivers do
 not need it.
 Example: Consider a command ring in bus space with a command ring pointer
 register, and a response ring in bus space with a response ring pointer
 register.
 error = bus_space_map(sc->sc_regt, ..., 0, &sc->sc_regh);
 if (error)
 ...
 error = bus_space_map(sc->sc_memt, ..., BUS_SPACE_MAP_PREFETCHABLE,
 &sc->sc_memh);
 if (error)
 ...
 To submit a command (assuming there is space in the ring), first write it
 out and then update the pointer:
 i = sc->sc_nextcmdslot;
 bus_space_write_4(sc->sc_memt, sc->sc_memh, CMDSLOT(i), cmd);
 bus_space_write_4(sc->sc_memt, sc->sc_memh, CMDSLOT(i) + 4, arg1);
 bus_space_write_4(sc->sc_memt, sc->sc_memh, CMDSLOT(i) + 8, arg2);
 ...
 bus_space_write_4(sc->sc_memt, sc->sc_memh, CMDSLOT(i) + 4*n, argn);
 bus_space_barrier(sc->sc_memt, sc->sc_memh, CMDSLOT(i), 4*n,
 BUS_SPACE_BARRIER_WRITE);
 bus_space_write_4(sc->sc_regt, sc->sc_regh, CMDPTR, i);
 sc->sc_nextcmdslot = (i + n + 1) % sc->sc_ncmdslots;
 To obtain a response, read the pointer first and then the ring data:
 ptr = bus_space_read_4(sc->sc_regt, sc->sc_regh, RESPPTR);
 while ((i = sc->sc_nextrespslot) != ptr) {
 bus_space_barrier(sc->sc_memt, sc->sc_memh, RESPSLOT(i), 4,
 BUS_SPACE_BARRIER_READ);
 status = bus_space_read_4(sc->sc_memt, sc->sc_memh, RESPSLOT(i));
 handle_response(status);
 sc->sc_nextrespslot = (i + 1) % sc->sc_nrespslots;
 }
 REGION OPERATIONS 
 Some devices use buffers which are mapped as regions in bus space.
 Often, drivers want to copy the contents of those buffers to or from mem-
 ory, e.g., into mbufs which can be passed to higher levels of the system
 or from mbufs to be output to a network. In order to allow drivers to do
 this as efficiently as possible, the bus_space_read_region_N () and
 bus_space_write_region_N () families of functions are provided.
 Drivers occasionally need to copy one region of a bus space to another,
 or to set all locations in a region of bus space to contain a single
 value. The bus_space_copy_region_N () family of functions and the
 bus_space_set_region_N () family of functions allow drivers to perform
 these operations.
 bus_space_read_region_1 ( space , handle , offset , datap , count )
 bus_space_read_region_2 ( space , handle , offset , datap , count )
 bus_space_read_region_4 ( space , handle , offset , datap , count )
 bus_space_read_region_8 ( space , handle , offset , datap , count )
 The bus_space_read_region_N () family of functions reads count 1, 2, 4, or
 8 byte data items from bus space starting at byte offset offset in the
 region specified by handle of the bus space specified by space and writes
 them into the array specified by datap . Each successive data item is
 read from an offset 1, 2, 4, or 8 bytes after the previous data item
 (depending on which function is used). All locations being read must lie
 within the bus space region specified by handle .
 For portability, the starting address of the region specified by handle 
 plus the offset should be a multiple of the size of data items being read
 and the data array pointer should be properly aligned. On some systems,
 not obeying these requirements may cause incorrect data to be read, on
 others it may cause a system crash.
 Read operations done by the bus_space_read_region_N () functions may be
 executed in any order. They may also be executed out of order with
 respect to other read and write operations if either are on prefetchable
 or cacheable mappings unless order is enforced by use of the
 bus_space_barrier () function. There is no way to insert barriers between
 reads of individual bus space locations executed by the
 bus_space_read_region_N () functions.
 These functions will never fail. If they would fail (e.g., because of an
 argument error), that indicates a software bug which should cause a
 panic. In that case, they will never return.
 bus_space_write_region_1 ( space , handle , offset , datap , count )
 bus_space_write_region_2 ( space , handle , offset , datap , count )
 bus_space_write_region_4 ( space , handle , offset , datap , count )
 bus_space_write_region_8 ( space , handle , offset , datap , count )
 The bus_space_write_region_N () family of functions reads count 1, 2, 4,
 or 8 byte data items from the array specified by datap and writes them to
 bus space starting at byte offset offset in the region specified by
 handle of the bus space specified by space . Each successive data item is
 written to an offset 1, 2, 4, or 8 bytes after the previous data item
 (depending on which function is used). All locations being written must
 lie within the bus space region specified by handle .
 For portability, the starting address of the region specified by handle 
 plus the offset should be a multiple of the size of data items being
 written and the data array pointer should be properly aligned. On some
 systems, not obeying these requirements may cause incorrect data to be
 written, on others it may cause a system crash.
 Write operations done by the bus_space_write_region_N () functions may be
 executed in any order. They may also be executed out of order with
 respect to other read and write operations if either are on prefetchable
 or cacheable mappings unless order is enforced by use of the
 bus_space_barrier () function. There is no way to insert barriers between
 writes of individual bus space locations executed by the
 bus_space_write_region_N () functions.
 These functions will never fail. If they would fail (e.g., because of an
 argument error), that indicates a software bug which should cause a
 panic. In that case, they will never return.
 bus_space_copy_region_1 ( space , srchandle , srcoffset , dsthandle ,
 dstoffset , count )
 bus_space_copy_region_2 ( space , srchandle , srcoffset , dsthandle ,
 dstoffset , count )
 bus_space_copy_region_4 ( space , srchandle , srcoffset , dsthandle ,
 dstoffset , count )
 bus_space_copy_region_8 ( space , srchandle , srcoffset , dsthandle ,
 dstoffset , count )
 The bus_space_copy_region_N () family of functions copies count 1, 2, 4,
 or 8 byte data items in bus space from the area starting at byte offset
 srcoffset in the region specified by srchandle of the bus space specified
 by space to the area starting at byte offset dstoffset in the region
 specified by dsthandle in the same bus space. Each successive data item
 read or written has an offset 1, 2, 4, or 8 bytes after the previous data
 item (depending on which function is used). All locations being read and
 written must lie within the bus space region specified by their respec-
 tive handles.
 For portability, the starting addresses of the regions specified by each
 handle plus its respective offset should be a multiple of the size of
 data items being copied. On some systems, not obeying this requirement
 may cause incorrect data to be copied, on others it may cause a system
 crash.
 Read and write operations done by the bus_space_copy_region_N () functions
 may be executed in any order. They may also be executed out of order
 with respect to other read and write operations if either are on
 prefetchable or cacheable mappings unless order is enforced by use of the
 bus_space_barrier () function. There is no way to insert barriers between
 reads or writes of individual bus space locations executed by the
 bus_space_copy_region_N () functions.
 Overlapping copies between different subregions of a single region of bus
 space are handled correctly by the bus_space_copy_region_N () functions.
 These functions will never fail. If they would fail (e.g., because of an
 argument error), that indicates a software bug which should cause a
 panic. In that case, they will never return.
 bus_space_set_region_1 ( space , handle , offset , value , count )
 bus_space_set_region_2 ( space , handle , offset , value , count )
 bus_space_set_region_4 ( space , handle , offset , value , count )
 bus_space_set_region_8 ( space , handle , offset , value , count )
 The bus_space_set_region_N () family of functions writes the given value 
 to count 1, 2, 4, or 8 byte data items in bus space starting at byte off-
 set offset in the region specified by handle of the bus space specified
 by space . Each successive data item has an offset 1, 2, 4, or 8 bytes
 after the previous data item (depending on which function is used). All
 locations being written must lie within the bus space region specified by
 handle .
 For portability, the starting address of the region specified by handle 
 plus the offset should be a multiple of the size of data items being
 written. On some systems, not obeying this requirement may cause incor-
 rect data to be written, on others it may cause a system crash.
 Write operations done by the bus_space_set_region_N () functions may be
 executed in any order. They may also be executed out of order with
 respect to other read and write operations if either are on prefetchable
 or cacheable mappings unless order is enforced by use of the
 bus_space_barrier () function. There is no way to insert barriers between
 writes of individual bus space locations executed by the
 bus_space_set_region_N () functions.
 These functions will never fail. If they would fail (e.g., because of an
 argument error), that indicates a software bug which should cause a
 panic. In that case, they will never return.
 READING AND WRITING A SINGLE LOCATION MULTIPLE TIMES 
 Some devices implement single locations in bus space which are to be read
 or written multiple times to communicate data, e.g., some ethernet
 devices' packet buffer FIFOs. In order to allow drivers to manipulate
 these types of devices as efficiently as possible, the
 bus_space_read_multi_N () and bus_space_write_multi_N () families of func-
 tions are provided.
 bus_space_read_multi_1 ( space , handle , offset , datap , count )
 bus_space_read_multi_2 ( space , handle , offset , datap , count )
 bus_space_read_multi_4 ( space , handle , offset , datap , count )
 bus_space_read_multi_8 ( space , handle , offset , datap , count )
 The bus_space_read_multi_N () family of functions reads count 1, 2, 4, or
 8 byte data items from bus space at byte offset offset in the region
 specified by handle of the bus space specified by space and writes them
 into the array specified by datap . Each successive data item is read
 from the same location in bus space. The location being read must lie
 within the bus space region specified by handle .
 For portability, the starting address of the region specified by handle 
 plus the offset should be a multiple of the size of data items being read
 and the data array pointer should be properly aligned. On some systems,
 not obeying these requirements may cause incorrect data to be read, on
 others it may cause a system crash.
 Read operations done by the bus_space_read_multi_N () functions may be
 executed out of order with respect to other read and write operations if
 the latter are on prefetchable or cacheable mappings unless order is
 enforced by use of the bus_space_barrier () function.
 bus_space_read_multi_N () makes no sense itself on prefetchable or
 cacheable mappings.
 These functions will never fail. If they would fail (e.g., because of an
 argument error), that indicates a software bug which should cause a
 panic. In that case, they will never return.
 bus_space_write_multi_1 ( space , handle , offset , datap , count )
 bus_space_write_multi_2 ( space , handle , offset , datap , count )
 bus_space_write_multi_4 ( space , handle , offset , datap , count )
 bus_space_write_multi_8 ( space , handle , offset , datap , count )
 The bus_space_write_multi_N () family of functions reads count 1, 2, 4, or
 8 byte data items from the array specified by datap and writes them into
 bus space at byte offset offset in the region specified by handle of the
 bus space specified by space . Each successive data item is written to
 the same location in bus space. The location being written must lie
 within the bus space region specified by handle .
 For portability, the starting address of the region specified by handle 
 plus the offset should be a multiple of the size of data items being
 written and the data array pointer should be properly aligned. On some
 systems, not obeying these requirements may cause incorrect data to be
 written, on others it may cause a system crash.
 Write operations done by the bus_space_write_multi_N () functions may be
 executed out of order with respect to other read and write operations if
 the latter are on prefetchable or cacheable mappings unless order is
 enforced by use of the bus_space_barrier () function.
 bus_space_write_multi_N () makes no sense itself on prefetchable or
 cacheable mappings.
 These functions will never fail. If they would fail (e.g., because of an
 argument error), that indicates a software bug which should cause a
 panic. In that case, they will never return.
 STREAM FUNCTIONS 
 Most of the bus_space functions imply a host byte-order and a bus byte-
 order and take care of any translation for the caller. In some cases,
 however, hardware may map a FIFO or some other memory region for which
 the caller may want to use multi-word, yet untranslated access. Access
 to these types of memory regions should be with the
 bus_space_*_stream_N () functions.
 bus_space_read_stream_1 ( space , handle , offset )
 bus_space_read_stream_2 ( space , handle , offset )
 bus_space_read_stream_4 ( space , handle , offset )
 bus_space_read_stream_8 ( space , handle , offset )
 bus_space_read_multi_stream_1 ( space , handle , offset , datap , count )
 bus_space_read_multi_stream_2 ( space , handle , offset , datap , count )
 bus_space_read_multi_stream_4 ( space , handle , offset , datap , count )
 bus_space_read_multi_stream_8 ( space , handle , offset , datap , count )
 bus_space_read_region_stream_1 ( space , handle , offset , datap , count )
 bus_space_read_region_stream_2 ( space , handle , offset , datap , count )
 bus_space_read_region_stream_4 ( space , handle , offset , datap , count )
 bus_space_read_region_stream_8 ( space , handle , offset , datap , count )
 bus_space_write_stream_1 ( space , handle , offset , value )
 bus_space_write_stream_2 ( space , handle , offset , value )
 bus_space_write_stream_4 ( space , handle , offset , value )
 bus_space_write_stream_8 ( space , handle , offset , value )
 bus_space_write_multi_stream_1 ( space , handle , offset , datap , count )
 bus_space_write_multi_stream_2 ( space , handle , offset , datap , count )
 bus_space_write_multi_stream_4 ( space , handle , offset , datap , count )
 bus_space_write_multi_stream_8 ( space , handle , offset , datap , count )
 bus_space_write_region_stream_1 ( space , handle , offset , datap , count )
 bus_space_write_region_stream_2 ( space , handle , offset , datap , count )
 bus_space_write_region_stream_4 ( space , handle , offset , datap , count )
 bus_space_write_region_stream_8 ( space , handle , offset , datap , count )
 These functions are defined just as their non-stream counterparts, except
 that they provide no byte-order translation.
 IMPLEMENTING BUS SPACES IN MACHINE-INDEPENDENT CODE 
 bus_space_tag_create ( obst , present , extpresent , ov , ctx , bstp )
 Create a copy of the tag obst at *bstp . Except for the behavior overrid-
 den by ov , *bstp inherits the behavior of obst under bus_space calls.
 ov contains function pointers corresponding to bus_space routines. Each
 function pointer has a corresponding bit in present or extpresent , and if
 that bit is 1, the function pointer overrides the corresponding bus_space 
 call for the new tag. Any combination of these bits may be set in
 present :
 BUS_SPACE_OVERRIDE_MAP
 BUS_SPACE_OVERRIDE_UNMAP
 BUS_SPACE_OVERRIDE_ALLOC
 BUS_SPACE_OVERRIDE_FREE
 BUS_SPACE_OVERRIDE_RESERVE
 BUS_SPACE_OVERRIDE_RELEASE
 BUS_SPACE_OVERRIDE_RESERVATION_MAP
 BUS_SPACE_OVERRIDE_RESERVATION_UNMAP
 BUS_SPACE_OVERRIDE_RESERVE_SUBREGION
 bus_space_tag_create () does not copy ov . After a new tag is created by
 bus_space_tag_create (), ov must not be destroyed until after the tag is
 destroyed by bus_space_tag_destroy ().
 The first argument of every override-function is a void * , and ctx is
 passed in that argument.
 Return 0 if the call succeeds. Return EOPNOTSUPP if the architecture
 does not support overrides. Return EINVAL if present is 0, if ov is
 NULL, or if present indicates that an override is present, but the corre-
 sponding override in ov is NULL.
 If the call does not succeed, *bstp is undefined.
 bus_space_tag_destroy ( bst )
 Destroy a tag, bst , created by a prior call to bus_space_tag_create ().
 If bst was not created by bus_space_tag_create (), results are undefined.
 If bst was already destroyed, results are undefined.
 EXPECTED CHANGES TO THE BUS_SPACE FUNCTIONS 
 The definition of the bus_space functions should not yet be considered
 finalized. There are several changes and improvements which should be
 explored, including:
 � Exporting the bus_space functions to userland so that applications
 (such as X servers) have easier, more portable access to device
 space.
 � Redefining bus space tags and handles so that machine-independent bus
 interface drivers (for example PCI to VME bridges) could define and
 implement bus spaces without requiring machine-dependent code. If
 this is done, it should be done in such a way that machine-dependent
 optimizations should remain possible.
 � Converting bus spaces (such as PCI configuration space) which cur-
 rently use space-specific access methods to use the bus_space func-
 tions where that is appropriate.
 � Redefining the way bus space is mapped and allocated, so that mapping
 and allocation are done with bus specific functions which return bus
 space tags. This would allow further optimization than is currently
 possible, and would also ease translation of the bus_space functions
 into user space (since mapping in user space would look like it just
 used a different bus-specific mapping function).
 COMPATIBILITY 
 The current version of the bus_space interface specification differs
 slightly from the original specification that came into wide use. A few
 of the function names and arguments have changed for consistency and
 increased functionality. Drivers that were written to the old, depre-
 cated specification can be compiled by defining the
 __BUS_SPACE_COMPAT_OLDDEFS preprocessor symbol before including
 < sys/bus.h >.
```

## 用途注记

Task 8.2 G5-P2 · V41《NetBSD 技术专题史》联网补证（D2 块；官方手册页，collection=NetBSD-current）。
