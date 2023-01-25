---
title: "Finding Security Bugs"
date: 2016-04-26 01:02:03
year: 2016
original: nwit
---
<p>
  Joseph P. Near and Daniel Jackson:
  "Finding Security Bugs in Web Applications Using a Catalog of Access Control Patterns".
  ICSE'16, May 2016, http://dx.doi.org/10.1145/2884781.2884836,
  <a href="http://dspace.mit.edu/openaccess-disseminate/1721.1/102281">http://dspace.mit.edu/openaccess-disseminate/1721.1/102281</a>.
</p>
<blockquote>
  <em>
    We propose a specification-free technique for finding missing
    security checks in web applications using a catalog of access
    control patterns in which each pattern models a common access
    control use case.  Our implementation, SPACE, checks that every
    data exposure allowed by an application's code matches an allowed
    exposure from a security pattern in our catalog.  The only
    user-provided input is a mapping from application types to the
    types of the catalog; the rest of the process is entirely
    automatic.  In an evaluation on the 50 most watched Ruby on Rails
    applications on Github, SPACE reported 33 possible bugs–23
    previously unknown security bugs, and 10 false positives.
  </em>
</blockquote>
<p>
  A lot of programmers use object-relational mapping systems (ORMs)
  that provide a more-or-less declarative interface between their code
  and their database.  Far fewer have ever used tools
  like <a href="http://alloy.mit.edu/alloy/">Alloy</a>, which allow
  them to model the ways their program is supposed to behave, then
  look for counter-examples that violate those constraints.
  In this paper, the authors use Alloy to look for security bugs in
  Rails applications; the user has to express what's allowed as a set
  of role-based access control (RBAC) constraints, and then the tool
  looks for execution paths in the code that don't obey those rules.
</p>
<p>
  The three most impressive things in this work for me are (a) how
  straightforward the modeling is, (b) how low the false positive rate
  is, and (c) the fact that Alloy's home page includes a link to
  questions about it on Stack Overflow.  One thing I <em>didn't</em>
  find was a link to the source: as far as I can tell,
  the <a href="https://github.com/emina/kodkod">underlying solver</a>
  is available, but the only source I could find for Alloy itself
  bills itself as
  "<a href="https://github.com/beckus/AlloyAnalyzer">an unofficial copy</a>".
  If anyone can clarify its availability,
  please let us know.
</p>
