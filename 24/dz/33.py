s = open('files/24_2499.txt').readline()
while 'XXXXX' in s:
    s = s.replace('XXXXX', 'XXXX XXXX')
print(s.count('XXXX'))