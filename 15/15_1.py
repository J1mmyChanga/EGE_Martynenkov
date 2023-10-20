def d(a, b):
    return a % b == 0

def f(a, x):
    return d(a, 35) and (d(730, x) <= ((not d(a, x)) <= (not d(110, x))))


for a in range(1, 2000):
    flag = True
    for x in range(1, 2000):
        if not f(a, x):
            flag = False
            break
    if flag:
        print(a)
        break