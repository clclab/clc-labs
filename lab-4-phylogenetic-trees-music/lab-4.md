---
title: Features, language
author: BSc Psychobiology, UvA
numbersections: true
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

Jelle could you fill in this part?

# Introduction

Explain something about (cultural) evolution of languages?

# Cognates

One way of establishing relatedness of languages is to quantify how many words they have that have a common (etymological) origin. These words are also called cognates. We will start by identifying cognates in a sentence from the declaration of human rights in 6 different languages:\footnote{for other languages, or more sentences from the same language, you can check http://unicode.org/udhr/assemblies/full\_all.txt}

\textit{English:} All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.

\textit{Italian:} Tutti gli esseri umani nascono liberi ed eguali in dignità e diritti. Essi sono dotati di ragione e di coscienza e devono agire gli uni verso gli altri in spirito di fratellanza.

\textit{Romanian:} Toate fiin\c{t}ele umane se nasc libere \c{c}i egale \^{i}n demnitate \c{s}i \^{i}n drepturi. Ele sunt \^{i}nzestrate cu ra\c{t}iune \c{s}i con\c{s}tiin\c{t}ă \c{s}i trebuie s\u{a} se comporte unele fa\c{t}\u{a} de altele \^{i}n spiritul fraternit\u{a}\c{t}ii.

\textit{German:} Alle Menschen sind frei und gleich an W\uml rde und Rechten geboren. Sie sind mit Vernunft und Gewissen begabt und sollen einander im Geist der Br\uml derlichkeit begegnen.

\textit{Hungarian:} Minden. emberi l\'{e}ny szabadon sz\uml letik \'{e}s egyenl\H{o} m\'{e}lt\'{o}s\'{a}ga \'{e}s joga van. Az emberek, \'{e}sszel \'{e}s lelkiismerettel b\'{i}rv\'{a}n, egym\'{a}ssal szemben testv\'{e}ri szellemben kell hogy viseltessenek.

\textit{Nederlands:} Alle mensen worden vrij en gelijk in waardigheid en rechten geboren. Zij zijn begiftigd met verstand en geweten, en behoren zich jegens elkander in een geest van broederschap te gedragen.

\begin{itemize}
\action Write down for every language pair how many cognates they have;\footnote{In reality, identifying cognates is not always so simple, but for now you can just go on similarity}
\action Make a distance matrix based on your results;
\action Draw a phylogenetic tree of the 5 languages using your distance matrix (you can do this loosely by looking at the numbers).
\end{itemize}

Now, we will have a look at the Indo-European Lexical Cognacy Database (IELex), a freely available database of cognate judgments in the Indo-European languages. This massive dataset gives you for each word from the "basic vocabulary" in each language whether or not there is a cognate in the focal language (check http://ielex.mpi.nl/languagelist/all/ to see the word lists and the languages).

\begin{itemize}
\action We preprocessed the dataset for you, load it by typing\begin{verbatim}
load('language_data.Rdata')\end{verbatim}
\end{itemize}

This will create an object called \verb|mydata| containing the dataset, you can check the languages in the data by typing \verb|names(mydata)|

\begin{itemize}
\action If you are working on a university computer, reinstall the packages \verb|ape| and \verb|phangorn| with the command \verb|install.packages| (put quotes around the name of the package);
\action Load the packages \verb|ape| and \verb|phangorn| by typing \verb|library(ape)| and \verb|library(phangorn)| in the console;
\action re-install and load the packages phangorn and ape.
\action Generate a lost of all the languages in the dataset by typing \verb|names(mydata)|, and select some languages to create a phylogenetic tree of.
\action Define your subset with the \verb|subset| function. For instance, if you want to select language 40,41,42, 58 and 60 you type:\begin{verbatim}
mysubset <- subset(mydata,c(40:42,58,60))\end{verbatim}
\action Create a distance matrix of your subset, use hamming distance:\begin{verbatim}
distance_matrix <- dist.hamming(mysubset)
\end{verbatim}
\action Pick your favourite clustering algorithm and method and generate a tree, for instance:\begin{verbatim}
tree <- upgma(distance_matrix, method='ward')
\end{verbatim}
\action Plot your tree:\begin{verbatim}
plot(tree, use.edge.length=FALSE, cex=2)
\end{verbatim}
\action Do the same thing for the entire dataset (you might want to adapt the \verb|cex| parameter, that sets the fontsize of the plot). Be aware of the influence the clustering algorithm and method for computing the distances between clusters can have.
\end{itemize}

# Identifying features

Identifying cognates is not the only method for establishing relatedness of languages. We will now look at the same 6 languages, but instead of looking at cognates, we will look at some syntactic features:\begin{itemize}
\item \textbf{Word-order}: The first feature we will look at, is word order of the language. A language is classified as SOV if the most common word order is subject, object verb, and as SVO if the most common word order is subject verb object (like in English). Note that the most common word order is not always necessarily the only one.
\item \textbf{Modifier position}: Secondly, we will look at the position of the modifier: does it appear before or after the noun?
\item \textbf{Prodrop}: The third feature we will look at, is if a language allows omission of pronouns. (Hint: English does not, "He walks to school" is a grammatical sentence, whereas "walks to school" is not).
\end{itemize}

To help you to detect the features in our six languages, look at the aditional 6 sentences:

\textit{English}: I love you

\textit{Italian}: Ti amo

\textit{Romanian}: Te iubesc

\textit{German}: Ich liebe dich

\textit{Hungarian}: Szeretlek

\textit{Dutch}: Ik hou van jou

\begin{itemize}
\action Establish the values of the 3 features for the 6 languages (if you cannot do it with the 2 example sentences, find more example sentences or google the problem)
\action Create a distance matrix based on your classification
\action Draw a phylogenetic tree that describes the relatedness of the languages.
\end{itemize}

