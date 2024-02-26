a = open('24-264.txt').readline()
for i in 'WERTYUIOPASDFGHJKLZXCVBNM':
    a = a.replace(i, 'Q')
for i in '023456789':
    a = a.replace(i, '1')
while 'QQ' in a:
    a = a.replace('QQ', 'Q Q')
while '11' in a:
    a = a.replace('11', '1 1')
print(max(len(c) for c in a.split()))