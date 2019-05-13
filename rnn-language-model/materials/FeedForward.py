from Util import *
from DataReader import  *

class FeedForwardNN:
    """
    Implements a feed forward neural network.
    """

    """
    Initializing the model.
    This method is called when you make an instance object from the FeedForwadNeuralNetwork Class, eg.:
    neural_network = FeedForwardNN(input_dim=10, hidden_dim=32, output_dim=10)
    """
    def __init__(self, input_dim, hidden_dim, output_dim):
        """
        These are the dimensions of the networks. We can also assume them as the hyper parameters.
        :param input_dim: length of the input vector.
        :param hidden_dim: number of hidden units in the hidden layer
        :param output_dim: length of the output vector.
        """

        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim

        # Initializing the parameters of the model, randomly.
        self.init_params()

    """
    This method is called in the init method. when the object of this class is initializing. It sets the values
    of the parameters (weight matrices) randomly.
    """
    def init_params(self):
        # The hidden_dim x input_dim weight matrix that maps input layer to hidden layer
        # --> hidden_state = W_in . input_vector
        bound = np.sqrt(1. / self.input_dim)
        self.W_in = np.random.uniform(-1 * bound, bound, (self.hidden_dim, self.input_dim))

        # The output_dim x hidden_dim weight matrix that maps hidden layer to output layer
        # --> output = W_out . hidden_state
        bound = np.sqrt(1. / self.hidden_dim)
        self.W_out = np.random.uniform(-1 * bound, bound, (self.output_dim, self.hidden_dim))

    """
    Pass the input signal through the network multiplying it by the respective weights an applying the activation
    functions to compute an output.
    """
    def forward_pass(self, inputs):
        # computing hidden_state: W_in . inputs
        # and applying the tanh activation function.
        hidden_state = np.tanh(self.W_in.dot(inputs))

        # computing output: W_out  . hidden_state
        # and applying the softmax activation function.
        output = softmax(self.W_out.dot(hidden_state))

        return hidden_state, output

    """
        evaluate the total loss on the data
    """
    def calculate_loss(self, input, target, eps=1e-6):
        # Forward propagation to calculate our predictions
        hidden_state, output = self.forward_pass(input)

        # Calculating the loss
        corect_logprobs = -np.log(np.clip(output[range(input.shape[0]), np.argmax(target, axis=1)], eps, 1 - eps))

        # Compute total loss:
        loss = np.sum(corect_logprobs)

        # Add L2 regulatization term to loss (optional).
        # This is to help the model avoid over-fitting. Can you see how?
        loss += 0.001 / 2 * (np.sum(np.square(self.W_in)) + np.sum(np.square(self.W_out)))

        # Compute mean loss:
        return (1. / input.shape[0]) * loss

    def backpropagate_update(self, input, target_output, learning_rate=0.01):

        #forward propagate the input to compute the outputs of each layer.
        hidden_state, probabilistic_output = self.forward_pass(input)

        # compute the error for the output layer
        delta3 = probabilistic_output
        delta3[range(target_output.shape[0]), np.argmax(target_output, axis=1)] -= 1

        # compute the update value for W_out
        dW2 = (hidden_state.T).dot(delta3)

        # compute the error for the hidden layer
        # you see that delta3, the error of the next layer is multiplied by the weight matrix from this layer to the next layer
        # Thus the error is propagated proportional to the contribution of each unit.
        #  (1 - np.power(hidden_state, 2)) is the derivative of tanh function. (activation function of the hidden layer)
        delta2 = delta3.dot(self.W_out) * (1 - np.power(hidden_state, 2))

        # compute the update value for the W_in
        dW1 = np.dot(input.T, delta2)

        # Gradient descent parameter update
        self.W_in += -learning_rate * dW1
        self.W_out += -learning_rate * dW2

    def train(self, 
        training_input, 
        training_output, 
        num_iterations=100, 
        learning_rate=0.01, 
        batch_size=50):

        # mini batch size can not be bigger than the whole traning samples.
        batch_size = min([len(training_input), batch_size])

        # compute number of mini batches based on the mini batch size
        number_of_baches = len(training_input) // batch_size

        # add the last batch for the remaining samples
        if len(training_input) % batch_size != 0:
            number_of_baches +=1
        
        # Trace the loss during training.
        trace = []

        # loop several times over the whole training data
        for iteration in range(num_iterations):

            # loop over batches of data.
            for k in np.arange(number_of_baches):

                # get current batch
                input = training_input[k*batch_size:(k+1)*batch_size]
                target_output = training_output[k*batch_size:(k+1)*batch_size]


                # compute output, compute loss, propagate the error and update the parameters.
                self.backpropagate_update(input, target_output,learning_rate )

            # calculate and print loss after each itereation
            total_loss = self.calculate_loss(training_input, training_output)
            trace.append((iteration, total_loss))
            print(f"loss after {iteration} iterations {total_loss}")
        
        return trace

    # Use the model to generate a sentence (sequence of words)
    def generate_sentence(self, word_to_index, index_to_word, sentence_start_token, sentence_end_token, unknown_token):
        onehotvectors = np.eye(len(word_to_index))
        # We start the sentence with the start token
        new_sentence = [word_to_index[sentence_start_token]]
        # Repeat until we get to the end of sentence token
        while not new_sentence[-1] == word_to_index[sentence_end_token]:
            [hidden_states,next_word_probs] = self.forward_pass(onehotvectors[new_sentence[-1]])
            sampled_word = word_to_index[unknown_token]
            # Do not sample unknown words
            while sampled_word == word_to_index[unknown_token]:
                samples = np.random.multinomial(1, next_word_probs)
                sampled_word = np.argmax(samples)
            new_sentence.append(sampled_word)
        sentence_str = [index_to_word[x] for x in new_sentence[1:-1]]
        return sentence_str

    """
        This method is called from the calculate_sentence_loss method.
        For computing the loss when the network is predicting a whole sentece.
    """
    def calculate_sentence_total_loss(self, input_sequence, output_sequence, one_hot):
        L = 0

        # For each sentence...
        for i in np.arange(len(output_sequence)):
            one_hot_input = [one_hot[word] for word in input_sequence[i]]

            s, o = self.forward_pass(one_hot_input)
            # We only care about our prediction of the "correct" words
            correct_word_predictions = o[np.arange(len(output_sequence[i])), output_sequence[i]]
            # Add to the loss based on how off we were
            L += -1 * np.sum(np.log(correct_word_predictions))
        return L

    """
    This method is use to calculate the loss of the feed forward neural network when trying to predict a whole sentence.
    """
    def calculate_sentence_loss(self, input_sequence, output_sequence, one_hot):
        # Divide the total loss by the number of training examples
        N = np.sum((len(y_i) for y_i in output_sequence))
        return self.calculate_sentence_total_loss(input_sequence, output_sequence,one_hot) / N


# if __name__ == "__main__":

#     # reads and pre-processes the data from ../data/reddit-comments-2015-08.csv
#     dr = DataReader()
#     """
#         dr.index_to_word is the ordered list of the vocabulary.
#         The ith word in this list is represented by vector witch its ith index is hot.

#         dr.word_to_index is the dictionary mapping each word to its index.

#         You may also need to use: dr.sentence_start_token, dr.sentence_end_token, dr.unknown_token
#     """

#     # train the model on bi-grams --> to predict the next word
#     train_on_bigrams(dr)

#     # Load the train model model
#     W_in = np.load("W_in.npy")
#     W_out = np.load("W_out.npy")
#     index_to_word = np.load("index_to_word.npy")

#     neural_network = FeedForwardNN(input_dim=W_in.shape[0], hidden_dim=W_in.shape[1], output_dim=W_out.shape[1])

#     # compute sentence generation loss
#     X_train, Y_train = dr.get_training_sentences()
#     onehot = np.eye(len(index_to_word))
#     sentence_generation_loss = neural_network.calculate_sentence_loss(X_train,Y_train,onehot)
#     print(f"sentence generation loss: {sentence_generation_loss}")

#     # generate sentences
#     sentence_min_length = 2
#     num_sentences = 10
#     for i in range(num_sentences):
#         sent = []
#         # get sentences with more than one word.
#         while len(sent) < sentence_min_length:
#             sent = neural_network.generate_sentence(dr.word_to_index, dr.index_to_word,
#                                          dr.sentence_start_token, dr.sentence_end_token, dr.unknown_token)
#         print(" ".join(sent))

#     # Computing and plotting word embeddings ...
#     input_vector = np.asarray([onehot[i] for i in np.arange(len(index_to_word))])
#     input_embeddings = np.dot(input_vector,W_in)
#     plot_distribution_t_SNE(input_embeddings, #vectors
#                             np.repeat([1],len(index_to_word)), # color codes
#                             [w.encode('utf-8') for w in index_to_word]) # string labels



