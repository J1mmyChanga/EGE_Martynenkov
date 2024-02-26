from itertools import *

for k, i in enumerate(sorted(product('МАРИЯ', repeat=4)), 1):
    if k == 211:
        print(k, i)