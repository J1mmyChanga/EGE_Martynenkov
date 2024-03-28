f = open('files/27A_2737.txt')
n = int(f.readline())
k = [0]*2000

for i in range(n):
    x = int(f.readline())
    if x < 2000:
        k[x] +=1

count = k[1000]*(k[1000]-1)//2
for i in range(1, 1000):
    count += k[i]*k[2000-i]
print(count)