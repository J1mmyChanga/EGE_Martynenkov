f = open('files/27A_2734.txt')
n = int(f.readline())
k = [0]*100000
for i in range(n):
    x = int(f.readline())
    k[sum(int(i) for i in str(x))] += 1
print(max(k))