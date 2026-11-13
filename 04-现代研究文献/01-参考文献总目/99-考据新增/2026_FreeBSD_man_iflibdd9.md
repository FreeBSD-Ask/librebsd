# iflibdd(9) — FreeBSD 内核开发者手册页（设备相关配置函数）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=iflibdd&sektion=9
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.7.4“多队列硬件的适配”补证（D2 块）：队列数与 qset 参数（D2 块，ref_id 见库）

## 抓取正文（节选）

```
     registers.

   Device Dependent Functions
   Soft Queue Setup and Teardown
	   ifdi_tx_queues_alloc()
	   Mandatory  function	that  is  called during iflib_attach to allocate
	   transmit queues.  vaddrs and paddrs are arrays of virtual and  physi-
	   cal addresses respectively of the hardware transmit queues.	ntxqs is
	   the number of queues per qset.  ntxqsets is the number of qsets.

	   ifdi_rx_queues_alloc()
	   Mandatory function that is called during iflib_attach to allocate re-
	   ceive  queues.   vaddrs and paddrs are arrays of virtual and physical
	   addresses respectively of the hardware receive queues.  nrxqs is  the
	   number of queues per qset.  nrxqsets is the number of qsets.

	   ifdi_queues_free()
	   Mandatory  function	that  frees  the allocated queues and associated
	   transmit buffers.

	   ifdi_txq_setup()
	   Optional function for each transmit queue that  handles  device  spe-
	   cific initialization.

	   ifdi_rxq_setup()
	   Optional function for each receive queue that handles device specific
	   initialization.

   Device Setup and Teardown
	   ifdi_attach_pre()
	   Mandatory  function	implemented  by the driver to perform any attach
	   logic that procedes interrupt and queue allocation, queue setup,  and
	   interrupt assignment.

	   ifdi_attach_post()
	   Mandatory  function	implemented  by the driver to perform any attach
	   logic that occurs after ifdi_attach_pre, and iflib's queue setup  and
	   MSI/MSIX(X) or legacy interrupt assignment.
```

## 引文摘录（空白已归一，供逐字核对）

registers. Device Dependent Functions Soft Queue Setup and Teardown ifdi_tx_queues_alloc() Mandatory function that is called during iflib_attach to allocate transmit queues. vaddrs and paddrs are arrays of virtual and physi- cal addresses respectively of the hardware transmit queues. ntxqs is the number of queues per qset. ntxqsets is the number of qsets. ifdi_rx_queues_alloc() Mandatory function that is called during iflib_attach to allocate re- ceive queues. vaddrs and paddrs are arrays of virtual and physical addresses respectively of the hardware receive queues. nrxqs is the number of queues per qset. nrxqsets is the number of qsets. ifdi_queues_free() Mandatory function that frees the allocated queues and associated transmit buffers. ifdi_txq_setup() Optional function for each transmit queue that handles device spe- cific initialization. ifdi_rxq_setup() Optional function for each receive queue that handles device specific initialization. Device Setup and Teardown ifdi_attach_pre() Mandatory function implemented by the driver to perform any attach logic that procedes interrupt and queue allocation, queue setup, and interrupt assignment. ifdi_attach_post() Mandatory function implemented by the driver to perform any attach logic that occurs after ifdi_attach_pre, and iflib's queue setup and MSI/MSIX(X) or legacy interrupt assignment.
