f = open('../files/26_2650.txt')
L, M, N = [int(x) for x in f.readline().split()]
a = [[int(x) for x in i.split()] for i in f.readlines()]
res = [0]*10_000_000
for i in a:
    for j in range(i[0]+1, i[0]+i[1]):
        res[j] = 1
res = ''.join([str(x) for x in res[:L]]).replace('1', ' ')
res = [x for x in res.split() if len(x) >= M]
print(len(res), max(len(c) for c in res))