a = [int(x) for x in open('files/17_2002.txt')]
ans = []
for i in range(len(a) - 3):
    if a[i] > a[i+1] > a[i+2] > a[i+3] and a[i] - a[i+3] > 1000:
        ans.append(a[i]+a[i+1]+a[i+2]+a[i+3])

print(len(ans), min(ans))