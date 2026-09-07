---
title: "Project_xz_Utils_Threaded_Decoder_Early_Free_EBOL_2025-072026-07-22"
source_url: https://tukaani.org/xz/threaded-decoder-early-free.html
download_date: 2026-09-07
---

# Project_xz_Utils_Threaded_Decoder_Early_Free_EBOL_2025-072026-07-22

来源: https://tukaani.org/xz/threaded-decoder-early-free.html

 

 CVE-2025-31115: Threaded .xz decoder frees memory too early 

  tukaani.org  &#187;  XZ Utils  &#187; CVE-2025-31115 

 CVE-2025-31115: Threaded .xz decoder frees memory too early 

 2025-04-03 

 In XZ Utils 5.3.3alpha to 5.8.0,
the multithreaded .xz decoder in liblzma has a bug
where invalid input can at least result in a crash
( CVE-2025-31115 ).
The effects include heap use after free and
writing to an address based on the null pointer plus an offset.
Applications and libraries
that use the  lzma_stream_decoder_mt  function are affected. 

 The bug has been fixed in XZ Utils 5.8.1,
and the fix has been committed to
the  v5.4 ,  v5.6 ,  v5.8 , and  master  branches in the xz Git repository.
No new release packages will be made from the old stable branches,
but a patch is available that applies to all affected releases: 

  xz-cve-2025-31115.patch &#8201;&#8212;&#8201; signature  

 The single-threaded .xz decoder ( lzma_stream_decoder ) isn&#8217;t affected.
The commands  xz --decompress --threads=1  and  xzdec  use
the single-threaded decoder. 

 Credits 

 Thanks to Harri K. Koskinen for discovering and reporting this issue. 

 Thanks to Sebastian Andrzej Siewior for reviewing the patches. 

 Thanks to Sam James for general help. 

 Why fuzzing didn&#8217;t find this? 

 XZ Utils is fuzzed by OSS-Fuzz.
However, there was no program to fuzz the multithreaded .xz decoder.
Even if there had been, it likely would have used the  fuzz_code  function
in  fuzz_common.h  like the existing fuzz targets did.
That function called  lzma_code  in such a way
that it would have been impossible to trigger this particular bug.
 A fuzzer has been added 
and  fuzz_common.h 
 has been modified . 

  tukaani.org  &#187;  XZ Utils  &#187; CVE-2025-31115 

 
