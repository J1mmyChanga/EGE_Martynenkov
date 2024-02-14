from functools import *
from math import *

@lru_cache(None)
def f(n):
    if n >= 5000:
        return factorial(n)
    if 1<=n<5000:
        return 2*f(n+1)/(n+1)

print(1/(0.4 * 1/3 * 2/7) * 1000)