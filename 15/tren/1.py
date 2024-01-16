def f(a, x):
    return (a % 9 == 0) and ((280 % x == 0) <= ( (a % x != 0) <= (730 % x != 0)))

# for a in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         if not f(a, x):
#             flag = False
#             break
#     if flag:
#         print(a)
#         break #90

# for a in range(1, 1000):
#     if all(f(a, x) for x in range(1, 10000)):
#         print(a)

for a in range(1, 1000):
    for x in range(1, 1000):
        if not f(a, x):
            break
    else:
        print(a)