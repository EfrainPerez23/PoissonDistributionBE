import random
from scipy.stats import poisson
from math import e
mu = 5
r = poisson.rvs(mu, size=12)
print(r)