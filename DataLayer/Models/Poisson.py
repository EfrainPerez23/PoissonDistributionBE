class PoissonModel:

    def __init__(self, x, poisson, acummulate, poissonValue):
        self.x = x
        self.poisson = poisson
        self.poissonValue = poissonValue
        self.acummulate = acummulate

    def json(self):
        return {
            'x': self.x,
            'poisson': self.poisson,
            'accumulate': self.acummulate,
            'poissonValue': self.poissonValue
        }