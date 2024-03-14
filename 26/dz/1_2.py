f = open('../files/26_813.txt')
S, N = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort()

res = []
while sum(res) + a[0] < S:
    for i in range(len(a)-1, 0, -1):
        if sum(res) + a[i] <= S:
            res += [a.pop(i)]
            break
    if sum(res) + a[0] <= S:
        res += [a.pop(0)]
print(sum(res))
print(len(res), res[-1])