c = 0
def f(n):
    if n < 3:
        return n + 1
    if n >= 3 and n % 2 == 0:
        return f(n-2) + n - 2
    if n >= 3 and n % 2 != 0:
        return f(n+2) + n + 2

for n in range(1, 10000):
    try:
        if len(str(f(n))) == 5:
            c += 1
    except:
        pass
print(c)