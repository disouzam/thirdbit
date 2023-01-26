---
title: "Don't Touch My Code!"
date: 2011-09-05 14:21:16
year: 2011
original: nwit
---
<p>Christian Bird, Nachiappan Nagappan, Brendan Murphy, Harald Gall, and Premkumar Devanbu: <a href="http://www.cabird.com/papers/bird2011dtm.pdf">"Don't Touch My Code! Examining the Effects of Ownership on Software Quality."</a> ESEC/FSE'11, 2011.</p>
<blockquote><em>Ownership is a key aspect of large-scale software development. We examine the relationship between different ownership measures and software failures in two large software projects: Windows Vista and Windows 7. We find that in all cases, measures of ownership such as the number of low-expertise developers, and the proportion of ownership for the top owner have a relationship with both pre-release faults and post-release failures. We also empirically identify reasons that low-expertise developers make changes to components and show that the removal of low-expertise contributions dramatically decreases the performance of contribution based defect prediction. Finally we provide recommendations for source code change policies and utilization of resources such as code inspections based on our results.</em></blockquote>
<p>I used to tell my students that a paper's abstract should be a summary, not a movie trailer. When I read, "We find that... measures of ownership... have a relationship with both pre-release faults and post-release failures," my reaction is, "What kind of relationship?" And when a paper's authors say, "We... identify reasons that low-expertise developers make changes to components," I want to grab my red pen and scribble, "Summarize them here!"</p>
<p>Fortunately, this paper's abstract is the only thing about it that I don't like. Over the course of its 11 pages, its authors explore three related questions:</p>
<ol>
	<li>Are higher levels of ownership associated with less defects?</li>
	<li>Is there a negative effect when a software entity is developed by many people with low ownership?</li>
	<li>Are these effects related to the development process used?</li>
</ol>
<p>They start by defining their units of measurement (a compiled binary such as a .dll or .exe), what they mean by major and minor contributors, and how they measure ownership. After grinding their data (they have <em>lots</em> of data), they come up with Table 1:</p>
<table border="1">
<tbody>
<tr>
<td colspan="2"></td>
<td colspan="2" align="center">Windows Vista</td>
<td colspan="2" align="center">Windows 7</td>
</tr>
<tr>
<td align="center">Category</td>
<td align="center">Metric</td>
<td align="center">Pre-release
Failures</td>
<td align="center">Post-Release
Failures</td>
<td align="center">Pre-release
Failures</td>
<td align="center">Post-Release
Failures</td>
</tr>
<tr>
<td rowspan="4" align="center">Ownership
Metrics</td>
<td align="center">Total</td>
<td align="center">0.84</td>
<td align="center">0.70</td>
<td align="center">0.92</td>
<td align="center">0.24</td>
</tr>
<tr>
<td align="center">Minor</td>
<td align="center">0.86</td>
<td align="center">0.70</td>
<td align="center">0.93</td>
<td align="center">0.25</td>
</tr>
<tr>
<td align="center">Major</td>
<td align="center">0.26</td>
<td align="center">0.29</td>
<td align="center">-0.40</td>
<td align="center">-0.14</td>
</tr>
<tr>
<td align="center">Ownership</td>
<td align="center">-0.49</td>
<td align="center">-0.49</td>
<td align="center">-0.29</td>
<td align="center">-0.02</td>
</tr>
<tr>
<td rowspan="3" align="center">"Classic"
Metrics</td>
<td align="center">Size</td>
<td align="center">0.75</td>
<td align="center">0.69</td>
<td align="center">0.70</td>
<td align="center">0.26</td>
</tr>
<tr>
<td align="center">Churn</td>
<td align="center">0.72</td>
<td align="center">0.69</td>
<td align="center">0.71</td>
<td align="center">0.26</td>
</tr>
<tr>
<td align="center">Complexity</td>
<td align="center">0.70</td>
<td align="center">0.53</td>
<td align="center">0.56</td>
<td align="center">0.37</td>
</tr>
<tr>
<td colspan="6" align="center"><em>Bivariate Spearman correlation of ownership and code metrics with pre- and post-release failures in Windows Vista and Windows 7.
All correlations are statistically significant except for that of Ownership and post-release failures in Windows 7.</em></td>
</tr>
</tbody>
</table>
<p>("Total" stands for the total number of contributors, "Major" and "Minor" for the number of major and minor contributors, respectively, and "Ownership" for the proportion of ownership of the contributor with the highest proportion of ownership—how much a single person owns that piece of code.)</p>
<p>There's a lot of information in that table, and I won't try to squeeze it all into this blog post, but as a taste, it allows them to conclude that:</p>
<blockquote><em>The results indicated that pre- and post-release defects in had strong relationships with Minor, Total, and Ownership. In fact, Minor had a higher correlation with both pre- and post-release defects in Vista and pre-release defects in Windows 7 than any other metric that Microsoft collects!. Post-release failures for Windows 7 present a difficulty for analysis as at the time of this analysis many binaries had no post-release failures reported. Thus the correlation values between metrics and and post-release failures are noticeably lower than the other failure categories...</em></blockquote>
<p>Later, after teasing apart the contributions of major and minor contributors, and the effects of dependencies between components, they conclude that:</p>
<blockquote><em>...the minor contribution edges [in the contributions graph] provide the "signal" used by defect predictors that are based on the contribution network. Without them, the ability to predict failure prone components is greatly diminished, further supporting our hypothesis that they are strongly related to software quality.</em></blockquote>
<p>and:</p>
<blockquote><em>After controlling for known software quality factors, binaries with more minor contributors had more pre- and post-release failures in both versions of Windows.</em></blockquote>
<p>They then recommend that:</p>
<ol>
	<li>Changes made by minor contributors should be reviewed with more scrutiny.</li>
	<li>Potential minor contributors should communicate desired changes to developers experienced with the respective binary.</li>
	<li>Components with low ownership should be given priority by QA resources.</li>
</ol>
<p>Even if you can't apply their results directly to your own projects, they show that it is possible to analyze the impact of different software manufacturing practices methodically and quantitatively. The next time someone suggests that your team start doing X, Y, or Z, ask them if they have this kind of data to back up their recommendation. If they don't, you might consider giving them a copy of this paper...</p>
