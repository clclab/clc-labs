---
title: Phylogenetic trees - genes, language and simulated data
author: Dieuwke Hupkes, Jelle Zuidema
header-includes:
    - \usepackage{graphicx}
    - \usepackage{fullpage}
...

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
