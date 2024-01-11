a = []
res = {}
for x in range(10):
    a.append(f'0{x}3')
    a.append(f'4{x}2')

for n in range(700_011, 1000000000, 13):
    for item in a:
        if item in str(n) or '1' in str(n):
            break
    else:
        res[str(n)] = sum(int(i) for i in list(str(n)))
    if len(res) == 5:
        print(*res.items(), sep='\n')
        break