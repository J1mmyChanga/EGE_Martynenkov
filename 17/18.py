a = [int(x) for x in open('files/17_2403.txt')]
ans = []

def f(a, b):
    if a % 9 == 0 and b % 9 != 0 and abs(b) % 8 == 3:
        return True
    return False

for i in range(len(a) - 1):
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        ans.append(max(a[i], a[i+1]))
print(len(ans), max((ans)))