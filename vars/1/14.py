def convert(x):
    res = ''
    while x > 0:
        res = str(x%5) + res
        x //= 5
    return res

print(convert(7*5**123 + 6*5**111 - 5*25**50 + 4*125**30 - 3*5**10).count('4'))