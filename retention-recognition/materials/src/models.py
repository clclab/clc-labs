import numpy as np
from RnR import RnR

class Param(object):
    """Class for Parameters"""

    def __init__(self, name, bounds=None, minim=0.0, maxim=1.0):
        """
        Params:
            name (str): a name for the parameter
            bounds (tuple of floats): the minimum and maximum value 
                the param can take. Defaults to `minim` and `maxim`.
            minim (float, default=0.0): the lower bound
            maxim (float, default=1.0): the upper bound
        """
        self.name = name
        self.clamped = False
        if bounds is not None:
            assert len(bounds) == 2
            self.min = bounds[0]
            self.max = bounds[1]
        else:
            self.min = minim
            self.max = maxim
        self.value = self.min
    
    def randomize(self):
        """Update parameter value to a random number within the bounds"""
        new_value = np.random.uniform(self.min, self.max)
        return self.update(new_value)

    def update(self, new_value):
        """Update the parameter value"""
        if new_value >= self.min and new_value <= self.max:
            self.value = new_value
        return self
    
    def __repr__(self):
        return f'Param({self.name}={self.value:.3f}, min={self.min:.1f}, max={self.max:.1f})'

class PolynomialModel:
    """Example model: a polynomial of degree 2"""

    def __init__(self, A, B, C, default_bounds=(-1, 1)):
        """Polynomial model
        
        Params:
            A, B, C (float/Param): the parameters (Param instances)
                or their initial values (floats). A
            default_bounds (tuple, default=(-1, 1)):
                the default parameter bounds (used when only initial 
                param values are passed)
        """
        if isinstance(A, Param):
            self.A = A
            self.B = B
            self.C = C
        else:
            self.A = Param('A', bounds=default_bounds).update(A)
            self.B = Param('B', bounds=default_bounds).update(B)
            self.C = Param('C', bounds=default_bounds).update(C)

        self.parameters = dict(A=self.A, B=self.B, C=self.C)

    def __repr__(self):
        return f'PolynomialModel(A={self.A.value:.3f}, B={self.B.value:.3f}, C={self.C.value:.3f})'

    def predict(self, x):
        """Model prediction for input x"""
        return self.A.value * x ** 2 + self.B.value * x + self.C.value

    def cost(self, data):
        """Cost function for observations X and Y using the current model parameters"""
        X, Y = data
        predictions = self.predict(X)
        return np.mean(np.abs(predictions - Y))

    @staticmethod
    def generate_training_data(num_datapoints, 
        x_min=-2, x_max=2, 
        A=.4, B=.3, C=0, 
        sigma=.5, random_seed=1234):
        """"""
        np.random.seed(random_seed)
        xs = np.linspace(x_min, x_max, num_datapoints)
        noise = sigma * np.random.randn(num_datapoints)
        ys = A * xs**2 + B * xs + C + noise
        return xs, ys

class RnRModel(RnR):
    """A wrapper around the original RnR implementation in `RnR.py`.
    It is basically a copy of `RnRv2`, but has the same form as the
    `PolynomialModel` above, so it can be trained using the optimization
    algorithms in `optimization.py`.
    """

    def __init__(self, A, B, C, D, n_max, 
        default_bounds=(0,1),
        memory_capacity="variable"):
        """"""
        # Check parameter values
        assert 0 <= A <= 1
        assert 0 <= B <= 1
        assert 0 <= C <= 1
        assert 0 <= D <= 1
        assert n_max > 0
 
        # Initialize original class
        RnR.__init__(self, A, B, C, D, munp=1, muwp=1, nmax=n_max, mcapacity=memory_capacity)    
        
        self.A = Param('A', bounds=default_bounds).update(A)
        self.B = Param('B', bounds=default_bounds).update(B)
        self.C = Param('C', bounds=default_bounds).update(C)
        self.D = Param('D', bounds=default_bounds).update(D)
        self.parameters = dict(A=self.A, B=self.B, C=self.C, D=self.D)
    
    def __repr__(self):
        return f'RnRModel(A={self.A.value:.3f}, B={self.B.value:.3f}, C={self.C.value:.3f}, D={self.D.value:.3f})'

    def cost(self, experiment):
        """"""
        _, correlation_coef = self.performance(experiment)
        cost = (2 - (correlation_coef + 1)) / 2
        return cost

    def performance(self, experiment):
        """Performance of the model compared to human performance
        as measured by the Pearson correlation
        
        Args:
            experiment: (Frank2010.Experiment): an experiment instance
                that loads all the relevant data.

        Returns:
            correlation_coef (float): the Pearson correlation coefficient of
                model accuracies and accuracies of human participants
        """
        # Compute accuracies
        accuracies = {}
        for value, condition in experiment.conditions.items():
            results = []

            for word, nonword in condition.test:
                prob_word, prob_nonword, chosen = self.luce(word, nonword)
                # correct = chosen == word # This varies randomly
                correct = prob_word > prob_nonword
                results.append(correct)

            accuracy = sum(results) / len(results) * 100
            accuracies[value] = accuracy

        # Compute correlation coefficient
        correlation_coef = experiment.pearsonR(accuracies)
        return accuracies, correlation_coef

    def expose(self, experiment):
        # Expose to stream
        for condition in experiment.conditions.values():
            self.memorizeOnline(condition.stream)

    def recognitionProbability(self, n, sequence):
        """Recognition probability"""
        attested_freq = self.subj_freq[n].get(sequence, 0)

        if self.mcapacity == "fixed":
            types = 4  # from working memory literature
        else:
            types = self.countTypes(n)
        
        probability = (1 - self.B.value ** attested_freq) * (self.D.value ** types)
        return probability
    
    def retentionProbability(self, sequence, seqlength):
        """Retention probability"""
        probability = (self.A.value ** seqlength) * (self.C.value ** self.pi)
        return probability 

    def luce(self, word_1, word_2):
        """Use Luce's choice rule (Luce, 1963) to decide which of 
        two words is an actual word (and which the part_word).
        The score for each word is the subjective frequency.

        Args:
            word_1, word_2 (str): the two words to choose between
        
        Returns:
            prob_1 (float): the probability of choosing word 1
            prob_2 (float): the probability of choosing word 2
            chosen (str): the word chosen according to luce's rule
                (i.e., either word_1 or word_2)
        """
        return self.Luce(word_1, word_2)
