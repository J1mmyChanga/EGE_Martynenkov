s = open('files/24_12476.txt').readline()
l = m = k_ro = k_oro = k_ror = 0
for r in range(2, len(s)):
    if s[r-2]+s[r-1]+s[r] == 'ORO': k_oro += 1
    if s[r-2]+s[r-1]+s[r] == 'ROR': k_ror += 1
    if s[r-1]+s[r] == 'RO': k_ro += 1
    while k_ro > 22 or k_oro > 0 or k_ror > 0:
        if s[l] + s[l+1] + s[l+2] == 'ORO': k_oro -= 1
        if s[l] + s[l+1] + s[l+2] == 'ROR': k_ror -= 1
        if s[l] + s[l+1] == 'RO': k_ro -= 1
        l += 1
    if k_ro == 21 and k_ror == 0 and k_oro == 0:
        m = max(m, r-l+1)
print(m)