s = open('files/24_4546.txt').readline()
m = [0] * len(s)
print(s[:10])
for i in range(2, len(s)):
    if s[i] == s[i-2] == 'C' or s[i] == s[i-2] == 'A':
        m[i] = m[i-3] + 1
print(max(m))