# Computer labs for Evolution of Language and Music

All styles are declared in `styles.sty`. Most importantly, it contains an `exercises` environment that prints the exercises on a light background. For example:

```latex
\begin{exercise}
  \action Open file bla.r and run it with parameter x=2
  \ask How would you interpret the result?
\end{exercise}
``` 

Please use the `lstlisting` environment for R code:
```latex
\begin{lstlisting}
x <- 2
y <- x * 5
\end{lstlisting}

All references are stored in `references.bib`.
``` 

# Suggested TODO

* add a makefile target to build the uploadable zip file for the lab (build the pdf, put in in a zip file together with the materials folder)
* add a master makefile in the root dir to build all labs 

# Notes per lab

## Lab 1

Not all files in the materials folder are used in the lab. When generating the zip file to upload to blackboard, check which ones are actually used in 

## Lab 2

## Lab 3

## Lab 4

## Lab 5
