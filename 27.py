# f = open('27A.txt')
f = open('27B.txt')
n = f.readline()
k = f.readline()
a = []
for i in range(int(n)):
    x = f.readline().split()
    a.append([int(x[0]), i+1])
a = sorted(a)[::-1]
for i in range(len(a)):
    if i + 1 == len(a):
        break
    if abs(a[i][1]-a[i+1][1]) >= int(k):
        print(a[i][0]+a[i+1][0])
        break


