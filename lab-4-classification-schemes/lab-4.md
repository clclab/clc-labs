---
title: Classification schemes of music and language
author: BSc Psychobiology, UvA
header-includes:
    - \usepackage{graphicx}
    - \usepackage{fullpage}
    - \usepackage{amsmath, amssymb}
    - \usepackage[round, authoryear]{natbib}
    - \newcommand{\uml}{\"{u}}
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

The goals of today's computer lab are to learn about some features of language and music, and about variation across languages and musics. You will further learn, by looking at some specific examples, to appreciate that both languages and musical traditions are transmitted culturally, and are subject to a process of cultural evolution. Finally, you will see how existing variation in languages and musics can be harnassed to reconstruct the cultural evolutionary history, using very similar methods as we saw for phylogenetic tree reconstruction of species and genomes.

* Gain familiarity with music and language classification schemes

# Introduction

The principles of evolution can in theory be applied to any self replicating system where some versions survive and others do not. Language and music also meet these requirements. Hence it is possible to study the *cultural* evolution of language and music. But how do we start start to disentangle historical relationships between cultural phenomona like language and music? Just as we would for biological species, we can apply the comparative method to studying language and music. Cultural phenomena do not have DNA that can be sequenced and compared, so instead we will look at *features* of musics and languages. Coming up with such features is the work of musicologists and linguists. Understanding them and recognizing can sometimes be quite challenging. In this lab, we will explore various approaches to applying the comparative method on music and language data.

# Part 1: Music

Last week, we read 

# Part 2: Language

## Cognates

One way of establishing relatedness of languages is to quantify how many words they have that have a common (etymological) origin. Such words are called cognates. To get a feeling for what cognates are, we will start by identifying cognates in two sentences we can easily find translations of in many languages: a sentence from the declaration of human rights\footnote{for other languages, or more sentences from the same language, you can check http://unicode.org/udhr/assemblies/full\_all.txt} and the favorite sentence from love songs all over the world:

\textit{English:} All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.

\textit{Italian:} Tutti gli esseri umani nascono liberi ed eguali in dignità e diritti. Essi sono dotati di ragione e di coscienza e devono agire gli uni verso gli altri in spirito di fratellanza.

\textit{Romanian:} Toate fiin\c{t}ele umane se nasc libere \c{c}i egale \^{i}n demnitate \c{s}i \^{i}n drepturi. Ele sunt \^{i}nzestrate cu ra\c{t}iune \c{s}i con\c{s}tiin\c{t}ă \c{s}i trebuie s\u{a} se comporte unele fa\c{t}\u{a} de altele \^{i}n spiritul fraternit\u{a}\c{t}ii.

\textit{German:} Alle Menschen sind frei und gleich an W\uml rde und Rechten geboren. Sie sind mit Vernunft und Gewissen begabt und sollen einander im Geist der Br\uml derlichkeit begegnen.

\textit{Hungarian:} Minden. emberi l\'{e}ny szabadon sz\uml letik \'{e}s egyenl\H{o} m\'{e}lt\'{o}s\'{a}ga \'{e}s joga van. Az emberek, \'{e}sszel \'{e}s lelkiismerettel b\'{i}rv\'{a}n, egym\'{a}ssal szemben testv\'{e}ri szellemben kell hogy viseltessenek.

\textit{Nederlands:} Alle mensen worden vrij en gelijk in waardigheid en rechten geboren. Zij zijn begiftigd met verstand en geweten, en behoren zich jegens elkander in een geest van broederschap te gedragen.

\textit{English}: I love you

\textit{Italian}: Ti amo

\textit{Romanian}: Te iubesc

\textit{German}: Ich liebe dich

\textit{Hungarian}: Szeretlek

\textit{Dutch}: Ik hou van jou


\begin{itemize}
\askstar Give three examples, using a different pair of languages for each example, of pairs of words in two languages that are cognates.
\action Write down for every language pair how many cognates they have;\footnote{In reality, identifying cognates is not always so simple, but for now you can just base your judgement on word-similarity}
\askstar Translate this into a distance matrix that captures the distance between the different languages (keep in mind that the more common cognates two languages have, the lower their distance should be);
\action Draw your best guess of the phylogenetic tree describing the historic relations between the 5 languages using your distance matrix (you don't need to run an algorithm).
\end{itemize}

We will now do the same trick but using a much more extensive collection of cognates. We will use the Indo-European Lexical Cognacy Database (IELex), a freely available database of cognate judgments in the Indo-European languages. This massive dataset tells you for each word from the "basic vocabulary" in each language whether or not there is a cognate in the focal language (check http://ielex.mpi.nl/languagelist/all/ to see the word lists and languages), yielding a long feature vector for each language.

\begin{itemize}
\action We preprocessed the dataset for you so it can be loaded into R. To do this, type
\begin{verbatim}
load('language_data.Rdata')
\end{verbatim}
\end{itemize}

This will create an object called \verb|mydata| containing the dataset, you can check the languages in the data by typing \verb|names(mydata)|

\begin{itemize}
\action If you are working from a university computer, reinstall the packages \verb|ape| and \verb|phangorn| with the command \verb|install.packages| (put quotes around the name of the package);
\action Load the packages \verb|ape| and \verb|phangorn| by typing \verb|library(ape)| and \verb|library(phangorn)| in the console;
\action Generate a list of all the languages in the dataset by typing \verb|names(mydata)|
\action Choose a subset of the list of languages. We will initially build a phylogenetic tree of this subset.
\action Define your subset with the \verb|subset| function. For instance, if you want to select language 40,41,42, 58 and 60 you type:\begin{verbatim}
mysubset <- subset(mydata,c(40:42,58,60))\end{verbatim}
\action Create a distance matrix of your subset, by letting the computer count the number of feature values that differ between two languages ("hamming distance"):\begin{verbatim}
distance_matrix <- dist.hamming(mysubset)
\end{verbatim}
\action Pick your favourite clustering algorithm and method and generate a tree, for instance:\begin{verbatim}
tree <- upgma(distance_matrix, method='ward')
\end{verbatim}
\action Plot your tree:\begin{verbatim}
plot(tree, use.edge.length=FALSE, cex=2)
\end{verbatim}
\action Do the same thing for the entire dataset (you might want to adapt the \verb|cex| parameter, that sets the fontsize of the plot). Be aware of the influence the clustering algorithm and method for computing the distances between clusters can have.
\askstar What are the nine main language families you can distinguish within the Indo-European family, and in which regions of the world are they spoken (before colonial times)?
\end{itemize}

## Syntactic features

Identifying cognates is not the only method for establishing relatedness of languages. We could for example also look at *syntactic* features. We will do this for the same 6 languages we used before:

\begin{description}
\item[Word-order] The first feature we will look at, is word order of the language. A language is classified as SOV if the most common word order is \textit{subject object verb}, and as SVO if the most common word order is \textit{subject verb object} (like in English), where the \textit{verb} is taken to be the main verb (e.g., "born" in "are born") and not the auxiliary verbs.  Note that the most common word order is not always necessarily the only one.
\item[Adjective position] Secondly, we will look at the position of the adjective: does it appear before or after the noun?
\item[Prodrop] The third feature we will look at, is whether a language allows omission of pronouns. (Hint: English does not, "He walks to school" is a grammatical sentence, whereas "walks to school" is not).
\end{description}

%Use the follow six sentences to determine if a language allows dropping of pronouns:

\begin{itemize}
\askstar Which of those 6 languages are SVO and which are SOV?
\askstar Dutch is an interesting language in that the basic word order is different in main than in subordinate clauses (the SC in "zij zegt dat S"). What are those basic word orders?
\action Establish the values of the 3 features for the 6 languages (if you cannot do it with the 2 example sentences, find more example sentences or google the problem)
\askstar Create a distance matrix based on your assignment of features
\action Sketch a phylogenetic tree that describes the relatedness of the languages. Is the identical to the tree obtained based on cognate features?
\end{itemize}

