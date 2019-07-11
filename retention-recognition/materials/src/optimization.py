import random
import time
import copy
import numpy as np
from matplotlib import pyplot as plt

class Param(object):
    """class for Parameters"""
    def __init__(self, name, bounds=None, minim=0.0, maxim=1.0):
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
        """Update value to random number within the bounds"""
        new_value = np.random.uniform(self.min, self.max)
        return self.update(new_value)

    def update(self, new_value):
        if new_value >= self.min and new_value <= self.max:
            self.value = new_value
        return self
    
    def __repr__(self):
        return f'Param({self.name}={self.value:.3f}, min={self.min:.1f}, max={self.max:.1f})'

# Class alias
parameter_value = Param

class Optimization:
    mRandom = random.Random(time.time())

    @staticmethod
    def grid_search(model, data, parameter_values, step_size):
        c = random.random()

        params_ranges = []
        best_params = []
        grid_size = []
        for i in np.arange(len(parameter_values)):
            param = parameter_values[i]
            params_ranges.append(np.arange(param.min,param.max,step_size))
            grid_size.append(int((param.max- param.min)/ step_size))
            best_params.append(param)

        result_mat = np.zeros((grid_size[0], grid_size[1]))
        X, Y = data
        count_a = 0
        best_cost = model.cost(X,Y)
        for a in params_ranges[0]:
            model.params[parameter_values[0].name] = a
            count_b=0
            for b in params_ranges[1]:
                model.params[parameter_values[1].name] = b
                result_mat[count_a, count_b] = model.cost(X,Y)
                if result_mat[count_a, count_b] <= best_cost:
                    best_cost = result_mat[count_a, count_b]
                    for i in np.arange(len(best_params)):
                        best_params[i].value = model.params[best_params[i].name]
                count_b+=1
            count_a +=1

        plt.imshow(result_mat, cmap='hot', interpolation='nearest')
        plt.show()
        
        return best_params

    @staticmethod
    def hill_climbing(maxIterations, max_jump, model, data, pramater_values
                      ):
        
        #Randomly initializing parameters
        for i in np.arange(len(pramater_values)):
            pramater_values[i].value = random.random()
            model.params[pramater_values[i].name] = pramater_values[i].value

        curr_model = copy.deepcopy(model)
        curr_param = [param for param in pramater_values]


        best_model = copy.deepcopy(curr_model)
        best_param = curr_param


        X = data[0]
        Y = data[1]
        
        iterations = 1
        cost_list = []
        while iterations < maxIterations:
            for i in np.arange(len(curr_param)):
                next_param = Optimization.get_hillClimbing_next_parameter(curr_param, max_jump, i)
                temp_param = next_param
                temp_model = copy.deepcopy(model)
                for i in np.arange(len(pramater_values)):
                    temp_model.params[pramater_values[i].name] = next_param[i].value

                if temp_model.cost(X,Y) < curr_model.cost(X,Y):
                    curr_param = temp_param
                    for i in np.arange(len(pramater_values)):
                        curr_model.params[pramater_values[i].name] = temp_model.params[pramater_values[i].name]
        
            if best_model.cost(X,Y) > curr_model.cost(X,Y):
                best_param = curr_param
                for i in np.arange(len(pramater_values)):
                    best_model.params[pramater_values[i].name] = curr_model.params[pramater_values[i].name]
            

            iterations += 1
            cost_list.append(best_model.cost(X,Y))

        #one can plot the development of the cost function to check convergence
        #plt.plot(range(len(cost_list)), cost_list)
        #plt.show()

        return best_param

    @staticmethod
    def get_hillClimbing_next_parameter(current_parameters, max_jump, changing_param_index):
        next_params = copy.deepcopy(current_parameters)

        #var = min(current_parameters[changing_param_index].max - current_parameters[changing_param_index].value, 
        #   current_parameters[changing_param_index].value - current_parameters[changing_param_index].min) * max_jump
        var = min(current_parameters[changing_param_index] - current_parameters[changing_param_index], 
                  current_parameters[changing_param_index] - current_parameters[changing_param_index]) * max_jump
        
        next_params[changing_param_index].update(Optimization.mRandom.gauss(current_parameters[changing_param_index].value, var))

        return next_params