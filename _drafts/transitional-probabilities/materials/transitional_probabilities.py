#Import the packages you need here
from __future__ import division #decimal division
import re #package for regular expressions


##################################



def readStimuli(filename):
    """ Reads syllables from a text file.
    Returns a list of syllables """

    # initialize the return list as an empty list
    result = []

    # open the file for reading and loop over the lines
    for line in open(filename, 'r'):
        # get rid of end-of-line ('\n') symbols 
        sline = line.strip()
        syll = re.findall('..',sline)
        result.extend(syll)

    # now that the result list is filled up, return it
    return result

def count(list_of_syllables):
    """ Extract counts of uni- & bigram occurrences from sequence
    of syllables in list_of_syllables """

    # dictionaries to hold the counts of the unigrams & bigrams
    unigram_dict = {}
    bigram_dict = {}

    # loop over the indices of list_of_syllables until the first to last element
    for syll_idx in range(len(list_of_syllables)):
        # form unigram of syllables at index
        unigram = list_of_syllables[syll_idx]

        # see if we have already seen this unigram
        if unigram in unigram_dict:
            # if so, up the count by 1
            unigram_dict[unigram] += 1
        else:
            # if not, set the count to 1
            unigram_dict[unigram] = 1

    #... (extend code for bigrams) 
    #Hint: store the two syllables of the bigram in a tuple

    # return the dictionaries with the unigram and bigram counts
    return unigram_dict, bigram_dict

def TP(bigram, unigram_dict, bigram_dict):
    """ Compute the transitional probability for bigram=(syll_1, syll_2): 
    P(syll_2 | syll_1) = counts (syll_1,syll_2) / counts syll_1.
    """


    # check if bigram is in our bigram dict
    # if so, set count to the value from bigram_dict
        #... COMPLETE

    # divide the (bigram) count by the unigram count of the first syllable to get the probability
    #... COMPLETE

    # return the calculated probability
    

def sequenceProbability(list_of_syllables, unigram_dict, bigram_dict):
    """ Estimate probability of sequence of syllables,
    represented as a list """
    
    # Create a variable to accumulate your result. Set it to 1 initially.
    p = 1.

    # loop over sequence indices
    for syll_idx in range(len(list_of_syllables) - 1):
        # read a bigram tuple from subsequent syllables
        bigram = (list_of_syllables[syll_idx], list_of_syllables[syll_idx + 1])
        
        # multiply previous probability with probability of this bigram
        #  ... (COMPLETE)

    # return the estimated probability of the entire sequence
    # COMPLETE


if __name__ == '__main__':

    print("This is Lab #2 of CMLM :)")
    stimuli = readStimuli("SaffranAslinNewport1996_2A.txt")
    unigram_dict, bigram_dict = count(stimuli)
    print("These are the counts for unigrams: ", unigram_dict)
