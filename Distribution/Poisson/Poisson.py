from random import random
from math import e, factorial, pow
from DataLayer.Models.Poisson import PoissonModel
from scipy.stats import poisson
import numpy as np  

class Poisson:

    def calculate(self, _range, miu):
        poissonValues = []
        for i in range(_range):
            # poisson equation...
            y = pow(miu, i) * pow(e, -miu) / factorial(i)
            poisson = PoissonModel(i, y, 0, 0)
            poissonValues.append(poisson.json())

        return poissonValues

    def accumulate(self, values, _range):
        for i in range(_range):
            if (i == 0):
                values[i]['accumulate'] = values[i]['poisson']
            else:
                values[i]['accumulate'] = values[i]['poisson'] + values[i - 1]['poisson']
        return values

    def pseudoRandom(self, values, _range):
        for i in range(_range):
            values[i]['pseudoRandom'] = round(random(), 4)
        return values

    def poissonValues(self, _range, mu, values):
        r = poisson.rvs(mu, size=_range).tolist()
        for i in range(_range):
            values[i]['poissonValue'] = r[i]
        return values
