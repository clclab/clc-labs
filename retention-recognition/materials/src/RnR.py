# -*- coding: utf-8 -*-

'''

@author: Raquel G. Alhama



Retention & Recognition Model
------------------------------


'''

import re
import time
import pickle
from math import exp as e
import numpy as np
import sys

## ----------------------------------
TYPELENGTH = "syllables"
SYLLABLE_LENGTH = 2
sybreg = re.compile("..")
verbose = False
timestamp = time.strftime("%d.%m.%Y.%H:%M")
#resultsFile = open("rnr.{}.process".format(timestamp), "w+")


''' Print if verbose mode. '''
def vprint(string):
    if verbose:
        print(string, file=sys.stderr)
        sys.stderr.flush()




''' Increment (or initialize if needed) the count of 'c' in dictionary 't' '''
def increment(t, c, amount=1):
        if c in t:
            t[c] += amount
        else:
            t[c] = amount




#---------------------------------------------------------------------------
class RnR:

    def __init__(self, A, B, C, D, munp, muwp, nmax, mcapacity="variable"):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.munp = munp
        self.muwp = muwp
        self.mcapacity = mcapacity
        self.mu = 1.0 
        self.nmin = 1
        self.nmax = nmax
        self.countTypes = self.__typesAll  # __typesAll or __typesLength
        self.ltypes = dict(list(zip(list(range(1, self.nmax + 1)), [0] * self.nmax))) #dict of length-ntypes
        self.ntypes = 0 #sum of all types
       
        self.subj_freq = {}  # {n:{"puliki":50}}
        self.abs_freq = {}
        for i in range(self.nmin - 1, self.nmax + 1):  # -1 because of the possibility of pauses
            self.subj_freq[i] = {}
            self.abs_freq[i] = {}
            
        # self.splittedCounts={} #{n:{"puliki":{"RETAINED":20,"RECOGNIZED":30}}}
        
        self.PAUSE = "##"


        for i in range(self.nmin, nmax + 1):
            self.subj_freq[i] = {}
            # self.splittedCounts[i]={}

    @staticmethod
    def addInitEndSymbols(stream):
        if stream[0:2] != "##":
            stream = "##" + stream
        if stream[-2:] != "##":
            stream = stream + "##"
        return stream

    ''' 2-Alternative Forced Choice test with sigmoid'''
    def twoAFCSigmoid(self, x, y):


        def sigmoid(d, k=0.05):
            return 1.0 / (1.0 + e(1) ** (-k * d))

        sf_x = sf_y = 0
        l_x = len(x) / 2
        l_y = len(y) / 2
        if x in list(self.subj_freq[l_x].keys()):
            sf_x = self.subj_freq[l_x][x]
        if y in list(self.subj_freq[l_y].keys()):
            sf_y = self.subj_freq[l_y][y]
        d = sf_x - sf_y
        prob_x = abs(sigmoid(d))
        prob_y = 1.0 - prob_x

        if verbose:
            vprint("{0}:sf {1}, prob {2}".format(x, sf_x, prob_x))
            vprint("{0}:sf {1}, prob {2}".format(y, sf_y, prob_y))

        die = np.random.uniform(0.0, 1.0)

        if die < prob_x:
            chosen = x
        else:
            chosen = y

        # Return the probabilities and the chosen segment
        return prob_x, prob_y, chosen



    ''' Luce choice rule (Luce, 1963)'''
    def Luce(self, x, y):
        sf_x = 0
        sf_y = 0
        score_x = 0
        score_y = 0
        l_x = len(x) / 2
        l_y = len(y) / 2
        if x in list(self.subj_freq[l_x].keys()):
            sf_x = self.subj_freq[l_x][x]
        if y in list(self.subj_freq[l_y].keys()):
            sf_y = self.subj_freq[l_y][y]
        if (sf_x + sf_y) > 0:
            score_x = float(sf_x) / float((sf_x + sf_y))
            score_y = float(sf_y) / float((sf_y + sf_x))
        else:
            score_x = 0.5
            score_y = 0.5

        if verbose:
            vprint("{0}:sf {1}, luce score {2}".format(x, sf_x, score_x))
            vprint("{0}:sf {1}, luce score {2}".format(y, sf_y, score_y))

        die = np.random.uniform(0.0, 1.0)

        if die < score_x:
            chosen = x
        else:
            chosen = y

        # Return the scores and the chosen segment
        return score_x, score_y, chosen


    '''All types of any length.
    '''
    def __typesAll(self, n):
        return self.ntypes
    
    '''Number of types of a particular length (for a version of the model that only takes into account types of the same length of the processed sequence)'''
    def __typesLength(self, n):
        return self.ltypes[n]

    
    def treatSequence(self, n, sequence, prevSyllable):
   
        # Increment absolute frequency
        increment(self.abs_freq[n], sequence)
        
        # Effect of pauses
        if prevSyllable == self.PAUSE:
            self.mu = self.muwp  # RnR3
            self.pi = 0.0  # RnR2
        else:
            self.mu = self.munp  # RnR3
            self.pi = 1.0  # RnR2
            
        r1 = np.random.uniform(0.0, 1.0)
        r2 = np.random.uniform(0.0, 1.0)

        if  r1 < self.recognitionProbability(n, sequence):
            if verbose:
                vprint (sequence + " recognized!")
            if sequence != self.PAUSE and sequence not in list(self.subj_freq[n].keys()):
                self.ltypes[n] += 1
                self.ntypes+=1
            increment(self.subj_freq[n], sequence)
#            if sequence not in self.splittedCounts[n].keys():
#                self.splittedCounts[n][sequence]={"RECOGNIZED":1,"RETAINED":0}
#            else:
#                self.splittedCounts[n][sequence]["RECOGNIZED"]+=1

        elif r2 < self.retentionProbability(sequence, n):
            if verbose:
                vprint(sequence + " retained")
            if sequence != self.PAUSE and sequence not in list(self.subj_freq[n].keys()):
                self.ltypes[n] += 1
                self.ntypes+=1
            increment(self.subj_freq[n], sequence)  # RETAINED!
#            if sequence not in self.splittedCounts[n].keys():
#                self.splittedCounts[n][sequence]={"RECOGNIZED":0,"RETAINED":1}
#            else:
#                self.splittedCounts[n][sequence]["RETAINED"]+=1
        else:
            if verbose:
                vprint(sequence + " ignored!")


    ''' Online reading of the input + memorizing (only efficient for a single run).
        Alternative: create_candidates + memorize.
    '''
    def memorizeOnline(self, stream):

        pausereg = re.compile("##")
        # Add initial and ending symbols if missing
        stream = self.addInitEndSymbols(stream)
        if verbose:
            vprint("Stream to memorize: " + stream)

        # Split into syllables (two character/syllable)
        syllables = sybreg.findall(stream)
    
        prev = 0
        act = 1
    
        while act < len(syllables):
            prevsyllable = syllables[prev]
            actsyllable = syllables[act]
            if actsyllable != self.PAUSE:  # segments that begin with a pause are ignored, to avoid duplicates
                for i in range(self.nmin, self.nmax + 1):
                    if act + i < len(syllables):
                        segment = syllables[act:act + i]
                        # If there's pauses in the segment, then read more syllables (as many as pauses) so that the segment has the right size
                        if self.PAUSE in segment:
                            np = len(pausereg.findall("".join(segment)))
                        else:
                            np=0
                        #np = Counter(segment)["##"] VERY SLOW!
                        if act + i + np < len(syllables):
                            segment = syllables[act:act + i + np]
                            # ignore segments that end with pause (to prevent duplicates)
                            if segment[-1] != self.PAUSE:
                                segment_filtered = [x  for x in segment if x != "##"]
                                if verbose:
                                    vprint("sequence {0}, which comes after {1}".format("".join(segment_filtered), prevsyllable))
                                if len(segment_filtered) > 0:
                                    if verbose:
                                        vprint ("SEGMENT: {}".format(segment_filtered))
                                    self.treatSequence(len(segment_filtered), "".join(segment_filtered), prevsyllable)
            prev = act
            act += 1

        return self.subj_freq


    ''' Read stimuli and create all possible candidate segments (to later memorize). Only efficient for more than one run over same stimuli.
        Returns: ordered list of candidate segments and previous syllable ((seg1,psyb1),...)
    '''
    @staticmethod
    def createCandidates(stream, nmax, outputFile=None):

        pausereg = re.compile("##")
        # Add initial and ending symbols if missing
        stream = RnR.addInitEndSymbols(stream)

        # Split into syllables (two character/syllable)
        syllables = sybreg.findall(stream)

        prev = 0
        act = 1

        #Allocate memory for candidates (right now more than needed, because pauses add extra syllables, but it's more efficient in time than to compute actual size)
        candidates=[None]*(nmax*len(syllables))
        cidx=0
        while act < len(syllables):
            prevsyllable = syllables[prev]
            actsyllable = syllables[act]
            if actsyllable != "##":  # segments that begin with a pause are ignored, to avoid duplicates
                for i in range(1, nmax + 1):
                    if act + i < len(syllables):
                        segment = syllables[act:act + i]
                        # If there's pauses in the segment, then read more syllables (as many as pauses) so that the segment has the right size
                        if "##" in segment:
                            np = len(pausereg.findall("".join(segment)))
                        else:
                            np=0
                        #np = Counter(segment)["##"] VERY SLOW!
                        if act + i + np < len(syllables):
                            segment = syllables[act:act + i + np]
                            # ignore segments that end with pause (to prevent duplicates)
                            if segment[-1] != "##":
                                segment_filtered = [x  for x in segment if x != "##"]
                                if len(segment_filtered) > 0:
                                    candidates[cidx]=("".join(segment_filtered), prevsyllable)
                                    cidx+=1
            prev = act
            act += 1

        if not outputFile is None:
           fh=open(outputFile, "wb")
           pickle.dump(candidates, fh)
           fh.close()
        return candidates

    ''' Expects candidate list as created by createCandidtes: ((seg1,psyb1),...).    '''
    def memorizeCandidates(self, candidates):

        i=0
        maxlen=len(candidates)
        #candidates may allocate more memory than needed, so stop when None is found
        while i < maxlen and not candidates[i] is None:
            segment=candidates[i][0]
            prevsyll=candidates[i][1]
            seglength=len(segment)/2
            self.treatSequence(seglength, segment, prevsyll)
            i+=1

        return self.subj_freq

#---------------------------------------------------------------------------
class RnRv2(RnR):
    
    def __init__(self, A, B, C, D, nmax, mcapacity="variable"):
        assert(0<=A<=1 and 0<=B<=1 and 0<=C<=1 and 0<=D<=1 and nmax>0)
        munp = 1
        muwp = 1
        RnR.__init__(self, A, B, C, D, munp, muwp, nmax, mcapacity)    
        
    ''' Recognition probability '''
    def recognitionProbability(self, n, sequence):
        attested_freq = self.subj_freq[n].get(sequence, 0)

        if self.mcapacity == "fixed":
            types = 4  # from working memory literature
        else:
            types = self.countTypes(n)
        
        prob = (1 - self.B ** attested_freq) * (self.D ** types)
        if verbose:
            vprint("Recognition prob is " + str(prob))
            vprint("subj frequency is " + str(attested_freq))
        return prob
    
    
    ''' Retention probability '''
    def retentionProbability(self, sequence, seqlength):
        prob = (self.A ** seqlength) * (self.C ** self.pi)

    
        vprint("Retention prob is " + str(prob))
        return prob 
#---------------------------------------------------------------------------



'''Example of usage'''
if __name__ == '__main__':

    import Frank2010 as fr
    expId=1
    exp = fr.experiment(expId)
    model = RnRv2(A=0.5, B=0.6, C=.3, D=0.85,nmax=5)
    for cnd, expcnd in list(exp.cnd.items()):
        memory = model.memorizeOnline(expcnd.stream)
        print(memory)

