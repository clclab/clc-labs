---
title: Bioacoustics with Praat
numbersections: true
header-includes:
    - \usepackage{graphicx}
    - \usepackage{fullpage}
    - \usepackage{color}
...

In this lab we'll learn how to use Praat for analysing and editing sounds. We'll explore sound signals and look at how they relate to the things we perceive, such as words, melodies or rhythms. Sounds are the raw materials in the study of language and music. 

Praat is a free and open-source computer program widely used in bioacoustics and linguistics. It is a swiss-army knife containing many tools for visualising data, analysing sounds and synthesizing sounds.

# Getting started

By default, Praat is not installed on the lab computes. So our the first step is to download the latest version of Praat from the website and run it.

* Go to [www.praat.org](www.praat.org) and download the latest version for your operating system.

There's no need to install, simply unpack and run the Praat executable.

Run Praat. You'll see two windows: **Praat objects** and **Praat picture**. **Praat objects** is where the sounds your editing or analyzing will appear. **Praat picture** is where you can visualize the output of various analyses. 

# The anatomy of a sound

From the **Praat objects** window, navigate to *Open > read from file*, or type Ctrl-o. In this lab's folder, you'll find a file called sine.wav. Open and load it into Praat. Now that we have a Praat object, let's have a look at what we can learn.

First, let's play the sound.

* Play the sound by selecting it in from *Praat objects* and clicking Play

## Soundwaves and spectrums

The most straightforward visual representation of sounds is the waveform. The waveform is a plot of air pressure changes over time. 

* Select, click View & Edit to look at the waveform of our sound

You'll see two visual representations of the sound. The upper one is the waveform.

The *frequency* of a sound is the amount of vibrations per second. I

* \textcolor{red}{In the view and edit window, use the zoom controls to zoom in to a region where you can easily make out the individual vibrations (have a look at the View menu on top of the window). Using the cursor and the time markings at the bottom of the window, calculate the frequency of this sound.}

That may have felt a bit tedious. Wouldn't it be nice if we could do this automatically? It turns out that we can. 

Praat objects can also be things other than sounds, such as the results of various sound-analyses. Go back to the Praat objects window, and create a Spectrum object using the buttons on the right. 

* Visualize Spectrum object by clicking view
* Find the x-coordinate of the peak in the spectrum as precisely as possible. You'll probably need to zoom in a bit (tip: select the area around the peak and select "Zoom to selection" from the View menu at the top of the window).

Let's now have a look at a different sound.

* Load the file sawtooth.wav into a Praat object and listen to it. Also listen to sine.wav again and compare how the two sound.
* Open the waveform view and zoom in until you can see the individual vibrations

* \textcolor{red}{What is different about the two sounds? What property do the two sounds share? Use the waveforms and spectograms of the two sounds in your analysis.}

* Open up the spectrum of sawtooth.wav. 
* \textcolor{red}{Take a closer look at the frequencies of the first few peaks in the spectrum. What can you tell about their relation to each other?}

## The waveform and spectogram

We'll now turn to some more complex sounds. 

* Load the files french-baby.wav and german-baby.wav into Praat objects and listen to both files.
* Click View & Edit to look at the waveform for one of the files.
* \textcolor{red}{Without zooming in, what information can we extract from just the waveform?}

As you can hear and see, these sounds are much more complex than the sounds we've dealt with so far. While before, the sounds that we dealt with didn't change over time, the pattern of vibrations in these sounds changes continuously. Counting vibrations or looking at the spectrum will not be tell us much. With these sort of sounds, a *spectogram* is a much more informative visualisation. The spectogram is shown in the View & Edit window below the waveform, but we'll explore some Praat functionality to draw the spectograms of both baby sounds above each other.

We've so far seen two object types in Praat: sounds and spectrums. Most objects in Praat can be viewed in a viewer, where you can interact with the objects and zoom in on regions of interest. When you're writing a paper however, you might want to somehow extract these visualisations and save them as pictures. For this reason, most Praat objects can, apart from being viewed, also be drawn into the **Praat picture** window, from where they can be saved as figures. We'll use this functionality to draw the spectograms of the two baby sounds. 

* Select the french-baby or german-baby sound. 
* In the *Praat picture* window draw a rectangle with a width of six and height of four by dragging the mouse.
* Create a Spectogram object. Click on the "Spectrum -" button under Analyse. From there, click on the "To spectogram..." button and accept the default settings.
* Select the freshly created Spectogram object and click "Paint..." under the "Draw - " button and accept the default settings again. 
* Draw a second rectangle below the first one. Use the second rectangle to draw the Spectogram of the other baby sound.

* \textcolor{red}{Given what we know about spectrums and waveforms, and by comparing the appearance of the spectogram to what the babies sound like, what property of the sound do you think the spectogram visualizes? What do the x- and y- axes represent? What does the darkness of pixels represent?}

# Speech

Speech is an arguably even more complex sound than the baby sounds.

* Load the file sometimes-behave-so-strangely.wav into Praat, play it and have a look at the waveform and spectogram. 

You'll notice that while it is difficult to make out individual words in the signal. However, you should be able to identify the different parts of the sentence spoken by comparing the waveform to what you'v heard.

* Cut out the "sometimes behave so strangely part"
* Notice lack of word-boundaries
* Notice lack of frequency peaks in spectogram for fricatives
* Notice silence in waveform for plosives
* Use knowledge acquired about spectograms to figure out what a formants are

Fun:

* Do a pitch analysis
* Synthesize the pitch

# The sound of silence

Very small changes to the signal can sometimes have large effects on perception. How significant an effect could a silence of 50ms inserted into a speech signal have? That's what we're going to find out now.

1. Load the file slit
2. Have a look at the paper and choose a sensible silence interval
3. Create sound from formula (0, ~60ms), call it silence.
4. Use the waveform and spectogram to localize the moment in between the s and the l
5. Insert the silence, listen
5. When time left, do the same for sore, or try to make up an example

\bibliographystyle{plain}
\bibliography{refs}
