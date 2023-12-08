def f(w, x, y, z):
    return (x or not(y)) and not(y == z) and not(w)


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(w, x, y, z):
                    print(x, y, z, w) # x z y w