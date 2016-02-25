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

# Introduction

Explain something about (cultural) evolution of languages?

# Cognates

One way of establishing relatedness of languages is to quantify how many words they have that have a common (etymological) origin. These words are also called cognates. More info on cognates? We will look at a ....
5 sentences from the declaration of human rights in different languages:

English: All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.

Italian: Tutti gli esseri umani nascono liberi ed eguali in dignità e diritti. Essi sono dotati di ragione e di coscienza e devono agire gli uni verso gli altri in spirito di fratellanza.

Romanian: Toate fiin\c{t}ele umane se nasc libere \c{c}i egale \^{i}n demnitate \c{s}i \^{i}n drepturi. Ele sunt \^{i}nzestrate cu ra\c{t}iune \c{s}i con\c{s}tiin\c{t}ă \c{s}i trebuie s\u{a} se comporte unele fa\c{t}\u{a} de altele \^{i}n spiritul fraternit\u{a}\c{t}ii.

German: Alle Menschen sind frei und gleich an W\uml rde und Rechten geboren. Sie sind mit Vernunft und Gewissen begabt und sollen einander im Geist der Br\uml derlichkeit begegnen.

Hungarian: Minden. emberi l\'{e}ny szabadon sz\uml letik \'{e}s egyenl\H{o} m\'{e}lt\'{o}s\'{a}ga \'{e}s joga van. Az emberek, \'{e}sszel \'{e}s lelkiismerettel b\'{i}rv\'{a}n, egym\'{a}ssal szemben testv\'{e}ri szellemben kell hogy viseltessenek.

Nederlands: Alle mensen worden vrij en gelijk in waardigheid en rechten geboren. Zij zijn begiftigd met verstand en geweten, en behoren zich jegens elkander in een geest van broederschap te gedragen.

\begin{itemize}
\action Identify cognates in the 5 sentences, write down for every language pair hom many cognates they have
\action Make a distance matrix based on your results
\action Draw a phylogenetic tree of the 5 languages using your distance matrix (you can do this loosely by looking at the numbers)
\end{itemize}

Brief word about IELex dataset. This massive dataset gives you for each word from the "basic vocabulary" in each language whether or not there is a cognate in the focal language (check http://ielex.mpi.nl/languagelist/all/ to see the word lists and the languages).

\begin{itemize}
\action re-install and load the packages phangorn and ape.
\action Load the dataset by typing\verb|load('language_data.Rdata')|, this will create an object called \verb|mydata| that contains
\action Generate a list of all the languages in the dataset by typing \verb|names(mydata)|, and select some languages to create a phylogenetic tree of.
\action Define your subset with the \verb|subset| function. For instance, if you want to select language 40,41,42, 58 and 60 you type:\begin{verbatim}
mysubset <- subset(mydata,c(40:42,58,60))\end{verbatim}
\action Create a distance matrix and plot your tree (give instructions, also about edgelengths e.d.)
\action Do the same thing for the entire dataset (note that using different clustering algorithms can give you very different results)
\end{itemize}

# Identifying features

Identifying cognates is not the only method for establishing relatedness of languages. We will now look at the same 6 languages, but instead of looking at cognates, we will look at some syntactic features:\begin{itemize}
\item \textbf{Word-order}: The first feature we will look at, is if the language's most common word order is SOV (subject, object, verb) or SVO (subject verb object). Note that the most common word order is not always necessarily the only one.
\item \textbf{Modifier position}: Secondly, we will look at the position of the modifier: does it appear before or after the noun?
\item \textbf{Prodrop}: The third feature we will look at, is if a language allows omission of pronouns. (Hint: English does not, "He walks to school" is a grammatical sentence, whereas "walks to school" is not).
\end{itemize}

To help you to detect the features in our six languages, look at the aditional 6 sentences:

English: I love you

Italian: Ti amo

Romanian: Te iubesc

German: Ich liebe dich

Hungarian: Szeretlek

Dutch: Ik hou van jou

\begin{itemize}
\action Establish the values of the features for the 6 languages (if you cannot do it with the 2 example sentences, find more example sentences or google the problem)
\action Create a distance matrix based on your classification
\action Draw a phylogenetic tree that describes the relatedness of the languages.
\end{itemize}

