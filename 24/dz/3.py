s = open('files/24_1040.txt').readline()
for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'.lower():
    s = s.replace(i, ' ')
for i in '123456789':
    s = s.replace(i, '0')
print(max(len(c) for c in s.split()))