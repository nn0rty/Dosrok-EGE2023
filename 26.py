f = open('26.txt')
n, m = map(int, f.readline().split())
a = []
for i in range(m):
    x, y = map(int, f.readline().split())
    a += [[x, y]]
a.sort()
d = [0]*n
res = 0
for i in range(len(a)):
    pr = False
    for j in range(len(d)):
        if pr == False:
            if a[i][0] > d[j]:
                d[j] = a[i][1]
                res += 1
                res2 = j + 1
                pr = True

print(res, res2)