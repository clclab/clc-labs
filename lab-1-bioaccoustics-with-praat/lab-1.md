---
title: "Computer lab 1: Bioacoustics with Praat"
author: BSc Psychobiology, UvA 
date: 1 February 2016
numbersections: true
header-includes:
    - \usepackage{graphicx}
    - \usepackage{fullpage}
    - \usepackage{color}
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

By default, Praat is not installed on the lab computers. There's no need to install Praat; we've included Praat in this lab's folder that you can run directly. If you need a Praat executable for a different operating system, go to \url{www.praat.org} and download the Praat version for your favourite operating system.

\begin{itemize}
\action Extract the Praat executable from this lab's folder
\action Run Praat, by double-clicking the executable
\end{itemize}

You'll see two windows: **Praat objects** and **Praat picture**. **Praat objects** is where the sounds your editing or analyzing will appear. **Praat picture** is where you can visualize the output of various analyses. 

# The anatomy of a sound

From the **Praat objects** window, navigate to *Open > read from file*, or type Ctrl-o. In this lab's folder, you'll find a file called \file{sine.wav}. Open and load it into Praat. Now that we have a Praat object, let's have a look at what we can learn.

First, let's play the sound.

\begin{itemize}
\action Play the sound by selecting it in from *Praat objects* and clicking Play
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

You'll notice this sound wave consists of a constantly repeating pattern. Each repetition of this pattern constitutes one vibration. The number of vibrations per second is called the *frequency* of the sound. Let's try and find out the frequency of this sound. To do this, we'll use a different representation of the sound, called a *Spectrum*.

Apart from sounds, Praat objects can also represent other information, such as the results of various sound-analyses. Go back to the Praat objects window, and create a Spectrum object using the buttons on the right.

\begin{itemize}
\action Create a Spectrum object: click the "Spectrum -" button under "Analyze", and click "To Spectrum...". Accept the default settings.
\action Select the Spectrum object if it isn't already and visualize it by clicking the "View \& Edit" button.
\ask Find the x-coordinate of the peak in the spectrum as precisely as possible. You'll probably need to zoom in a bit to do this accurately (tip: select the area around the peak you want to study and select "Zoom to selection" from the View menu at the top of the window, or press Ctrl-n). What is the frequency of the sound? 
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
\action Create a Spectrum object of \file{bassoon.wav} and display it with View \& Edit. 
\ask Can you find a peak in the spectrum corresponding to the frequency you found before?  
\ask Read the frequencies of some other peaks in the spectrum. Wat can you say about their relation to each other numerically? 
\end{itemize}

## The waveform and spectogram

Now we'll have a look at some human vocalizations. 

\begin{itemize}
\action Load the files \file{french-baby.wav} and \file{german-baby.wav} into Praat objects and listen to both files.
\action Click View \& Edit to look at the waveform for one of the files.
\ask Without zooming in, what information can we extract from just the waveform?
\end{itemize}

As you can hear and see, these sounds are more complex than the sounds we've dealt with so far. While before, the sounds that we dealt with didn't change over time in terms of pitch, the pattern of vibrations in these sounds changes continuously. Counting vibrations or looking at the spectrum will not be tell us much. With these sort of sounds, a *spectogram* is a much more informative visualisation. The spectogram is shown in the View & Edit window below the waveform, but we'll explore some Praat functionality to draw the spectograms of both baby sounds above each other.

So far we've seen how we can view and edit Praat objects. Praat has different viewers for different objects, where you can interact with the objects and zoom in on regions of interest. When you're writing a paper however, you might want to somehow extract these visualisations and save them as pictures. For this reason, most Praat objects can, apart from being viewed, also be drawn into the **Praat picture** window, from where they can be saved as figures. We'll use this functionality to draw the spectograms of the two baby sounds. 

\begin{itemize}
\action Select the french-baby or german-baby sound. 
\action In the *Praat picture* window draw a rectangle with a width of six and height of four by dragging the mouse.
\action Create a Spectogram object. Click on the "Spectrum -" button under Analyse. From there, click on the "To spectogram..." button and accept the default settings.
\action Select the freshly created Spectogram object and click "Paint..." under the "Draw - " button and accept the default settings again. 
\action Draw a second rectangle below the first one. Use the second rectangle to draw the Spectogram of the other baby sound.
\ask Given what we know about spectrums and waveforms, and by comparing the appearance of the spectogram to what the babies sound like, what property of the sound do you think the spectogram visualizes? What do the x- and y- axes represent? What does the darkness of pixels represent?
\end{itemize}

# Speech

Although we're all very familiar with how to produce and interpret speech sounds, recognizing them in waveforms and spectograms is a bit of an art.

## Phonemes

Phonemes are the components of speech. The word "slit", for example consists of a fricative, a liquid, a vowel, and a plosive. Fricatives and plosives are generated without using the vocal chords, liquids, vowels and plosives do require vocal chords. Plosives are generated by completely stopping the airflow for a fraction of a section. 

\begin{itemize}
\action Load the file \file{slit.wav}
\action Take a look at the waveform and spectogram and listen to the file
\ask By looking at the waveform and spectrogram, can identify the different phonemes that make up the word? 
\askstar Which is the easiest way to identify a plosive; the spectogram or the waveform? Why?
\askstar Which is the easiest way to identify a vowel; the spectogram or the waveform? Why?
\end{itemize}

## The sound of silence

Very small changes to the signal can sometimes have large effects on perception. How significant an effect could a silence of 50ms inserted into a speech signal have? That's what we're going to find out now.

Inserting a small period of silence (silent interval) at specific places in words can create the effect of hearing an extra phoneme. Have a look at the paper included with this lab. 

First, we'll create a small silence to be inserted into the \file{slit.wav} sound.

\begin{itemize}
\action In the Praat objects window, go to the menu "New" > "Sound" and click "Create sound from formula"
\action Change the value of the "Name" field to "silence". 
\action Adjust the end time to create a sound of about 50ms
\action Change the sampling frequency to 22050
\action In the formula field, type "0" (that's a zero)
\action Click OK
\action Open the View \& Edit screen for your new sound
\action Select the entire sound (have a look a the Select menu if you run into issues)
\action Copy it, using "Edit > Copy selection to Sound clipboard" or Ctrl-c
\end{itemize}

Now we're going to insert the silence into our recording of the word "slit".

\begin{itemize}
\action Go to the View \& Edit window for the sound \file{slit.wav}
\action Using the spectogram and waveform, find a spot in between the "s" and the "l" sound and place the cursor there
\end{itemize}

To prevent sudden jumps in the waveform, we'll want to insert our sound at a moment where the wave crosses the zero line. 

\begin{itemize}
\action After having placed the cursor between the "s" and "l" sound, click on "Select" > "Move cursor to nearest zero crossing"
\action Now insert the silence we copied earlier by clicking "Edit" > "Paste after selection", or by pressing Ctrl-v.
\ask Play the sound. Which word do you hear?
\end{itemize}
