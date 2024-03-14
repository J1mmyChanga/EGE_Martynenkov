f = open('../files/26_813.txt')
S, N = [int(x) for x in f.readline().split()]
a = []
flag = True
for i in range(N):
    a.append(int(f.readline()))

sum = 0
count = 0
last = 0
while sum < S:
    a = sorted(a, reverse=flag)
    for i in range(len(a)):
        if sum + a[i] <= S and a[i]>0:
            sum += a[i]
            count += 1
            last = a[i]

            flag = not(flag)
            a[i] = -1
            break
    else:
        break

print(sum)
print(S)
print(count, last)