f = open('files/27B_2735.txt')
n = int(f.readline())
ky = kx = k = 0
for i in range(n):
    x, y = [int(j) for j in f.readline().split()]
    if y == 0: ky += 1
    elif x == 0: kx += 1
    else: k += 1
print(ky*kx*k)