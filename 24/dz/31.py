s = open('files/24_279.txt').readline()
k = 0
for i in range(4, len(s)-1):
    if s[i-3]+s[i-2]+s[i-1]+s[i] == 'BOSS' and s[i-4] != 'J' and s[i+1] != 'J':
        k += 1
print(k)

s = s.replace('BOSS', '1').replace('1J1', ' ').replace('J1', ' ').replace('1J', ' ')
print(s.count('1'))