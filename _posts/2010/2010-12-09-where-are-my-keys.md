---
date: 2010-12-09 09:00:00
year: 2010
original: swc
title: Where Are My Keys?
---
<p>I was looking through some Python code a few days ago, and noticed that its author was using this:</p>
<pre>if something in dict.keys():
    dict[something] += 1</pre>
<p>instead of:</p>
<pre>if something in dict:
    dict[something] += 1</pre>
<p>It seems like a small difference, but it's actually a very important one. The second form checks to see whether <code>something</code> is a key in the dictionary <code>dict</code>.  The first form, on the other hand, creates a list of all the keys in the dictionary, then searches that list from start to finish to see if <code>something</code> is there. They both produce the right answer, but the fast form does it in constant time, while the slow form (the one with the call to <code>dict.keys()</code>) takes time proportional to the size of the dictionary. The really bad news is, the "error" is silent.</p>
<p>What other examples have you seen of people getting the right answer the wrong way? And what more could we do to teach people how to avoid these traps?  Does it have to be done case by case, or is there something larger or more general we could try to convey?</p>