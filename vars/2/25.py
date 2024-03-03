for N in range(200_000_000, 400_000_001):
    for m in range(0, 1000, 2):
        for n in range(1, 1000, 2):
            if 2**m*3**n > N:
                break
            if 2**m*3**n == N:
                print(N)