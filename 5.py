for i in range(1,1500):
    N = bin(i)[2:]
    if i % 3 == 0:
        N = N + N[-3:]
    else:
        N = N + bin((i%3)*3)[2:]
    if int(N, 2) < 100:
        print(i)