def f(w, x, y, z):
    return (x and not(y)) or (y == z) or not(w)


print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not f(w, x, y, z):
                    print(w, x, y, z) # w z y x