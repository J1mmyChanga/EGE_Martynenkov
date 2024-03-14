f = open('../files/26-119.txt')
N, L, M = [int(x) for x in f.readline().split()]
a = []
for i in range(N):
    st, r, t = f.readline().split()
    a.append([int(st), int(st)+int(r), t])
a.sort()

#первые - L
#потом - M
park = [0]*(L+M)
mvs = 0
counter = 0
for i in range(N):
    st, end, t = a[i]
    if t == 'A':
        for j in range(L+M):
            if park[j] <= st:
                park[j] = end
                counter += 1
                break
    elif t == 'B':
        for j in range(L, L+M):
            if park[j] <= st:
                park[j] = end
                mvs += 1
                counter += 1
                break
print(mvs, N-counter)