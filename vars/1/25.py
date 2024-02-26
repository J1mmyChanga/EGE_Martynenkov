from fnmatch import fnmatch
from itertools import *

d = {}
num1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num2 = num1 + list(''.join(i) for i in product('0123456789', repeat=2))
print(num2)
for i in num1:
    for j in num2:
        if int(f'12{j}34{i}5') % 2025 == 0:
            d[f'12{j}34{i}5'] = str(int(f'12{j}34{i}5') // 2025)
for i in sorted(d, key=lambda x:int(x)):
    print(i, d[i])