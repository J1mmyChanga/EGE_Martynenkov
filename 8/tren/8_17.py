from itertools import permutations

a = []
for i in permutations('01234567', 6):
    s = ''.join(i)
    if s[0] != '0':
        s = s.replace('2', '0').replace('4', '0').replace('6', '0')\
             .replace('3', '1').replace('5', '1').replace('7', '1')
        if '00' not in s and '11' not in s:
            a.append(s)
print(len(a))