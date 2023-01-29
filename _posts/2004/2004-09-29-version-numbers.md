---
title: "Version Numbers"
date: 2004-09-29 16:19:33
year: 2004
---
Since I was asked... Most projects I've worked on have used something
like the following scheme to identify releases.  A version number like "6.2.3.1407" means:
<ul>
  <li>major version 6</li>
  <li>minor version 2</li>
  <li>patch 3</li>
  <li>build 1407</li>
</ul>
The major version number is only incremented when significant changes
are made.  In practice, "significant" means "changes that make this
version's data/configuration/whatever impossible for older versions
to read".  In practice, major version numbers are often under the
control of the marketing department—if a competitor releases a
new major version, we'd pretty much have to as well.

Minor version numbers are what most people think of as releases.  If
you've added a few new features, changed part of the GUI, etc., you
increment the minor version number and throw it to customers.

Patches are things that don't have their own installers.  If, for
example, you need to change one HTML form, or one DLL, you will often
just mail that out to customers, along with instructions about where
to put it, rather than creating a new installer.  You should still
give it a number, though, and make an entry in your release log [<a href="#1">1</a>].

The build number is incremented every time you create a new
version of the product for QA to test.  Build numbers are never reset,
i.e. you don't go from 5.2.2.1001 to 6.0.0.0, but from 5.2.2.1001 to
6.0.0.1002, and so on.  Build numbers are what developers care about:
they're often only matched up with version numbers after the fact (i.e.
you create build #1017, QA says, "Yeah, it looks good," so you say,
"All right, this'll be 6.1.0," and voila, you have 6.1.0.1017.)

Finally, groups will sometimes identify pre-releases as "beta 1", "beta 2", and so on, as in "6.2 beta 2".  Again, this label is usually attached to a particular build after the fact—you wait until QA (or whoever) says that build #1017 is good enough to send out to customers, then tag it in version control.

[<a name="1"></a>1] A "release log" is a file (often a spreadsheet) that records exactly what was shipped to whom, when.
