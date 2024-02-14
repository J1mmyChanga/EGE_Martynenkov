from functools import *

@lru_cache(None)
def f(n):
    if n > 100_000:
        return n
    if n <= 100_000:
        return f(n+1) + 5*n + 2

# print(f(3) - f(7))
print(17 + 22 + 27 + 32)