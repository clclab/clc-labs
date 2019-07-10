
from optimization import *
import random
import matplotlib.pyplot as plt
import numpy as np
import math

class ExampleModel:

    def __init__(self,init_A,init_B,init_C):
        self.params = {}
        self.params['A'] = init_A
        self.params['B']= init_B
        self.params['C'] = init_C

    def get_Y(self,x):
        return self.params['A'] * math.pow(x, 2) + self.params['B'] * x + self.params['C']


    def cost(self,X,Y):
          return np.mean([(abs(self.get_Y(x) - y)) for x,y in zip(X,Y)])


    @staticmethod
    def generate_random_data_points(number_of_data_points):
        x_data = np.arange(-2,2,1./number_of_data_points)

        return [x for x in x_data],[ 0.4*math.pow(x,2) + 0.3*x + random.Random().random() for x in x_data]




if __name__ == '__main__':

    #Generate Random points
    X,Y = ExampleModel.generate_random_data_points(30)

    model = ExampleModel(init_A=2,init_B=3,init_C=0.5)



    plt.plot(x_val, y_val, 'r')
    plt.scatter(X,Y)
    plt.show()



