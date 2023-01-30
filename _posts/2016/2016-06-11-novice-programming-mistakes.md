---
title: "Novice Programming Mistakes"
date: 2016-06-09 01:02:03
year: 2016
original: nwit
---
<p>
  Amjad Altadmri and Neil C. C. Brown:
  "37 Million Compilations: Investigating Novice Programming Mistakes in Large-Scale Student Data".
  SIGCSE'15, March 2015, http://dx.doi.org/10.1145/2676723.2677258,
  <a href="https://kar.kent.ac.uk/46742/1/fp1187-altadmri.pdf">https://kar.kent.ac.uk/46742/1/fp1187-altadmri.pdf</a>.
</p>
<blockquote>
  <em>
    Educators often form opinions on which programming mistakes novices make most often – for example, in Java:
    "they always confuse equality with assignment", or "they always call methods with the wrong types".
    These opinions are generally based solely on personal experience.
    We report a study to determine if programming educators form a consensus about which Java programming mistakes are the most common.
    We used the Blackbox data set to check whether the educators' opinions matched data from over 100,000 students –
    and checked whether this agreement was mediated by educators' experience.
    We found that educators formed only a weak consensus about which mistakes are most frequent,
    that their rankings bore only a moderate correspondence to the students in the Blackbox data,
    and that educators' experience had no effect on this level of agreement.
    These results raise questions about claims educators make regarding which errors students are most likely to commit.
  </em>
</blockquote>
<p>
  So,
  what's the most common kind of error novice Java programmers make?
  Turns out it isn't confusing assignment "=" with equality "==",
  but rather mis-matched or unbalanced parentheses.
  Invoking methods with the wrong argument (e.g., <code>list.get("abc")</code>) is the second most common,
  and control flow being able to reach the end of a non-void method without returning a value is third.
  And which errors take the most time to fix?
  The answer to that turns out to be:
</p>
<ul>
  <li>
    Confusing short-circuit logical operators like <code>&amp;&amp;</code> and <code>||</code>
    with their non-short-circuiting bitwise equivalents <code>&amp;</code> and <code>|</code>.
  </li>
  <li>
    Using <code>==</code> instead of <code>.equals</code> to compare strings.
  </li>
  <li>
    Ignoring the return value from a non-void method.
  </li>
</ul>
<p>
  As if this data wasn't enough, the authors also compared this data
  to a survey of what teachers believe about student errors (see Brown
  and Altadmri,
  "<a href="http://www.twistedsquare.com/Educators.pdf">Investigating
  Novice Programming Mistakes: Educator Beliefs vs Student Data</a>",
  ICER'14, http://dx.doi.org/10.1145/2632320.2632343).  Their main
  finding: "…educators formed only a weak consensus about which
  mistakes are most frequent, that their rankings bore only a moderate
  correspondence to the students in the Blackbox data, and that
  educators' experience had no effect on this level of agreement."  It
  may be years before textbooks begin to reflect these insights, and
  decades before they start to influence language design, but at least
  we now know that better is possible.
</p>
