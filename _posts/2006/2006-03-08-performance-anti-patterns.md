---
title: "Performance Anti-Patterns"
date: 2006-03-08 13:42:14
year: 2006
---
<p><a href="http://www.acmqueue.org/modules.php?name=Content&amp;pa=printer_friendly&amp;pid=366&amp;page=1">This article</a>, by Sun's <a href="http://blogs.sun.com/barts">Bart Smaalders</a>, describes ten common performance mistakes software developers make. One example:</p>

<blockquote><em>
During Solaris 10 development, Solaris engineers fixed a long list of performance problems across the kernel and user libraries. Toward the end of the release, [they] spent some time reviewing just what had been improved and by how much…and what was the underlying cause of the performance problem. Interestingly enough, all the really big improvements (above, say, 200 percent) resulted from changes in algorithms. Over and over again, all the other performance fixes using specialized SIMD processor instructions such as SSE2 or VIS, inserting memory prefetch instructions, cycle shaving…paled in significance compared with simply going back and rethinking the locking algorithms and/or data structures.
</em></blockquote>
