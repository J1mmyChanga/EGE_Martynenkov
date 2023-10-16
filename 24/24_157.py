from string import ascii_uppercase
with open('24-157.txt') as f:
    data = f.read()
d = {}
for i in range(len(data) - 2):
    if data[i] == data[i + 1]:
        d[data[i + 2]] = d.get(data[i + 2], 0) + 1
print(sorted(d.items(), key=lambda x: x[1], reverse=True))