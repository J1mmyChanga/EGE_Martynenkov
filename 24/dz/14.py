s = open('files/24_2427.txt').readline().strip()
m = [1]*len(s)
start = 1
end = 1
for i in range(1, len(s)):
    if s[i] < s[i-1]:
        m[i] = m[i-1]+1
print(max(m))

for i in range(len(s)):
    if m[i] == 8:
        print(s[i-7 :i+1])