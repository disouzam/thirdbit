---
title: "Pull-Based Development"
date: 2016-06-07 01:02:03
year: 2016
original: nwit
---
<p>
  Georgios Gousios, Margaret-Anne Storey, and Alberto Bacchelli:
  "Work Practices and Challenges in Pull-Based Development: The Contributor's Perspective".
  ICSE, May 2016, http://dx.doi.org/10.1145/2884781.2884826,
  <a href="http://sback.it/publications/icse2016b.pdf">http://sback.it/publications/icse2016b.pdf</a>.
</p>
<blockquote>
  <em>
    We conducted a survey with 645 top contributors to active OSS
    projects using the pull-based model on GitHub, the prevalent
    social coding site. We also analyzed traces extracted from
    corresponding GitHub repositories.  Our research shows that:
    contributors have a strong interest in maintaining awareness of
    project status to get inspiration and avoid duplicating work, but
    they do not actively propagate information; communication within
    pull requests is reportedly limited to low-level concerns and
    contributors often use communication channels external to pull
    requests; challenges are mostly social in nature, with most
    reporting poor responsiveness from integrators; and the increased
    transparency of this setting is a confirmed motivation to
    contribute.  Based on these findings, we present recommendations
    for practitioners to streamline the contribution process and
    discuss potential future research directions.
  </em>
</blockquote>
<p>
  How do developers actually use GitHub's pull-based workflow,
  particularly its support for concurrent development and extensive
  pre-commit review?  Are most PRs really self-contained?  How do the
  people responsible for merging tell whether a change is right?  (It
  turns out that testing is used much more often than code review,
  which surprised me.)  And how do people communicate: through issues,
  through pull requests, or through email and IRC?  (It turns out that
  "minimal PRs" are used almost as often as issues, and that both are
  used more than chat and email, which has some interesting
  implications for design.)  While research based on GitHub has its
  limits, which are ably analyzed
  in <a href="http://modeling-languages.com/wp-content/uploads/2016/03/2016-MSR.pdf">this
  paper by Cosentino, Luis, and Cabot</a>, this is the kind of paper
  that ought to feed directly into both the undergraduate curriculum
  and professional development.
</p>
