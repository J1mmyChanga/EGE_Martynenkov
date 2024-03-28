f = open('files/27B_2727.txt')
n = int(f.readline())
k31 = []
k = []
for i in range(n):
    x = int(f.readline())
    if x % 31 == 0: k31.append(x)
    elif x % 31 != 0: k.append(x)
k31.sort()
k.sort()
print(min(k31[0]*k31[1], k31[0]*k[0]))