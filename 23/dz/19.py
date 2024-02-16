def f(c, n):
    if n == 15:
        return k.add(c)
    else:
        f(c*2,n+1)
        f(c*2 + 1, n+1)

k = set()
f(1,0)
print(len(k))