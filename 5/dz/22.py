for n in range(1, 300):
    for m in range(1, 300):
        nums_p1 = 1
        for i in str(n):
            if int(i) % 2 == 0 and int(i) != 0:
                nums_p1 *= int(i)
        for i in str(m):
            if int(i) % 2 == 0 and int(i) != 0:
                nums_p1 *= int(i)

        nums_p2 = 1
        for i in str(n):
            if int(i) % 2 != 0:
                nums_p2 *= int(i)
        for i in str(m):
            if int(i) % 2 != 0:
                nums_p2 *= int(i)
        if n == 120 and abs(nums_p1 - nums_p2) == 29:
            print(m)