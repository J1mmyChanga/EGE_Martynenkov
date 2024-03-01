def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

def p(x):
    return x > 1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))


for i in range(499_999, 490_000, -1):
    d = [x for x in f(i) if p(x)]
    if len(d) > 0:
        if sum(d) % 10 == 0:
            print(i, sum(d))
