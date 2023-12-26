from itertools import permutations, product

a = []
for i in product('01234567', repeat=4):
    s = ''.join(i)
    if s[0] in '246':
        pred = 11111110
        flag = True
        for i in s:
            if int(i) <= pred:
                pred = int(i)
                continue
            else:
                flag = False
                break
        if flag:
            print(s)
            a.append(s)
print(len(a))