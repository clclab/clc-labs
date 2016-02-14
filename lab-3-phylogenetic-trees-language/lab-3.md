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

In today's computer lab we will extend last week's simulation of evolution a little bit, and think about the patterns of genetic variation the evolutionary process leaves in a population. We will then look at ways in which we can use the genetic variation in the last generation to reconstruct the evolutionary history of a population or a set of species. We will use a simple clustering algorithm for such 'phylogenetic tree reconstruction' with the goal of understanding the possibilities and difficulties of approaches based on such algorithms or more complex variants.

# Simulated evolution (continued)

In the previous computer lab, we simulated the evolution of strings of symbols, and looked at the effect of using different fitness functions. Today we are going to do this again, but this time, we will keep track of ancestry during the simulation, so that we can reconstruct family trees of different individuals.

\begin{itemize}
\action Download the scripts for this week's lab and extract them all in the same folder.
\action Start R-studio (or a terminal) and set your working directory to the folder you created for the scripts (if you forgot how, maybe this website \url{https://support.rstudio.com/hc/en-us/articles/200711843-Working-Directories-and-Workspaces} can help you)
\end{itemize}

We will start with a very small simulation. 

\begin{itemize}
\action Change the parameters at the top of the file \verb|lab-3.R|. Set both \texttt{population\_size} and \texttt{simulation\_length} to 10 and run the script by executing the following command in the console: \begin{verbatim}source('lab-3.R')\end{verbatim}
This will generate a matrix, called \texttt{parent\_matrix} storing information about the parents of the current and all previous generations, and plot the development of the average fitness and the diversity of genotypes over generations.
\action Visualise the parent matrix by running\begin{verbatim}print_parent_matrix(parent_matrix)\end{verbatim}
\askstar Follow some paths up and down. Why do downward paths often end in dead ends, whereas upward paths always go all the way up?
\action Now change the parameters back to its original parameters (\texttt{population\_size} 100, \texttt{simulation\_length} 1000), and run the simulation again. After the simulation is finished (this may take a while), print the parent matrix using the same command as before. What do you see?
\end{itemize}

We will now use our parent matrix to reconstruct a tree for the last generation (i.e., we only look at the members of previous generations that have offspring that is still alive).

\begin{itemize}
\action Run the script again, generate a tree with the function \verb|reconstruct_tree| and print it with the function \verb|print_tree|:\begin{verbatim}
        tree <- reconstruct_tree(parent_matrix)
        print_tree(tree)
        \end{verbatim} This will generate a string representation of the tree, that represents a phylogenetic tree
\action To visualize the tree, we will use an online tree viewer. Copy everything between the double quotes in the output of \texttt{print\_tree}. Go to \url{http://evolangmus.knownly.net/newick.html}. Change the tree type from \textit{Cladogram} to \textit{Rectangular cladogram} and paste the tree representation you copied into the text area. After clicking "show", you can zoom in on the tree by scrolling and move it around by dragging it with your mouse.
\askstar How many generations ago did the LCA of the current population live?
\askstar Which aspects of evolution leave traces that we can detect in the current generation and which aspects do not?
\end{itemize}

# Phylogenetic reconstruction with R

In the first part of the lab we reconstructed a family tree based on information that we stored during evolution. In real life, we usually do not have this kind of information. However, we can still attempt to reconstruct trees by looking at the variation in the current population. For instance, horses and donkeys might genetically be more similar than horses and frogs, so the branches of the latter probably connect further up in the hierarchy than the branches of the former. This type of analysis, that is based on a distance measure between current population members, is called phylogenetic reconstruction. In this part of the lab, we will use two \texttt{R} to automatically construct phylogenetic trees.

\begin{itemize}
    \action Install the packages \texttt{ape} and \texttt{phangorn} and load them:\begin{verbatim}
    install.packages("ape")
    install.packages("phangorn")
    library(ape)
    library(phangorn)
    \end{verbatim}
\end{itemize}

We will first look at a dataset that comes with the \texttt{phangorn} package. It contains genetic data (i.e. RNA samples) from many different species. Load the dataset by typing:

`data(Laurasiatherian)`

To get a summary of the data you can type `str(Laurasiatherian)`. The data originally comes from  <http://www.allanwilsoncentre.ac.nz/>, you can have a look there to find out more.

To reconstruct the evolutionary relationship between the different species in this dataset, we start by measuring 'genetic distance' between the genetic samples for each species. For simplicity, we assume that all species ultimately originate from one common ancestor (an uncontroversial assumption in evolutionary biology), and that species have diverged genetically by picking up mutations at a roughly constant rate (a more problematic assumption). 

The distance between strings of DNA or RNA is typically measured by counting the number of mutations required to change one into the other. Because of the second assumption, the genetic distance between two species is proportional to the time that has passed since their last common ancestor.

\begin{itemize}
    \action Select 5 species from the Laurasiatherian dataset  (for instance 3 that are closely related and 2 that are more distantly related) and create a subset of the data containing just these species using:\begin{verbatim}
    mysubset <- subset(Laurasiatherian, subset=c(19,20,28,29,30))\end{verbatim}(The numbers should correspond to the position of the species in the list printed by \texttt{str(Laurasiatherian)}, i.e. Platypus = 1, Possum = 3, etc. )
    \action Verify that your subset contains the right species using:
    \begin{verbatim}
    str(mysubset)
    \end{verbatim}
    \action Compute the pairwise distance between all elements in the set using the function \verb|dist.ml| and print it\begin{verbatim}
    distance_matrix <- dist.ml(mysubset)
    print(distance_matrix)\end{verbatim}
    \ask Do the numbers correspond to your intuitions about the selected species' relatedness?
    \ask Using pen and paper, or your favourite drawing software, try to reconstruct a phylogenetic tree (without doing any calculations) that describes the evolutionary relations between your selected species.
\end{itemize}

We can use a simple method called 'hierarchical clustering' to build such phylogenetic trees automatically. Hierarchical clustering can be done with a simple algorithm that follows these steps:

\begin{enumerate}
\item treat each datapoint as a separate ``cluster'' containing just one datapoint;
\item compute the distances between all clusters;
\item merge the two clusters that are nearest to each other into a new cluster;
\item repeat steps 2 and 3 until only one cluster is left. 
\end{enumerate}

To construct a phylogenetic tree, we can represent each merge as the joining of two branches. In the simplest version of this algorithm, we define 'distance' between a cluster A and a cluster B as the average distance between any data point in A and any data point in B (a slightly more complicated method, Ward's clustering, uses the square root of the average of the squared point-to-point distances).

\begin{itemize}
	\askstar Using the distances between species in \texttt{mysubset}, manually perform three of this algorithm with pen and paper.
\end{itemize}

The \texttt{phangorn} package we installed earlier provides several pre-defined functions for hierarchical clustering methods. 

\begin{itemize}
    \action Generate a phylogenetic tree for your subset and plot it using:\begin{verbatim}
    tree <- upgma(distance_matrix, method='average')
    plot(tree)\end{verbatim}
\ask Is the tree the same as the one that you created?
\action Now create a tree for the entire dataset. Does it agree with your expectations?
\ask (optional) Try different ways to compute the distance between clusters by changing the parameter \texttt{method} (options are, for instance, \textit{ward}, \textit{single} and \textit{median}). Do you notice any changes in the resulting phylogenetic trees?
\end{itemize}

# Phylogenetic reconstruction of simulated data

We will now investigate what happens if we perform phylogenetic analysis on the population resulting from our own simulated evolution.

\begin{itemize}
    \action Rerun the script \verb|lab-3.R| to generate a new population and parent matrix
    \action Generate a distance matrix of the last generation from your simulation using the function \verb|compute_distance_matrix|:
    \begin{verbatim}
    distance_matrix <- compute_distance_matrix(parent_matrix)
    \end{verbatim}
    \action Generate a tree with the upgma function (choose your own \textit{method}) and plot it:
    \begin{verbatim}
    tree <- upgma(distance_matrix, method='ward')
    plot(tree,cex=0.3)
    \end{verbatim}    
    The parameter \textit{cex} sets the fontsize of the plot, adjust it if the numbers are illegible.
    \action Now generate \textit{the actual} family tree of the simulation by running\begin{verbatim}
    gold_standard_tree <- reconstruct_tree(parent_matrix)
    print_tree(gold_standard_tree)\end{verbatim} and plot it using the online tree visualiser we have used before.
    \ask How well did the clustering algorithm reproduce the actual family tree?
    \askstar How can you explain the differences between the reconstructed and the actual family tree?
\end{itemize}
