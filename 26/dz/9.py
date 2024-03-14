f = open('../files/26_2651.txt')
N = int(f.readline())
a = sorted([[int(j) for j in i.split()] for i in f.readlines()])
d = {}
for i in a:
    if i[0] not in d:
        d[i[0]] = [i[1]]
    elif i[1] not in d[i[0]]:
        d[i[0]] = d.get(i[0], []) + [i[1]]
print(len(d)*8 - sum(len(d[i]) for i in d), 1985)