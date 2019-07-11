import time
import RnR
import Frank2010
import numpy as np
import random
from optimization import Optimization
import copy
import matplotlib.pyplot as plt


def perf(RnRmodel, expId, data_dir):

    exp = Frank2010.experiment(expId, data_dir=data_dir)

    for cnd, expcnd in exp.cnd.items():
        RnRmodel.memorizeOnline("##".join(expcnd.stimuli))


    performance_exp = dict.fromkeys(Frank2010.EXP_COND[expId])
    for cnd, expcnd in exp.cnd.items():
        #print expcnd.stream
        correct = incorrect = 0
        for pair in expcnd.test:
            (prob_x, prob_y, chosen) = RnRmodel.Luce(pair[0], pair[1])
            if chosen in expcnd.words:
                correct += 1
            else:
                incorrect += 1
        percentage_correct = correct * 100.0 / (correct + incorrect)
        performance_exp[cnd] = percentage_correct

    pearsonR = exp.pearsonR(performance_exp)

    return pearsonR

def gridSearchRnR(grid, expId):
    aList = bList = cList = dList= grid
    space = []
    for i in range(len(aList)):
        for j in range(len(bList)):
            for k in range(len(cList)):
                for l in range(len(dList)):
                    space.append([aList[i], bList[j], cList[k], dList[l]])
    costList_grid=[]
    for i in range(len(space)):
        param = space[i]
        rnr_model = RnR.RnRv2(A=param[0], B=param[1], C=param[2], D=param[3], nmax=4)

        pearsonR = perf(rnr_model, expId)

        costList_grid.append(pearsonR)
        #print exp.pearsonR(performance_exp)

    max_value = max(costList_grid)
    max_index = costList_grid.index(max_value)

    return costList_grid, max_value, space[max_index]

def hillClimbRnR(expId, maxIterations, max_jump, data_dir):
    a_curr, b_curr, c_curr, d_curr = random.random(), random.random(), random.random(), random.random()
    curr_model = RnR.RnRv2(A=a_curr, B=b_curr, C=c_curr, D=d_curr, nmax=4)
    curr_param = [curr_model.A, curr_model.B, curr_model.C, curr_model.D]
    curr_perf = perf(curr_model, expId, data_dir)

    best_param = curr_param
    best_perf = curr_perf

    iterations = 1
    costList_hill = []

    while iterations < maxIterations:
        print(iterations)
        par_save2 = [curr_model.A, curr_model.B, curr_model.C, curr_model.D]
        for i in range(len(curr_param)):
            curr_perf = perf(curr_model, expId, data_dir)
            par_save = [curr_model.A, curr_model.B, curr_model.C, curr_model.D]
            next_param = Optimization.get_hillClimbing_next_parameter(curr_param, max_jump, i)
            temp_param = next_param
            curr_model.A, curr_model.B, curr_model.C, curr_model.D = next_param[0], next_param[1], next_param[2], next_param[3]
            #temp_model = RnR.RnRv2(A=next_param[0], B=next_param[1], C=next_param[2], D=next_param[3], nmax=4)
            temp_perf = perf(curr_model, expId)
            if temp_perf > curr_perf:
                curr_perf = temp_perf
                curr_param = temp_param
            else:
                curr_model.A, curr_model.B, curr_model.C, curr_model.D = par_save[0], par_save[1], par_save[2], par_save[3]
        #par_save2 = [curr_model.A, curr_model.B, curr_model.C, curr_model.D]
        curr_perf = perf(curr_model, expId)
        if best_perf < curr_perf:
            best_perf = curr_perf
            best_param = curr_param
        else:
            curr_model.A, curr_model.B, curr_model.C, curr_model.D = par_save2[0], par_save2[1], par_save2[2], par_save2[3]
        print(perf(curr_model, expId, data_dir)[1])
        iterations += 1
        costList_hill.append(best_perf)

    return best_param, costList_hill



class TrainAndEvaluate:

    def __init__(self,model):
        self.model = model

    def fit(self,cost_function,data,optimization_algorithm):
        pass





if __name__ == "__main__":
    seed = time.time()

    #Example experiment
    expId = 2
    grid = [0, 0.5, 1]
    hillClimbJump = 0.1
    hillClimbIterations = 6
    exp = Frank2010.experiment(expId)

    print('Results for Experiment '  + str(expId) + ' are as follows:')
    #grid = gridSearchRnR(grid, expId)
    #print 'Best correlation grid: ' + str(grid[1])
    #print 'Best parameters grid: ' + str(grid[2])
    hill = hillClimbRnR(expId, hillClimbIterations, hillClimbJump)
    print('Best parameters hill: ' + str(hill[0]))
    print('Cost convergence hill: ' + str(hill[1]))

    x = range(len(hill[1]))
    y = hill[1]
    plt.plot(x,y)
    plt.show()



