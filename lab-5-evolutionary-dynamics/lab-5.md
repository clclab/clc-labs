---
title: "Evolutionary dynamics and statistical universals"
author: BSc Psychobiology, UvA
bibliography: refs
numbersections: true
header-includes:
    - \usepackage{graphicx}
    - \usepackage{fullpage}
    - \usepackage{graphicx}
    - \usepackage[round, authoryear]{natbib}
    - \usepackage{fixltx2e}
    - \bibliographystyle{plainnat}
    - \input{../labs.tex}
    - \usepackage{listings}
...

\newcommand{\qzz}{q_{00}}
\newcommand{\gain}{q_{01}}
\newcommand{\qoo}{q_{11}}
\newcommand{\loss}{q_{10}}

\begin{itemize}
\action These are actions for you to do
\ask These are questions
\askstar This is a question that could be on the exam
\end{itemize}

# Goals

Last week we had some first-hand experience with music and language features. This week we will study in more detail at the phylogenetic analysis. Specifically, we'll take a close look at the methods used by \cite{Savage2015} to find statistical universals. By the end of this lab you will know about:

* probabilistic models of evolutionary dynamics;
* fitting these models to phylogenetic trees

# Introduction

In their paper, \cite{Savage2015} look for so called *statistical universals* in the world's music. In earlier work, \cite{Brown2013} proposed a comprehensive list of candidate universals in music. Savage et al. take up the challenge of *empirically* testing the validity of these candidate universals. The empirical data used in their study is a set of recordings accompanying the *Garland Encyclopedia of World Music* (GEWM), chosen for the wide geographical and cultural coverage of this dataset. 

One major issue for the identification of musical universals is one that we encountered last week: music from all over the world is so tremendously diverse, how are we to identify any universals *at all*? Brown and Jordania argue that absolute universals in human cultural phenomena, that is a feature that occurs without fail in every instance of the phenomenon at any time, do not exist. Instead, they promote the search for statistical universals.   

\begin{itemize}
\askstar What is a statistical universal?
\askstar Can you think of an example of an absolute universal?
\end{itemize}

As \cite{Savage2015} point out, another issue that's particular to the identification of *statistical* universals, is the fact that different cultures have different degrees of historical relatedness. This is an issue for statistical analysis, because the occurrence of features in different cultures cannot be treated as independent. To overcome this, Savage et al. treat the different recordings as the products of *cultural* evolution and resort to special kind of statistical analysis that models the *evolutionary dynamics*. This analysis can be used to predict what the expected distribution of features would be if the evolution had been running for a long time. In this lab, we'll go study this analysis in more detail.

# Finding musical universals

Savage et al. propose 32 *binary* features (features that can have just two possible values: ***1*** for present and ***0*** for absent) to empirically test the validity of many of the candidate universals proposed by \cite{Brown2013}. Using this classification scheme, Savage et al. *encode* each recording as a vector indicating the presence or absence of each of the 32 features. 

The trick to finding statistical universals is to find out how each has changed over evolutionary time and derive the evolutionary "forces" (the evolutionary dynamics) working on each feature. Once these forces are known, we can calculate the expected frequency of occurrence of any feature in a hypothetical population in the far future, when evolution has been running for a long time. Any feature that is expected to occur in significantly more than half of this future population is considered to be a statistical universal by Savage et al.

\begin{itemize}
\ask Which of the following features of an organism are binary?
\begin{itemize}
\item The color of the organism's hair.
\item The organism's average walking speed.
\item Whether the organism is bipedal.
\item The amount of wings on the organism.
\item The ability to remain under water for longer than 5 minutes.
\end{itemize}
\end{itemize}

So how will we go about calculating the evolutionary "forces"? First, we'll need to run a phylogenetic analysis.  

With a binary classification scheme, Savage et al. encoded each recording in the GEWM as a vector of zeros and ones. This representation can be treated as the recording's genotype. The genotype specifies which traits are active in a particular recording. We now have a representation that can be subjected to evolutionary analysis.

As a simplified example, let's assume a classification scheme with three binary features: 1) the presence of lyrics 2) the use of multiple instruments 3) use of percussion. Using this scheme, we can encode a song as a vector of features. Let's say that a value of $\mathbf{1}$ indicates the presence of a feature and a value of $\mathbf{0}$ indicates its absence.

The particular model used by Savage et al. is a continuous-time Markov process. This might sound intimidating, but don't worry; we'll go through the steps of applying such a model to phylogenetic analysis in this lab. If you're interested reading more about this, have a look at \cite{Pagel1994}. Pagel introduced this method as a way of testing the hypothesis that two discrete traits are correlated. Sage et al. use this method to find what they call "universal relationships", but to find statistical universals, a simpler application of Pagel's method is used.

# Modeling phylogenetic change with Markov processes

*Markov models* can be used to model changes in a stochastic variable over time. Markov models are based on a simplifying assumption, called the Markov assumption, or Markov property. By saying that a process has the Markov property, we mean that the probability of the next state of a stochastic variable depends only on the current state, and not on previous states.

For example, say we want to predict the location, velocity and direction of a spear thrown by an athlete. In order to predict this location, we only need to know the spear's current location, direction and speed. The previous locations and speeds of the spear are irrelevant.

\begin{itemize}
\askstar Which of the following processes have the Markov property?
\begin{itemize}
\item Drawing marbles from a vase filled with red and blue marbles *without replacement*
\item Drawing marbles from a vase filled with red and blue marbles *with replacement*
\item The next word in a sentence given the current word. 
\end{itemize}
\end{itemize}

Let's return to the three encodings we created earlier in this lab. This encoding consisted of a vector of three binary features. We'll assume that each feature is a trait. In this lab, we'll model how a trait changes from generation to generation as a Markov model. We will assume that we can create such a model for each trait independently. In other words, we assume that the way a trait changes from generation to generation is independent from the presence or absence of other traits.

We'll say that the *state* of a trait in a particular generation is whether it's present or absent (1 or 0 in our encoding scheme). Say a particular trait is present at generation $x$. The model we're interested in should give us the probability that that same trait is still present or absent in the next generation. 

\begin{itemize}
\ask Our binary traits have only two states: 1 (present) or 0 (absent). What are the four possible *state transitions* a trait can go through from one generation to the next?
\end{itemize}

Let's associate probabilities with our state transitions. We'll call these state transition probabilities $\qzz$, $\gain$, $\qoo$ and $\loss$.\footnote{In a continuous-time Markov model, we speak of transition \textit{rates}. However, for now it's okay to think of them as transition probabilities.} The subscripts indicate what state transition the probability is associated with. E.g. $\gain$ is the probability of a trait to go from absent (0) to present (1) over the course of one generation. Because of the Markov assumption, the transition probabilities depend only on the state of a trait in the last generation. 

Savage et al. speak of a gain rate and a loss rate. The *gain rate* corresponds to the probability of acquiring a trait, the loss rate corresponds to the probability of losing a trait.

\begin{itemize}
\ask Which of our state transition probabilities ($\qzz$, $\gain$, $\qoo$ or $\loss$) corresponds to the gain rate and which one corresponds to the loss rate?
\end{itemize}

Note that we don't *know* the state transition probabilities yet, we'll just assume that they're there. We call such unknown quantities the *parameters* of a model. Note that Savage et al. write that the gain and loss rate are the only two parameters of the model, while we just identified *four* parameters. 

\begin{itemize}
\askstar Can you express $\qzz$ and $qoo$ in terms of the gain ($\gain$) and loss ($\loss$) rate?
\end{itemize}



* Create a phylogenetic tree of our toy data
* Observe how we don't know the states of a trait at non-leaf nodes
* Calculate the likelihood of the model under given parameters and a given evolutionary history (state at non-leaf nodes) 
* Use R to plot a 3D likelihood surface (along the dimensions of gain and loss)
* Find the maximum likelihood solution for Q

\begin{itemize}
\askstar What is the difference between a statistical universal and a non-statistical universal?
\askstar Are there absolute universals in music?
\end{itemize}

\begin{equation*}
Q = \left( 
\begin{array}{cc}
q_{00} & q_{01} \\
q_{10} & q_{11} \\
\end{array}
\right)
\end{equation*}

A quote from Savage et al.:

> We... ...made all branch lengths equal by assigning them a value of 1. It should be noted that this decision means that we are implicitly assuming that the rate of evolution is punctuated in such a way that trait evolution is related to the points at which lineages diverge or “speciate.” 

* Make sure this assumption is understood

\bibliography{refs}
