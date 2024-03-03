def convert(x):
    res = ''
    while x > 0:
        res = str(x%7) + res
        x //= 7
    return res

mas = []
for x in '0123456789abcdefghij':
    for y in '01234':
        d = int(f'{x}1{x}2{x}3{x}4', 20) - int(f'1{y}2{y}3{y}4{y}', 5)
        mas.append(sum(int(i) for i in convert(d)))
print(max(mas))