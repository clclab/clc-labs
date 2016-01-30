---
title: Evolution of communication systems
author: BSc Psychobiology, UvA
bibliography: bib.bib
numbersections: true
header-includes:
    - \usepackage{graphicx}
    - \usepackage{fullpage}
    - \usepackage{amsmath, amssymb}
    - \usepackage[round, authoryear]{natbib}
    - \usepackage{fixltx2e}
    - \bibliographystyle{plainnat}
    - \input{../labs.tex}
...

\begin{itemize}
\action These are actions for you to do
\ask These are questions
\askstar This is a question that could be on the exam
\end{itemize}

# Goals

In today's computer lab you will experiment with simulated evolution and look at a simple model of the evolution of communication. The goals are to
\begin{itemize}
\item Better understand the concepts of genotype, genotype space, fitness, fitness landscape, selection, mutation, selection-mutation balance, frequency dependent selection;

\item See how these concepts can be formalized in a computer program;
\item Appreciate both the power and the limits of natural selection.
\end{itemize}

# Simulated Evolution

\begin{itemize}
\item Create a random string of length 10 of the characters AGCU.
\item Now create a random string of length 100 of the characters AGCU.
\item *How many such strings are possible? This is the genotype space.
\item Create a population of 100 such strings.
\item Define a fitness function. Imagine, for instance, that the string CAC codes for a very useful aminoacids, such that the more CAC's in the genome, the higher the expected number of offspring. Fitness = count(CAC). Create a vector of fitnesses.
\item Create 100 children, each with a probability of inheriting their genome from a parent that is proportional to the parent's fitness. This is selection.
\item Repeat 100 times. Plot fitness. This is selection without mutation.
\item *Why does the fitness level off at a relatively low level?
\item Now introduce mutation: every child's nucleotide has probability $\mu$ to change into a random nucleotide.
\item Repeat 100 times with $\mu=0.01$. Plot fitness. This is selection with mutation.
\item Repeat 1000 times with $\mu=0.001$. Plot fitness. This shows the mutation-selection balance.
\item *Why does the fitness with relatively high mutation rate level off at a slightly lower level?
\end{itemize}

# Evolution of communication

\begin{itemize}
\item Consider the two matrix model of communication. For 3 meanings and 3 signals, both the sender and receiver matrix contain 9 values.
\item *What are the optimal S* and R*, for maximal communicative success in a population?
\item Assume that every individual is characterised by a genome of length 18, where each nucleotide codes for one value in S and R with A=3, G=2, C=1 and U=0. To construct the S and R matrices, rows are normalized.
\item Compute fitness by communicating with a a fixed target S and R. Fitness = sum of diagonal values of S\%*\%R* + S*\%*\%R.
\item Run an evolutionary simulation with low mutation rate for 100 iteration. What is the average fitness and most frequent communication system at the end of it?
\item Compute fitness by communicating with a a random other agent, with its own (evolved) S' and R'. Fitness = sum of diagonal values of S\%*\%R' + S'\%*\%R.
\item Run an evolutionary simulation with low mutation rate for 100 iteration. What is the average fitness and most frequent communication system at the end of it?
\item *This is frequency dependent selection. Why does it not always evolve to the optimal communication system?
\end{itemize}





# Communication Systems as Matrices
A possible way of representing a communication system is by using matrices that describe a mapping from a set of meanings to a set of forms (or signals). For instance, the well known alarm call system of Vervet monkeys \citep(seyfarth1980monkey}
 in its usual idealization, can be described as follows:

\begin{table}[h!]
\begin{tabular}{ll}
$
S =
\left(
\begin{array}{c|ccc}
& \text{chip} & \text{grunt} & \text{chutter}\\
\hline
\text{leopard} & 1 & 0 & 0\\
\text{eagle} & 0 & 1 & 0\\
\text{snake} & 0 & 0 & 1\\
\end{array}
\right)
$
&
$
R =
\left(
\begin{array}{c|ccc}
& \text{leopard} & \text{eagle} & \text{snake}\\
\hline
\text{chirp} & 1 & 0 & 0\\
\text{grunt} & 0 & 1 & 0\\
\text{chutter} & 0 & 0 & 1\\
\end{array}
\right)
$
\end{tabular}  
\end{table}

The $S$ matrix represents the sender: the first column contains the meanings (or situations) that the sender may want to express, the first row the signals that it can use to express these meanings. The numbers in the matrix represent the probabilities that the sender will use a certain signal to express a certain meaning. The matrix $R$ describes the behaviour of the receiver in a similar way: the numbers in the matrix are the probabilities that the receiver will interpret a certain signal (first column) as having a certain meaning (first row).

**Exercise**  
*Some question to make them think a little bit about what this means?*

More generally, if we have a set $M$ with possible meanings and a set $F$ with possible signals, then $S$ is a $|M|\times|F|$ matrix that gives for every meaning $m\in M$ and signal $f\in F$ the probability that $m$ is expressed with $f$. Similarly, $R$ is a $|F|\times|M|$ matrix that gives for every $\langle f, m\rangle$ pair the probability that $f$ is interpreted as $m$.

**Exercise**  
*What is the sum of the values in each row?*

Campbell monkeys have an alarm call system where the calls for leopards and eagles can be preceded by a "boom" call, which generally has the effect of changing the meaning of the calls from predator-specific alarms to a general signal of disturbance, although they are sometimes still interpreted as alarms \citep{zuberbuhler2002syntactic}. If we consider just the calls for leopards and eagles, with and without preceding boom, we have 4 different signals and, if we add "disturbance" a set of 3 different meanings.

**Exercise**  
Create an $S$ and $R$ matrix that describes the communication system of the Campbell monkeys. What is reasonable to assume for the probability that a boom + leopard call (lets call it "B + L\textsubscript{C}") is interpreted by the sender as a call for a leopard or a disturbance? And the probability that a disturbance is expressed by the signal "B + L\textsubscript{C}"?

You can compute the chance of successful communication by summing up the chance of success for each individual meaning-signal combination.For instance, let's assume the sender wants to convey the meaning "leopard". We multiply the probabilities for all signals the sender could use for this meaning (the row in $S$ starting with "leopard") with the chance that the receiver will interpret this signal as having the meaning "leopard" (the "leopard" column in $R$). In this case as the sender only uses the signal L_\textsubscript{C} to express the meaning leopard, and the receiver interprets this signal as having the meaning leopard with probability 1, the chance of successfully conveying the meaning "leopard" in this system is 1.

**Exercise** 
*Compute the probability that the sender will successfully convey that there is a disturbance, using the $S$ and $R$ matrices you constructed in the previous assignment. What is the overall chance of successful communication for your matrices?*

**Exercise** 
*What are the $S$ and $R$ matrices maximising the success of communication in Campbell monkeys? Are these matrices realistic?*  

# Communication systems in R

Explain how you can put the communication matrices in R and how you can compute the chance of success for a meaning/system. 

**Misschien kan ik hier ook wat vragen stellen als: stel dat dit de receiver matrix is, wat is dan optimaal voor de zender, of andersom. Als communicatief success als fitness criterium wordt gebruikt (zenden, ontvangen of allebei) wat kan een individu doen om een fitness voordeel te krijgen? Is dit ook goed voor de groep?

\bibliography{bib}
