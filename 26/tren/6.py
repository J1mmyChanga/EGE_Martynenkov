f = open('../files/26-124.txt')
K, M, N = [int(x) for x in f.readline().split()]
a = []
for i in range(N):
    t = [int(x) for x in f.readline().split()][0]
    a.append(t)
a.sort(reverse=True)

rows = [0]*K
count = 0
for i in range(N):
    t = a[i]
    for j in range(K):
        if t + rows[j] <= M:
            rows[j] += t
            count += 1
            break
print(count, K*M-sum(rows))