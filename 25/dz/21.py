from fnmatch import *

# for i in '0123456789':
#     for j in '0123456789':
#         if int(f'12345{i}6{j}8') % 17 == 0:
#             print(f'12345{i}6{j}8', int(f'12345{i}6{j}8')//17)

for i in range(0, 10**9, 17):
    if fnmatch(str(i), f'12345?6?8'):
        print(i, i//17)