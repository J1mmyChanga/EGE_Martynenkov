a = [int(x) for x in open('files/17_2310.txt')]
ans = []
for i in a:
    if str(i)[-1] == '4':
        ans.append(i)
num = max(ans) + min(ans)
ans.clear()
for i in range(len(a) - 1):
    if a[i] + a[i+1] < num:
        ans.append(a[i]+a[i+1])
print(len(ans), max(ans))