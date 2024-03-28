f = open('files/27B_2736.txt')
n = int(f.readline())
k = [0]*10
for i in range(n):
    x = int(f.readline())
    k[int(str(x)[0])] += 1
print(k)