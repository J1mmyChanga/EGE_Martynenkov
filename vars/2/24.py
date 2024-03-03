s = open('24_1039.txt').readline()
m = [1] * len(s)
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        m[i] = m[i-1] + 1
print(max(m))