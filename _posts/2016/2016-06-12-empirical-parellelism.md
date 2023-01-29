---
title: "Parallelism in Open Source Projects"
date: 2016-06-12 01:02:03
year: 2016
original: nwit
---
<p>
  Marc Kiefer, Daniel Warzel, and Walter Tichy:
  "An Empirical Study on Parallelism in Modern Open-Source Projects".
  SEPS'15, October 2015, 
  <a href="https://ps.ipd.kit.edu/backend/index.php/veroeffentlichungen-details/items/3803.html">https://ps.ipd.kit.edu/backend/index.php/veroeffentlichungen-details/items/3803.html</a>.
</p>
<blockquote>
  <em>
    <p>
      We present an empirical study of 135 parallel open-source
      projects in Java, C# and C++ ranging from small (&lt;1000 lines
      of code) to very large (&gt;2M lines of code) codebases. We
      examine the projects to find out how language features,
      synchronization mechanisms, parallel data structures and
      libraries are used by developers to express parallelism. We also
      determine which common parallel patterns are used and how the
      implemented solutions compare to typical textbook advice.
    </p>
    <p>
      The results show that similar parallel constructs are used
      equally often across languages, but usage also heavily depends
      on how easy to use a certain language feature is. Patterns that
      do not map well to a language are much rarer compared to other
      languages. Bad practices are prevalent in hobby projects but
      also occur in larger projects.
    </p>
  </em>
</blockquote>
<p>
  I wrote my first parallel program in 1986 on an ICL DAP with 4096
  bit-serial processors.  I wrote my second in Occam the following
  spring for a 16-transputer machine, and spent the next ten years
  thinking, "There has to be a better way."  Two decades later, the
  answer to that is still, "Not yet," but in those years parallelism
  of various kinds has gone from esoteric to everyday.
</p>
<p>
  But how do we actually use it?  And how well?  To answer those
  questions, the authors of this paper explored open source programs
  written in several different languages.  Here are a few of their
  findings (the figures for Java are omitted, since those tables are
  larger than the ones for C# and C++ combined):
</p>
<table class="table table-striped">
  <tr>
    <th colspan="4">Use of High-Level Constructs</th>
    <th colspan="4">Use of Synchronization Primitives</th>
  </tr>
  <tr>
    <th>Language</th>
    <th>Feature</th>
    <th># projects</th>
    <th>% of total</th>
    <th>Language</th>
    <th>Feature</th>
    <th># projects</th>
    <th>% of total</th>
  </tr>
  <tr>
    <td>C#</td>
    <td>Task</td>
    <td>33</td>
    <td>73.33%</td>
    <td>C#</td>
    <td>lock()</td>
    <td>42</td>
    <td>93.33%</td>
  </tr>
  <tr>
    <td></td>
    <td>ThreadPool</td>
    <td>19</td>
    <td>42.22%</td>
    <td></td>
    <td>ManualResetEvent</td>
    <td>22</td>
    <td>48.89%</td>
  </tr>
  <tr>
    <td></td>
    <td>TaskScheduler</td>
    <td>10</td>
    <td>22.22%</td>
    <td></td>
    <td>Monitor</td>
    <td>17</td>
    <td>37.78%</td>
  </tr>
  <tr>
    <td></td>
    <td>Parallel.For</td>
    <td>8</td>
    <td>17.78%</td>
    <td></td>
    <td>AutoResetEvent</td>
    <td>16</td>
    <td>35.56%</td>
  </tr>
  <tr>
    <td></td>
    <td>BlockingCollection</td>
    <td>6</td>
    <td>13.33%</td>
    <td></td>
    <td>ReaderWriterLockSlim</td>
    <td>15</td>
    <td>33.33%</td>
  </tr>
  <tr>
    <td></td>
    <td>Parallel.ForEach</td>
    <td>6</td>
    <td>13.33%</td>
    <td></td>
    <td>WaitHandle</td>
    <td>13</td>
    <td>28.89%</td>
  </tr>
  <tr>
    <td></td>
    <td>TaskFactory</td>
    <td>5</td>
    <td>11.11%</td>
    <td></td>
    <td>EventWaitHandle</td>
    <td>10</td>
    <td>22.22%</td>
  </tr>
  <tr>
    <td></td>
    <td>Parallel.Invoke</td>
    <td>1</td>
    <td>2.22%</td>
    <td></td>
    <td>Mutex</td>
    <td>10</td>
    <td>22.22%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>ManualResetEventSlim</td>
    <td>8</td>
    <td>17.78%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>Barrier</td>
    <td>7</td>
    <td>15.56%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>Semaphore</td>
    <td>6</td>
    <td>13.33%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>SpinWait</td>
    <td>4</td>
    <td>8.89%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>CountdownEvent</td>
    <td>3</td>
    <td>6.67%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>ReaderWriterLock</td>
    <td>3</td>
    <td>6.67%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>SemaphoreSlim</td>
    <td>3</td>
    <td>6.67%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>MethodImplOptions Synchronized</td>
    <td>2</td>
    <td>4.44%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>Interlocked.MemoryBarrier</td>
    <td>1</td>
    <td>2,22%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>SpinLock</td>
    <td>0</td>
    <td>0.00%</td>
  </tr>
  <tr>
    <td>C++</td>
    <td>#pragma omp parallel for</td>
    <td>6</td>
    <td>13.64%</td>
    <td></td>
    <td>mutex</td>
    <td>39</td>
    <td>88.64%</td>
  </tr>
  <tr>
    <td></td>
    <td>future/promise</td>
    <td>3</td>
    <td>6.82%</td>
    <td></td>
    <td>condition variable</td>
    <td>28</td>
    <td>63.63%</td>
  </tr>
  <tr>
    <td></td>
    <td>#pragma omp parallel</td>
    <td>2</td>
    <td>4.55%</td>
    <td></td>
    <td>Semaphore</td>
    <td>18</td>
    <td>40.91%</td>
  </tr>
  <tr>
    <td></td>
    <td>packaged task</td>
    <td>0</td>
    <td>0.00%</td>
    <td></td>
    <td>CriticalSection</td>
    <td>17</td>
    <td>38.64%</td>
  </tr>
  <tr>
    <td></td>
    <td>shared future</td>
    <td>0</td>
    <td>0.00%</td>
    <td></td>
    <td>unique lock</td>
    <td>16</td>
    <td>36.36%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>lock guard</td>
    <td>12</td>
    <td>27.27%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>barrier</td>
    <td>5</td>
    <td>11.36%</td>
  </tr>
  <tr>
    <td colspan="4"></td>
    <td></td>
    <td>#pragma omp critical</td>
    <td>3</td>
    <td>6.82%</td>
  </tr>
</table>
<p>
  But these tables don't tell the most important parts of the story.
  For that, we have to look at patterns:
</p>
<table class="table table-striped">
  <tr>
    <td>Pattern</td>
    <td>Java</td>
    <td>C#</td>
    <td>C++</td>
  </tr>
  <tr>
    <td>Master-worker</td>
    <td>29</td>
    <td>23</td>
    <td>23</td>
  </tr>
  <tr>
    <td>Producer-consumer</td>
    <td>10</td>
    <td>5</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Pipeline</td>
    <td>8</td>
    <td>9</td>
    <td>8</td>
  </tr>
  <tr>
    <td>Parallel Loop</td>
    <td>1</td>
    <td>8</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Fork-join</td>
    <td>3</td>
    <td>1</td>
    <td>1</td>
  </tr>
</table>
<p>
  But the authors go even further
  and look at where programmers do things they shouldn't:
</p>
<ul>
  <li>
    "Smaller projects tend to reimplement slight variations of existing
    functionality, while projects with a larger codebase often reuse
    existing functionality and extend these classes via subclassing."
  </li>
  <li>
    "An exception is the master-worker pattern. It seems that it is
    such an intuitive pattern, that some developers seem to implement
    it by accident. Unexperienced developers just create threads and
    distribute their work to them. In larger projects comments and
    class naming suggests that they are aware of the master-worker
    pattern and implement it on purpose…"
  </li>
  <li>
    "Prime examples of bad pratice are the synchronized() and lock()
    features in Java and C#. Both language references strongly advise
    against locking on publicly accessible types or classes. Nevertheless
    this is what happens in most instances in both Java and C# regardless
    of the size of the project."
  </li>
</ul>
<p>
  It's easy to say this means we need better
  documentation–better, but wrong.  Just as you can't refactor
  your way to better security, you can't document your way to better
  usability.  Knowing what people use, how they use it, and how
  they <em>mis</em>-use it could and should inform the design of the
  next generation of parallel programming tools.  And if that's too
  optimistic, we can at least hope that it will give the builders of
  the next generation of program checking tools a larger list of
  things to look for…
</p>
