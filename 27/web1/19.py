f = open('files/27B_2731.txt')
n = int(f.readline())
x1 = []
ym = 0

for i in range(n):
    x, y = map(int, f.readline().split())
    if y == 0: x1.append(x)
    else: ym = max(ym, abs(y))

print((max(x1)-min(x1))*ym/2)