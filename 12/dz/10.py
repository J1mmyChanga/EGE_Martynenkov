d = set()
for n in range(1, 40):
    s = n * '5'
    while '555' in s or '888' in s:
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    print(s)
    d.add(s)
print(len(d))