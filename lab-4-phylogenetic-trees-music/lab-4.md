---
title: "Phylogenetic trees: Music"
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

Last week, we read a paper by \cite{Savage2015}. In this computer lab we will study one of the methods they used in detail. By the end of this lab you will understand:

* how to construct probabililistic models of evolutionary dynamics;
* what a Markov process is;
* what a maximum likelihood solution is.

# Theory

In their paper, \cite{Savage2015} try to find so called *statistical universals* in the world's music. To do this, they make use of the *Garland Encyclpedia of World Music*. Earlier, \cite{Brown2013} proposed a list of candidate universals. Savage et al. use a two music classification schemes to operationalize these candidate universals in the shape of 32 binary (only having two possible states; e.g. 1 and 0 or present and absent) features. Using this scheme, Savage et al. represent each song as a vector indicating the presence or absence of each of the 32 features.

For example, let's assume a simple encoding scheme with three features: 1) the presence of lyrics 2) the use of multiple instruments 3) use of percussion. Using this scheme, we can *encode* a song as a vector of features. Let's say $\mathbf{1}$ means a feature is present and $\mathbf{0}$ means a feature is absent.

\begin{itemize}
\action Listen to recordings in the materials folder. Encode each recording as a vector of three numbers, using our simple classification scheme.
\end{itemize}

We can view this encoding as a genotype, representing the particular traits that are active in a particular recording. We now have a representation that can be subjected to evolutionary analysis.

In order to find statistical universals, Savage et al. used phylogenetic analysis methods.

\begin{itemize}
\askstar Why did \cite{Savage2015} resort to phylogenetic analysis? Why didn't they just look at prevalence of the binary features in their encodings?
\end{itemize}

The goal of Savage et al. is not to reconstruct the underlying phylogeny of the recordings. Instead, they are interested in finding statistical universals while compensating for the effect of cultural transmission. The trick they use to achieve this is to use a phylogenetic analysis to create a statistical model of the evolutionary dynamics. This model was used to simulate what would happen (i.e. which features would emerge) if the evolution would run for a long time. 

The particular model used by Savage et al. is a continuous-time Markov process. This might sound intimidating, but don't worry. We'll go through the steps of applying such a model to phylogenetic analysis in this lab. If you're interested reading more about this, have a look at \cite{Pagel1994}. Pagel introduced this method as a way of testing the hypothesis that two discrete traits are correlated. Sage et al. use this method to find what they call "universal relationships", but to find statistical universals, a simpler application of Pagel's method is used.

# Modeling phylogenetic change with Markov processes

*Markov models* can be used to model changes in a stochastic variable over time. These models are based on a simplifying assumption, called the Markov assumption, or Markov property. By saying that a process has the Markov property, we mean that the probability of the next state of a stochastic variable depends only on the current state, and not on previous states. Such processes are called Markov processes.

For example, say you know the velocity and direction of a spear thrown by an athlete. In order to predict where the spear will be one second later, all we need to know is where the spear is now, what direction it is traveling and at what speed. The change in location given 

\begin{itemize}
\askstar For which of the following processes have the Markov property?
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

Let's associate probabilities with our state transitions. We'll call these state transition probabilities $\qzz$, $\gain$, $\qoo$ and $\loss$.\footnote{In a continuous-time Markov model, we speak of transition \textit{rates}. However, for now it's okay to think of them as transition probabilities.} Because of the Markov assumption, the transition probabilities depend only on the state of a trait in the last generation. 

Note that we don't *know* the state transition parameters yet, we'll just assume that they're there. Savage et al. speak of a gain rate and a loss rate. The gain rate corresponds to $\gain$ and the loss rate to $\loss$.  

\begin{itemize}
\askstar Savage et al. write that the gain and loss rate are the only two parameters of the model. Can you express $\qzz$ and $qoo$ in terms of the gain and loss rate?
\end{itemize}

* Create a phylogenetic tree of our toy data
* Observe how we don't know the states of a trait at non-leaf nodes
* Calculate the likelihood of the model under given parameters and a given evolutionary history (state at non-leaf nodes) 
* Use R to plot a 3D likelihood surface (along the dimensions of gain and loss)
* Find the maximum likelihood solution for Q

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
