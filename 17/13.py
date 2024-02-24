a = [int(x) for x in open('files/17_2401.txt')]
ans = []
for i in range(len(a) - 1):
    if 50 <= abs(a[i]) + abs(a[i+1]) <= 200:
        ans.append(min(a[i], a[i+1]))
print(len(ans), min(ans))