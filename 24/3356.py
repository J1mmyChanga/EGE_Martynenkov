with open('24-3356.txt') as f:
    data = f.read()
a = []
res = []
pred = chr(100000)
for i in data:
    if i < pred:
        res.append(i)
    else:
        if len(res) > 1:
            a.append(tuple(res))
            res = [i]
    pred = i
a = sorted(a, key=len)
for i in a:
    if len(i) == len(a[-1]):
        print(i)
        break