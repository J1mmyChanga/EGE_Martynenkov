s = open('files/24_4643.txt').readline()
s = s.replace('A', 'B').replace('2', '1')
s = s.replace('11B', '*')
for i in '1B':
    s = s.replace(i, ' ')
print(max(len(c) for c in s.split()))