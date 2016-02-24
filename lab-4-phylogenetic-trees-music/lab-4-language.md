---
title: Features, language
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

# Introduction

Explain something about evolution of languages?

# Cognates

Identifying cognates manually in example sentences?

- Copy 5 example sentences from declaration of human rights, find cognates
- Make distance matrix based on cognates
- Make tree based on distance matrix, does it make sense?

IELex dataset
This massive dataset gives you for each word from the "basic vocabulary" in each language whether or not there is a cognate in the focal language (check http://ielex.mpi.nl/languagelist/all/ to see the word lists and the languages).

\begin{itemize}
\action Load the dataset by typing\verb|load('language_data.Rdata')|, this will create an object called \verb|mydata| that contains
\action Generate a list of all the languages in the dataset by typing \verb|names(mydata)|, and select some languages to create a phylogenetic tree of.
\action Define your subset with the \verb|subset| function. For instance, if you want to select language 40,41,42, 58 and 60 you type:\begin{verbatim}
mysubset <- subset(mydata,c(40:42,58,60))
\action Create a distance matrix and plot your tree (different methods give different results)
\action Do the same thing for the entire dataset, differences
\end{itemize}


# Identifying features

- put 5 sample sentences (romanian, italian, french, hungarian, bulgarian?)
- Find some sample sentences, identify features (SOV/SVO, modifiers, prodrop)
- make distance matrix
- make tree based on that
- check in dataset if correct?

