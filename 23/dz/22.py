def f(c, e, count):
    if c > e:
        return 0
    if c == e and count == 1:
        return count == 1
    if c == e and count != 1:
        return 0
    if c < e:
        return f(c+1, e, count) + f(c+2, e, count) + f(c*2, e, count+1)


print(f(2, 12, 0))