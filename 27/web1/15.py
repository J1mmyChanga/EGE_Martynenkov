f = open('files/27B_2732.txt')
n = int(f.readline())
k = [[] for i in range(80)]
for i in range(n):
    x = int(f.readline())
    k[x%80] += [x]

a = []
for i in range(80):
    k[i].sort()
    try:
        a.append((k[i][-1] - k[i][0]))
    except Exception:
        pass
print(max(a))