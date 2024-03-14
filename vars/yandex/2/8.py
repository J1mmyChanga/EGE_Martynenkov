from itertools import *

k = 0
for i in product('ГИПЕРБОЛА', repeat=6):
    i = ''.join(i).replace('Е', 'И').replace('О', 'И').replace('А', 'И').replace('П', 'Г').replace('Р', 'Г').replace('Б', 'Г').replace('Л', 'Г')
    if i[0] != 'И' and i[-1] != 'И' and 'ГИГ' not in i:
        k += 1
print(k)