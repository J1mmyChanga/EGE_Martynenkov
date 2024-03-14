f = open('../files/26_1079.txt')
N = int(f.readline())
a = [int(x) for x in f]
a.sort()
res = []
for i in range(N):
    for j in range(i+1, N):
        if (a[i]+a[j]) % 2 == 0:
            sr = (a[i]+a[j])//2
            if sr > a[2499] and sr < a[3750]:
                res.append(sr)
print(len(res), min(res))