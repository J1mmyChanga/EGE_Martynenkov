f = open('../files/26-111.txt')
K = int(f.readline())
N = int(f.readline())
a = []

for i in range(N):
    st, end = [int(x) for x in f.readline().split()]
    a.append([st, end])
a.sort()

c = 0
cur = 0
slots = [0]*K
for i in range(N):
    st, end = a[i]
    for j in range(K):
        if st > slots[j]:
            slots[j] = end
            c += 1
            cur = j+1
            break
print(c, cur)