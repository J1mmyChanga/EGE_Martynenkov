f = open('files/27B_2726.txt')
n = int(f.readline())
k0 = []
k1 = []
for i in range(n):
    x = int(f.readline())
    if x % 2 == 0: k0.append(x)
    elif x % 2 != 0: k1.append(x)
k0.sort()
k1.sort()
print(k0[-1]+k1[-1])