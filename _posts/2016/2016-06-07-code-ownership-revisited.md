---
title: "Code Ownership Revisited"
date: 2016-06-07 01:02:03
year: 2016
original: nwit
---
<p>
  Patanamon Thongtanunam, , Shane McIntosh, , Ahmed E. Hassan, and , Hajimu Iida:
  "Revisiting Code Ownership and its Relationship with Software Quality in the Scope of Modern Code Review".
  ICSE, May 2016, http://dx.doi.org/10.1145/2884781.2884852,
  <a href="http://sail.cs.queensu.ca/Downloads/ICSE2016_RevisitingCodeOwnershipAndItsRelationshipWithSoftwareQualityInTheScopeOfModernCode%20Review.pdf">http://sail.cs.queensu.ca/Downloads/ICSE2016_RevisitingCodeOwnershipAndItsRelationshipWithSoftwareQualityInTheScopeOfModernCode%20Review.pdf</a>.
</p>
<blockquote>
  <em>
    Code ownership establishes a chain of responsibility for modules
    in large software systems. Although prior work uncovers a link
    between code ownership heuristics and software quality, these
    heuristics rely solely on the authorship of code changes. In
    addition to authoring code changes, developers also make important
    contributions to a module by reviewing code changes. Indeed,
    recent work shows that reviewers are highly active in modern code
    review processes, often suggesting alternative solutions or
    providing updates to the code changes. In this paper, we
    complement traditional code ownership heuristics using code review
    activity. Through a case study of six releases of the large Qt and
    OpenStack systems, we find that: (1) 67%-86% of developers did not
    author any code changes for a module, but still actively
    contributed by reviewing 21%-39% of the code changes, (2) code
    ownership heuristics that are aware of reviewing activity share a
    relationship with software quality, and (3) the proportion of
    reviewers without expertise shares a strong, increasing
    relationship with the likelihood of having post-release defects.
    Our results suggest that reviewing activity captures an important
    aspect of code ownership, and should be included in approximations
    of it in future studies.
  </em>
</blockquote>
<p>
  Code ownership is one of those things that everyone understands
  intuitively, but which is hard to quantify.  This paper looks at how
  our notion of ownership should change once reviewing is given equal
  weight with writing, i.e., once we accept that some people are
  code critics or editors (in the sense of film critics or newspaper
  editors) as well as authors.  More importantly, it shows that having
  people in those roles seems to reduce post-release defects.  This
  has interesting implications for the design of tools:
  <code>git blame</code> can tell someone who gets credit for writing
  various parts of a package, but so far as I know, there isn't yet a
  tool that will give people credit for their reviewing work.
</p>
