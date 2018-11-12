import random
from scipy.stats import poisson
from math import e, log
mu = 5
# r = poisson.rvs(mu, size=12)
print(poisson.isf(random.random(), mu, loc=0))