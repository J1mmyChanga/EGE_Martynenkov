from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(0, 10**7, 217):
    d = [x for x in f(i) if x % 2 != 0]
    if fnmatch(str(i), '14?4*'):
        print(i, sum(d))