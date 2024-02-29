s = open('files/24_1143.txt').readline()
k = 0
for i in range(len(s) - 6):
    if s[i] == 'A' and s[i + 6] == 'F':
        k += 1
for i in range(len(s) - 7):
    if s[i] == 'A' and s[i + 7] == 'F':
        k += 1
for i in range(len(s) - 8):
    if s[i] == 'A' and s[i + 8] == 'F':
        k += 1
for i in range(len(s) - 9):
    if s[i] == 'A' and s[i + 9] == 'F':
        k += 1
print(k)