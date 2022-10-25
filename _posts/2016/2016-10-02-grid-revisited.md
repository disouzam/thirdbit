---
title: "Revisiting the Anatomy and Physiology of the Grid"
date: 2016-10-02 01:02:03
year: 2016
original: nwit
---
<p>
  Chris A. Mattmann, Joshua Garcia, Ivo Krka, Daniel Popescu, and Nenad Medvidovic:
  "Revisiting the Anatomy and Physiology of the Grid".
  <em>Journal of Grid Computing</em>, 13(1), March 2015,
  <a href="http://link.springer.com/article/10.1007/s10723-015-9324-0">http://link.springer.com/article/10.1007/s10723-015-9324-0</a>.
</p>
<blockquote>
  <em>
    A domain-specific software architecture (DSSA) represents an
    effective, generalized, reusable solution to constructing software
    systems within a given application domain. In this paper, we
    revisit the widely cited DSSA for the domain of grid computing. We
    have studied systems in this domain over the last ten
    years. During this time, we have repeatedly observed that, while
    individual grid systems are widely used and deemed successful, the
    grid DSSA is actually underspecified to the point where providing
    a precise answer regarding what makes a software system a grid
    system is nearly impossible. Moreover, every one of the existing
    purported grid technologies actually violates the published grid
    DSSA. In response to this, based on an analysis of the source
    code, documentation, and usage of eighteen of the most pervasive
    grid technologies, we have significantly refined the original grid
    DSSA. We demonstrate that this DSSA much more closely matches the
    grid technologies studied. Our refinements allow us to more
    definitively identify a software system as a grid technology, and
    distinguish it from software libraries, middleware, and
    frameworks.
  </em>
</blockquote>
<p>
  Ernest Rutherford may or may not have once said that
  <a href="http://quoteinvestigator.com/2015/05/08/stamp/">all science is either physics or stamp collecting</a>.
  It's generally assumed that if he did, he meant it disparagingly,
  but if the physicists of his generation hadn't collected subatomic particles,
  he probably wouldn't have won the Nobel Prize.
  Until stamps are collected and organized,
  theoreticians don't know what patterns and exceptions they need to explain;
  to put it another way, no finches, no Darwin.
</p>
<p>
  This paper makes two significant contributions to the "natural history" side of software engineering.
  First, it compares 18 grid computing systems
  to a reference architecture popularized by a pair of influential papers written in 2001-02,
  and painstakingly itemizes four kinds of discrepancies:
  upcalls, skipped layers, multi-layer components, and empty layers.
  Second, it presents an improved reference architecture
  that eliminates 85% of these discrepancies,
  i.e.,
  that is a better (though not perfect) "theory" of grid computing.
</p>
<p>
  It was interesting to read this paper so soon after
  <a href="{{'/2016/09/30/rethinking-git.html' | relative_url}}">Perez De Rosso and Jackson's analysis of Git</a>:
  Mattmann et al. seem less concerned with developing a general framework for critiquing software architecture,
  but have invested several years in an exhaustive (and no doubt exhausting) compare-and-contrast exercise.
  Their time has paid off handsomely,
  and we can only hope that others will do similar work in other application areas.
</p>
<p>
  <em>My thanks to <a href="http://danielskatz.org/">Daniel Katz</a> for suggesting this paper.</em>
</p>
