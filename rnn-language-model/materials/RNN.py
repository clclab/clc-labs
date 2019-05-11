from Util import *
from DataReader import *
import sys

class RNN:

    # Initializing the RNN object
    def __init__(self, input_dim,output_dim,hidden_dim=512):
        """
        These are the dimensions of the networks. We can also assume them as the hyper parameters.
        :param input_dim: length of the input vector at each time step. (It is not the length of the sequence)
        :param hidden_dim: number of hidden units in the hidden layer
        :param output_dim: length of the output vector at each time step.
        """
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.hidden_dim = hidden_dim

        # Initializing the parameters of the model, randomly.
        self.init_params()

    """
        This method is called in the init method. when the object of this class is initializing. It sets the values
        of the parameters (weight matrices) randomely.
    """
    def init_params(self):
        self.U = np.random.uniform(-np.sqrt(1. / self.input_dim), np.sqrt(1. / self.input_dim),
                                   (self.hidden_dim, self.input_dim))
        self.V = np.random.uniform(-np.sqrt(1. / self.hidden_dim), np.sqrt(1. / self.hidden_dim),
                                   (self.input_dim, self.hidden_dim))
        self.W = np.random.uniform(-np.sqrt(1. / self.hidden_dim), np.sqrt(1. / self.hidden_dim),
                                   (self.hidden_dim, self.hidden_dim))


    def forward_pass(self, input_sequence):
        # The total number of time steps
        sequence_length = len(input_sequence)

        # During forward propagation we save all hidden states.
        hidden_state = np.zeros((sequence_length + 1, self.hidden_dim))
        # For the first time step, the hidden state of the previous step (timestep -1) is set to zero.
        hidden_state[-1] = np.zeros(self.hidden_dim)


        # The outputs at each time step.
        output = np.zeros((sequence_length, self.output_dim))

        # For each time step...
        for t in np.arange(sequence_length):

            # Note: indxing U by input_sequence[t]. This is the same as multiplying U with a one-hot vector.
            hidden_state[t] = np.tanh(self.U[:, input_sequence[t]] + self.W.dot(hidden_state[t - 1]))

            # comuting the output
            output[t] = softmax(self.V.dot(hidden_state[t]))

        # Note: output and hidden_state are both sequences.
        return [output, hidden_state]

    def predict(self, input_sequence):
        # Perform forward propagation and return index of the highest score
        output, hidden_state = self.forward_pass(input_sequence)

        return np.argmax(output, axis=1)

    def back_propagation_through_time(self,x,y,max_back_steps=10):
        T = len(y)
        # Perform forward propagation
        o, s = self.forward_pass(x)

        # Initialize the gradients variables
        dLdU = np.zeros(self.U.shape)
        dLdV = np.zeros(self.V.shape)
        dLdW = np.zeros(self.W.shape)

        # compute error for the output layer for all time steps.
        delta_o = o
        delta_o[np.arange(len(y)), y] -= 1.
        # For each output backwards...
        for t in np.arange(T)[::-1]:
            dLdV += np.outer(delta_o[t], s[t].T)
            # Initial delta calculation for the hidden state with tanh activation
            delta_t = self.V.T.dot(delta_o[t]) * (1 - (s[t] ** 2))
            # Backpropagation through time
            for bptt_step in np.arange(t + 1)[::-1]:
                # print "Backpropagation step t=%d bptt step=%d " % (t, bptt_step)
                dLdW += np.outer(delta_t, s[bptt_step - 1])
                dLdU[:, x[bptt_step]] += delta_t
                # Update delta for next step
                delta_t = self.W.T.dot(delta_t) * (1 - s[bptt_step - 1] ** 2)

        return [dLdU, dLdV, dLdW]

    # compute categorical cross entropy loss
    def calculate_total_loss(self, input_sequence, output_sequence):
        L = 0
        # For each sentence...
        for i in np.arange(len(output_sequence)):
            # compute output and hidden state with forward pass
            o, s = self.forward_pass(input_sequence[i])
            # keep the probability predictions of the correct (target) output
            correct_word_predictions = o[np.arange(len(output_sequence[i])), output_sequence[i]]

            # different between the predicted probability distribution and the target output
            L += -1 * np.sum(np.log(correct_word_predictions))
        return L

    # Divide the total loss by the number of training examples
    def calculate_loss(self, input_sequence, output_sequence):
        # compute total number of words.
        N = np.sum((len(y_i) for y_i in output_sequence))
        return self.calculate_total_loss(input_sequence, output_sequence) / N


    def sgd_backpropagate_update(self, x, y, learning_rate):
        # Calculate the gradients
        dLdU, dLdV, dLdW = self.back_propagation_through_time(x, y)

        # Change parameters according to gradients and learning rate
        self.U -= learning_rate * dLdU
        self.V -= learning_rate * dLdV
        self.W -= learning_rate * dLdW

    def train(self,X_train, y_train, number_of_iterations=30,evaluate_step=1,learning_rate=0.01):
        losses = []
        num_examples_seen = 0
        for epoch in range(number_of_iterations):
            # Optionally evaluate the each evaluate_step number of epochs.
            if (epoch % evaluate_step == 0):
                loss = self.calculate_loss(X_train, y_train)
                #save all the losses in a list so that we can plot them later.
                losses.append((num_examples_seen, loss))

                print "Loss after num_examples_seen=%d epoch=%d: %f" % ( num_examples_seen, epoch, loss)

                # Adjust the learning rate if loss increases
                if (len(losses) > 1 and losses[-1][1] > losses[-2][1]):
                    learning_rate = learning_rate * 0.5
                    print "Setting learning rate to %f" % learning_rate

                sys.stdout.flush()

            # For each training example...
            for i in range(len(y_train)):
                # Apply backpropagation with stochastic gradient decent to update the parameters.
                self.sgd_backpropagate_update(X_train[i], y_train[i], learning_rate)

                # Increase total number of seen examples.
                num_examples_seen += 1

    def generate_sentence(self,word_to_index, index_to_word,sentence_start_token,sentence_end_token,unknown_token):
        # We start the sentence with the start token
        new_sentence = [word_to_index[sentence_start_token]]
        # Repeat until we get to the end of sentence token
        while not new_sentence[-1] == word_to_index[sentence_end_token]:
            [next_word_probs,hidden_states] = self.forward_pass(new_sentence)
            sampled_word = word_to_index[unknown_token]
            # Do not sample unknown words
            while sampled_word == word_to_index[unknown_token]:
                samples = np.random.multinomial(1, next_word_probs[-1])
                sampled_word = np.argmax(samples)
            new_sentence.append(sampled_word)
        sentence_str = [index_to_word[x] for x in new_sentence[1:-1]]
        return sentence_str


if __name__ == '__main__':
    #Teach the RNN to generate english sentences
    dr = DataReader()
    X_train, Y_train = dr.get_training_sentences()

    rnn = RNN(input_dim=len(dr.index_to_word),output_dim=len(dr.index_to_word),hidden_dim=512)
    rnn.train(X_train[0:1000], Y_train[0:1000],number_of_iterations=100)

    sentence_min_length = 1
    num_sentences = 10

    for i in range(num_sentences):
        sent = []
        # get sentences with more than one word.
        while len(sent) < sentence_min_length:
            sent = rnn.generate_sentence(dr.word_to_index, dr.index_to_word,
                                         dr.sentence_start_token,dr.sentence_end_token,dr.unknown_token)
        print " ".join(sent)



