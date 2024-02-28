s = open('files/24_9169.txt').readline()
m = 1000000
l = k = 0
for r in range(2, len(s)):
    if s[r-2]+s[r-1]+s[r] in ['BAD', 'FAT']:
        k += 1
    while k >= 3:
        m = min(m, r-l+1)
        if s[l]+s[l+1]+s[l+2] in ['BAD', 'FAT']:
            k -= 1
        l += 1
print(m)