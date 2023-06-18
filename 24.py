f = open('24.txt')
a = f.readline()
a = a.replace('Q', '*')
a = a.replace('R', '*')
a = a.replace('S', '*')
a = a.split('**')
bb = 'QWERTYUIOPASDFGHJKLZXCVBNM'
b = sorted(bb)
cc = 0
maxx = 0
for i in range(len(a)):
    maxx = max(maxx, len(a[i]))
print(maxx + 2)

