for n in range(4,100):
    a = '3' + '5'*n
    while '25' in a or '355' in a or '555' in a:
        if '25' in a:
            a = a.replace('25', '3', 1)
        if '355' in a:
            a = a.replace('355', '52', 1)
        if '555' in a:
            a = a.replace('555', '23', 1)
    if sum([int(k) for k in a]) == 27:
        print(n)
        break