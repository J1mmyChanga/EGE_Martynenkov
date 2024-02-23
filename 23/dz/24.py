from functools import *

@lru_cache(None)
def f(c, e, nechet):
    if c > e:
        return 0
    if c == e:
        return nechet + c % 2 == 1
    if c < e:
        return f(c+1, e, nechet+(c+1)%2) + f(c+2, e, nechet+(c+2)%2) + f(c*2, e, nechet+(c*2)%2)

print(f(2, 40, 0))