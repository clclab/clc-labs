---
title: Evolution of communication systems
author: Dieuwke Hupkes, Jelle Zuidema
bibliography: bib.bib
header-includes:
    - \usepackage{graphicx}
    - \usepackage{fullpage}
    - \usepackage{amsmath, amssymb}
    - \usepackage{mathspec}
    - \usepackage[round, authoryear]{natbib}
    - \usepackage{fixltx2e}
    - \bibliographystyle{plainnat}
...

# Introduction

In today's computerlab we will study the evolution of communication systems.


# Communication Systems as Matrices
A possible way of representing a communication system is by using matrices that describe a mapping from a set of meanings to a set of forms (or signals). For instance, the well known alarm call system of Vervet monkeys \citep(seyfarth1980monkey} in its usual idealization, can be described as follows:

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

# Evolving communication systems

**Iets met Federico's app, ik ben er nog niet helemaal achter hoe dit werkt en wat het doet. Misschien is het een goed idee om ze die paper van Oliphant te laten lezen?**

Explanation:  
- consider only matrices with 0 or 1 probabilities (thus no synonyms or homonyms)
- communication (how does this work exactly?)
- fitness in payoff matrix
- how do we create a new population

**Exercise**  
*Write an exercise that lets the students investigate what impact the conditions have on the communication system that evolves, and why under some conditions an optimal system evolves, and sometimes it doesn't. Maybe also the differences between individual/group fitness (e.g., what happens if you reward unsuccessful communication)?*


\bibliography{bib}
