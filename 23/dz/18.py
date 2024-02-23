def f(c, e, n):
    if c > e:
        return 0
    if c == e and n == 7:
        return 1
    if c == e and n != 7:
        return 0
    if c < e:
        return f(c+1, e, n+1) + f(c + 4, e, n+1) + f(c*2, e, n+1)

print(f(3,27, 0))