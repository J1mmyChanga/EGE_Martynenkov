s = open('files/24_6734.txt').readline()
l = k = 0
m = 10000
for r in range(len(s)):
    if s[r] == '.': k += 1
    while k >= 7:
        m = min(m, r-l+1)
        if s[l] == '.': k -= 1
        l += 1
print(m)