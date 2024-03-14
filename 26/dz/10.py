f = open('../files/26_2653.txt')
N = int(f.readline())
a = sorted([int(x) for x in f])
weight = [0]*(sum(a)+1)
for x in a:
    weight2 = weight.copy()
    for i in range(sum(a)+1):
        if weight[i] == 1:
            weight2[i+x] = 1
    weight2[x] = 1
    weight = weight2.copy()

k, m = 0, 0
for i in range(1, sum(a)+1):
    if weight[i] == 0:
        k += 1
        m = i
print(k, m)