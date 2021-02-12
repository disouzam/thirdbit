---
title: "Is Transactional Programming Actually Easier?"
date: 2011-08-24 09:30:24
year: 2011
original: nwit
---
<p>Christopher J. Rossbach, Owen S. Hofmann, and Emmett Witchel: "<a href="http://www.cs.utexas.edu/users/rossbach/pubs/ppopp012-rossbach.pdf">Is Transactional Programming Actually Easier?</a>" <cite>Principles and Practice of Parallel Programming</cite>, 2010.</p>
<blockquote><em>In this paper, we describe a user-study in which 147 undergraduate students in an operating systems course implemented the same programs using coarse and fine-grain locks, monitors, and transactions. We surveyed the students after the assignment, and examined their code to determine the types and frequency of programming errors for each synchronization technique. Inexperienced programmers found baroque syntax a barrier to entry for transactional programming. On average, subjective evaluation showed that students found transactions harder to use than coarse-grain locks, but slightly easier to use than fine-grained locks. Detailed examination of synchronization errors in the students' code tells a rather different story. Overwhelmingly, the number and types of programming errors the students made was much lower for transactions than for locks. On a similar programming problem, over 70% of students made errors with fine-grained locking, while less than 10% made errors with transactions.</em></blockquote>
<p><a href="http://en.wikipedia.org/wiki/Software_transactional_memory">Software Transactional Memory</a> (STM) has been receiving a lot of press lately as people try to find ways of making parallelism safe for human consumption. The results presented in this paper are a very hopeful sign: students who used it did better on simple problems than students using more traditional mechanisms. What's equally interested is that they <em>thought</em> they had done worse, possibly because of the "baroque syntax" the authors mention.  And once again, this paper highlights the fact that the usability of software engineering tools, including programming languages, can and should be studied empirically.</p>