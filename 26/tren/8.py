f = open('../files/26-76.txt')
L, N = [int(x) for x in f.readline().split()]
a = [0] * L
for i in range(N):
    st, end = [int(x) for x in f.readline().split()]
    for j in range(st, end):
        a[j] = 1
m = 1
k = 1
for i in range(2, len(a)):
    if a[i] == a[i-1] == 0:
        k += 1
        m = max(k, m)
    else:
        k = 1
print(a.count(0), m)

a = ''.join([str(x) for x in a]).replace('1', ' ')
print(a.count('0'), max(len(c) for c in a.split()))