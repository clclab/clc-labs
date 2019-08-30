# -*- coding: utf-8 -*-
"""
@author: Raquel G. Alhama

Generate stimuli following Frank et al. 2010 (Cognition)

Vocabulary: 6 words, 2 with 2 syllables, 2 with 3 syllables, 2 with 4 syllables
The stimuli is composed of sentences.
Inside a sentence there can not be two consecutive tokens of the same word.

The length (number of words) of the sentences and the number of tokens of each word are given by command line options.

Experiments / Conditions:
1. Sentence length: 1,2,3,4,6,8,12,24.
2. Amount of exposure: 48,100,300,600,900,1200
3. Number of word types: 3,4,5,6,9


# Changelog:
july 2019: Substantially rewritten by Bas Cornelissen. Cleaned up the code,
    and started fixing a bug in the generation of the stimuli. Also made all
    randomness controllable by using numpy. So setting np.random.seed(0) makes
    everything replicable.
"""

import re
import math
import numpy as np
import csv
import os

# Fix random seed
np.random.seed(0)

""""""

EXPERIMENTS = {
    1: {
        'name': 'sentence_length',
        'sentence_length': [1, 2, 3, 4, 6, 8, 12, 24],
        'num_tokens': 100,
        'num_types': 6
    },
    2: {
        'name': 'num_tokens',
        'sentence_length': 4,
        'num_tokens': [48, 100, 300, 600, 900, 1200],
        'num_types': 6
    },
    3: {
        'name': 'vocabulary_size',
        'sentence_length': 4,
        'num_tokens': [200, 150, 100, 66],
        'num_types': [3, 4, 5, 6, 9]
    }
}

EXPERIMENTAL_CONDITIONS = {
    1: (1, 2, 3, 4, 6, 8, 12, 24), 
    2: (48, 100, 300, 600, 900, 1200), 
    3: (3, 4, 5, 6, 9)
}
EXP_COND = EXPERIMENTAL_CONDITIONS

CONDITION_LABELS = {1: "sentence_length", 2: "num_tokens", 3:"vocabulary_size"}
CONDITION = CONDITION_LABELS

FILENAMES = {1: 'E1-data.csv', 2: 'E2-data.csv', 3: 'E3-data.csv'}
COLUMNS = ("sbjId", "condition", "timestamp", "wordlen", "rt", "keypressed", "correct")

""""""

class Experiment:
    """A whole experiment, with all its conditions, streams, test items, etc.\
    It also loads the real data of the experiment.
    Structure: experiment.cnd[condition].stream, test, ..."""
    def __init__(self, experiment_id, data_dir='../data/'):
        expId = experiment_id
        self.expId = expId
        self.CONDS_LIST = EXP_COND[expId]

        # Generate experiment for all conditions
        self.cnd = dict.fromkeys(EXP_COND[expId])
        for condition in EXP_COND[expId]:
            self.cnd[condition] = ExpCondition(expId, condition)

        # Load human data of real experiment
        self.expResults = ExperimentResults(expId, data_dir=data_dir)

    def __repr__(self):
        return f'Experiment({self.expId})'

    @property
    def conditions(self):
        return self.cnd

    @property
    def results(self):
        return self.expResults

    def pearsonR(self, modelData):
        """ PearsonR between human data and some model simulation"""
        values_model = [v for (_, v) in sorted(modelData.items())]
        values_humans = [v for (_, v) in sorted(self.expResults.avg_performance.items())]
        values_humans = [x * 100 for x in values_humans]
        # print("PR: ",len(values_humans))
        pearsonr = self._pearsonr(values_humans, values_model)

        if math.isnan(pearsonr):
            pearsonr = 0.0

        return pearsonr

    @staticmethod
    def _pearsonr(x,y):
        # Assume len(x) == len(y)
        n = len(x)
        sum_x = float(sum(x))
        sum_y = float(sum(y))
        sum_x_sq = sum([pow(x, 2) for x in x])
        sum_y_sq = sum([pow(x, 2) for x in y])
        psum = sum(list(map(lambda x, y: x * y, x, y)))
        num = psum - (sum_x * sum_y/n)
        den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)
        if den == 0: return 0
        return num / den

    def plotPerformance(self):
        """
        Plot performance line of model simulation.
        modelData: {exp:{x:(mean_y, std_y)}} (registered in summary)
        """ 
        import matplotlib.pyplot as plt
        plt.figure()
        ax = plt.subplot(111)
        human_data = [ (int(k),v*100) for (k,v) in list(self.expResults.avg_performance.items())]
        ind, data = list(zip(*sorted(human_data)))
        p1 = plt.plot(ind, data, marker=None, linestyle='-', color='black',  linewidth=3.5)
        plt.xlim(plt.xlim()[0]-1,plt.xlim()[1]+2)
        plt.ylim(50, 100)
        plt.ylabel("Performance", fontsize=14)
        plt.xlabel("Condition", fontsize=14)
        plt.title("Experiment {}".format(self.expId))
        plt.show()

class ExpCondition:
    """A complete experimental condition.
    When "shuffle" is False, the order of the test pairs is not randomized. 
    This is just to make it more efficient since the model is blind to the effect of order.
    If used for generating the experiment for humans, then shuffle must be set to True.
    """

    def __init__(self, expId, condition, shuffle_test=False):
        """"""
        self.SYLLABLES = ("ba", "bi", "da", "du", "ti", "tu", 
        "ka", "ki", "la", "lu", "gi", "gu", "pa", "pi", "va", "vu", "zi", "zu")
        self.expId = expId
        self.condition = condition
        self.test_length = 30
        self.shuffle_test = shuffle_test

        # Experiment 1: varies the sentence length
        if self.expId == 1:
            self.sentence_length = condition
            self.tokens = 100
            self.types = 6

        # Experiment 2: varies the number of tokens
        elif self.expId == 2:
            self.sentence_length = 4
            self.tokens = condition
            self.types = 6 # (BC: Changing this has no effect...?)

        # Experiment 3: varies the size of the vocabulary (number of types)
        elif self.expId == 3:
            self.sentence_length = 4
            self.tokens = 600 / condition
            self.types = condition 

        # Set up experiment
        self.tokens = int(self.tokens)
        self.words = self.generate_vocabulary(self.types, self.SYLLABLES)
        self.sentences = self.generate_sentences()
        self.stimuli = self.sentences
        self.stream = "##".join(self.sentences)
        self.distractors = self.generate_distractors()
        self.test = self.generate_test()

    def __repr__(self):
        return f'ExpCondition({CONDITION[self.expId]}={self.condition}, experiment={self.expId})'

    @staticmethod
    def generate_vocabulary(num_types, syllables):
        """"Generate a random vocabulary"""

        # Default case: 3 types
        word_lengths = [2, 3, 4]
        
        # BC: I think there was a bug in the code; both self.types == 4 and 5 
        # resulted in vocabularies of 5 words
        if num_types == 4:
            length = np.random.choice(word_lengths[:3])
            word_lengths.append(length)
        elif num_types == 5:
            lengths = np.random.choice(word_lengths[:3], size=2, replace=True)
            word_lengths.extend(lengths)
        elif num_types == 6:
            word_lengths += word_lengths
        elif num_types == 9:
            word_lengths += 2 * word_lengths
        
        # Generate all words 
        vocabulary = []
        for length in word_lengths:
            word_syllables = np.random.choice(syllables, size=length, replace=True)
            word = "".join(word_syllables)
            vocabulary.append(word)
        
        # Check and return
        assert len(vocabulary) == num_types
        return vocabulary

    def generate_sentences(self):
        """Generate sentences"""
        # BC: I've completely reimplemented this, since the
        # original method contained various typos. It's not entirely correct
        # now (some repetitions might be left), but hopefully good enough.
        if self.expId == 3:
            sentences = generate_sentences(self.words, self.tokens, self.sentence_length, 
                total_num_tokens=600)
        else:
            sentences = generate_sentences(self.words, self.tokens, self.sentence_length)

        # Join words in sentences
        joined_sentences = ["".join(sentence) for sentence in sentences]
        return joined_sentences

    def generate_test(self):
        """Generate Test"""
        test = []
        for i in range(self.test_length):
            word = np.random.choice(self.words)
            partword = self.__getRandomDistractor(len(word))
            pair = [word, partword]
            if self.shuffle_test:
                np.random.shuffle(pair)
            test.append(pair)
        
        if self.shuffle_test:
            np.random.shuffle(test)
        return test

    def generate_distractors(self):
        self.distractors = []
        stream = "##".join(self.stimuli)
        syllables = re.findall('..', stream)

        buff = {}
        for i in (2, 3, 4):
            buff[i] = ["##"] * i
        while len(syllables) > 0:

            # Read next syllable
            if len(syllables) > 0:
                nextSyllable = syllables.pop(0)

            # Add syllable to buffers of all window size
            for i in (2, 3, 4):
                buff[i].pop(0)
                buff[i].append(nextSyllable)

            # See if we have partwords
            for i in (2, 3, 4):
                sequence = "".join(buff[i])
                if (sequence.find("##") == -1) and (sequence not in self.words):
                    self.distractors.append(sequence)
                # Exceptional case of 1 word sentences
                if self.expId == 1 and self.condition == 1 and sequence not in self.words:
                    self.distractors.append(sequence)
        self.distractors = list(set(self.distractors))
        
        return self.distractors

    def __getRandomDistractor(self, length):
        """Return a random distractor of a certain length"""
        distractor = ""
        length_k_distractors = []
        for d in self.distractors:
            if len(d) == length:
                length_k_distractors.append(d)
        if len(length_k_distractors) > 1:
            distractor = np.random.choice(length_k_distractors)
        else:
            distractor = length_k_distractors[0]
        return distractor

class ExperimentResults:
    def __init__(self, expId, data_dir='../data/'):
        self.expId = expId
        self.data_dir = data_dir
        self.TEST_LENGTH=30.0
        self.data = []
        self.performance={}
        self.avg_performance={}
        self.std_performance={}
        self.loadData(expId)

    def __repr__(self):
        return f'ExperimentResults(id={self.expId})'

    ''' Given an experiment id, it loads the data from the file. It only stores the average performance across subjects for each condition. '''
    def loadData(self, expId):
        filename = FILENAMES[expId]
        path = os.path.join(self.data_dir, filename)
        f = open(path, 'Ur')
        reader = csv.reader(f)
        data = []
        row_num = 0
        #Read condition, subject, correct
        for row in reader:
            if row_num > 0: 
                condition = row[1]
                sbjId = row[0]
                correct = row[6]
                data.append((condition, sbjId, correct))
            row_num+=1
        #Performance of each subject
        performance={}
        nsubjects_cond=dict([(k,0.0) for k in EXP_COND[expId]])
        for row in data:
            cond=int(row[0])
            nsubjects_cond[cond] += 1
            if not( (row[0],row[1]) in list(performance.keys()) ):
                performance[(row[0],row[1])] = int(row[2])
            else:
                performance[(row[0],row[1])] += int(row[2])
        nsubjects_cond=dict([(k,(float(v)/self.TEST_LENGTH)) for (k,v) in list(nsubjects_cond.items())])
        for k in list(performance.keys()):
            performance[k] = performance[k] / self.TEST_LENGTH
        #dict(map(lambda k,v: (k, v/self.TEST_LENGTH), list(performance.items())))
        
        #Average performance in each condition
        cond_performance = {}
        for k, v in list(performance.items()):
            cond=int(k[0])
            if cond not in cond_performance:
                cond_performance[cond] = [v]
            else:
                cond_performance[cond].append(v)
        avg_performance={}
        std_performance={}
        for cond,v in list(cond_performance.items()):
            avg_performance[cond] = np.mean(np.array(v))
            std_performance[cond] = np.std(np.array(v))
        
        f.close()
        #Instantiate self
        self.data = data
        self.performance=performance
        self.avg_performance=avg_performance
        self.std_performance=std_performance
               
"""
# Generate sentences without repetitions
"""

def segment_list(mylist, segment_length):
    """Split a list in several successive segments 
    (such as sentences) of identical length"""
    assert len(mylist) % segment_length == 0
    num_segments = int(len(mylist) / segment_length)
    segments = []
    for i in range(num_segments):
        start = i * segment_length
        end = (i + 1) * segment_length
        segment = mylist[start:end]
        segments.append(segment)
    return segments

def contains_repetitions(sentence):
    """Checks if a sentence contains repetitions"""
    for word, next_word in zip(sentence, sentence[1:]):
        if word == next_word:
            return True
    return False

def split_sentences(sentences):
    """Split sentences in correct and incorrect ones"""
    correct = []
    incorrect = []
    for sentence in sentences:
        if contains_repetitions(sentence):
            incorrect.append(sentence)
        else:
            correct.append(sentence)
    return correct, incorrect

def shuffle_words(correct, incorrect, max_shuffles=10):
    """Shuffles words in a sentence until there are 
    no repetitions any more (or max_shuffles is reached)"""
    new_incorrect = []
    for sentence in incorrect:
        corrected = False
        for _ in range(max_shuffles):
            np.random.shuffle(sentence)
            if not contains_repetitions(sentence):
                corrected = True
                correct.append(sentence)
                break
                
        if not corrected:
            new_incorrect.append(sentence)
    
    return correct, new_incorrect

def recombine_sentences(sentences):
    """Shuffle words across a set of sentences"""
    sentence_length = len(sentences[0])
    words = [word for sentence in sentences for word in sentence]
    np.random.shuffle(words)
    new_sentences = segment_list(words, sentence_length)
    return new_sentences

def remove_repetitions(correct, incorrect, 
    max_shuffles=15, max_recursion=100, margin=10):
    """Remove repetitions stochastically.
    
    First it shuffles the words in the incorrect sentences until
    repetitions have disapeared. Then it recombines the remaining
    incorrect sentences, together with a few correct ones (to add
    new words) to a set of new sentences, and apply the same
    procedure recursively, until no incorrect sentences remain.
    
    Args:
        max_shuffles (int): the maximum number of times words in
            a sentence are shuffled to exclude repetitions
        max_recursion (int)
        margin (int): the number of correct sentences to include
            in the recombination of the incorrect ones
    
    Returns:
        correct, incorrect
    """
    # Base case
    if len(incorrect) == 0 or max_recursion == 0:
        return correct, incorrect
    
    # Fix sentences by shuffling words of incorrect sentences
    correct, incorrect = shuffle_words(correct, incorrect, max_shuffles=max_shuffles)
    
    # If that didn't work, create new sentences from the words in
    # the incorrect sentences and some correct sentences; and recurse.
    if len(incorrect) > 0:
        new_incorrect = incorrect + correct[:margin]
        new_sentences = recombine_sentences(new_incorrect)
        new_correct, incorrect = split_sentences(new_sentences)
        correct = correct[margin:] + new_correct
        
    # Recurse.
    return remove_repetitions(correct, incorrect, max_recursion=max_recursion-1)
    
def generate_sentences(vocabulary, num_tokens, sentence_length, 
    total_num_tokens=None):
    """Generate sentences of length sentence_length with no repetitions
    
    Args:
        vocabulary (list): list of words to use
        num_tokens (int): the number of occurences of every type 
            (can be None if total_num_tokens is set)
        sentence_length (int): the number of words per sentence
        total_num_tokens (optional, None): if set, it will generate
            this many tokens, meaning that some tokens might be slightly
            more frequent than others
    
    Returns:
        sentences (list): a list of sentences

    """
    if total_num_tokens is not None:
        num_tokens = int(np.floor(total_num_tokens / len(vocabulary)))
        words = num_tokens * vocabulary
        
        # We might need to add some words to get total_num_tokens
        num_missing = total_num_tokens - len(words)
        missing = np.random.choice(vocabulary, num_missing, replace=True)
        words.extend(missing)
        assert len(words) == total_num_tokens
    else:
        words = num_tokens * vocabulary

    # Generate sentences and make sure they satisfy the constraints
    np.random.shuffle(words)
    sentences = segment_list(words, sentence_length)
    correct, incorrect = split_sentences(sentences)
    correct, incorrect = remove_repetitions(correct, incorrect)
    
    # Todo: this will ofen result in a few incorrect sentences....
    # Warning if incorrect sentences remain, but return all anyway
    # if len(incorrect) > 0:
    #     print(f'Including {len(incorrect)} incorrect sentences')

    return correct + incorrect
