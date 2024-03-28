f = open('files/27B_2719.txt')
n = int(f.readline())
k = [[] for i in range(11)]

for i in range(n):
    x = int(f.readline())
    k[x%11] += [x]

a = []
for i in range(11):
    k[i].sort()
    a += k[i][:3]

res = []
for i in range(33):
    for j in range(i+1, 33):
        for h in range(j+1, 33):
            if (a[i]+a[j]+a[h]) % 11 == 0:
                res.append((a[i]+a[j]+a[h]))
print(min(res))