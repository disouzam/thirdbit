---
title: "Experiences with OpenID?"
date: 2006-12-27 12:20:23
year: 2006
---
As regular readers will know, one of the features I like most in <a href="http://www.drproject.org">DrProject</a> (and its predecessor, <a href="http://trac.edgewall.org">Trac</a>) is the RSS feed it automatically creates showing events from each project.  Unfortunately, we've had to disable the feeds for class projects at <a href="http://www.cs.toronto.edu">U of T</a>, since we don't want students in one group to be able to see the check-in comments or ticket updates of another, and web-based blog reading services like <a href="http://www.bloglines.com">Bloglines</a> haven't standardized on an authentication mechanism.

However, I've been seeing a lot of buzz about <a href="http://www.openid.net">OpenID</a> recently, which has me wondering whether it's worth rolling the dice and incorporating support for it into <a href="http://www.drproject.org">DrProject</a>.  Oh, and running some sort of authentication server in the department, tied into the IDs students are automatically allocated for courses.  I don't want to venture into these waters without a guide --- anyone out there done this yet?
