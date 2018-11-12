class PoissonModel:

    def __init__(self, x, y):
        self.x = x
        # self.poisson = poisson
        self.y = y
        # self.acummulate = acummulate

    def json(self):
        return {
            'x': self.x,
            # 'poisson': self.poisson,
            # 'accumulate': self.acummulate,
            'y': self.y
        }