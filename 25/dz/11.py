def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(300_001, 301_000):
    d = [x for x in f(i) if x % 3 == 0]
    if len(d) == 5:
        print(i, d[-1])