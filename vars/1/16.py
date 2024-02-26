from functools import *

c = 0
@lru_cache(None)
def f(n):
    if n == 1: return 1
    return n + f(n-1)

for n in range(1, 2023):
    f(n)

for n in range(1, 101):
    if f(2023) // f(n) % 2 == 0:
        c += 1
print(c)