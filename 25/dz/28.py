from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(0, 10**9, 3*7*8):
    # if fnmatch(str(i), '?6*6*?6'):
    #     print(i, sum(f(i)))
    if fnmatch(str(i), '?6*6*?6') and i % 7 == 0 and i % 6 == 0 and i % 8 == 0:
        print(i, sum(f(i)))