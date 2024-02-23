def f(c, e, k):
    if c > e:
        return 0
    if c == e:
        return k <= 3
    if c < e:
        return f(c+2, e, k) + f(c*3, e, k+1) + f(c*5, e, k+1)

print(f(2, 200, 0))