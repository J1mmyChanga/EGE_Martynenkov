f = open('../files/26_1257.txt')
N = int(f.readline())
a = sorted([int(x) for x in f])
b = set(a)
res = []
for i in range(N):
    for j in range(i+1, N):
        if (a[i] % 2) != (a[j] % 2) and (a[i]+a[j]) in b:
            res.append(a[i]+a[j])
print(len(res), max(res))