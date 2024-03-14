f = open('../files/26-112.txt')
N, M = [int(x) for x in f.readline().split()]
a = []
for i in range(M):
    st, r = [int(x) for x in f.readline().split()]
    a.append([st, st+r, r])
a.sort(key=lambda x: x[0])

banks = [0]*N
banks_c = [0]*N
last = 0
for i in range(M):
    st, end, r = a[i]
    for j in range(N):
        if banks[j] <= st:
            banks[j] = end
            if st <= 60 * 24:
                banks_c[j] += 1
                last = st
            break
    else:
        #клиент ждет освобождения банкомата
        m = min(banks)
        for j in range(N):
            if banks[j]==m:
                if banks[j] <= 60 * 24:
                    banks_c[j] += 1
                    last = banks[j]
                banks[j] += r
                break

print(max(banks_c), last)