from fnmatch import *

for i in range(0, 10**8, 141):
    if fnmatch(str(i), '1234*7'):
        print(i, i//141)