f = open('../files/26-122.txt')
K, N = [int(x) for x in f.readline().split()]
a = []
for i in range(N):
    st, end = [int(x) for x in f.readline().split()]
    a.append([st, end])
a.sort()

domiki = [0]*K*N
domiki_c = [0]*K*N
chas = 0
count = 0
for i in range(N):
    st, end = a[i]
    for j in range(len(domiki)):
        if domiki[j] < st:
            chas = st + 1
            domiki[j] = end
            domiki_c[j] = 1
            break
print(domiki, chas)
for i in domiki[:140]:
    if i >= chas:
        count += 1
print(14, count)