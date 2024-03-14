f = open('../files/26_2652.txt')
N = int(f.readline())
a = sorted([int(x) for x in f])
d = {}
for i in a:
    d[str(i)] = d.get(str(i), 0) + 1
print(sorted(d.items(), key=lambda x:x[1], reverse=True))
print(len(set(a)))