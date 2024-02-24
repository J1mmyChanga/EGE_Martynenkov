a = [int(x) for x in open('files/17_2239.txt')]
num = max(x for x in a if x % 19 == 0)
ans = []
for i in range(len(a) - 1):
    if a[i] > num or a[i+1] > num:
        ans.append(a[i] + a[i+1])
print(len(ans), min(ans))