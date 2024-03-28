f = open('files/27B_2722.txt')
n = int(f.readline())
k0_5 = k1_5 = k0_0 = k1_0 = 0
for i in range(n):
    x = int(f.readline())
    if x % 5 == 0 and x % 2 == 0: k0_0 += 1
    elif x % 5 == 0 and x % 2 != 0: k1_0 += 1
    elif x % 5 != 0 and x % 2 == 0: k0_5 += 1
    elif x % 5 != 0 and x % 2 != 0: k1_5 += 1
print(k0_0*k1_5 + k1_0*k0_5 + k0_0*k1_0)