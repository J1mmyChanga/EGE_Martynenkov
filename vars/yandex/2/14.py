m = -12
mx, my = 0, 0
d = {}
for x in '0123456789abcd':
    for y in '0123456789abcd':
        if (int(f'14{y}5{x}2', 14) + int(f'31{x}2{y}3', 14)) % 9 == 0 and int(x, 14) + int(y, 14) >= m:
            mx, my = x, y
            m = int(x, 14) + int(y, 14)
            d[m] = d.get(m, []) + [(int(x, 14), int(y, 14))]
print(mx, my)
print((int(f'14{my}5{mx}2', 14) + int(f'31{mx}2{my}3', 14)) // 9)