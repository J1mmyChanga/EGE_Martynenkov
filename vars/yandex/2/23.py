def f(c, e):
    if c > 115:
        return 0
    if c == 25:
        return 0
    if c == e:
        return 1
    return f(c+3, e) + f(c*2, e) + f(c*5, e)
print(f(5, 115))