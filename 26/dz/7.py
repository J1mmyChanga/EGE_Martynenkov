f = open('../files/26_2480.txt')
N = int(f.readline())
a = sorted([[int(j) for j in i.split()] for i in f.readlines()])
res = [0]*2_000_000
for i in a:
    for x in range(i[0], i[-1]):
        res[x] = 1
res = ''.join([str(x) for x in res]).replace('0', ' ')
print(len(res.split()), res.count('1'))