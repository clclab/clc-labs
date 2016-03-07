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
    - \usepackage{qtree}
...

\newcommand{\pzero}{p_{00}}
\newcommand{\gain}{p_{01}}
\newcommand{\pone}{p_{11}}
\newcommand{\loss}{p_{10}}

\begin{itemize}
\action These are actions for you to do
\ask These are questions
\askstar This is a question that could be on the exam
\end{itemize}

# Goals

Last week we had some first-hand experience with music and language features. This week we will study in more detail at the phylogenetic analysis. Specifically, we'll take a close look at the methods used by \cite{Savage2015} to find statistical universals. By the end of this lab you will know about:

* probabilistic models of evolutionary dynamics;
* fitting these models to phylogenetic trees

This lab will be a bit more theoretical than previous labs.

# Introduction

In their paper, \cite{Savage2015} look for so called *statistical universals* in the world's music. In earlier work, \cite{Brown2013} proposed a comprehensive list of candidate universals in music. Savage et al. take up the challenge of *empirically* testing the validity of these candidate universals. The empirical data used in their study is a set of recordings accompanying the *Garland Encyclopedia of World Music* (GEWM), chosen for the wide geographical and cultural coverage of this dataset. 

One major issue for the identification of musical universals is one that we encountered last week: music from all over the world is so tremendously diverse, how are we to identify any universals *at all*? Brown and Jordania argue that absolute universals in human cultural phenomena, that is a feature that occurs without fail in every instance of the phenomenon at any time, do not exist. Instead, they promote the search for statistical universals.   

\begin{itemize}
\askstar What is a statistical universal?
\askstar Can you think of an example of an absolute universal in a non-cultural phenomenon?
\end{itemize}

As \cite{Savage2015} point out, another issue that's particular to the identification of *statistical* universals, is the fact that different cultures have different degrees of historical relatedness. This is an issue for statistical analysis, because the occurrence of features in different cultures cannot be treated as independent. To overcome this, Savage et al. treat the different recordings as the products of *cultural* evolution and resort to special kind of statistical analysis that models the *evolutionary dynamics*. This analysis can be used to predict what the expected distribution of features would be if the evolution had been running for a long time.

In this lab, we'll go study this analysis in more detail, and apply a simpler version of the analysis to a single feature in the GEWM.

# Finding musical universals

Savage et al. propose 32 *binary* features (features that can have just two possible values: ***1*** for present and ***0*** for absent) to empirically test the validity of many of the candidate universals proposed by \cite{Brown2013}. Using this classification scheme, Savage et al. *encode* each recording as a vector indicating the presence or absence of each of the 32 features. We've seen examples of these features last week: the presence of a isochronous beat, the presence of metrical hierarchy, etc.

\begin{itemize}
\askstar Which of the following features of an organism are binary?
\begin{itemize}
\item The color of the organism's hair.
\item The organism's average walking speed.
\item Whether the organism is bipedal.
\item The amount of wings on the organism.
\item The ability to remain under water for longer than 5 minutes.
\end{itemize}
\end{itemize}

The trick to finding statistical universals is to find out how each has changed over evolutionary time and derive the evolutionary "forces" (the evolutionary dynamics) working on each feature. Once these forces are known, we can calculate the expected frequency of occurrence of any feature in a hypothetical population in the far future, when evolution has been running for a long time. Any feature that is expected to occur in significantly more than half of this future population is considered to be a statistical universal by Savage et al. 

This analysis finds extracts the evolutionary forces operating on traits in the population. By simulating what 

So how will we go about calculating the evolutionary "forces"? In order to know how a feature has changed over evolutionary time, we need some way of reconstructing the evolutionary history of the different recordings. We've seen this before sort of problem before.

\begin{itemize}
\askstar What method can we use to reconstruct the evolution of a population consisting of a variety of different recordings?
\end{itemize}

With a binary classification scheme, Savage et al. encoded each recording in the GEWM as a vector of zeros and ones. This representation can be treated as the recording's genotype. The genotype specifies which traits are active in a particular recording. We now have a representation that can be subjected to phylogenetic analysis.

To model the evolutionary dynamics, Savage et al. use a continuous time Markov process. In the next section, we'll find out what a Markov process is. If you're interested in the raw details of this model, have a look at \cite{Pagel1994}. Pagel introduced this method as a way of testing the hypothesis whether two discrete traits are correlated. Savage et al. also make use of this method this application of the method to find "universal relationships", in this lab, we'll only be concerned with evolutionary dynamics. 

# The Markov property

Markov models are used to model how a *state* changes over time. Markov models are based on a simplifying assumption, called the Markov assumption, or Markov property, which says that the probability of the *next* state depends only on the *current* state and is independent of *previous* states. 

For example, say we want to predict the location, velocity and direction of a spear thrown by an athlete. We'll say that the *state* of the spear consists of its location, direction and speed. In order to predict state of the spear a certain duration of time later, the information in the current state is all we need to know (for the purpose of this example we'll ignore other factors like wind direction). Knowing anything about previous states of the spears will not give us any extra information.

\begin{itemize}
\askstar Which of the following processes have the Markov property?
\begin{itemize}
\item The next word in a sentence given the current word. 
\item Drawing marbles from a vase filled with red and blue marbles *without replacement*
\item Drawing marbles from a vase filled with red and blue marbles *with replacement*
\end{itemize}
\end{itemize}

# Modeling cultural evolution with Markov models 

Savage et al. use a continuous-time Markov process to model evolutionary dynamics. We will look at a simplified *discrete*-time Markov model. In modelling how a trait changes over generations, we'll apply the Markov assumption. Remember that traits are represented as binary features.

\begin{itemize}
\ask What are the possible \textit{states} of a trait in a Markov model of evolutionary change.
\end{itemize}

Say a particular trait is present at generation $x$. The model we're interested in should give us the probability that that same trait is still present or absent in the next generation. 

\begin{itemize}
\ask What are the four possible \textit{state transitions} a trait can go through from one generation to the next?
\end{itemize}

In a Markov model, each state transition is associated with a *transition probability*. We'll call these state transition probabilities $\pzero$, $\gain$, $\pone$ and $\loss$. The subscripts indicate what state transition the probability is associated with. Generally, $p_{ij}$ is the probability of going from state $i$ to state $j$. For example, $\gain$ is the probability of a trait to go from absent (0) to present (1) over the course of one generation. Because of the Markov assumption, the transition probabilities depend only on the state of a trait in the last generation. 

Savage et al. speak of a gain rate and a loss rate. In our discrete-time model, these correspond to the *gain probability* and *loss probability*. The gain probability corresponds to the probability of acquiring a trait, the loss probability corresponds to the probability of losing a trait.

\begin{itemize}
\ask Which of our transition probabilities ($\pzero$, $\gain$, $\pone$ or $\loss$) corresponds to the gain probability and which one corresponds to the loss probability?
\ask If the state of a trait is $1$. Which are the two transitions can the trait undergo in the next generation? Which transition probabilities are associated with these transitions?
\end{itemize}

Note that Savage et al. write that the gain and loss rate (probabilities in our case) are the only two parameters of the model, while we just identified *four* parameters. 

\begin{itemize}
\askstar Can you express $\pzero$ and $\pone$ in terms of the gain ($\gain$) and loss ($\loss$) probabilities?
\end{itemize}

Note that we don't *know* the state transition probabilities yet, the ultimate goal is to find a way of estimating these probabilities so we can extrapolate what would happen many generations down the line. We call such unknown quantities the *parameters* of a model. 

# A toy example: the pentatonic scale

Last week, we encoded some recordings from the GEWM into a restricted set of features. It was in fact possible to cheat on this assignment, because the entire set of encodings for each recording in the GEWM done by Savage et al. is available in the supplementary information of \cite{Savage2015}. We've included this data in this lab's zip file. For the next few questions, we will focus on one specific trait: the use of a pentatonic scale (for an entertaining example of a pentatonic scale, see [Bobby McFerrin's demonstration](https://www.youtube.com/watch?v=ne6tB2KiZuk))

\begin{itemize}
\action Open the file \file{pnas.1414495112.sd01.xls}. Find recordings 12, 109, 157, 180 and 260. Write down for each of them whether they make use of a pentatonic scale.
\end{itemize}

Now let's assume that we know the evolutionary history (the phylogenetic tree) of these recordings. We could for example use a phylogenetic algorithm to reconstruct this, but for now we'll just use a made up phylogeny as shown in Figure \ref{fig:phylo}.

\begin{figure}
\input{tree.tex}
\caption{A made-up phylogeny of recordings 12, 109, 157, 180 and 260 from GEWM}
\label{fig:phylo}
\end{figure}

Remember that the goal is to find the parameters ($\pzero$, $\gain$, $\pone$ or $\loss$) of the model given the data that we have. To illustrate how this works, we'll imagine a hypothetical gain and loss probability for the pentatonic scale trait. For example: $\gain = 0.6$ and $\loss = 0.2$.

\begin{itemize}
\action Calculate $\pone$ and $\pzero$ based on the given gain and loss probabilities.
\end{itemize}

In order to know how well the chosen parameters explain the observed data, we need to calculate the *likelihood* of the phylogenetic tree given our choice of parameters. To do this, we need to take the product of all the observed state transitions. However, here we run into a problem. We don't *know* the state of of our trait at the ancestor nodes, so how can we calculate the probability of the tree? We'll see how to deal with this problem in a bit, but for now, assume that the states of the pentatonic scale trait in the ancestors of our set of recordings are as illustrated in Figure \ref{fig:phylo-ancestors}.

\begin{figure}[b]
\input{tree-ancestors.tex}
\caption{A made-up phylogeny of recordings 12, 109, 157, 180 and 260 from GEWM with (also made-up) ancestor trait-states}
\label{fig:phylo-ancestors}
\end{figure}

\begin{itemize}
\action Copy the tree in Figure \ref{fig:phylo-ancestors} and replace the recording numbers at the *leaf nodes* (the end of the branches of the tree) with the values of the pentatonic scale feature corresponding to these recordings. 
\action Write down a list of all the state transitions you can spot in Figure \ref{fig:phylo-ancestors} (hint: there should be 10)
\end{itemize}

The likelihood is calculated by taking the product of all the state transitions.

\begin{itemize}
\action Replace the state transitions that you wrote down previously by transition probabilities that we derived earlier ($\gain = 0.6$ and $\loss = 0.2$ and the $\pzero$ and $\pone$ you derived earlier)
\ask What is the likelihood of the tree in Figure \ref{fig:phylo-ancestors}?
\end{itemize}

In order to calculate the likelihood, we've assumed quite a few things. To begin with, we don't actually know the whether or not the pentatonic scale trait was present in the ancestors. We can deal with this problem by calculating the likelihood for *any* assignment of trait to the ancestors. This is done by looking at every possible assignment of the pentatonic scale feature in the ancestors, and summing the likelihood calculated based on this assignment. 

\begin{itemize}
\askstar Have a look at the tree in Figure \ref{fig:phylo}. How many possibilities are there for the assignment of the pentatonic scale feature to ancestors?
\end{itemize}

# The maximum likelihood solution

Now that we know how to calculate the likelihood based on a guessed set of parameters, how do we find the actual parameters? Finding the best parameters of a model given some data is a very common task. One possible way of doing this is to find the *maximum likelihood* solution. The maximum likelihood solution is the parameter setting that maximizes the likelihood of the observed data. There are several ways of finding the maximum likelihood solution. The simplest method is the so-called brute force approach, where we try calculate the likelihood for many different parameter and choose the one that maximizes the likelihood. 

As you can imagine, this brute force method requires quite a bit of number-crunching. We have provided an R-function for you to try out the brute force method for the example we gave here. It contains the following useful functions: 

\begin{description}
\item[calculate\_likelihood(gain, loss)] calculates the likelihood of a tree for a given \verb|<gain>| and \verb|<loss>| (you can use this function to check your earlier calculation!).
\item[calculate\_likelihood\_surface(resolution)] is a function that will calculate the likelihood for \verb|<resolution>| different values of gain spaced evenly between 0 and 1 and \verb|<resolution>| different values of loss spaced evenly between 0 and 1.
\item[plot\_2d(likelihood\_surface)] is a function that visualize \verb|<likelihood_surface>| in a 2D plot.
\end{description}

If you're not yet sure what a likelihood surface represents, perhaps generating seeing one will help.

\begin{itemize}
\action Start R
\action Install the package plot3D by typing \verb|install.packages('plot3D')| and \verb|library(plot3D)|
\action Load the functions in \file{dynamics.r} by following commands (make sure your working directory is set to the lab's folder):
\begin{verbatim}
source('dynamics.R')
\end{verbatim}
\action Create a likelihood surface by running the these commands:
\begin{verbatim}
likelihood_surface <- calculate_likelihood_surface(100)
plot_2d(likelihood_surface)
\end{verbatim}
\ask What are the optimal (maximum likelihood) gain and loss parameters for the pentatonic scale feature in our example phylogenetic tree?
\askstar What do you expect would happen to the likelihood surface if we decreased the number of recordings in the populations with the pentatonic scale feature?
\end{itemize}

The occurrence of the pentatonic scale feature at the leaf nodes (the current population) is set in the \verb|leaf_nodes| variable. The variable is set to \verb|c(0, 1, 0, 1, 1)|. You can give a new value to the variable by typing (for instance) \verb|leaf_nodes <- c(1,0,1,1,1)| in the console.

\begin{itemize}
\action Verify your expectations by changing one or two ones in zeros in the \verb|leaf_nodes| variable, and rerun the commands for plotting the likelihood surface.
\end{itemize}


\bibliography{refs}
