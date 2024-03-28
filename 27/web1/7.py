f = open('files/27B_2725.txt')
n = int(f.readline())
k = [0]*69
for i in range(n):
    x = int(f.readline())
    k[int(x%69)] += 1

count = 0
for i in range(69):
    count += k[i]*(k[i]-1)//2
print(count)