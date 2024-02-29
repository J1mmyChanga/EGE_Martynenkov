s = open('files/24_2498.txt').readline()
while 'XIXIX' in s:
    s = s.replace('XIXIX', 'XIX XIX')
print(s.count('XIX'))