def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(1204300, 1204381):
    d = [x for x in f(i) if x % 2 == 0]
    if len(d) > 0 and sum(d) % 10 == 0:
        print(i, sum(d))