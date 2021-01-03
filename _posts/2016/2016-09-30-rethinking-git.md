---
title: "Purposes, Concepts, Misfits, and a Redesign of Git"
date: 2016-09-30 01:02:03
year: 2016
original: nwit
---
<p>
  Santiago Perez De Rosso and Daniel Jackson:
  "<a href="http://people.csail.mit.edu/sperezde/pre-print-oopsla16.pdf">Purposes, Concepts, Misfits, and a Redesign of Git</a>",
  <em>SPLASH 2016</em>.
</p>
<blockquote>
  <em>
    <p>
      Git is a widely used version control system that is powerful but
      complicated. Its complexity may not be an inevitable consequence
      of its power but rather evidence of flaws in its design. To
      explore this hypothesis, we analyzed the design of Git using a
      theory that identifies concepts, purposes, and misfits. Some
      well-known difficulties with Git are described, and explained as
      misfits in which underlying concepts fail to meet their intended
      purpose. Based on this analysis, we designed a reworking of Git
      (called Gitless) that attempts to remedy these flaws.
    </p>
    <p>
      To correlate misfits with issues reported by users, we conducted
      a study of Stack Overflow questions. And to determine whether
      users experienced fewer complications using Gitless in place of
      Git, we conducted a small user study. Results suggest our
      approach can be profitable in identifying, analyzing, and fixing
      design problems.
    </p>
  </em>
</blockquote>
<p>
  This paper presents a detailed, well-founded critique of one of the
  most powerful, but frustrating, tools in widespread use today.
  A follow-up to earlier work published in 2013, it is distinguished
  from most other discussion of software design by three things:
</p>
<ol>
  <li>
    <p>
      It clearly describes its design paradigm, which
      comprises <em>concepts</em> (the major elements of the user's
      mental model of the system), <em>purposes</em> (which motivate
      the concepts), and <em>misfits</em> (which are instances where
      concepts do not satisfy purposes, or contradict one another).
    </p>
  </li>
  <li>
    <p>
      It lays out Git's concepts and purposes, analyzes its main
      features in terms of them, and uses that analysis to identify
      mis-matches.
    </p>
  </li>
  <li>
    <p>
      Crucially, it then analyzes independent discussion of Git (on
      Stack Overflow) to see if users are stumbling over the misfits
      identified in step 2.
    </p>
  </li>
</ol>
<p>
  That would count as a major contribution on its own, but the authors
  go further.  They have designed a tool called Gitless that directly
  addresses the shortcomings they have identified, and the penultimate
  section of this paper presents a usability study that compares it to
  standard Git.  Overall, subjects found Gitles more satisfying and
  less frustrating than Git, even though there was no big difference
  in efficiency, difficulty, or confusion.  Quoting the paper, "This
  apparent contradiction might be due to the fact that all of the
  participants had used Git before but were encountering Gitless for
  the first time without any substantive training. Some participants
  (2 regular, 1 expert) commented that indeed their problems with
  Gitless were mostly due to their lack of practice using it."
</p>
<p>
  This paper is one of the best examples I have ever seen of how
  software designs ought to be critiqued.  It combines an explicit,
  coherent conceptual base, detailed analysis of a specific system,
  design grounded in that analysis, and an empirical check of that
  design.  Sadly, nothing shows the actual state of our profession
  more clearly than the way this work has been greeted:
</p>
<blockquote>
  <p>
    In some respects, this project has been a fool's errand. We picked
    a product that was popular and widely used so as not to be
    investing effort in analyzing a strawman design; we thought that
    its popularity would mean that a larger audience would be
    interested in our experiment. In sharing our research with
    colleagues, however, we have discovered a significant
    polarization. Experts, who are deeply familiar with the product,
    have learned its many intricacies, developed complex, customized
    workflows, and regularly exploit its most elaborate features, are
    often defensive and resistant to the suggestion that the design
    has flaws. In contrast, less intensive users, who have given up on
    understanding the product, and rely on only a handful of memorized
    commands, are so frustrated by their experience that an analysis
    like ours seems to them belaboring the obvious.
  </p>
</blockquote>
