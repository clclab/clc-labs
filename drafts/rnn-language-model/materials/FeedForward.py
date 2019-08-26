from Util import *

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
    def calculate_loss(self, inputs, targets, eps=1e-6):
        voc_size, num_datapoints = inputs.shape
        
        # Forward propagation to calculate our predictions
        hidden_state, output = self.forward_pass(inputs)

        # Calculating the loss
        target_indices = np.argmax(targets, axis=0)
        probs = output[target_indices, range(num_datapoints)]
        log_probs = -np.log(np.clip(probs, eps, 1 - eps))
        loss = np.sum(log_probs)

        # Add L2 regulatization term to loss (optional).
        # This is to help the model avoid over-fitting. Can you see how?
        loss += 0.001 / 2 * (np.sum(np.square(self.W_in)) + np.sum(np.square(self.W_out)))

        # compute mean loss:
        return loss / num_datapoints

    def backpropagate_update(self, inputs, targets, learning_rate=0.01):
        voc_size, num_datapoints = inputs.shape

        #forward propagate the input to compute the outputs of each layer.
        hidden_state, outputs = self.forward_pass(inputs)

        # compute the error for the output layer
        delta3 = outputs
        target_indices = np.argmax(targets, axis=0)
        delta3[target_indices, range(num_datapoints)] -= 1
        # delta3[range(targets.shape[0]), np.argmax(targets, axis=1)] -= 1

        # compute the update value for W_out
        # print(delta3.shape, hidden_state.shape)
        dW2 = (hidden_state.T).dot(delta3)

        # compute the error for the hidden layer
        # you see that delta3, the error of the next layer is multiplied by the weight 
        # matrix from this layer to the next layer
        # Thus the error is propagated proportional to the contribution of each unit.
        #  (1 - np.power(hidden_state, 2)) is the derivative of tanh function. 
        # (activation function of the hidden layer)
        delta2 = delta3.dot(self.W_out) * (1 - np.power(hidden_state, 2))

        # compute the update value for the W_in
        dW1 = np.dot(inputs.T, delta2)

        # Gradient descent parameter update
        self.W_in += -learning_rate * dW1
        self.W_out += -learning_rate * dW2

    def train(self, 
        inputs, 
        targets, 
        num_iterations=100, 
        learning_rate=0.01, 
        batch_size=50, 
        verbose=1):

        # mini batch size can not be bigger than the whole traning samples.
        batch_size = min([len(inputs), batch_size])

        # compute number of mini batches based on the mini batch size
        num_batches = len(inputs) // batch_size

        # add the last batch for the remaining samples
        if len(inputs) % batch_size != 0:
            num_batches +=1
        
        # Trace the loss during training.
        trace = []

        # loop several times over the whole training data
        for iteration in range(num_iterations):

            # loop over batches of data.
            for k in np.arange(num_batches):

                # get current batch
                batch_inputs = inputs[:, k*batch_size:(k+1)*batch_size]
                batch_targets = targets[:, k*batch_size:(k+1)*batch_size]

                # compute output, compute loss, propagate the error and update the parameters.
                self.backpropagate_update(batch_inputs, batch_targets, learning_rate)

            # calculate and print loss after each itereation
            total_loss = self.calculate_loss(inputs, targets)
            trace.append((iteration, total_loss))

            if verbose is not 0:
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

if __name__ == "__main__":
    from DataReader import  *
    dr = DataReader('reddit-comments-2015-08.txt', silent=True)
    
    np.random.seed(1234)
    inputs, targets = dr.get_training_bigrams()
    voc_size, num_datapoints = inputs.shape
    neural_network = FeedForwardNN(voc_size, 256, voc_size)
    loss = neural_network.calculate_loss(inputs, targets)
    print("initial loss", loss)

    # Train the network
    trace = neural_network.train(
        inputs, targets,
        num_iterations=100,
        learning_rate=0.01,
        batch_size=50)
