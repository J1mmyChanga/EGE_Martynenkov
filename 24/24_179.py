with open('24-179.txt') as f:
    data = f.read()
k = 0
d = {}
alph = 'CDE'
sp = [f'CB{i}BC' for i in alph]
for i in range(len(data) - 5):
    x = data[i:i + 5]
    if data[i:i + 5] in sp:
        k += 1
        d[x] = d.get(x, 0) + 1
print(k)
print(sorted(d.items(), key=lambda x: x[1], reverse=True))
