print(int('100', 2))
print(int('11101', 2))
def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    if c < e:
        return f(c+1, e) + f(c*2, e) + f(c*2 + 1, e)

print(f(4, 29))