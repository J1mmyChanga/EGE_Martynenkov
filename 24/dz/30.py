s = open('files/24_314.txt').readline()
k = 0
for i in range(4, len(s)):
    if s[i-4]+s[i-3]+s[i-2]+s[i-1]+s[i] != 'STOCK' and s[i-2]+s[i-1]+s[i] == 'OCK':
        k += 1
print(k)