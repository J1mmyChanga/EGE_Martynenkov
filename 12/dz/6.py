s = '>' + 11 * '1' + 12 * '2' + 30 * '3'
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s: s = s.replace('>1', '22>')
    if '>2' in s: s = s.replace('>2', '2>')
    if '>3' in s: s = s.replace('>3', '1>')
    print(s)
print(sum(int(i) for i in s if i != '>'))
print(11 * 4 + 12 * 2 + 30)