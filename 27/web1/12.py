f = open('files/27B_2728.txt')
n = int(f.readline())
k0 = []
k1 = []
k23_0 = []
k23_1 = []
for i in range(n):
    x = int(f.readline())
    if x % 23 == 0 and x % 2 == 0: k23_0 += [x]
    elif x % 23 == 0 and x % 2 != 0: k23_1 += [x]
    elif x % 23 != 0 and x % 2 != 0: k1 += [x]
    elif x % 23 != 0 and x % 2 == 0: k0 += [x]
k0.sort()
k1.sort()
k23_0.sort()
k23_1.sort()
a = k0[-2:] + k1[-2:] + k23_0[-2:] + k23_1[-2:]
res = []
for i in range(8):
    for j in range(i+1, 8):
        if (a[i]+a[j])%2 == 0 and (a[i] % 23 == 0 or a[j] % 23 == 0):
            res.append(a[i]+a[j])
print(max(res))