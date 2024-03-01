def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(500_001, 510_000):
    d = [x for x in f(i) if x%10 == 8 and x != 8]
    if len(d) > 0:
        print(i, d[0])