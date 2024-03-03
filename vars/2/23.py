d = {str(x):0 for x in range(40, 50)}
def f(c, e, nach):
    if c == e and not nach:
        return 1
    if c < 40 or c > 49:
        return 0
    d[str(c)] += 1
    if d[str(c)] >= 2:
        return 0
    return f(c+1, e, False) + f(c+3, e, False) + f(c-1, e, False) + f(c-3, e, False)
print(f(42, 42, True))