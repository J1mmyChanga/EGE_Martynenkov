def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

def p(x):
    return x > 1 and all(x%i != 0 for i in range(2, int(x**0.5)+1))

for i in range(25317, 51238):
    d = [x for x in f(i) if p(x)]
    if len(d) >= 6:
        print(i, d[-1])