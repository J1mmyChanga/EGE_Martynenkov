def f(c, e, chet):
    if c > e:
        return 0
    if c == e:
        return chet == 6
    if c % 2 == 0:
        chet += 1
    if c < e:
        return f(c+1, e, chet) + f(c+3, e, chet) + f(c+5, e, chet)

print(f(3, 25, 0))