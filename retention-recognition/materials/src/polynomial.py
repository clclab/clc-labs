import numpy as np
from optimization import Param

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
    
    def update(self, a, b, c):
        """Update all parameter values"""
        self.A.update(a)
        self.B.update(b)
        self.C.update(c)
        return self

    def randomize(self):
        """Randomize all parameters"""
        self.A.randomize()
        self.B.randomize()
        self.C.randomize()
        return self

    def predict(self, x):
        """Model prediction for input x"""
        return self.A.value * x ** 2 + self.B.value * x + self.C.value

    def cost(self, X, Y):
        """Cost function for observations X and Y using the current model parameters"""
        predictions = self.predict(X)
        return np.mean(np.abs(predictions - Y))

    def grid_search_2d(self, data, step_size, 
        param_name_1='A', 
        param_name_2='B',
        return_best=False):
        """Perform a 2 dimensional grid search of the parameter space and
        update the model parameters to the best parameters found.
        
        Params:
            data (tuple): inputs and outputs
            step_size (float)
            param_name_1 (str): name of the first parameter in the grid
            param_name_1 (str): name of the second parameter in the grid
            return_cost_matrix (bool, default False): return only the best parameters:
                (index_1, index_2, cost)
        Returns:
            w_grid (np.array): grid values of the first parameter
            v_grid (np.array): grid values of the second parameter
            cost_matrix (np.array): cost at every point in the grid
        """
        W = self.parameters[param_name_1]
        V = self.parameters[param_name_2]
        w_grid = np.arange(W.min, W.max, step_size)
        v_grid = np.arange(V.min, V.max, step_size)
        
        # Compute cost matrix
        X, Y = data
        cost_matrix = np.zeros((len(w_grid), len(v_grid)))
        for i, w in enumerate(w_grid):
            W.update(w)
            for j, v in enumerate(v_grid):
                V.update(v)
                cost_matrix[i, j] = self.cost(X, Y)

        # Find best parameters and update
        best_ws, best_vs = np.where(cost_matrix == cost_matrix.min())
        best_cost = cost_matrix[best_ws[0], best_vs[0]]
        best_w = w_grid[best_ws[0]]
        best_v = v_grid[best_vs[0]]
        W.update(best_w)
        V.update(best_v)

        # Return either the best param values, or the full cost matrix
        if return_best: 
            return best_w, best_v, best_cost
        else:
            return w_grid, v_grid, cost_matrix

    def plot_cost_matrix(self, cost_matrix, 
        grid_1=None,
        grid_2=None,
        param_name_1='A', 
        param_name_2='B'):
        """Plot a heatmap of the cost matrix"""
        import matplotlib.pyplot as plt

        if grid_1 is None:
            grid_1 = np.arange(cost_matrix.shape[0])
        if grid_2 is None:
            grid_2 = np.arange(cost_matrix.shape[1])

        extent = [min(grid_2), max(grid_2), min(grid_1), max(grid_1)]
        plt.matshow(cost_matrix, extent=extent, interpolation=None)
        plt.ylabel(self.parameters[param_name_1].name)
        plt.xlabel(self.parameters[param_name_2].name)

    def hill_climbing(self, data, num_iterations, max_step_size, random_init=True):
        """Optimize parameters using hill climbing
        
        Params:
            data (X, Y tuple)
            num_iterations (int)
            max_jump (float): the maximum update for parameters
            random_init (optional, bool): whether to randomly initialize the parameters
            
        Returns:
            history (list): a list containing the cost after every parameter update
                (so it has length num_iterations * num_params)
        """

        def next_param_value(param, max_step_size):
            """Draws the next parameter value from a Gaussian around the current value"""
            scale = max_step_size * min(param.max - param.value, param.value - param.min)
            next_value = np.random.normal(loc=param.value, scale=scale)
            return next_value

        if random_init: self.randomize()
        X, Y = data
        current_cost = self.cost(X, Y)
        cost_history = [current_cost]
        for iteration in range(num_iterations):
            for name, param in self.parameters.items():
                orig_value = param.value
                
                # Compute cost with new parameter value
                next_value = next_param_value(param, max_step_size)
                param.update(next_value)
                new_cost = self.cost(X, Y)

                # Update current cost if it has decreased; otherwise reset the parameter
                if new_cost < current_cost:
                    current_cost = new_cost
                else:
                    param.update(orig_value)

                # Store cost
                cost_history.append(current_cost)  
        
        return cost_history

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
