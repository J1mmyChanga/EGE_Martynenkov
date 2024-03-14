f = open('../files/26-125.txt')
D, P = [int(x) for x in f.readline().split()]
a = []
for i in range(D):
    st, mana = [int(x) for x in f.readline().split()]
    if mana > 1:
        a.append([st, st+mana//2, mana//2])
a.sort()

cotl = [0]*P
cotl_c = [0]*P
gnom_max = 0
count = 0
for i in range(len(a)):
    st, end, zel = a[i]
    for j in range(P):
        if cotl[j] <= st:
            cotl_c[j] += 1
            if cotl_c[j] > 1:
                cotl[j] = 2 + end
            else:
                cotl[j] = end
            if cotl[j] > 1440:
                zel -= cotl[j] - 1440
            count += zel
            gnom_max = max(zel, gnom_max)
            break
print(count, gnom_max)