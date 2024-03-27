f = open('files/27B_2720.txt')
n = int(f.readline())
k0 = k7 = 0
for i in range(n):
    x = int(f.readline())
    if x % 7 == 0: k7 += 1
    else: k0 += 1
print(k0*k7 + k7*(k7-1)//2)