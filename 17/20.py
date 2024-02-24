a = [int(x) for x in open('files/17_2399.txt')]
ans = []
num = sum(int(i) for x in a for i in str(x) if x % 35 == 0)

def convert(x):
    res = ''
    st = '0123456789ABCDEF'
    while x != 0:
        res = st[x%16] + res
        x //= 16
    return res

def f(a, b):
    return a > num and convert(b).endswith('EF') and b < num

for i in range(len(a) - 1):
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        ans.append(a[i]+a[i+1])
print(len(ans), min(ans))