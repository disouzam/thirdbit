---
title: "An Empirical Investigation into Programming Language Syntax"
date: 2014-01-29 10:00:00
year: 2014
original: nwit
---
<p><a href="http://web.cs.unlv.edu/stefika/">Andreas Stefik</a> and <a href="http://microbialgenomics.org/people/susanna-siebert/">Susanna Siebert</a>: "An Empirical Investigation into Programming Language Syntax." ACM Transactions on Computing Education, 13(4), Nov. 2013.</p>

<blockquote><em>
  Recent studies in the literature have shown that syntax remains a
  significant barrier to novice computer science students in the
  field. While this syntax barrier is known to exist, whether and how
  it varies across programming languages has not been carefully
  investigated. For this article, we conducted four empirical studies
  on programming language syntax as part of a larger analysis into
  the, so called, programming language wars. We first present two
  surveys conducted with students on the intuitiveness of syntax,
  which we used to garner formative clues on what words and symbols
  might be easy for novices to understand. We followed up with two
  studies on the accuracy rates of novices using a total of six
  programming languages: Ruby, Java, Perl, Python, Randomo, and
  Quorum. Randomo was designed by randomly choosing some keywords from
  the ASCII table (a metaphorical placebo). To our surprise, we found
  that languages using a more traditional C-style syntax (both Perl
  and Java) did not afford accuracy rates significantly higher than a
  language with randomly generated keywords, but that languages which
  deviate (Quorum, Python, and Ruby) did. These results, including the
  specifics of syntax that are particularly problematic for novices,
  may help teachers of introductory programming courses in choosing
  appropriate first languages and in helping students to overcome the
  challenges they face with syntax.
</em></blockquote>

<p>
  This paper is a follow-on to one we
  <a href="http://neverworkintheory.org/2011/10/24/an-empirical-comparison-of-the-accuracy-rates-of-novices-using-the-quorum-perl-and-randomo-programming-languages.html">wrote
  about</a> a couple of years ago that generated a lot of comments,
  many of them unpleasant.
  Stefik <a href="http://neverworkintheory.org/2011/10/27/author-response-quorum-vs-perl-vs-randomo-novice-accuracy-rates.html">responded</a>
  then, and he and Siebert have now followed up with several more
  studies that show:
</p>
<ol>
  <li>
    Programming language designers needlessly make programming
    languages harder to learn by not doing basic usability testing.
    For example, "...the three most common words for looping in
    computer science, for, while, and foreach, were rated as the three
    most unintuitive choices by non-programmers."
  </li>
  <li>
    C-style syntax, as used in Java and Perl, is just as hard for
    novices to learn as a randomly-designed syntax.  Again, this pain
    is needless, because the syntax of other languages (such as Python
    and Ruby) is significantly easier.
  </li>
</ol>

<p>
  They have also developed a technique called Token Accuracy Maps to
  make detailed studies of language syntax more methodical, and are
  using this to improve the design of a new language called Quorum
  that, wonder of wonders, incorporates feedback from studies of
  novice programmers to eliminate stumbling blocks.
</p>

<p>
  I would like to see every proposed change to widely-used languages
  go through similar testing before being incorporated into standards.
  More than that, I would like to see programmers demand this kind of
  evidence from language designers (and each other).  I suspect that
  would have a lot more impact than yet another type system or any
  number of sermons on the beauty of functional programming.
</p>

<p><em>Note that this paper is available
from <a href="http://web.cs.unlv.edu/stefika/Papers.php">the author's
website</a>, but only after a redirect to an ACM website that makes
you wait a few seconds for another redirect, because that's what the
ACM does to encourage people to take research seriously.</em></p>
