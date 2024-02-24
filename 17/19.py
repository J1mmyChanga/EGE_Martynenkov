a = [int(x) for x in open('files/17_2398.txt')]
ans = []

def f(a, b, c):
    return not(a > 0 and str(a)[-1] == '9') and (b > 0 and str(b)[-1] == '9') and not(c > 0 and str(c)[-1] == '9')

for i in range(len(a) - 2):
    if f(a[i], a[i+1], a[i+2]):
        ans.append(a[i]+a[i+1]+a[i+2])
print(len(ans), max(ans))