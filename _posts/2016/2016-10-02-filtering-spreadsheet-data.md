---
title: "FIDEX: Filtering Spreadsheet Data using Examples"
date: 2016-10-02 01:02:03
year: 2016
original: nwit
---
<p>
  Xinyu Wang, Sumit Galwani, and Rishabh Singh:
  "FIDEX: Filtering Spreadsheet Data using Examples".
  OOPSLA 2016,
  <a href="https://www.cs.utexas.edu/~xwang/pubs/oopsla16.pdf">https://www.cs.utexas.edu/~xwang/pubs/oopsla16.pdf</a>.
</p>
<blockquote>
  <em>
    <p>
      Data filtering in spreadsheets is a common problem faced by
      millions of end-users. The task of data filtering requires a
      computational model that can separate intended positive and
      negative string instances. We present a system, FIDEX, that can
      efficiently learn desired data filtering expressions from a
      small set of positive and negative string examples.
    </p>
    <p>
      There are two key ideas of our approach. First, we design an
      expressive DSL to represent disjunctive filter expressions
      needed for several real-world data filtering tasks. Second, we
      develop an efficient synthesis algorithm for incrementally
      learning consistent filter expressions in the DSL from very few
      positive and negative examples. A DAG-based data structure is
      used to succinctly represent a large number of filter
      expressions, and two corresponding operators are defined for
      algorithmically handling positive and negative examples, namely,
      the intersection and subtraction operators. FIDEX is able to
      learn data filters for 452 out of 460 real-world data filtering
      tasks in real time (0.22s), using only 2.2 positive string
      instances and 2.7 negative string instances on average.
    </p>
  </em>
</blockquote>
<p>
  Another solid piece of engineering,
  another reason to be sad that I won't be at SPLASH this year.
  The authors start by creating a small language to describe
  the things that people do when filtering spreadsheet data,
  like starts-with, ends-with, matches, and contains.
  They then create a sound, complete, and efficient algorithm
  that learns how to construct filter expressions using these operations
  along with intersection and subtraction operators.
  They then show that their algorithm learns both quickly enough and well enough
  to be useful to real people.
  And yes,
  it only works on strings (for now),
  and cannot yet handle noisy examples,
  but given the quality of the engineering shown off here,
  I'm confident the authors will have lots to report on both fronts soon.
</p>
