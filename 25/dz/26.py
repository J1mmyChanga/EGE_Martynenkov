from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(65001, 1_000_000):
    d = [x for x in f(i) if x % 2 == 0]
    if len(d) >= 4 and fnmatch(str(i), '6*97*5?'):
        print(i, sum(d))