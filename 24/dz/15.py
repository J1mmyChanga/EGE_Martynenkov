s = open('files/24_4113.txt').readline()
m = [0] * len(s)
for i in range(2, len(s)):
    if s[i-1] + s[i] in ['BB', 'DD']:
        m[i] = m[i-2] + 1
print(max(m))