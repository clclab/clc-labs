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

In today's computer lab we will extend last week's simulation of evolution a little bit, and think about the patterns of genetic variation the evolutionary process leaves in a population. We will then look at ways in which we can use current genetic variation to reconstruct the evolutionary history of a population or a set of species. We will use a simple clustering algorithm for such 'phylogenetic tree reconstruction' with the goal of understanding the possibilities and difficulties of approaches based on such algorithms or more complex variants.

# Simulated evolution (continued)

In the previous computer lab, we simulated the evolution of strings, using different fitness functions. Today we are going to do this again, but we will keep track of ancestry during the simulation, so that we can reconstruct family trees of different individuals.

\begin{itemize}
\action Download the scripts for this week's lab and extract them all in the same folder.
\action Start up R-studio (or a terminal) and set your working directory to the folder you created for the scripts (if you forgot how, maybe this website \url{https://support.rstudio.com/hc/en-us/articles/200711843-Working-Directories-and-Workspaces} can help you)
\action We will start with a very small simulation. Change the parameters at the top of the file \verb|lab-3.R|. Set both the population size and the simulation length to 10 and run the script by executing the following command in the console: \begin{verbatim}source('lab-3.R')\end{verbatim}
It will generate a matrix storing information about the parents of the current and all previous generations, and plot the development of the average fitness and the diversity of genotypes over generations.
\action Visualise the parent matrix by running\begin{verbatim}print_parent_matrix(parent_matrix)\end{verbatim}
\askstar Follow some paths up and down. Why do downward paths often end in dead ends, whereas upward paths always go all the way up?
\action Now change the parameters back to its original parameters, and run the simulation again. Print the parent matrix using the same command as before. What do you see?
\end{itemize}

We will now use our parent matrix to reconstruct a tree for the last generation (i.e., we only look at the members of previous generations that have offspring that is still alive).
\begin{itemize}
\action Run the script again, generate a tree with the function \verb|reconstruct_tree| and print it with the function \verb|print_tree|:\begin{verbatim}
        tree <- reconstruct_tree(parent_matrix)
        print_tree(tree)
        \end{verbatim} This will generate a string representation of the tree, that represents a family tree of the living offspring.
\action Copy the string representation and visualise it with the online tree viewer you can find here: \url{http://evolangmus.knownly.net/newick.html}. Set the tree type to \textit{Rectangular cladogram} and paste the tree representation you copied in the box. You can zoom in on the tree by scrolling and move it by clicking on it and dragging the mouse.
\askstar How many generations ago did the LCA live?
\askstar Which aspects of evolution leave traces that we can detect in the current generation and which aspects don't?
\end{itemize}

# Phylogenetic reconstruction with R

In the first part of the lab we reconstructed a family tree based on information that we stored during evolution. In real life, we usually do not have this kind of data. However, we can still try to reconstruct trees by looking at the variation in the current population. For instance, horses and donkeys might genetically be more similar than horses and frogs, so the branches of the latter probably connect further up in the hierarchy than the branches of the former. This type of analysis, that is based on a distance measure between current population members, is called phylogenetic reconstruction. In this part of the lab, we will use two \texttt{R} to automatically construct phylogenetic trees.\begin{itemize}
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

To reconstruct the evolutionary relationship between the different species in this dataset, we start by measuring 'genetic distance' between the genetic samples for each species. For simplicity, we assume that all species ultimately originate from one common ancestor (an uncontroversial assumption in evolutionary biology), and that species have diverged genetically by picking up mutations at a roughly constant rate (a more problematic assumption). The genetic distance between two species is then proportional to the time that has passed since their last common ancestor. distance between strings of DNA or RNA is typically measured by counting how many mutations are needed to change one into the other.

\begin{itemize}
    \action Select 5 species from the Laurasiatherian dataset  (for instance 3 that are closely related and 2 that are more distantly related) and create a subset containing their data using:\begin{verbatim} mysubset <- subset(Laurasiatherian, subset=c(19,20,28,29,30))\end{verbatim}(The numbers should correspond to your selection)
    \action Compute the pairwise distance between all elements in the set using the function \verb|dist.ml| and print it\begin{verbatim}dm <- dist.ml(mysubset)
    print(dm)\end{verbatim}
    \ask Why are some numbers small and some numbers large?
\end{itemize}

You can use the distance matrix to perform the hierarchical clustering: merge the two clusters that are closest, compute the new distances between all clusters, merge again the two clusters that are closest and so on. \begin{itemize}
    \action Manually perform the hierarchical clustering for your subset and create the phylogenetic tree.
    \action The \texttt{phangorn} package provides several functions that automise different hierarchical clustering methods, use one of these clustering algorithms to automatically generate a phylogenetic tree for your subset and plot it:
    \ask Draw a tree (without any calculations) that describes the phylogenetic relations between these different species.
\end{itemize}

We can use a simple algorithm called 'hierarchical clustering' to build such phylogenetic trees automatically. In hierarchical clustering we start by thinking about each datapoint as its own 'cluster'. We then start making bigger clusters by repeating the following steps over and over again:
\begin{enumerate}
\item compute the distances between all clusters;
\item merge the two clusters that are closest to eachother.
\end{enumerate}

We can represent the process of repeated merges as a tree, and interpret it as a phylogenetic tree. In the simplest instance of this algorithm, we define 'distance' between a cluster A and a cluster B as the average distance between any data point in A and any data point in B (a slightly more complicated method, Ward's clustering, uses the square root of the average of the squared point-to-point distances).

\begin{itemize}
	\askstar Perform 3 iterations of this algorithm with pen and paper.
    \action The \texttt{phangorn} package provides several functions that automise different hierarchical clustering methods. Automatically generate a phylogenetic tree for your subset and plot it using:\begin{verbatim}
        tree <- upgma(dm, method='average')
        print(dm)
    \end{verbatim}
\ask Is the tree the same as the one that you created?
\action Now create a tree for the entire dataset, does it make sense?
\action Try different ways to compute the distance between clusters by changing the parameter \texttt{method} (options are, for instance \textit{ward}, \textit{single} and textit{median}). Do you observe many changes in the tree?
\ask Now create a tree for the entire dataset. Does it make sense?
\ask (optional) Try different ways to compute the distance between clusters by changing the parameter \texttt{method} (options are, for instance \textit{ward}, \textit{single} and textit{median}). Do you observe many changes in the tree?
\end{itemize}

# Phylogenetic reconstruction of simulated data

We will now investigate what happens if we use the clustering methods in the \texttt{phangorn} package to analyse our own simulated data.\begin{itemize}
    \action Rerun the script \verb|lab-3.R| to generate a new population and parent matrix
    \action Generate a distance matrix using the function \verb|compute_distance_matrix|, generate a tree with the upgma function (choose your own \textit{method}) and plot it:\begin{verbatim}
        dm <- compute_distance_matrix(parent_matrix)
        tree <- upgma(dm, method='ward')
        plot(tree,cex=0.3)
    \end{verbatim}    
    The parameter \textit{cex} sets the fontsize of the plot.
    \action Now generate a family tree of the simulation by running\begin{verbatim}
        tree_gold <- reconstruct_tree(parent_matrix)
        print_tree(tree_gold)
        \end{verbatim} and plot it using the tree visualiser you used before.
    \ask How well did the clustering algorithm retrieve the original clustering?
    \askstar How can you explain the differences between the two trees?
\end{itemize}
