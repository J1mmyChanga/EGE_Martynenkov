s = open('files/24_1428.txt').readline()
s = s.replace('XZ', 'X Z').replace('XY', 'X Y')
print(max(len(c) for c in s.split()))