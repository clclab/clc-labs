---
title: Bioacoustics in Praat
slug: bioacoustics
authors:
    - Bastiaan van der Weij
    - Dieuwke Hupkes
contributors:
    - Bas Cornelissen
    - Peter Dekker
    - Marianne de Heer Kloots
credits: >
  Written by Bastiaan van der Weij and Dieuwke Hupkes in 2016.  
  Updated by Peter Dekker (2017), Bas Cornelissen (2017, 2018, 2019) and Marianne de Heer Kloots (2018).
bibliography: labs/bioacoustics/references.bib
reference-section-title: References
link-citations: true
layout: lab
software: Praat
courses: [Evolamus]
published: true
---


Sounds are the raw materials in the study of language and music. In this
lab we'll learn how to use Praat for analysing and editing sounds. We'll
explore sound signals and look at how they relate to the things we
perceive, such as words, melodies or rhythms.

Getting started
===============

Praat is a free and open-source computer program widely used in
phonetics (the study of human speech) and bioacoustics. It is a
swiss-army knife containing many tools for visualising, analysing and
synthesizing sounds.

- Go to [www.praat.org](www.praat.org), find the download page for
    your favourite operating system and follow the installation
    instructions until you have started the Praat program (usually this
    involves double-clicking a beautiful pink icon).
- You will see two windows: **Praat objects** and **Praat picture**.
    **Praat objects** is where the sounds you are editing or analyzing
    will appear. **Praat picture** is where you can visualize the output
    of various analyses.

The anatomy of a sound
======================

From the **Praat objects** window, navigate to *Open \> Read from file*,
or type Ctrl-O. In the folder we provided with this lab, you'll find a
file called . Open and load it into Praat. Now that we have a Praat
object, let's have a look at what we can learn. First, let's play the
sound.

<div class="exercise">
Play the sound by selecting it from **Praat objects** and clicking
`Play`.
</div>

Soundwaves and spectrums
------------------------

The waveform is the most straightforward visual representation of a
sound. The waveform is a plot of how the air pressure, recorded by the
microphone, changes over time.

<div class="exercise">
- Click `View & Edit` to look at the waveform of our sound. You'll see two
visual representations of the sound. The waveform is the upper one. 
- In the `View & Edit` window, zoom in on the waveform until you can clearly see the shape of the sound waves.
</div>

You'll notice that this sound wave consists of a constantly repeating
pattern. Each repetition of this pattern constitutes one vibration. The
number of vibrations per second is called the *frequency* of the sound.
Let's try to find out the frequency of the sound we've opened. To do
this, we'll use a different representation of the sound, called a
*Spectrum*. The Spectrum can be stored in a new Praat object (apart from
sounds, Praat objects can also represent other information, such as the
results of various sound-analyses).

<div class="exercise">
- In the Praat objects window, with the sine sound object selected, click
`Analyse Spectrum -` and then `To Spectrum...`. Accept the default
settings by clicking OK. 
- Select the Spectrum object (if it isn't already
selected) and visualize it by clicking the `View & Edit` button.
- Study the window and play around with it for a while: click anywhere in the plot, drag the mouse. What does the x-axis represent? What does the
y-axis represent?
- Find the x-coordinate of the peak in the spectrum as
precisely as possible. You'll probably need to zoom in a bit to do this
accurately (tip: select the area around the peak you want to study and
select `Zoom to selection` from the View menu at the top of the window,
or press Ctrl-N). What is the frequency of the sound?
</div>

As you have heard, and seen, this sound is not particularly exciting.
Let's look at a more interesting sound.

<div class="exercise">
- Load the file into a Praat object. 
- Listen to both sounds ( and ) and
compare. Do you hear any similarites, if so which? Which differences do
you hear? 
- Open the waveform view and zoom in (to somewhere in the middle
of the sound) until you can see the individual vibrations of
air-pressure (you can use the same zoom to selection technique that you
used previously).
</div>

You should notice that the individual vibrations form a self-repeating
pattern.

<div class="exercise">
- Find the shortest pattern in the waveform that contains no repetitions
(Praat may already have marked this for you; you can turn this on or off
by clicking *Pulses > Show pulses* in the View & Edit window). 
- Place
the cursor at the start of the pattern, write down the exact time
marking of the cursor. 
- Place the cursor at the end of the pattern
(exactly where it begins to repeat itself again), write down the exact
time marking of the cursor. 
- Using the two time markings, calculate the
frequency (in repetitions per second) of the pattern you found.
</div>

The frequency you just found---the frequency of the shortest
non-repeating pattern---is called the *fundamental frequency*. The
fundamental frequency usually (but not always) corresponds to perceived
pitch. As we will see now, sounds often contain many more frequencies,
which can be discovered by looking at the spectrum.

<div class="exercise">
Having analyze the fundamental frequency of and frequency of , can you
now, more precisely, describe the similarity between the two sounds?
</div>

<div class="exercise">
- Create a Spectrum object of and display it with `View & Edit`. 
- Can you find a peak in the spectrum corresponding to the frequency you found before? 
- Read the frequencies of some other peaks in the spectrum. What
do you notice about their relation to each other? 
- Does the pitch that we
perceive (the fundamental frequency) always correspond to the frequency
of the highest peak in the spectrum?
</div>

The peaks you found in the spectrum are called harmonics. The same note
on various instruments may have the same pitch, but the energy
distribution over the harmonics varies, resulting in different
*timbres*. The same principle allows us to distinguish between different
vowels.

The waveform and spectrogram
----------------------------

Now we'll look at human vocalizations.

<div class="exercise">
- Load the files and into Praat and listen to both sounds.[^1] 
- Click
`View & Edit` to look at the waveform for one of the files. Without
zooming in, which properties of the sound can you recognize by just
looking at the waveform?
</div>

As you can hear and see, these sounds are more complex than the sounds
we've dealt with so far. The previous two sounds didn't change in pitch
and maintained a (relatively) constant timbre throughout their duration.
In the new sounds, the pattern of vibrations in is continuously
changing. Counting vibrations or looking at the spectrum will not be
able to tell us much. With these sort of sounds, a *spectrogram* is a
much more informative visualisation.

<div class="exercise">
- You can view the spectrogram in the View & Edit window, just below the
waveform (if you don't see it, click *Spectrum > Show spectrogram*).
There might be some colorful lines and dots displayed on top, that
correspond to different analyses. You can turn these on and off by
clicking *Pitch > Show pitch* (for the blue Pitch line), *Intensity
$>$ Show intensity* (for the yellow Intensity line), and *Formant >
Show formants* (for the red Formant dots). 
- Note that the Pitch and
Intensity analyses have different y-axis values from the spectrogram
itself. The spectrogram y-axis values are shown on the *left* of the
spectrogram, in *black*. You can change the range of the spectrogram
y-axis in the *Spectrum $>$ Spectrogram settings\...* window. The Pitch
y-axis values (if turned on) are shown on the *right* of the
spectrogram, in *blue*. You can change the range of the Pitch analysis
in the *Pitch $>$ Pitch settings\...* window. The Intensity y-axis
values (if turned on) are also shown on the *right* of the spectrogram,
in *green*. You can change the range of the Intensity analysis in the
*Intensity $>$ Intensity settings\...* window. If you want, play around
with these things a bit by changing the numbers in the settings windows
and clicking *Apply* to see what changes in the spectrogram and analysis
lines. Click *Standards* in the settings windows to go back to the
default settings. 
- Are the default settings for the Pitch analysis (blue
line) appropriate for analyzing this baby's cry? Why/why not?
</div>

<div class="exercise">
- Now turn the Pitch, Intensity and Formant analyses off so you can
clearly see the spectrogram itself. 
- What information does a spectrogram
visualize? What do the x- and y-axes represent? What does the darkness
of pixels mean? 
- Now turn the Pitch analysis on again and change the
settings so that the Pitch y-axis range is the same as the Spectrogram
y-axis range. Given what you learned about pitch in the previous section
and what you know about the spectrogram, do you agree with the result of
Praat's Pitch tracking algorithm (i.e. is the blue line correct)?
Why/why not?
</div>

Plotting spectrograms
---------------------

Now we're going to explore some Praat functionality to draw two
spectrograms above eachother in a picture. We've seen how to view and
edit Praat objects. Praat has different viewers for different objects.
In these viewers, you can interact with the objects and zoom in to
regions of interest. However, when you're, for example, writing a paper,
you want to draw nice pictures containing these visualisations. For this
reason, most Praat objects can be drawn into the **Praat picture**
window. That picture, in turn, can be exported to various image formats.

<div class="exercise">
- Select one of the two baby sounds. 
- In the *Praat picture* window draw a
rectangle with a width of six and height of four (click and drag the
mouse). 
- Create a spectrogram object. Click on the `Analyse spectrum -`
button. From there, click on the `To spectrogram...` button and accept
the default settings. 
- Select spectrogram object that you just created,
click `Paint...` (under the `Draw - ` button) and accept the default
settings. 
- Draw a second rectangle below the first one. Use the second
rectangle to draw the spectrogram of the other baby sound. 
- Suppose you
have heard the two sounds, and are now given these two spectrograms.
Would you be able to figure which spectrogram belongs to which baby
sound? If so, how? If not, explain why not.
</div>

Plotting pitch contours
-----------------------

A common analysis used for sounds is the $F_0$ analysis, or fundamental
frequency analysis. As we've learned, the fundamental frequency
generally corresponds to perceived pitch. We can use Praat to draw a
*Pitch contour* (this is actually the same type of analysis as the blue
line we saw before on top of the spectrogram).

<div class="exercise">
- Erase your Praat picture, by going to the Praat picture window, and
clicking *Edit > Erase all*.
- If you want, you can change the color and
thickness of the drawn lines to make them stand out better. To do this,
open the `Pen` menu, and set the line width to 2.0 (by clicking on
`Line width...`) 
- In the same menu, change the color from black to
something else. For example, red.
</div>

Now we'll run the $F_0$ analysis and draw the results.

<div class="exercise">
- Go to the Praat objects window.
- Select the *Sound* object you want to analyze.
- Under `Analyse periodicity`, click `To pitch...`
- Draw the created Pitch object using the same method we used earlier. How do you think does Praat construct the Pitch contour given a sound? Think of the manual analyses we did before. Describe the process informally, i.e., you don't need to be very precise.
</div>

Speech
======

Although we're all very good at producing and interpreting speech
sounds, recognizing sounds in waveforms or spectrograms is much harder.
In the lecture and tutorial you have learned how different vowels are
distinguished by their first two formants ($F_1$ and $F_2$), and
different consonants are distinguished on the three dimensions of
*manner*, *place* and *voicing*.

<div class="exercise">
- How would you identify different vowels by just looking at their
spectrogram, without listening? (i.e. how would you distinguish /i/ and
/u/?)
- How would you distinguish voiced sounds from unvoiced sounds in a
spectrogram?
- How would you identify a *fricative* in a spectrogram?\
What about a *plosive*?
</div>

Phonemes
--------

Phonemes are the basic components of speech. The word "slit", for
example, consists of a *fricative* /s/, a *lateral* /l/, a *vowel* /i/,
and a *plosive* (or *stop*) /t/. Fricatives are generated by making air
'whirl' through a constriction created by two articulators (e.g. your
two lips, or your tongue and palate). Laterals are generated by letting
air flow around the sides of the tongue. Plosives are generated by
completely stopping the airflow for a very small fraction of time,
resulting in complete silence.

<div class="exercise">
- Load the file `slit.wav`.
- Take a look at the waveform and spectrogram and listen to
the file. 
- By looking carefully at the waveform and spectrogram, see if
you can identify the individual phonemes making up the word. This may be
harder than you expect.
</div>

<div class="exercise">
- To verify your identifications, extract each phoneme into a separate
Praat object. Select the phoneme in the sound signal (you can either
drag in the waveform or in the spectrogram), and click *File \> Extract
selected sound (preserve times)*. This will create a new Praat object,
"untitled". Use the rename button to rename it "s", "l", "i" or "t" to
help you remember which phoneme it contains. 
- Create a spectrum (not a
spectrogram) object for the /s/ (*fricative*) and /i/ (*vowel*) sound
and compare the two.
- Now compare the /s/ and /i/ spectrums to the corresponding part of the spectrogram for slit.
</div>

Previously, we looked at harmonic frequencies in the bassoon sound.
Amplified harmonics in speech sounds show up as peaks in the spectrum,
or dark spots in the spectrogram. These peaks are called formants.
Vowels can be differentiated by looking at how their formants are
distributed.

<div class="exercise">
Articulatorily, what is the difference between formants and harmonics?
How do they relate to the source-filter model?
</div>

The sound of silence
--------------------

Very small changes to the signal can sometimes have dramatic effects on
perception. For example, inserting a small period of silence (silent
interval) at specific places in words can create the effect of hearing
an extra phoneme. In this final part of the lab we'll explore the effect
of inserting a small silence in our recording of "slit" at just the
right place.

First, we'll create a small silence to be inserted into the sound. To
find out an appropriate duration for this silence, we'll look at a paper
that investigated the effect of a silent interval in the word "slit".
Have a look at the methods section, as well as the graph with results,
in the paper by [@Marcus1978] that's attached to this lab (). Use the
graph summarizing their results to find a good duration for the silent
interval.

<div class="exercise">
- In the Praat objects window, go to the menu *New > Sound* and click
*Create sound from formula*. 
- Change the value of the *Name* field to "silence". 
- Adjust the end time to the duration of the silent interval
that you found.
- In the *Formula* field, type "0" (zero).
- Click OK Open the `View & Edit` screen for your new sound.
- Select the entire sound (have a look a the *Select* menu if you run into issues).
- Copy it, using *Edit \ Copy selection to Sound clipboard* or Ctrl-C.
</div>

Now we're going to insert the silence into our recording of the word
"slit".

<div class="exercise">
- Go to the View & Edit window for the sound.
- Using the spectrogram and
waveform, find a spot in between the "s" and the "l" sound and place the
cursor there.
- To prevent sudden jumps in the waveform, we should insert
our silence at a moment where the wave crosses the zero line. After
having placed the cursor between the "s" and "l" sound, click on *Select
> Move cursor to nearest zero crossing*.
- Now insert the silence we copied earlier by clicking *Edit > Paste after selection*, or by pressing Ctrl-V. 
- Play the sound. Which word do you hear?
</div>

[^1]: During the lecture, you heard cries from a French and a German
    baby. These were used in a study done by [@Mampe2009]. The
    recordings that you are analyzing in this lab were recorded for a
    recent follow-up study done by [@Wermke2016] comparing German and
    Chinese babies. Have a look at the studies and the accompanying
    sounds if you're interested! Both are included in this lab's
    materials.
