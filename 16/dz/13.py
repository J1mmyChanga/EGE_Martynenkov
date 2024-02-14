c = 0
def f(n):
    if n <= 18:
        return n + 3
    if n > 18 and n % 3 == 0:
        return (n//3) * f(n//3) + n - 12
    if n > 18 and n % 3 != 0:
        return f(n-1) + n**2 + 5

for n in range(1, 1001):
    if all(int(i) % 2 == 0 for i in str(f(n))):
        c += 1
print(c)