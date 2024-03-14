a = [int(x) for x in open('17.txt')]
num = sorted([x for x in a if len(str(x)) == 3])[1]
res = []
for i in range(len(a)-1):
    if a[i] + a[i+1] < num**2:
        res.append(a[i] + a[i+1])
print(len(res), max(res))