from functools import *

@lru_cache(None)
def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 3 == 0:
        return n + f(n/3)
    if n < 10000 and n % 3 != 0:
        return 2 * n + f(n+3)

# print(f(999) - f(46))
print(999+333+111+74+80+86)