from itertools import  *

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (not A) <= (P or (not Q))

a = []
p = list(i for i in product('01', repeat=8) if i[0] == '1' and i[1] == '1')
q = list(i for i in product('01', repeat=8) if i[-1] == '0')
for x in product('01', repeat=8):
    if not f(x):
        a.append(x)
print(len(a)) #96