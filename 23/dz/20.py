d = set()

def f(c, n):
    if n == 8:
        if 1000 <= c <= 1024:
            d.add(c)
    else:
        f(c+1, n+1)
        f(c+5, n+1)
        f(c*3, n+1)

f(1,0)
print(len(d))