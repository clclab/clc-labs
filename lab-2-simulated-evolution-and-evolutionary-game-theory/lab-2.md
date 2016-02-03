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

In the first part of this computer lab we will simulate the evolution of a (DNA) string of letters under a particular fitness function by using R. 

Lets start by creating an individual of our population: 

\begin{itemize}
    \action First, start R or R-studio, depending on your operating system and preferences.
    \action Load the library \texttt{stringr} by typing \texttt{library(stringr)} in the command line.
    \action Generate a random string of length 10 containing the characters A,G,C and U. You can use the following command:
    \begin{itemize}
        \item[] \texttt{paste(sample(c('A','G','C','U'), size=10, replace=TRUE), collapse='')}
    \end{itemize} which creates a vector of length 10 containing the letters 'A', 'G', 'C' and 'U' and them puts them all together in a string.
    \action Generate a couple of such strings to confirm that this does what you want (hint: you can use the arrow keys to scroll to commands you previously used in the command line).
    \action Now generate a random string of length 100 with the characters 'A', 'G', 'C' and 'U'. If you want, you can store the string under a name (for instance \texttt{x}), by typing \texttt{x <- paste(....}' (where the previous command goes on the dots).
    \askstar How many such strings are possible? This is the genotype space.
\end{itemize}

Now, we want to create a population 100 of such strings:\begin{itemize}
    \action First create an empty vector to store your population: \texttt{population <- rep(0, 100)}
    \action Fill your vector by creating a string for every position:\begin{itemize}
        \item[] \texttt{for (i in 1:100) \{}
        \item[] \texttt{\hspace{3mm} population[i] <- paste(sample(c('A','G','C','U'), size=100, replace=TRUE), collapse='')}
        \item[] \texttt{\}}
    \end{itemize}
\end{itemize}

Now we need to define a fitness function. Imagine, for instance, that the string CAC codes for a very useful aminoacids, such that the more CAC's in the genome, the higher the expected number of offspring. Thus, fitness = count(CAC).\begin{itemize}
    \action Create a vector containing the fitness of all the members of your population: first generate an empty vector to store the fitness' (\texttt{fitness <- rep(0, 100)}) and then use a for-loop to fill the vector with the fitness values, like in the previous bit of code. You can compute the fitness of an individual member of the population that is stored at place \texttt{i} in the population vector by using the function \texttt{str\_count(}: the fitness of this member is \texttt{str\_count(population[i], "CAC")}.
    \ask What is the highest fitness a member of this population can have?
\end{itemize}

Now we will generate the next generation. Assume that each 'child' in the new population has a probability of inheriting their genome from a parent that is proportional to the parent's fitness. This is selection. (I think I need to formulate this a bit differently).
\begin{itemize}
    \action Compute the average fitness and store it in a variable:\begin{itemize}
        \item[] \texttt{av\_fitness <- mean(fitness)}
    \end{itemize}
    \action Generate 100 new children, using the built in function \texttt{sample} (the same one we used before):\begin{itemize}
        \item[] \texttt{population = sample(population, size=100, replace=TRUE, prob=100*av\_fitness}
    \end{itemize}
    \ask If one population member has fitness 20 and all the other population members have fitness 1, what is the probability that a child will inherit its genome from this one population member? What do you expect to happen with the population?
    \action Repeat this process 100 times and plot the result. If you feel like doing some implementation yourself, you can do this by creating a for-loop that executes the previous bits of codes 100 times, storing the fitness of every population in a vector. To plot your results, use:\begin{itemize}
        \item[] \texttt{plot(seq(1,100,1), av\_fitness, type="l", ann=FALSE)}
    \end{itemize}
    (Assuming you stored the fitness values in av\_fitness).
    \item[] To label your axes and titles you can use:\begin{itemize}
        \item[] \texttt{title(main="title", xlab="x label", ylab="y label")}
    \end{itemize}
    Alternatively, you can use the provided script. Put your own values at the top!
    \askstar Why does the fitness level off at a relatively low level?
\end{itemize}

Now lets introduce mutation: every child's nucleotide has a probability $\mu$ to change into a random nucleotide.

TODO fix this function

\begin{itemize}
    \action Use the provided script to do the same simulation, but with a mutation level $\mu=0.01$. This is selection with mutation.
    \action Do 1000 repetitions with $\mu=0.001$, plot the fitness. This shows the mutation-selection balance.
    \askstar Why does the fitness with relatively high mutation rate level off at a slightly lower level?
\end{itemize}

# Evolution of communication

A possible way of representing a communication system is by using matrices that describe a mapping from a set of meanings to a set of forms (or signals). For instance, the well known alarm call system of Vervet monkeys \citep{seyfarth1980monkey} in its usual idealization, can be described as follows:

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

\begin{itemize}
\askstar What are the optimal S* and R*, for maximal communicative success in a population?
\end{itemize}

\begin{itemize}
\item Assume that every individual is characterised by a genome of length 18, where each nucleotide codes for one value in S and R with A=3, G=2, C=1 and U=0. To construct the S and R matrices, rows are normalized.
\item Compute fitness by communicating with a a fixed target S and R. Fitness = sum of diagonal values of S\%*\%R* + S*\%*\%R.
\item Run an evolutionary simulation with low mutation rate for 100 iteration. What is the average fitness and most frequent communication system at the end of it?
\item Compute fitness by communicating with a a random other agent, with its own (evolved) S' and R'. Fitness = sum of diagonal values of S\%*\%R' + S'\%*\%R.
\item Run an evolutionary simulation with low mutation rate for 100 iteration. What is the average fitness and most frequent communication system at the end of it?
\item *This is frequency dependent selection. Why does it not always evolve to the optimal communication system?
\end{itemize}





# Communication Systems as Matrices

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
