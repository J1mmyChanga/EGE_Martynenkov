s = open('files/24_4627.txt').readline()
s = s.replace('NPO', '*').replace('PNO', '*')
for i in 'NPO':
    s = s.replace(i, ' ')
print(max(len(c) for c in s.split()))