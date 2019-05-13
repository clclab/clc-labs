import csv
import itertools
import nltk
import numpy as np

class DataReader:
    def __init__(self, filename, vocabulary_size=1000):
        self.vocabulary_size = vocabulary_size
        self.unknown_token = "UNKNOWN_TOKEN"
        self.sentence_start_token = "SENTENCE_START"
        self.sentence_end_token = "SENTENCE_END"
        self.sentences = []
        self.tokenized_sentences = []

        self.read_file(filename)
        self.preprocess()

    def read_file(self, filename):
        # Read the data and append SENTENCE_START and SENTENCE_END tokens
        print("Reading CSV file...")
        with open(filename, 'r') as handle:
            reader = csv.reader(handle, skipinitialspace=True)
            # Skip header row
            next(reader)
            # Load sentences
            lines = [line[0].lower() for line in reader]
            tokens = [nltk.sent_tokenize(line) for line in lines]
            self.sentences = itertools.chain(*tokens)
            # Append SENTENCE_START and SENTENCE_END
            self.sentences = ["%s %s %s" % (self.sentence_start_token, x, self.sentence_end_token) for x in self.sentences]
            self.sentences = self.sentences[:1000]

        print(f"Parsed {len(self.sentences)} sentences.")

        # Tokenize the sentences into words
        self.tokenized_sentences = [nltk.word_tokenize(sent) for sent in self.sentences]

    def preprocess(self):
        # Count the word frequencies
        self.word_freq = nltk.FreqDist(itertools.chain(*self.tokenized_sentences))
        print(f"Found {len(self.word_freq.items())} unique words tokens.")

        # Get the most common words and build index_to_word and word_to_index vectors
        self.vocab = self.word_freq.most_common(self.vocabulary_size - 1)
        self.index_to_word = [x[0] for x in self.vocab]
        self.index_to_word.append(self.unknown_token)
        self.word_to_index = dict([(w, i) for i, w in enumerate(self.index_to_word)])

        print(f"Using vocabulary size {self.vocabulary_size}.")
        print(f"The least frequent word in our vocabulary is '{self.vocab[-1][0]}' and appeared {self.vocab[-1][1]} times.")

        # Replace all words not in our vocabulary with the unknown token
        for i, sent in enumerate(self.tokenized_sentences):
            self.tokenized_sentences[i] = [w if w in self.word_to_index else self.unknown_token for w in sent]

        print(f"Example sentence: '{self.sentences[0]}'")
        print(f"Example sentence after Pre-processing: '{self.tokenized_sentences[0]}'")

    def get_training_sentences(self):

        # Create the training data
        X_train = np.asarray([[self.word_to_index[w] for w in sent[:-1]] for sent in self.tokenized_sentences])
        y_train = np.asarray([[self.word_to_index[w] for w in sent[1:]] for sent in self.tokenized_sentences])

        return X_train, y_train

    def get_training_bigrams(self):

        # Replace all words not in our vocabulary with the unknown token
        one_hot = np.eye(len(self.index_to_word))
        one_grams = []
        i = 0
        for sent in self.tokenized_sentences:
            for j in np.arange(len(sent) - 1):
                if sent[j] != self.unknown_token:
                    one_grams.append(one_hot[self.word_to_index[sent[j]]])
                    i += 1
                # Huh: where is it replacing the OOVs?

        # Create the training data
        X_train = np.asarray(one_grams[:-1])
        y_train = np.asarray(one_grams[1:])

        return X_train, y_train


if __name__ == '__main__':
    dr = DataReader()
    print(dr.index_to_word)
    bigram_input, bigram_output = dr.get_training_bigrams()
    print(bigram_input[0], bigram_output[0])
