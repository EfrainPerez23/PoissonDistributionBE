from random import random
from math import e, factorial, pow, log, log10, log2
from DataLayer.Models.Poisson import PoissonModel

class Poisson:

    def inversePoisson(self, _range):
        values = []
        _poisson = PoissonModel(0, 0)

        for i in range(_range):
            ran = random()
            _poisson.x = ran
            _poisson.y = -log(ran)
            values.append(_poisson.json())

        return values