from functools import *

@lru_cache()
def f(n):
    if n <= 1:
        return 1/2
    return (n + 1) * f(n - 1)

for i in range(200):
    f(i)


print(f(200)/f(198))
print(200*201)