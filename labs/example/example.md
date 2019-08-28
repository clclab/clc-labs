---
title: Example lab
credits: Written by Bastiaan van der Weij and Dieuwke Hupkes in 2016.  
  Updated by Peter Dekker (2017), Bas Cornelissen (2017, 2018, 2019) and Marianne de Heer Kloots (2018).
bibliography: labs/evolution-of-communication/references.bib
reference-section-title: References
link-citations: true
toc: false
layout: lab
---

This is an example lab.

Mathematics
===========

- Works on Jekyll
- Works in PDF
- Does not work on GitHub

You can use inline mathematics: `$a^2 + b^2 = c^2$` renders to $a^2 + b^2 = c^2$.
Display math: `$$ ... $$` but with empty lines above and below (otherwise it is
rendered as inline math):

$$ a^2 + b^2 + c^2$$

You can also align multiple equations. The syntax is important here since 
MathJax and Pandoc differ slightly. The `\begin{align} ... \end{align}` block
need not have empty lines above and below. If not, the paragraph is 
uninterrupted in the PDF.

```latex
\begin{align}
    x &= \sum_{i=1}^N a_i^2 + b_i^2 + c_i^2 \\\ % <-- Use 3 slashes!
    N &= 5 + \text{argmin}_{x \in \mathbb{R}} x^2
\end{align}
```

\begin{align}
x &= \sum_{i=1}^N a_i^2 + b_i^2 + c_i^2 \\\
N &= 5 + \text{argmin}_{x \in \mathbb{R}} x^2
\end{align}

Question blocks
===============

- Works on Jekyll
- Works in PDF
- Does not work on GitHub

Question blocks get special styling and are delimited by `<div class="question">
... </div>`. A Lua filter converts this to a special question environment
before Pandoc renders the PDF. On GitHub, it is simply ignored.

<div class="question">
What are the optimal $S$ and $R$, for maximal communicative success in a
population? How is ambiguity (i.e., one signal with multiple meanings)
reflected in S and R matrices? And synonymity (two signals that have the
same meaning).
</div>

<div class="exercise">
What are the optimal $S$ and $R$, for maximal communicative success in a
population? How is ambiguity (i.e., one signal with multiple meanings)
reflected in S and R matrices? And synonymity (two signals that have the
same meaning).
</div>

<div class="question">
What are the optimal $S$ and $R$, for maximal communicative success in a
population? How is ambiguity (i.e., one signal with multiple meanings)
reflected in S and R matrices? And synonymity (two signals that have the
same meaning).
</div>


Code highlighting
=================

```javascript
var x = 2
```
