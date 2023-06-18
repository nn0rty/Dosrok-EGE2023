'''
def f(x, y):
    N = bin(x)[2:]
    R = bin(y)[2:]
    f = abs(len(N) - len(R))
    if f != 0:
        if len(N) < len(R):
            N = '0'*f + N
        else:
            R = '0'*f + R
    c = ''
    for k in range(len(N)):
        if N[k] == R[k]:
            c = c + '1'
        else:
            c = c + '0'
    return int(c, 2)
'''
def g(x, A):
    #return (bool(f(x, 39) == 0)) or (not(bool(f(x, 11) == 0)) or not(bool(f(x, A) == 0)))
    return (x&39 == 0) or (not(x&11 == 0) or not(x&A == 0))

for A in range(1, 100):
    pr = True
    for x in range(1, 100):
        if g(x, A) == False:
            pr = False
    if pr == True:
        print(A)
        # +
        break
