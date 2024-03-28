f = open('files/27B_2724.txt')
n = int(f.readline())
k = [0]*131
for i in range(n):
    x = int(f.readline())
    k[int(x%131)] += 1

count = k[0]*(k[0]-1)//2
for i in range(1, 66):
    count += k[i]*k[131-i]
print(count)