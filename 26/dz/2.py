f = open('../files/26_838.txt')
N = int(f.readline())
a = sorted([int(x) for x in f])
res = [0, 0]
first = 0
second = 0
while a:
    res[0] += a.pop(-1)
    first += 1
    while res[1] <= res[0]:
        res[1] += a.pop(0)
        second += 1
print(first, second)