from fnmatch import *

for i in range(700_000, 1_000_000):
    if i % 13 == 0 and not fnmatch(str(i), '*0??3*') and not fnmatch(str(i), '*4??2') and not fnmatch(str(i), '*1*'):
        print(i, sum(int(j) for j in str(i)))