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
