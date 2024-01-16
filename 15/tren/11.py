def f(x, y):
    return not (((x > 6) and ((x + y) > 5)) or (y >= 5))

c = 0
for x in range(1000):
    for y in range(1000):
        if f(x, y):
            c += 1
print(c) #35