f = open('files/27B_2730.txt')
n = int(f.readline())
k = [[] for i in range(12)]
for i in range(n):
    x = int(f.readline())
    k[x%12] += [x]

a = []
for i in range(12):
    k[i].sort()
    a += k[i][-4:]

res = []

for i in range(48):
    for j in range(i+1, 48):
        for h in range(j+1, 48):
            for d in range(h+1, 48):
                try:
                    if (a[i]*a[j]*a[h]*a[d]) % 12 == 0:
                        res.append((a[i]+a[j]+a[h]+a[d]))
                except Exception:
                    pass
print(max(res))