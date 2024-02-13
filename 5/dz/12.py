mas = []
def convert(n):
    res = ''
    while n != 0:
        res = str(n % 6) + res
        n //= 6
    return res

for n in range(1, 100):
    st = convert(n)
    if n % 3 == 0: st += st[:2]
    else: st += convert(n % 3 * 10)
    if int(st, 6) > 680:
        mas.append(int(st, 6))
print(min(mas))