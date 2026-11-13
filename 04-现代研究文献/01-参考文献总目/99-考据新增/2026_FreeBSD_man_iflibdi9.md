# iflibdi(9) — FreeBSD 内核开发者手册页（设备无关配置函数）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=iflibdi&sektion=9
- 抓取日期：2026-11-13
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.2.7.4“多队列硬件的适配”补证（D2 块）：框架侧生命周期接口（D2 块，ref_id 见库）

## 抓取正文（节选）

```
IFLIBDI(9)		    Kernel Developer's Manual		      IFLIBDI(9)

NAME
     iflibdi -- Device Independent Configuration Functions

SYNOPSIS
     #include <ifdi_if.h>

   Device Independent Functions
     int
     iflib_device_attach(device_t dev);

     int
     iflib_device_detach(device_t dev);

     int
     iflib_device_suspend(device_t dev);

     int
     iflib_device_resume(device_t dev);

     int
     iflib_device_register(device_t dev, void *softc, if_shared_ctx_t sctx,
	 if_ctx_t *ctxp);

     int
     iflib_device_deregister(if_ctx_t ctx);

     int
     iflib_irq_alloc(if_ctx_t ctx, if_irq_t irq_info, int rid,
	 driver_filter_t filter, void *filter_arg, driver_intr_t handler,
	 void *arg, char *name);

```

## 引文摘录（空白已归一，供逐字核对）

IFLIBDI(9) Kernel Developer's Manual IFLIBDI(9) NAME iflibdi -- Device Independent Configuration Functions SYNOPSIS #include <ifdi_if.h> Device Independent Functions int iflib_device_attach(device_t dev); int iflib_device_detach(device_t dev); int iflib_device_suspend(device_t dev); int iflib_device_resume(device_t dev); int iflib_device_register(device_t dev, void *softc, if_shared_ctx_t sctx, if_ctx_t *ctxp); int iflib_device_deregister(if_ctx_t ctx); int iflib_irq_alloc(if_ctx_t ctx, if_irq_t irq_info, int rid, driver_filter_t filter, void *filter_arg, driver_intr_t handler, void *arg, char *name);
