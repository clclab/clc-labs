---
title: "Lab 3: Phylogenetic trees - genes, language and simulated data"
author: BSc Psychobiology, UvA
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

Omschrijf doelen

# Simulated evolution (continued)

In the previous computer lab, we simulated the evolution of strings, using different fitness functions. Today we are going to do this again, but we will keep track of ancestry during the simulation, so that we can reconstruct family trees of different individuals.

\begin{itemize}
\action Download the scripts for this week's lab and extract them all in the same folder.
\action Start up R-studio (or a terminal) and set your working directory to the folder you created for the scripts (if you forgot how, maybe this website \url{https://support.rstudio.com/hc/en-us/articles/200711843-Working-Directories-and-Workspaces} can help you)
\action Run the script \verb|lab-3.R| in R-studio by running the following command in the console: \begin{verbatim}source('lab-3.R')\end{verbatim}
It will generate a matrix storing information about the parents of the current and all previous generations, and plot the development of the average fitness and the diversity of genotypes over generations.
\ask Visualise the parent matrix by running\begin{verbatim}print_parent_matrix{parent_matrix}\end{verbatim}\textcolor{red}{Is this possible like this in R-studio??}. What do you see?
\end{itemize}

If you did not change the parameters of the simulation, you probably just saw an almost black square. To understand what this means, lets run the same code for a much smaller simulation:\begin{itemize}
\action Change the parameters at the top of the file. Set both the population size and the simulation length to 10, run the script and print the parent matrix using the same command as before.
\askstar Follow some paths up and down. Why do downward paths often end in dead ends, whereas upward paths always go all the way up?
\end{itemize}

We will now use our parent matrix to reconstruct a tree for the last generation (i.e., we only look at the members of previous generations that have offspring that is still alive).
\begin{itemize}
\action Set the population size back to 100 and the simulation length to 1000, run the script again.
\action Generate a tree by using the function \verb|reconstruct_tree| and print it:\begin{verbatim}
        tree <- reconstruct_tree(parent_matrix)
        print_tree(tree)
        \end{verbatim} This will generate a string representation of the tree, that represents a family tree of the living offspring.
\action Copy the string representation and visualise it with the online tree viewer you can find here: \url{http://evolangmus.knownly.net/newick.html}. Set the tree type to \textit{Rectangular cladogram} and paste the tree representation you copied in the box. You can zoom in on the tree by scrolling and move it by clicking on it and dragging the mouse.
\askstar How many generations ago did the LCA live?
\askstar Which aspects of evolution leave traces that we can detect in the current generation and which aspects don't?
\end{itemize}

# Phylogenetic reconstruction with R

# Phylogenetic reconstruction for simulated data

#1. Introduction

In today's computer lab we will look at techniques for constructing phylogenetic trees. Some explanation about genetic trees what they are and what they mean...

We will work in R, using the packages "ape" and "phangorn". You can install these packages by typing:

`install.packages("ape")`  
`install.packages("phangorn")`  
`library(ape)`  
`library(phangorn)`

#2. Genetic Data

We will first look at a dataset that comes with the phangorn package. It contains genetic data (i.e. RNA samples) from many different species. Load the dataset by typing:

`data(Laurasiatherian)`

To get a summary of the data you can type `str(Laurasiatherian)`. The data originally comes from  <http://www.allanwilsoncentre.ac.nz/>, you can have a look there to find out more.

## 2.1 Phylogenetic trees

Explain something about phylogenetic analysis: that it is based on a predefined distance metric that decides how far species are apart and that based on this distance metric we can do hierarchical clustering of the data.

Explain agglomerative hierarchical clustering (bottom up), explain you need a distance matrix. Explain something about greediness?

*To understand how this works, let's first look at a small (manageable) subset of the dataset, and do the clustering by hand. To create a subset of the data by using the `subset` command:

mysubset <- subset(Laurasiatherian, subset=c(19,20,28,29,30))`

**Exercise**  

 - *Select 5 species from the Lauraiatherian dataset  (for instance 3 that are closely related and 2 that are more distantly related) and create a subset containing their data.*  
 - *You can compute the distance between the elements in the set (pairwise) using `dist.ml(mysubset)`. Compute the distance matrix and see if you understand what it means. Why are some numbers small and some numbers large?*

 **Ik snap eigenlijk niet echt wat dit nou precies output. In de documentatie staat dist.ml fits distances for nucleotide and amino acid models, er is blijkbaar ook dist.logDet en dist.hamming.**  

- *You can use the distance matrix to perform the hierarchical clustering: merge the two clusters that are closest, compute the new distances between all clusters (**are they supposed to do that by averaging the numbers in the distance matrix?**), merge again the two clusters that are closest and so on. Perform the hierarchical clustering for your subset and create the phylogenetic tree.*

The phangorn package provides a function that automises the hierarchical clustering method: `NJ`. You can build and plot a phylogenetic tree blabla

`dm <- dist.ml(mysubset)`  
`tree <- NJ(dm)`  
`plot(tree)`  

**Exercise**

*Use the `NJ` function to build a phylogenetic tree for your own subset. Is the tree the same as the one that you created?*  
 **Als ik dit doe met de subset uit de vorige opdracht (donkey, horse, spermwhale, finwhale en bluewhale) krijg ik een wel hele vreemde tree: (bluewhale finwhale ((donkey horse) spermwhale)), die dus bovendien niet binair is (wat onze manueel geconstrueerde bomen wel vrijwel altijd zijn). Dit zal wel iets te maken hebben met de clustering techniek die gebruikt wordt - neighbour joining neem ik aan? - maar ik begrijp niet echt waar dit resultaat vandaag komt.** 

- Create a tree for the entire dataset, does it make sense?

**Ik zou ook nog wat dingen willen toevoegen die het wat duidelijker maken dat deze techniek niet echt bijzonder robuust is, maar ik heb op het moment even niet echt ideeen**

#3. Language Data

In this part of today's lab exercise, we will look at language data.

Blabla explain dataset, explain cognates
<http://language.cs.auckland.ac.nz/what-we-did/>

**Ik begrijp niet hoe ik deze dataset in de goede vorm kan krijgen, de code uit Jelle's oude computer lab helpt me niet echt verder helaas. Daardoor weet ik ook nog even niet wat een goede opdracht hiermee is, omdat ik niet zelf een beetje kan spelen en kijken wat er gebeurt. Het lijkt me een goed idee om de data al in het goede format te leveren aan de studenten.**


#4. Data from prev assignment?

Misschien kunnen we ook nog data analyseren uit een van de eerdere assignments, dat zou wel leuk zijn. Misschien is het een beetje veel though.

Er moeten ook nog wat meer vragen in het practicum (ipv opdrachten) die evt terug kunnen komen op het tentamen, daar moet ik nog even over nadenken.

#5. Technical problems

If you have trouble with installing the phangorn package on ubuntu, have a look at the following two links:

 - To get a newer version of R: <http://ubuntuforums.org/showthread.php?t=2264580>
 
 - To install Biostrings manually: <http://permalink.gmane.org/gmane.comp.lang.r.phylo/4471>
