def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(650_000, 700_000):
    d = f(x)
    if len(d) != 6:
        continue
    k = d[0] + d[-1]
    if len(str(k)) == 4:
        print(x, k)