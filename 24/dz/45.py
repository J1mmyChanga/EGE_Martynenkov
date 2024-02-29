from string import ascii_uppercase

s = open('files/24_2504.txt').readline()
d = {x:0 for x in ascii_uppercase}
for i in range(2, len(s)-2):
    if s[i-2]+s[i-1] == s[i+2]+s[i+1] == 'CB':
        d[s[i]] += 1
for i in d:
    if d[i] == max(d.values()):
        print(i+str(d[i]))