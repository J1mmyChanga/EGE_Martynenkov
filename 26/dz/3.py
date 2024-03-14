f = open('../files/26_936.txt')
N, S = [int(x) for x in f.readline().split()]
a = sorted([int(x) for x in f], reverse=True)
sum = 0
count = 0
while len(a) > 0:
    while a and sum + a[-1] <= S:
        for i in range(len(a)):
            if sum + a[i] <= S:
                sum += a.pop(i)
                break
    if len(a) != 0:
        sum = 0
    count += 1
print(count, sum)