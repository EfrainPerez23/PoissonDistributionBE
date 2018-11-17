from random import random
from math import e, factorial, pow, log, log10, log2
from DataLayer.Models.Poisson import PoissonModel
from scipy.stats import poisson
from scipy.special import gamma
import numpy as np  
import xlwt

class Poisson:

    def calculate(self, _range, miu):
        poissonValues = []
        for i in range(_range):
            # poisson equation...
            y = pow(miu, i) * pow(e, -miu) / factorial(i)
            poisson = PoissonModel(i, y)
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


    def inversePoisson(self, _range, _lambda):
        values = []
        _poisson = PoissonModel(0, 0)
        wb = xlwt.Workbook()

        ws = None

        for i in range(_range):
            ran = random()
            _poisson.x = ran
            _poisson.y = abs((log(gamma(ran + 1)) + log(ran) + _lambda) / log(_lambda))

            if i  == 0:
                ws = wb.add_sheet('Values')
                ws.write(0,0, 'x', xlwt.easyxf('font: bold on;align: horiz center'))
                ws.write(0,1, 'y', xlwt.easyxf('font: bold on;align: horiz center'))
            
            ws.write(i + 1, 0, _poisson.x)
            ws.write(i + 1, 1, _poisson.y)
                
            
            values.append(_poisson.json())
        
        if ws:
            wb.save('Inverse Poisson.xls')
        return values