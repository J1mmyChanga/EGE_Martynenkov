def inc11(n):
    if str(n)[0] == '9' and str(n)[1] == '9':
        pass
    elif str(n)[0] == '9' and str(n)[1] != '9':
        n += 1
    elif str(n)[0] != '9' and str(n)[1] == '9':
        n += 10
    else:
        n += 11
    return n

def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    if c < e:
        return f(c+1, e) + f(inc11(c), e)

print(f(25, 51))