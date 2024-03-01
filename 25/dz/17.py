def p(x):
    return x > 1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))

for i in range(int(106732567**0.25)+1, int(152673837**0.25)):
    if p(i):
        print(i**4, i**3)