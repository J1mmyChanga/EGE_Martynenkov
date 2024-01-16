a = set()
b = {2, 4, 6, 8, 10, 12}
c = {3, 6, 9, 12, 15}

def f(x):
    A = x in a
    B = x in b
    C = x in c
    return B <= ((C and (not A)) <= (not B))
    

for x in range(1, 1000):
    if not f(x):
        print(x)