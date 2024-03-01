def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(400_000_001, 400_100_000):
    d = f(i)
    if len(d) >= 5:
        p = d[0]*d[1]*d[2]*d[3]*d[4]
        if p%100 == 17 and p <= i:
            print(p, d[4])