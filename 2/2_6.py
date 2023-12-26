def f1(w, x, y, z):
    return (w or not(y)) <= (x == z)


def f2(w, x, y, z):
    return (w or not(y)) == (x <= z)


print('w x y z f1 f2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f1(w, x, y, z) or not f2(w, x, y, z):
                    print(w, x, y, z, f1(w, x, y, z), f2(w, x, y, z)) # y w z x