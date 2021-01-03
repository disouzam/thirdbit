---
title: "Test-Driven Development"
date: 2016-10-05 01:02:03
year: 2016
original: nwit
---

<p>
  Davide Fucci, Giuseppe Scanniello, Simone Romano, Martin Shepperd, Boyce Sigweni, Fernando Uyaguari, Burak Turhan, Natalia Juristo, and Markku Oivo:
  "An External Replication on the Effects of Test-driven Development Using a Multi-site Blind Analysis Approach".
  ESEM 2016, <a href="http://people.brunel.ac.uk/~csstmms/FucciEtAl_ESEM2016.pdf">http://people.brunel.ac.uk/~csstmms/FucciEtAl_ESEM2016.pdf</a>.
</p>

<blockquote>
  <em>
    Context: Test-driven development (TDD) is an agile practice
    claimed to improve the quality of a software product, as well as
    the productivity of its developers. A previous study (i.e.,
    baseline experiment) at the University of Oulu (Finland) compared
    TDD to a test-last development (TLD) approach through a randomized
    controlled trial. The results failed to support the claims. Goal:
    We want to validate the original study results by replicating it
    at the University of Basilicata (Italy), using a different
    design. Method: We replicated the baseline experiment, using a
    crossover design, with 21 graduate students. We kept the settings
    and context as close as possible to the baseline experiment. In
    order to limit researchers bias, we involved two other sites (UPM,
    Spain, and Brunel, UK) to conduct blind analysis of the
    data. Results: The Kruskal-Wallis tests did not show any
    significant difference between TDD and TLD in terms of testing
    effort (p-value = .27), external code quality (p-value = .82), and
    developers' productivity (p-value = .83). Nevertheless, our data
    revealed a difference based on the order in which TDD and TLD were
    applied, though no carry over effect. Conclusions: We verify the
    baseline study results, yet our results raises concerns regarding
    the selection of experimental objects, particularly with respect
    to their interaction with the order in which of treatments are
    applied.
  </em>
</blockquote>

<p>
  This painstaking study is the latest in a long line to find that
  test-driven development (TDD) has little or no impact on development
  time or code quality.  Here, the authors repeated an earlier study
  with a couple of new wrinkles, and then blinded their data before
  giving it to someone else to analyze to remove any possibility of
  bias.  The result: no significant difference between TDD and
  iterative test-last (ITL) development.
</p>
<p>
  ...which still surprises me seven years after Turhan et al's
  meta-analysis in
  <a href="https://www.amazon.com/Making-Software-Really-Works-Believe/dp/0596808321/"><em>Making
  Software</em></a>.  reported the same result.  I don't program very
  much any more, but when I do, I feel that writing tests up front
  makes me more productive.  I'd like to be able to say that these
  researchers and others must be measuring the wrong things, or
  measuring things the wrong way, but after so many years and so many
  different studies, those of us who believe might just have to accept
  that our self-assessment is wrong.
</p>
