s = open('files/24_11954.txt').readline()
m = 100000000
l = kx = 0
for r in range(len(s)):
    if s[r] == 'X': kx += 1
    if s[r] == 'Y':
        l = r + 1
        kx = 0
    while kx >= 500:
        m = min(m, r-l+1)
        if s[l] == 'X': kx -= 1
        l += 1
print(m)