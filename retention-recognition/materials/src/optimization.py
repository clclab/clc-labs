import numpy as np

def grid_search(model, data, step_size, optimize=None, return_best=False):
    """Perform a grid search of the parameter space and
    update the model parameters to the best parameters found.
    
    Params:
        model (object): a model instance. This can be any class instance with 
            a property `parameters` that contains a dictionary mapping names to 
            `Param` instances. Also the model needs to have a `cost(X,Y)`method.
        data (tuple): inputs and outputs
        step_size (float)
        optimize (list): list of parameter names to optimize in the grid search.

    Returns:
        cost_matrix (np.array): cost at every point in the grid
        domains (list): list of domains for all parameters (i.e., the values
            the parameter takes in the grid)
    """
    from itertools import product

    # Optimize all parameters if none are passed
    parameter_names = model.parameters.keys() if optimize is None else optimize
    parameters = [model.parameters[name] for name in parameter_names]

    # Collect the domains: which values every parameter takes in the grid.
    domains = []
    for param in parameters:
        domain = np.arange(param.min, param.max, step_size)
        domains.append(domain)
    
    # `product` creates an iterable that goes through all points 
    # in the grid: it iterates over the (cartesian) product of the ranges
    grid = product(*domains)

    # For every item in the iterable, we need the index: which row/column/etc are we?
    # Otherwise we can't index the cost matrix
    indices = product(*[range(len(r)) for r in domains])
    grid_shape = list(map(len, domains))
    cost_matrix = np.zeros(grid_shape)

    # Compute cost matrix
    for index, param_values in zip(indices, grid):

        # Update all parameters
        for param, param_value in zip(parameters, param_values):
            param.update(param_value)
        
        # Compute the new cost function
        cost_matrix[index] = model.cost(data)
    
    # Identify the indices of the best performing settings
    best_indices = np.where(cost_matrix == cost_matrix.min())
    best_indices = tuple(index[0] for index in best_indices)
    
    # Update the model parameters to the best params
    for i, param in enumerate(parameters):
        domain = domains[i]
        best_param_value = domain[best_indices[i]]
        param.update(best_param_value)

    return cost_matrix, domains

def plot_cost_matrix(cost_matrix, domains=None):
    """Plot a heatmap of the cost matrix"""
    import matplotlib.pyplot as plt
    assert len(cost_matrix.shape) == 2

    if domains is None:
        domain_1 = np.arange(cost_matrix.shape[0])
        domain_2 = np.arange(cost_matrix.shape[1])
    else:
        domain_1, domain_2 = domains

    extent = [min(domain_2), max(domain_2), min(domain_1), max(domain_1)]
    plt.matshow(cost_matrix, extent=extent, interpolation=None)

def hill_climbing(model, data, num_iterations, max_step_size, random_init=True):
    """Optimize parameters using hill climbing
    
    Params:
        model (object): a model instance. This can be any class instance with 
            a property `parameters` that contains a dictionary mapping names to 
            `Param` instances. Also the model needs to have a `cost(X,Y)`method.
            For random initialization, it needs a `randomize()` method.
        data (X, Y tuple)
        num_iterations (int)
        max_jump (float): the maximum update for parameters
        random_init (optional, bool): whether to randomly initialize the parameters
        
    Returns:
        history (list): a list containing the cost after every parameter update
            (so it has length num_iterations * num_params)
    """
    if random_init: randomize(model)
    current_cost = model.cost(data)
    cost_history = [current_cost]
    for iteration in range(num_iterations):
        for name, param in model.parameters.items():
            orig_value = param.value
            
            # Compute cost with new parameter value
            next_value = hill_climbing_next_param_value(param, max_step_size)
            param.update(next_value)
            new_cost = model.cost(data)

            # Update current cost if it has decreased; otherwise reset the parameter
            if new_cost < current_cost:
                current_cost = new_cost
            else:
                param.update(orig_value)

            # Store cost
            cost_history.append(current_cost)  
    
    return cost_history

def randomize(model):
    """Randomize all the model parameters"""
    for param in model.parameters.values():
        param.randomize()

def hill_climbing_next_param_value(param, max_step_size):
    """Draws the next parameter value from a Gaussian around the current value"""
    scale = max_step_size * min(param.max - param.value, param.value - param.min)
    next_value = np.random.normal(loc=param.value, scale=scale)
    return next_value
