alphx = '123456789abcdefghijklmnop'
alphy = '0123456789abcdefghijklmnop'
# def convert(n, k):
#     s = ''
#     while n != 0:
#         s += alph[n % k]
#         n //= k
#     return s[::-1]

for x in range(22):
    for y in range(13):
        n = int(f'{alphx[x]}23{alphx[x]}5', 22) - int(f'67{alphy[y]}9{alphy[y]}', 13)
        if n % 57 == 0:
            print(n / 57, x, y)