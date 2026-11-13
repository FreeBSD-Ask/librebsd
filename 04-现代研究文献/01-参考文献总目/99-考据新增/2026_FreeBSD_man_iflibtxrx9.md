# iflibtxrx(9) — FreeBSD 内核开发者手册页（设备相关收发函数）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=iflibtxrx&sektion=9
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.7.2“中断与队列的抽象”补证（D2 块）：收发接口以队列为参数（D2 块，ref_id 见库）

## 抓取正文（节选）

```

     int
     isc_rxd_pkt_get(void *sc, if_rxd_info_t ri);

   Global Variables
     extern struct if_txrx

DATA STRUCTURES
     The  device  dependent  mechanisms for handling packet transmit and receive
     are primarily defined by the functions named above.  The  if_pkt_info  data
     structure	contains  statistics  and  identifying info necessary for packet
     transmission.   While  the  data  structure  for  packet  receipt	is   the
     if_rxd_info structure.

   The if_pkt_info Structure
     The fields of struct if_pkt_info are as follows:

	   ipi_len	    (uint32_t)	Denotes the size of packet to be sent on
			    the transmit queue.

	   ipi_segs	    (bus_dma_segment_t *) A pointer to the  bus_dma_seg-
			    ment  of  the  device independent transfer queue de-
			    fined in iflib.

	   ipi_qsidx	    Unique index value	assigned  sequentially	to  each
			    transmit  queue.   Used  to  reference the currently
			    transmitting queue.

	   ipi_nsegs	    (uint16_t) Number of descriptors to be read into the
			    device dependent transfer descriptors.

	   ipi_ndescs	    (uint16_t) Number of descriptors in use.  Calculated
			    by subtracting the old pidx value from the new  pidx
			    value.

	   ipi_flags	    (uint16_t) Flags defined on a per packet basis.

	   ipi_pidx	    (uint32_t) Value of first pidx sent to the isc_encap
```

## 引文摘录（空白已归一，供逐字核对）

int isc_rxd_pkt_get(void *sc, if_rxd_info_t ri); Global Variables extern struct if_txrx DATA STRUCTURES The device dependent mechanisms for handling packet transmit and receive are primarily defined by the functions named above. The if_pkt_info data structure contains statistics and identifying info necessary for packet transmission. While the data structure for packet receipt is the if_rxd_info structure. The if_pkt_info Structure The fields of struct if_pkt_info are as follows: ipi_len (uint32_t) Denotes the size of packet to be sent on the transmit queue. ipi_segs (bus_dma_segment_t *) A pointer to the bus_dma_seg- ment of the device independent transfer queue de- fined in iflib. ipi_qsidx Unique index value assigned sequentially to each transmit queue. Used to reference the currently transmitting queue. ipi_nsegs (uint16_t) Number of descriptors to be read into the device dependent transfer descriptors. ipi_ndescs (uint16_t) Number of descriptors in use. Calculated by subtracting the old pidx value from the new pidx value. ipi_flags (uint16_t) Flags defined on a per packet basis. ipi_pidx (uint32_t) Value of first pidx sent to the isc_encap
