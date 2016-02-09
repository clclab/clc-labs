---
title: "Lab 2: Evolution of communication systems"
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
    - \usepackage{listings}
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

In the first part of this computer lab we will simulate the evolution of a (DNA) string of letters under a particular fitness function. We will use the programming language R.

Lets start by creating an individual of our population: 

\begin{itemize}
    \action First, start R or R-studio, depending on your operating system and preferences.
    \action Install the package stringr by typing \verb|install.packages("stringr")|. As you (probably) have no rights to install the package globally, the computer will ask you if you want to install the package in a personal library, click okay and accept the default settings.
    \action Load the library \texttt{stringr} by typing \texttt{library(stringr)} in the console.
    \action Generate a random string of length 10 containing the characters A,G,C and U. You can use the following command:
    \begin{itemize}
        \item[] \begin{verbatim}sample(c('A','G','C','U'), size=10, replace=TRUE)\end{verbatim}
    \end{itemize} which creates a vector of length 10 containing the letters 'A', 'G', 'C' and 'U'.
    \action Generate a couple of such vectors to confirm that this does what you want (hint: use the up-arrow key to scroll to previous commands).
    \action Now generate a random string of length 50 with the characters 'A', 'G', 'C' and 'U'. If you want, you can store the vector under a name (to call it \texttt{x} for instance, type \texttt{x <- sample($\cdots$)}, and replace the dots by previous command).
    \askstar The set of all possible strings is called the genotype space. How many genotypes are possible in our simulation?
\end{itemize}

Now, let's create a population. To do this, we will make 100 genotype strings:

\begin{itemize}
\action We will store our population in a matrix, where our population members are the rows of the matrix. Lets start with creating a matrix filled with zero's that we can later fill:\footnote{The command \texttt{matrix(x, height, width)} command transforms a vector \texttt{x} into a matrix with height \texttt{height} and width \texttt{width}.}
    \begin{itemize}
        \item[] \texttt{population <- matrix(rep(0, 100), 100, 50)}
    \end{itemize}
    \ask What do we find in column 30 of our population matrix?
    \action Fill your matrix by generating 100 population members in a for-loop and filling the matrix with them:\footnote{\texttt{x[i,]} accesses the \textit{i}th row of the matrix \texttt{x}, which in our case thus corresponds with the \textit{i}th member of our population}\begin{verbatim}
for (i in 1:population_size) {
    population[i,] <- sample(c('A','G','C','U'), size=50, replace=TRUE)
}
    \end{verbatim}
\end{itemize}

Now we need to define a fitness function. Imagine, for instance, that the string `CAC' codes for some very useful aminoacid, such that the more CAC's in the genome, the higher the expected number of offspring. Thus, for our example, we define fitness to be the number of times CAC appears in the genotype string.

To keep track of the fitness of all members in our population, we will create a vector containing the fitness values of each member of the population. 

\begin{itemize}
    \action Generate an empty vector to store the fitnesses, and call it \texttt{fitness}:\begin{verbatim}fitness <- rep(0, population\_size)\end{verbatim}
    \action Use a for-loop to fill the vector with the fitness values, like in the previous bit of code:
    \begin{verbatim}for (i in 1:100) {      # loop over population size
        member <- paste(population[i,], collapse='')    # generate string representation
        fitness_member <- str_count(population_member, "CAC")   # compute fitness member
        fitness[i] <- fitness_member                            # store in fitness vector
    }
    \end{verbatim}
    
    Note that comments in R are preceded by the character #, everything following that character is not interpreted by the interpreter.
    
    \ask What is the highest possible fitness a member of this population can have?
    \action Compute the mean fitness of your population by using \verb|mean(fitness)|.
    \ask What is the average fitness of your population?
\end{itemize}

Now we will generate the next generation. To simulate this, we will assume that each member of the next generation will inherit the genome of one of the members of the previous generation. The probability of inheriting each genome is proportional to the genome's fitness: a child is most likely to inherit the genome of the fittest member of the previous population. This simulates selection.

\begin{itemize}
    \action Compute the average fitness of the population and store it in a variable using:
    \begin{itemize}
        \item[] \texttt{av\_fitness <- mean(fitness)}
    \end{itemize}
    \action Generate 100 new children, using the built-in function \texttt{sample} (the same one we used before):\footnote{We first draw 100 random numbers between 1 and 100 (repetitions possible). If population member 2 has a very high fitness, it will have a very high chance of being drawn. Then we use the drawn numbers to create a new population of the members corresponding to the numbers.}\begin{itemize}
        \item[] \texttt{indices <- sample(100, size=100, replace=TRUE, prob=fitness/sum(fitness))}
        \item[] \texttt{new\_population <- population[indices,]}
    \end{itemize}
    \ask If one population member has fitness 10 and all the other population members have fitness 1, what is the probability that a child will inherit its genome from this one population member? What do you expect to happen with the population?
    \action To simulate the evolution of the population, we want to repeat this process several times and plot the average fitness over time. If you like programming, you can try to do the implementation yourself. You should create a for-loop that executes the previous bits of code 100 times, storing the fitness of every population in a vector. To plot your results, use:\begin{itemize}
        \item[] \texttt{plot(seq(1,100,1), av\_fitness, type="l", ann=FALSE)}
    \end{itemize}
    (Assuming you stored the fitness values in av\_fitness).
    \item[] To label your axes and titles use:\begin{itemize}
        \item[] \texttt{title(main="title", xlab="x label", ylab="y label")}
    \end{itemize}
    Alternatively, you can use the provided script \texttt{lab-2.R}. You can run a script in R by typing \verb|source('scriptname')| in the command line. You should make sure that both the file \texttt{lab-2.R} and the file \texttt{auxiliary\_functions.R} are available to R. If you are working in R-studio, the easiest way to do this, is to put them both in the same folder and set this folder as the \textit{working directory} of R-studio. Look at this website \url{https://support.rstudio.com/hc/en-us/articles/200711843-Working-Directories-and-Workspaces} to find out how to do that for your version of R-studio. You can use tab for auto completion.

    \askstar You will notice the fitness stops increasing quite early in the simulation. Why is this?
\end{itemize}

This was selection without mutation. Lets now look at the case where every child's nucleotide has a probability $\mu$ to change into a random other nucleotide.

\begin{itemize}
    \ask If $\mu=0.01$, what is the chance that no changes occur in a genome. What is the chance that no changes occur in an entire population? And if $\mu=0.001$?
    \action Use the provided script to do the same simulation, but with a mutation level $\mu=0.001$. You can chance the values of the parameters at the top of the script. After changing them, save the file and run the script again by typing \verb|source('lab-2.R')|. Adapt the length of the simulation to a number you think is suitable.
    \action Now repeat the simulation with $\mu=0.001$, plot the fitness. This shows the mutation-selection balance.
    \askstar Why does the fitness with relatively high mutation rate level off at a slightly lower level?
\end{itemize}

# Evolution of communication

In the second part of this assignment, we will model the evolution of a communication system. A possible way of representing a communication system is by using matrices that describe a mapping from a set of meanings to a set of forms (or signals). For instance, the well known alarm call system of Vervet monkeys \citep{seyfarth1980monkey} in its usual idealization, can be described as follows:

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
\askstar What are the optimal S and R, for maximal communicative success in a population?
\askstar How is ambiguity reflected in S and R matrices? And synonymity?
\end{itemize}

By using a bit of a trick, we can study the evolution of such a communication system using the same protocol as in the first part of this assignment. The S and R matrices of an individual are uniquely defined by 18 numbers. Assume that we model this by saying that every individual is characterized by a genome of length 18, where each nucleotide codes for one value in S and R. Let's say A=3, G=2, C=1 and U=0. To construct the S and R matrices, we put the numbers corresponding to the nucleotides in two matrices and normalise the rows, such that the probabilities add up to 1.

\begin{itemize}
\ask What would a genome corresponding to the S and R matrix depicted above look like?
\ask Can you think of two strings that have a different genotype but the same phenotype?
\end{itemize}

Of course our previous fitness function - the count of the substring "CAC" - does not make much sense in this case. We will have to define a new one. We can compute the chance of successful communication between two agents by summing up the chance of success for each individual meaning-signal combination. For instance, let's assume the sender wants to convey the meaning "leopard". We multiply the probabilities for all signals the sender could use for this meaning (the row in $S$ starting with "leopard") with the chance that the receiver will interpret this signal as having the meaning "leopard" (the "leopard" column in $R$). In this case as the sender only uses the signal chirp to express the meaning leopard, and the receiver interprets this signal as having the meaning leopard with probability 1, the chance of successfully conveying the meaning "leopard" in this system is 1. Due to the fact that agents have both a sender and receiver matrix, it is possible that the communication in one direction runs flawlessly, but any communication in the other direction is unsuccesful. We define the fitness as the sum of the chances of success for all meanings in both directions. Note that it is not possible to compute the fitness of one individual without taking into account who he is communicating with.

We implemented some fitness functions that you can find in the file \texttt{auxiliary\_functions.R}: \begin{itemize}
\item \texttt{CAC\_count}: This is the fitness function you used before, that counts the number of occurrences of the substring "CAC" in the genome;
\item \texttt{communication\_fixed\_target}: This fitness function captures how well the population member can communicate with a fixed target with S and R matrix that allows perfect communication (i.e., it does not use the same signal for different meanings, or assign different meanings to the same signal).
\item \texttt{communication\_random\_target}: This fitness function describes the more realistic situation, in which the fitness of a population member is determined based on its communication with a random other member of the population.
\end{itemize}

You can change the fitness function - like the rest of the parameters - at the top of the file \texttt{lab-2.R}, by uncommenting the line with the preferred fitness function (and commenting out all other fitness function lines). As you may have guessed, you can (un)comment a line in an R script by placing (removing) a '#' at the beginning. Leave the file \texttt{auxiliary\_functions.R} untouched, you don't have to change anything there.

\begin{itemize}
\ask What is the maximal fitness that an individual can have?
\action Change the fitness function in the script to \texttt{communication\_fixed\_target}. Run an evolutionary simulation with a low mutation rate for 100 iterations. What is the average fitness and most frequent communication system at the end of it? You can check the population at the end by typing \texttt{population} in your command line.
\ask Can the members of the resulting population also communicate with each other or only with the preset fixed target?
\ask What would happen if the target was fixed, but not perfect? You can test your assumption by changing the target matrices in the \texttt{auxiliary\_functions file}. 
\end{itemize}

A more realistic situation is the one in which the members of the population do not all communicate with the same fixed target, but with other members of the population, that have their own (evolved) S and R matrix.
\begin{itemize}
\action Run some evolutionary simulations for this scenario (compute the fitness by using the function \texttt{communication\_random\_target}). What is the average fitness and most frequent communication system at the end of it? Experiment with the learning rate.
\askstar This is frequency dependent selection. Why does it not always evolve to the optimal communication system?
\askstar What do you expect to happen if only successfully \textit{receiving} but not \textit{sending} contributes to fitness?
\action Test your assumption by using the fitness function \texttt{sending\_random\_target}. 
\end{itemize}

\bibliography{bib}
