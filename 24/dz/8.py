s = open('files/24_4602.txt').readline()
s = s.replace('A', 'O').replace('C', 'B').replace('D', 'B')
s = s.replace('BO', '*')
for i in 'BO':
    s = s.replace(i, ' ')
print(max(len(c) for c in s.split()))