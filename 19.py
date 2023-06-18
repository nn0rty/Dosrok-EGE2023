def f(s, p, m):
    if s >= 78:
        return p%2 == m%2
    if p == m:
        return 0

    h = [f(s+1,p+1,m), f(s+4,p+1,m), f(s*4,p+1,m)]

    return any(h) if (p+1)%2 == m%2 else all(h)

for s in range(1,78):
    for m in range(1,5):
        if f(s, 0, m):
            if m == 2:
                print(s, m)