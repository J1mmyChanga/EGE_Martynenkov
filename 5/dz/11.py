mas = []
def convert(n):
    res = ''
    while n != 0:
        res = str(n % 3) + res
        n //= 3
    return res

for n in range(1, 100):
    st = convert(n)
    if n % 3 == 0: st = '1' + st + '02'
    else: st += convert(n % 3 * 4)
    if int(st, 3) < 199:
        mas.append(n)
print(max(mas))