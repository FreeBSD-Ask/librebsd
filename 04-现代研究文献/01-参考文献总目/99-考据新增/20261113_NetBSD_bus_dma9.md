<!-- 网页存档｜来源：https://man.netbsd.org/bus_dma.9｜抓取：2026-11-13｜curl 直取两次一致，HTML 标签剥离与空白归一 -->

# bus_dma.9 — NetBSD 手册页（DMA mapping interface）

## 抓取正文（NAME 至 SEE ALSO 前，节选）

```
BUS_DMA(9) NetBSD Kernel Developer's Manual BUS_DMA(9)
 NAME 
 bus_dma , bus_dmamap_create , bus_dmamap_destroy , bus_dmamap_load ,
 bus_dmamap_load_mbuf , bus_dmamap_load_uio , bus_dmamap_load_raw ,
 bus_dmamap_unload , bus_dmamap_sync , bus_dmamem_alloc , bus_dmamem_free ,
 bus_dmamem_map , bus_dmamem_unmap , bus_dmamem_mmap , bus_dmatag_subregion ,
 bus_dmatag_destroy -- Bus and Machine Independent DMA Mapping Interface
 SYNOPSIS 
 #include <sys/bus.h> 
 int 
 bus_dmamap_create ( bus_dma_tag_t tag , bus_size_t size , int nsegments ,
 bus_size_t maxsegsz , bus_size_t boundary , int flags ,
 bus_dmamap_t *dmamp );
 void 
 bus_dmamap_destroy ( bus_dma_tag_t tag , bus_dmamap_t dmam );
 int 
 bus_dmamap_load ( bus_dma_tag_t tag , bus_dmamap_t dmam , void *buf ,
 bus_size_t buflen , struct proc *p , int flags );
 int 
 bus_dmamap_load_mbuf ( bus_dma_tag_t tag , bus_dmamap_t dmam ,
 struct mbuf *chain , int flags );
 int 
 bus_dmamap_load_uio ( bus_dma_tag_t tag , bus_dmamap_t dmam ,
 struct uio *uio , int flags );
 int 
 bus_dmamap_load_raw ( bus_dma_tag_t tag , bus_dmamap_t dmam ,
 bus_dma_segment_t *segs , int nsegs , bus_size_t size , int flags );
 void 
 bus_dmamap_unload ( bus_dma_tag_t tag , bus_dmamap_t dmam );
 void 
 bus_dmamap_sync ( bus_dma_tag_t tag , bus_dmamap_t dmam , bus_addr_t offset ,
 bus_size_t len , int ops );
 int 
 bus_dmamem_alloc ( bus_dma_tag_t tag , bus_size_t size ,
 bus_size_t alignment , bus_size_t boundary , bus_dma_segment_t *segs ,
 int nsegs , int *rsegs , int flags );
 void 
 bus_dmamem_free ( bus_dma_tag_t tag , bus_dma_segment_t *segs , int nsegs );
 int 
 bus_dmamem_map ( bus_dma_tag_t tag , bus_dma_segment_t *segs , int nsegs ,
 size_t size , void **kvap , int flags );
 void 
 bus_dmamem_unmap ( bus_dma_tag_t tag , void *kva , size_t size );
 paddr_t 
 bus_dmamem_mmap ( bus_dma_tag_t tag , bus_dma_segment_t *segs , int nsegs ,
 off_t off , int prot , int flags );
 int 
 bus_dmatag_subregion ( bus_dma_tag_t tag , bus_addr_t min_addr ,
 bus_addr_t max_addr , bus_dma_tag_t *newtag , int flags );
 void 
 bus_dmatag_destroy ( bus_dma_tag_t tag );
 DESCRIPTION 
 Provide a bus- and machine-independent ``DMA mapping interface''.
 Implementation Notes 
 All data types and constants will be defined by the port-specific header
 < machine/bus_defs.h >. All functions will be defined by the port-specific
 header < machine/bus_funcs.h >. Note that this document assumes the exis-
 tence of types already defined by the current bus_space(9) interface.
 Unless otherwise noted, all function calls in this interface may be
 defined as cpp(1) macros.
 Data Types 
 Individual implementations may name these structures whatever they wish,
 providing that the external representations are:
 bus_dma_tag_t 
 A machine-dependent opaque type describing the implementation
 of DMA for a given bus.
 bus_dma_segment_t 
 A structure with at least the following members:
 bus_addr_t ds_addr;
 bus_size_t ds_len;
 The structure may have machine-dependent members and arbitrary
 layout. The values in ds_addr and ds_len are suitable for pro-
 gramming into DMA controller address and length registers.
 bus_dmamap_t 
 A pointer to a structure with at least the following members:
 bus_size_t dm_maxsegsz;
 bus_size_t dm_mapsize;
 int dm_nsegs;
 bus_dma_segment_t *dm_segs;
 The structure may have machine-dependent members and arbitrary
 layout. The dm_maxsegsz member indicates the maximum number of
 bytes that may be transferred by any given DMA segment. The
 dm_mapsize member indicates the size of the mapping. A value
 of 0 indicates the mapping is invalid. The dm_segs member may
 be an array of segments or a pointer to an array of segments.
 The dm_nsegs member indicates the number of segments in
 dm_segs .
 Functions 
 bus_dmamap_create ( tag , size , nsegments , maxsegsz , boundary , flags , dmamp )
 Allocates a DMA handle and initializes it according to the param-
 eters provided.
 tag This is the bus_dma_tag_t passed down from the parent
 driver via <bus>_attach_args .
 size This is the maximum DMA transfer that can be mapped by
 the handle.
 nsegments 
 Number of segments the device can support in a single DMA
 transaction. This may be the number of scatter-gather
 descriptors supported by the device.
 maxsegsz 
 The maximum number of bytes that may be transferred by
 any given DMA segment and will be assigned to the
 dm_maxsegsz member.
 boundary 
 Some DMA controllers are not able to transfer data that
 crosses a particular boundary. This argument allows this
 boundary to be specified. The boundary lines begin at 0,
 and occur every boundary bytes. Mappings may begin on a
 boundary line but may not end on or cross a boundary
 line. If no boundary condition needs to be observed, a
 boundary argument of 0 should be used.
 flags 
 BUS_DMA_WAITOK
 It is safe to wait (sleep) for resources during
 this call.
 BUS_DMA_NOWAIT
 It is not safe to wait (sleep) for resources dur-
 ing this call.
 BUS_DMA_ALLOCNOW
 Perform any resource allocation this handle may
 need now. If this is not specified, the alloca-
 tion may be deferred to bus_dmamap_load (). If
 this flag is specified, bus_dmamap_load () will
 not block on resource allocation.
 BUS_DMA_BUS[1-4]
 These flags are placeholders, and may be used by
 busses to provide bus-dependent functionality.
 dmamp This is a pointer to a bus_dmamap_t . A DMA map will be
 allocated and pointed to by dmamp upon successful comple-
 tion of this routine. dmamp is undefined if this routine
 fails.
 Behavior is not defined if invalid arguments are passed to
 bus_dmamap_create ().
 Returns 0 on success, or an error code to indicate mode of fail-
 ure.
 bus_dmamap_destroy ( tag , dmam )
 Frees all resources associated with a given DMA handle.
 tag This is the bus_dma_tag_t passed down from the parent
 driver via <bus>_attach_args .
 dmam The DMA handle to destroy.
 In the event that the DMA handle contains a valid mapping, the
 mapping will be unloaded via the same mechanism used by
 bus_dmamap_unload ().
 Behavior is not defined if invalid arguments are passed to
 bus_dmamap_destroy ().
 If given valid arguments, bus_dmamap_destroy () always succeeds.
 bus_dmamap_load ( tag , dmam , buf , buflen , p , flags )
 Loads a DMA handle with mappings for a DMA transfer. It assumes
 that all pages involved in a DMA transfer are wired.
 tag This is the bus_dma_tag_t passed down from the parent
 driver via <bus>_attach_args .
 dmam The DMA handle with which to map the transfer.
 buf The buffer to be used for the DMA transfer.
 buflen The size of the buffer.
 p Used to indicate the address space in which the buffer is
 located. If NULL, the buffer is assumed to be in kernel
 space. Otherwise, the buffer is assumed to be in proc
 p 's address space.
 flags 
 BUS_DMA_WAITOK
 It is safe to wait (sleep) for resources during
 this call.
 BUS_DMA_NOWAIT
 It is not safe to wait (sleep) for resources dur-
 ing this call.
 BUS_DMA_STREAMING
 By default, the bus_dma API assumes that there is
 coherency between memory and the device perform-
 ing the DMA transaction. Some platforms, how-
 ever, have special hardware, such as an ``I/O
 cache'', which may improve performance of some
 types of DMA transactions, but which break the
 assumption that there is coherency between memory
 and the device performing the DMA transaction.
 This flag allows the use of this special hard-
 ware, provided that the device is doing sequen-
 tial, unidirectional transfers which conform to
 certain alignment and size constraints defined by
 the platform. If the platform does not support
 the feature, or if the buffer being loaded into
 the DMA map does not conform to the constraints
 required for use of the feature, then this flag
 will be silently ignored. Also refer to the use
 of this flag with the bus_dmamem_alloc () func-
 tion.
 BUS_DMA_READ
 This is a hint to the machine-dependent back-end
 that indicates the mapping will be used only for
 a device -> memory transaction. The back-end may
 perform optimizations based on this information.
 BUS_DMA_WRITE
 This is a hint to the machine-dependent back-end
 that indicates the mapping will be used only for
 a memory -> device transaction. The back-end may
 perform optimizations based on this information.
 BUS_DMA_BUS[1-4]
 These flags are placeholders, and may be used by
 busses to provide bus-dependent functionality.
 As noted above, if a DMA handle is created with BUS_DMA_ALLOCNOW,
 bus_dmamap_load () will never block.
 If a call to bus_dmamap_load () fails, the mapping in the DMA han-
 dle will be invalid. It is the responsibility of the caller to
 clean up any inconsistent device state resulting from incomplete
 iteration through the uio.
 Behavior is not defined if invalid arguments are passed to
 bus_dmamap_load ().
 Returns 0 on success, or an error code to indicate mode of fail-
 ure. Possible error codes include the following:
 EFBIG Too many segments.
 EINVAL buflen is too large for the DMA map.
 ENOMEM Could not allocate memory for, e.g., a bounce
 buffer.
 bus_dmamap_load_mbuf ( tag , dmam , chain , flags )
 This is a variation of bus_dmamap_load () which maps mbuf chains
 for DMA transfers. Mbuf chains are assumed to be in kernel vir-
 tual address space.
 bus_dmamap_load_uio ( tag , dmam , uio , flags )
 This is a variation of bus_dmamap_load () which maps buffers
 pointed to by uio for DMA transfers. Determination if the
 buffers are in user or kernel virtual address space is done
 internally, according to uio -> uio_vmspace . See uiomove(9) for
 details of the uio structure.
 bus_dmamap_load_raw ( tag , dmam , segs , nsegs , size , flags )
 This is a variation of bus_dmamap_load () which maps buffers allo-
 cated by bus_dmamem_alloc () (see below). The segs argument is an
 array of bus_dma_segment_t's filled in by bus_dmamem_alloc ().
 The nsegs argument is the number of segments in the array. The
 size argument is the size of the DMA transfer.
 bus_dmamap_unload ( tag , dmam )
 Deletes the mappings for a given DMA handle.
 tag This is the bus_dma_tag_t passed down from the parent
 driver via <bus>_attach_args .
 dmam The DMA handle containing the mappings which are to be
 deleted.
 If the DMA handle was created with BUS_DMA_ALLOCNOW,
 bus_dmamap_unload () will not free the corresponding resources
 which were allocated by bus_dmamap_create (). This is to ensure
 that bus_dmamap_load () will never block on resources if the han-
 dle was created with BUS_DMA_ALLOCNOW.
 bus_dmamap_unload () will not perform any implicit synchronization
 of DMA buffers. This must be done explicitly by
 bus_dmamap_sync ().
 bus_dmamap_unload () will restore the dm_maxsegsz member to its
 initial value assigned by bus_dmamap_create ().
 Behavior is not defined if invalid arguments are passed to
 bus_dmamap_unload ().
 If given valid arguments, bus_dmamap_unload () always succeeds.
 bus_dmamap_sync ( tag , dmam , offset , len , ops )
 Performs pre- and post-DMA operation cache and/or buffer synchro-
 nization.
 tag This is the bus_dma_tag_t passed down from the parent
 driver via <bus>_attach_args .
 dmam The DMA mapping to be synchronized.
 offset The offset into the DMA mapping to synchronize.
 len The length of the mapping from offset to synchronize.
 ops One or more synchronization operations to perform. The
 following DMA synchronization operations are defined:
 BUS_DMASYNC_PREREAD
 Perform any synchronization required prior to an
 update of host memory by the device.
 BUS_DMASYNC_POSTREAD
 Perform any synchronization required after an
 update of host memory by the device and prior to
 CPU access to host memory.
 BUS_DMASYNC_PREWRITE
 Perform any synchronization required after an
 update of host memory by the CPU and prior to
 device access to host memory.
 BUS_DMASYNC_POSTWRITE
 Perform any synchronization required after device
 access to host memory.
 where each operation may involve cache flush/invalida-
 tion, bounce buffer copying, and/or memory barriers.
 More than one operation may be performed in a given syn-
 chronization call. Mixing of PRE and POST operations is
 not allowed, and behavior is undefined if this is
 attempted.
 Synchronization operations are expressed from the per-
 spective of the host RAM, i.e., a device -> memory opera-
 tion is a READ, and a memory -> device operation is a
 WRITE.
 bus_dmamap_sync () may consult state kept within the DMA map to
 determine if the memory is mapped in a DMA coherent fashion. If
 so, bus_dmamap_sync () may elect to skip certain expensive opera-
 tions, such as flushing of the data cache. See bus_dmamem_map ()
 for more information on this subject.
 On platforms which implement a weak memory access ordering model,
 bus_dmamap_sync () will always cause the appropriate memory barri-
 ers to be issued.
 This function exists to ensure that the host and the device have
 a consistent view of a range of DMA memory, before and after a
 DMA operation.
 An example of using bus_dmamap_sync (), involving multiple read-
 write use of a single mapping might look like this:
 bus_dmamap_load(...);
 while (not done) {
 /* invalidate soon-to-be-stale cache blocks */
 bus_dmamap_sync(..., BUS_DMASYNC_PREREAD);
 [ do read DMA ]
 /* copy from bounce */
 bus_dmamap_sync(..., BUS_DMASYNC_POSTREAD);
 /* read data now in driver-provided buffer */
 [ computation ]
 /* data to be written now in driver-provided buffer */
 /* flush write buffers and writeback, copy to bounce */
 bus_dmamap_sync(..., BUS_DMASYNC_PREWRITE);
 [ do write DMA ]
 /* probably a no-op, but provided for consistency */
 bus_dmamap_sync(..., BUS_DMASYNC_POSTWRITE);
 }
 bus_dmamap_unload(...);
 This function must be called to synchronize DMA buffers before
 and after a DMA operation. Other bus_dma functions can not be
 relied on to do this synchronization implicitly. If DMA read and
 write operations are not preceded and followed by the appropriate
 synchronization operations, behavior is undefined.
 Behavior is not defined if invalid arguments are passed to
 bus_dmamap_sync ().
 If given valid arguments, bus_dmamap_sync () always succeeds.
 bus_dmamem_alloc ( tag , size , alignment , boundary , segs , nsegs , rsegs ,
 flags )
 Allocates memory that is ``DMA safe'' for the bus corresponding
 to the given tag.
 The mapping of this memory is machine-dependent (or ``opaque'');
 machine-independent code must not assume that the addresses
 returned are valid in kernel virtual address space, or that the
 addresses returned are system physical addresses. The address
 value returned as part of segs can thus not be used to program
 DMA controller address registers. Only the values in the dm_segs 
 array of a successfully loaded DMA map (using bus_dmamap_load ())
 can be used for this purpose.
 Allocations will always be rounded to the hardware page size.
 Callers may wish to take advantage of this, and cluster alloca-
 tion of small data structures.
 tag This is the bus_dma_tag_t passed down from the parent
 driver via <bus>_attach_args .
 size The amount of memory to allocate.
 alignment 
 Each segment in the allocated memory will be aligned to
 this value. If the alignment is less than a hardware
 page size, it will be rounded up to the hardware page
 size. This value must be a power of two.
 boundary 
 Each segment in the allocated memory must not cross this
 boundary (relative to zero). This value must be a power
 of two. A boundary value less than the size of the allo-
 cation is invalid. If no boundary condition needs to be
 observed, a boundary argument of 0 should be used.
 segs An array of bus_dma_segment_t's, filled in as memory is
 allocated, representing the opaque addresses of the mem-
 ory chunks.
 nsegs Specifies the number of segments in segs , and this is the
 maximum number of segments that the allocated memory may
 contain.
 rsegs Used to return the actual number of segments the memory
 contains.
 flags 
 BUS_DMA_WAITOK
 It is safe to wait (sleep) for resources during
 this call.
 BUS_DMA_NOWAIT
 It is not safe to wait (sleep) for resources dur-
 ing this call.
 BUS_DMA_STREAMING
 Adjusts, if necessary, the size, alignment, and
 boundary constraints to conform to the platform-
 dependent requirements for the use of the
 BUS_DMA_STREAMING flag with the bus_dmamap_load ()
 function. If the platform does not support the
 BUS_DMA_STREAMING feature, or if the size, align-
 ment, and boundary constraints would already sat-
 isfy the platform's requirements, this flag is
 silently ignored. The BUS_DMA_STREAMING flag
 will never relax the constraints specified in the
 call.
 BUS_DMA_BUS[1-4]
 These flags are placeholders, and may be used by
 busses to provide bus-dependent functionality.
 All pages allocated by bus_dmamem_alloc () will be wired down
 until they are freed by bus_dmamem_free ().
 Behavior is undefined if invalid arguments are passed to
 bus_dmamem_alloc ().
 Returns 0 on success, or an error code indicating mode of fail-
 ure.
 bus_dmamem_free ( tag , segs , nsegs )
 Frees memory previously allocated by bus_dmamem_alloc (). Any
 mappings will be invalidated.
 tag This is the bus_dma_tag_t passed down from the parent
 driver via <bus>_attach_args .
 segs The array of bus_dma_segment_t's filled in by
 bus_dmamem_alloc ().
 nsegs The number of segments in segs .
 Behavior is undefined if invalid arguments are passed to
 bus_dmamem_free ().
 If given valid arguments, bus_dmamem_free () always succeeds.
 bus_dmamem_map ( tag , segs , nsegs , size , kvap , flags )
 Maps memory allocated with bus_dmamem_alloc () into kernel virtual
 address space.
 tag This is the bus_dma_tag_t passed down from the parent
 driver via <bus>_attach_args .
 segs The array of bus_dma_segment_t's filled in by
 bus_dmamem_alloc (), representing the memory regions to
 map.
 nsegs The number of segments in segs .
 size The size of the mapping.
 kvap Filled in to specify the kernel virtual address where the
 memory is mapped.
 flags 
 BUS_DMA_WAITOK
 It is safe to wait (sleep) for resources during
 this call.
 BUS_DMA_NOWAIT
 It is not safe to wait (sleep) for resources dur-
 ing this call.
 BUS_DMA_BUS[1-4]
 These flags are placeholders, and may be used by
 busses to provide bus-dependent functionality.
 BUS_DMA_COHERENT
 This flag is a hint to machine-dependent code.
 If possible, map the memory in such a way as it
 will be DMA coherent. This may include mapping
 the pages into uncached address space or setting
 the cache-inhibit bits in page table entries. If
 DMA coherent mappings are impossible, this flag
 is silently ignored.
 Later, when this memory is loaded into a DMA map,
 machine-dependent code will take whatever steps
 are necessary to determine if the memory was
 mapped in a DMA coherent fashion. This may
 include checking if the kernel virtual address
 lies within uncached address space or if the
 cache-inhibit bits are set in page table entries.
 If it is determined that the mapping is DMA
 coherent, state may be placed into the DMA map
 for use by later calls to bus_dmamap_sync ().
 Note that a device driver must not rely on
 BUS_DMA_COHERENT for correct operation. All
 calls to bus_dmamap_sync () must still be made.
 This flag is provided only as an optimization
 hint to machine-dependent code.
 Also note that this flag only applies to
 coherency between the CPU and memory. Coherency
 between memory and the device is controlled with
 a different flag. See the description of the
 bus_dmamap_load () function.
 BUS_DMA_NOCACHE
 This flag is a hint to machine-dependent code.
 If possible, map the memory uncached. This flag
 may be useful in the case that the memory cache
 causes unexpected behavior of the device.
 Exclusive with BUS_DMA_PREFETCHABLE.
 BUS_DMA_PREFETCHABLE
 This flag is a hint to machine-dependent code.
 If possible, map the memory prefetchable/write-
 combining.
 Exclusive with BUS_DMA_NOCACHE.
 Behavior is undefined if invalid arguments are passed to
 bus_dmamem_map ().
 Returns 0 on success, or an error code indicating mode of fail-
 ure.
 bus_dmamem_unmap ( tag , kva , size )
 Unmaps memory previously mapped with bus_dmamem_map (), freeing
 the kernel virtual address space used by the mapping.
 tag This is the bus_dma_tag_t passed down from the parent
 driver via <bus>_attach_args .
 kva The kernel virtual address of the mapped memory.
 size The size of the mapping.
 Behavior is undefined if invalid arguments are passed to
 bus_dmamem_unmap ().
 If given valid arguments, bus_dmamem_unmap () always succeeds.
 bus_dmamem_mmap ( tag , segs , nsegs , off , prot , flags )
 Provides support for user mmap(2) 'ing of DMA-safe memory. This
 function is to be called by a device driver's (* d_mmap )() entry
 point, which is called by the device pager for each page to be
 mapped.
 tag This is the bus_dma_tag_t passed down from the parent
 driver via <bus>_attach_args .
 segs The array of bus_dma_segment_t's filled in by
 bus_dmamem_alloc (), representing the memory to be
 mmap(2) 'ed.
 nsegs The number of elements in the segs array.
 off The offset of the page in DMA memory which is to be
 mapped.
 prot The protection codes for the mapping.
 flags 
 BUS_DMA_WAITOK
 It is safe to wait (sleep) for resources during
 this call.
 BUS_DMA_NOWAIT
 It is not safe to wait (sleep) for resources dur-
 ing this call.
 BUS_DMA_BUS[1-4]
 These flags are placeholders, and may be used by
 busses to provide bus-dependent functionality.
 BUS_DMA_COHERENT
 See bus_dmamem_map () above for a description of
 this flag.
 BUS_DMA_NOCACHE
 See bus_dmamem_map () above for a description of
 this flag.
 Behavior is undefined if invalid arguments are passed to
 bus_dmamem_mmap ().
 Returns -1 to indicate failure. Otherwise, returns an opaque
 value to be interpreted by the device pager.
 bus_dmatag_subregion ( tag , min_addr , max_addr , newtag , flags )
 Given a bus_dma_tag_t create a new bus_dma_tag_t with a limited
 bus address space. This function should not normally be used,
 but is useful for devices that do not support the full address
 space of the parent bus. Not all ports implement this method; on
 ports where it is unavailable, EOPNOTSUPP is returned.
 tag This is the bus_dma_tag_t to subregion.
 min_addr 
 The smallest address this new tag can address.
 max_addr 
 The largest address this new tag can address.
 newtag Pointer filled in with the address of the new
 bus_dma_tag_t .
 flags 
 BUS_DMA_WAITOK
 It is safe to wait (sleep) for resources during
 this call.
 BUS_DMA_NOWAIT
 It is not safe to wait (sleep) for resources dur-
 ing this call.
 The address range min_addr to max_addr is inclusive of both
 addresses.
 bus_dmatag_destroy ( tag )
 Free a tag created by bus_dmatag_subregion ().
```

## 用途注记

Task 8.2 G5-P2 · V41《NetBSD 技术专题史》联网补证（D2 块；官方手册页，collection=NetBSD-current）。
