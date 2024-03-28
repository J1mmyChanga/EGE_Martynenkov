f = open('files/27B_2733.txt')
n = int(f.readline())
k = [0]*80
k_5k = [0]*80
for i in range(n):
    x = int(f.readline())
    if x > 50000: k_5k[x%80] += 1
    else: k[x%80] += 1

count = k[0]*k_5k[0] + k_5k[0]*(k_5k[0]-1)//2 + k_5k[40]*(k_5k[40]-1)//2 + k[40]*k_5k[40]
for i in range(1, 80):
    if i != 40:
        count += k[i]*k_5k[80-i]

for i in range(1, 40):
    count += k_5k[i]*k_5k[80-i]
print(count)