---
title: "The MSR Cookbook: Mining a Decade of Research"
date: 2013-06-13 10:44:40
year: 2013
original: nwit
---
<p>Hadi Hemmati, Sarah Nadi, Olga Baysal, Oleksii Kononenko, Wei Wang, Reid Holmes, and Michael W. Godfrey: "The MSR Cookbook: Mining a Decade of Research". <cite>ICSE'13</cite>, 2013, <a href="https://cs.uwaterloo.ca/~obaysal/msr2013_hemmati.pdf">https://cs.uwaterloo.ca/~obaysal/msr2013_hemmati.pdf</a>.</p>
<blockquote><em>The Mining Software Repositories (MSR) research community has grown significantly since the first MSR workshop was held in 2004. As the community continues to broaden its scope and deepens its expertise, it is worthwhile to reflect on the best practices that our community has developed over the past decade of research. We identify these best practices by surveying past MSR conferences and workshops. To that end, we review all 117 full papers published in the MSR proceedings between 2004 and 2012. We extract 268 comments from these papers, and categorize them using a grounded theory methodology. From this evaluation, four high-level themes were identified: data acquisition and preparation, synthesis, analysis, and sharing/replication. Within each theme we identify several common recommendations, and also examine how these recommendations have evolved over the past decade. In an effort to make this survey a living artifact, we also provide a public forum that contains the extracted recommendations in the hopes that the MSR community can engage in a continuing discussion on our evolving best practices.</em></blockquote>
<p>From modest beginnings a decade ago, the idea of applying data mining and machine learning techniques to software repositories has grown into a dynamic and game-changing research area. Instead of talking about how programmers <em>ought</em> to work, we can now say quite a bit about how they <em>actually</em> work, and about what practices work (or don't).</p>
<p>This paper summarizes what the MSR community has learned over those years. The authors went through 117 papers published in the MSR conference, extracted comments, and categorized them to produce the following insights and advice:</p>
<ul>
  <li>D1: SCM repositories contain a variety of noise; validation of heuristics and assumptions is essential.</li>
  <li>D2: The choice of code extraction approach (simple diff, building AST or CFG, etc.) is often heavily influenced by analysis cost.</li>
  <li>D3: When working with issue trackers, it is often best to only consider closed and fixed issues.</li>
  <li>D4: Social communication data requires extensive pre-processing before it can be used.</li>
  <li>D5: Plain text requires splitting, stemming, normalization and smoothing before analysis.</li>
  <li>D6: Text analyses should be manually verified (e.g., sampled) in addition to regular bias reporting.</li>
  <li>D7: Multiple online personas can cause individuals to be represented as multiple people.</li>
  <li>S1: Be careful to remove collinearities and deal with skewness when synthesizing models from data.</li>
  <li>S2: Carefully tuning parameters and performing sensitivity analysis can improve the modelling process.</li>
  <li>S3: Simple analyses often outperform their complex counterparts.</li>
  <li>S4: Be aware of the assumptions made by regression analyses.</li>
  <li>A1: Manual verification of all outputs is required.</li>
  <li>A2: Correlation analysis can be used to quickly check initial hypotheses about a set of data.</li>
  <li>A3: While precision and recall are valuable measures, be aware that other indicators may be more appropriate in a given context.</li>
  <li>A4: While applying rigorous statistical analyses is important, consider practical differences when drawing conclusions.</li>
  <li>R1: Sharing data, tools, and techniques helps push the community forward and is just Good Science<sup>TM</sup>.</li>
</ul>
<p>We look forward to more great work in the coming years.</p>
<p><em>Postscript: readers interested in this paper may also enjoy Kocaguneli et al's "Distibuted Development Considered Harmful?" (<a href="http://menzies.us/pdf/13distributed.pdf">http://menzies.us/pdf/13distributed.pdf</a>), which presents three rules for reporting research results to industrial practitioners.</em></p>
