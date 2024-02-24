a = [int(x) for x in open('files/17_2238.txt')]
ans = []
avg = sum(a)/len(a)
for i in range(len(a) - 2):
    if (a[i] > avg) + (a[i+1] > avg) + (a[i+2] > avg) >= 2:
        ans.append(a[i] + a[i+1] + a[i+2])
print(len(ans), max(ans))