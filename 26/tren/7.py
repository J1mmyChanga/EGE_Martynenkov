f = open('../files/26-75.txt')
N = int(f.readline())
a = [0] * 1000000
for i in range(N):
    st, end = [int(x) for x in f.readline().split()]
    a[st] += 1
    a[end] -= 1

k = 0
m_k = 0
count = 0
for i in range(1_000_000):
    k += a[i]
    m_k = max(k, m_k)
    if k > 0:
        count += 1
print(m_k, count)