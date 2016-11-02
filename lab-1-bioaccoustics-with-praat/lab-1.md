---
title: "Computer lab 1: Bioacoustics with Praat"
author: BSc Psychobiology, UvA 
date: 1 February 2016
numbersections: true
header-includes:
    - \usepackage{graphicx}
    - \usepackage{fullpage}
    - \usepackage{color}
    - \usepackage[round]{natbib}
    - \input{../labs.tex}
...

\begin{itemize}
\action These are actions for you to do
\ask These are questions
\askstar This is a question that could be on the exam
\end{itemize}

# Goals

Sounds are the raw materials in the study of language and music. In this lab we'll learn how to use Praat for analysing and editing sounds. We'll explore sound signals and look at how they relate to the things we perceive, such as words, melodies or rhythms.

# Getting started

Praat is a free and open-source computer program widely used in phonetics (the study of human speech) and bioaccoustics. It is a swiss-army knife containing many tools for visualising,  analysing and synthesizing sounds.

By default, Praat is not installed on the lab computers. There's no need to install Praat; we've included a Praat executable  that you can run directly in this lab's \file{materials} folder.  If you need a Praat executable for a different operating system, go to \url{www.praat.org} and download the Praat version for your favourite operating system.

\begin{itemize}
\action Extract the Praat executable from this lab's folder
\action Run Praat, by double-clicking the executable
\end{itemize}

You'll see two windows: **Praat objects** and **Praat picture**. **Praat objects** is where the sounds you're editing or analyzing will appear. **Praat picture** is where you can visualize the output of various analyses. 

# The anatomy of a sound

From the **Praat objects** window, navigate to *Open > read from file*, or type Ctrl-o. In the \file{materials} folder, you'll find a file called \file{sine.wav}. Open and load it into Praat. Now that we have a Praat object, let's have a look at what we can learn.

First, let's play the sound.

\begin{itemize}
\action Play the sound by selecting it from \textbf{Praat objects} and clicking \textit{Play}
\end{itemize}

## Soundwaves and spectrums

The most straightforward visual representation of sounds is the waveform. The waveform is a plot of how the air pressure changes over time.

\begin{itemize}
\action Click View \& Edit to look at the waveform of our sound
\end{itemize}

You'll see two visual representations of the sound. The waveform is the upper one. 

\begin{itemize}
\action In the View \& Edit window, zoom in on the waveform until you can clearly see the shape of the sound waves.
\end{itemize}

You'll notice this sound wave consists of a constantly repeating pattern. Each repetition of this pattern constitutes one vibration. The number of vibrations per second is called the *frequency* of the sound. To find out the frequency of \file{sine.wav}, we'll use a different representation of the sound, called a *Spectrum*.

Apart from sounds, Praat objects can also represent other information, such as the results of various sound analyses. 

\begin{itemize}
\action In the Praat objects window, create a Spectrum object: click ``Spectrum -'' under ``Analyze'', and click ``To Spectrum...''. Accept the default settings.
\action Select the Spectrum object if it isn't already and visualise it by clicking the ``View \& Edit'' button.
\ask Find the x-coordinate of the peak in the spectrum as precisely as possible. You'll probably need to zoom in a bit to do this accurately (tip: select the area around the peak you want to study and select ``Zoom to selection'' from the View menu at the top of the window, or press Ctrl-n). What is the frequency of the sound? 
\end{itemize}

Let's look at a more interesting sound.

\begin{itemize}
\action Load the file \file{bassoon.wav} into a Praat object and listen to it. 
\action Listen to \file{sine.wav} again and compare how the two sound.
\ask What simularities do you hear between the sounds? What are the differences?
\action Open the waveform view and zoom in somewhere in the middle of the sound until you can see the individual vibrations (you can use the same zoom to selection technique that you used previously).
\action Find the shortest pattern in the waveform that contains no repetitons (Praat may already have marked this for you).
\action Place the cursor at the start of the pattern, write down the exact time marking of the cursor. 
\action Place the cursor at the end of the pattern (exactly where it begins to repeat itself again), write down the exact time marking of the cursor. 
\ask Using the two time markings, calculate the frequency (in repetitions per second) of the pattern you found. 
\end{itemize}

The frequency you just found is called the *fundamental frequency*. The fundamental frequency usually (but not always) corresponds to perceived pitch. As we will see now, sounds often contain many more frequencies, which can be discovered by looking at the spectrum.

\begin{itemize}
\action Create a Spectrum object of \file{bassoon.wav} and display it with View \& Edit. 
\ask Can you find a peak in the spectrum corresponding to the frequency you found before?  
\askstar Does the pitch that we perceive always correspond to the frequency of the highest peak in the spectrum? 
\action Read the frequencies of some other peaks in the spectrum. What do you notice about their relation to each other?
\end{itemize}

The peaks you found in the spectrum are called harmonics. The same note on various instruments may have the same pitch, but the energy distribution over the harmonics varies, resulting in different *timbres*. The same principle allows us to distinguish between different vowels. 

## The waveform and spectogram

Now we'll have a look at some human vocalisations.\footnote{These soundfiles originate from a study by \cite{Mampe2009}, in which they found that newborn's cries are influenced by their native language. Have a look at the paper if you're interested!}

\begin{itemize}
\action Load the files \file{french-baby.wav} and \file{german-baby.wav} into Praat objects and listen to both files.
\action Click View \& Edit to look at the waveform for one of the files.
\ask Without zooming in, what information can we extract from just the waveform?
\end{itemize}

As you can hear and see, these sounds are more complex than the sounds we've dealt with so far. While before, the sounds that we dealt with didn't change over time in terms of pitch, the pattern of vibrations in these sounds changes continuously. Counting vibrations or looking at the spectrum will not be tell us much. With these sort of sounds, a *spectogram* is a much more informative visualisation. The spectogram is shown in the View & Edit window below the waveform, but we'll explore some Praat functionality to draw the spectograms of both baby sounds above each other.

So far we've seen how we can view and edit Praat objects. Praat has different viewers for different objects, where you can interact with the objects and zoom in on regions of interest. When you're writing a paper however, you might want to somehow extract these visualisations and save them as pictures. For this reason, most Praat objects can, apart from being viewed, also be drawn into the **Praat picture** window, from where they can be saved as figures. We'll use this functionality to draw the spectograms of the two baby sounds. 

\begin{itemize}
\action Select the french-baby or german-baby sound. 
\action In the \textbf{Praat picture} window draw a rectangle with a width of six and height of four by dragging the mouse.
\action Create a Spectogram object. Click on the ``Spectrum -'' button under Analyse. From there, click on the ``To spectogram...'' button and accept the default settings.
\action Select the freshly created Spectogram object and click ``Paint...'' under the ``Draw - '' button and accept the default settings again. 
\action Draw a second rectangle below the first one. Use the second rectangle to draw the Spectogram of the other baby sound.
\ask Having listened to the French baby, could you pick out which spectogram was derived from the French baby sound?
\askstar Given what we know about spectrums and waveforms and harmonics, what does a spectrogram represent? What do the x- and y- axes represent? What does the darkness of pixels represent?
\end{itemize}

# Speech

Although we're all very familiar with producing and interpreting speech sounds, recognising them in waveforms and spectograms is a bit of an art.

## Phonemes

Phonemes are the basic components of speech. The word "slit", for example consists of a fricative, a liquid, a vowel, and a plosive. Fricatives and plosives are generated without using the vocal chords, liquids, vowels and plosives do require vocal chords. Plosives are generated by completely stopping the airflow for a fraction of a section, resulting in complete silence.

\begin{itemize}
\action Load the file \file{slit.wav}
\action Take a look at the waveform and spectogram and listen to the file
\end{itemize}

By looking carefully at the waveform and spectogram, see if you can identify the individual phonemes making up the word. This may be harder than you expect. 

\begin{itemize}
\action To verify your identifications, extract each phoneme into a separate Praat object. Select the phoneme in the sound signal (you can either drag in the waveform or in the spectogram), and click ``File'' > ``Extract selected sound (preserve times)''. This will create a new Praat object, untitled. Use the rename button to rename it s, l, i or t to help you remember which phoneme it contains. 
\action Create a spectrum (not a spectogram) object for the s (fricative) and i (vowel) sound and compare the two
\action Now compare the s and i spectrums to the corresponding part of the spectogram for slit. 
\end{itemize}

Previously, we looked at harmonic frequencies in the bassoon sound. Amplified harmonics in speech sounds show up as peaks in the spectrum, or dark spots in the spectogram. These peaks are called formants. Vowels can be differentiated by looking at how their formants are distributed.

\begin{itemize}
\ask How can you identify a fricative in the spectogram?
\askstar How can you recognize a plosive in the spectogram? And in the waveform?
\end{itemize}

## The sound of silence

Very small changes to the signal can sometimes have dramatic effects on perception. For example, inserting a small period of silence (silent interval) at specific places in words can create the effect of hearing an extra phoneme. In this final part of the lab we'll explore the effect of inserting a small silence in our recording of "slit" at just the right place. 

First, we'll create a small silence to be inserted into the \file{slit.wav} sound. To find out an appropriate duration for this silence, we'll look at a paper that investigated the effect of a silent interval in the word "slit". Have a look at the methods section, as well as the graph with results, in the paper by \cite{Marcus1978} that's attached to this lab (\file{paper.pdf}). Use the graph summarizing their results to find a good duration for the silent interval. 


\begin{itemize}
\action In the Praat objects window, go to the menu ``New'' > ``Sound'' and click ``Create sound from formula''
\action Change the value of the ``Name'' field to ``silence''. 
\action Adjust the end time to the duration of the silent interval that you found
\action In the formula field, type ``0'' (zero)
\action Click OK
\action Open the View \& Edit screen for your new sound
\action Select the entire sound (have a look a the Select menu if you run into issues)
\action Copy it, using ``Edit > Copy selection to Sound clipboard'' or Ctrl-c
\end{itemize}

Now we're going to insert the silence into our recording of the word "slit". 

\begin{itemize}
\action Go to the View \& Edit window for the sound \file{slit.wav}
\action Using the spectogram and waveform, find a spot in between the ``s'' and the ``l'' sound and place the cursor there
\end{itemize}

To prevent sudden jumps in the waveform, we should insert our silence at a moment where the wave crosses the zero line. 

\begin{itemize}
\action After having placed the cursor between the ``s'' and ``l'' sound, click on ``Select'' > ``Move cursor to nearest zero crossing''
\action Now insert the silence we copied earlier by clicking ``Edit'' > ``Paste after selection'', or by pressing Ctrl-v.
\ask Play the sound. Which word do you hear?
\end{itemize}

\bibliographystyle{plainnat}
\bibliography{refs}
