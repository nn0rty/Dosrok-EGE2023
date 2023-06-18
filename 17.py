with open('17.txt') as f:
    a = [int(x) for x in f]

count = 0
maxx = 1000000000000
b = []
for i in range(len(a)):
    if len(str(a[i])) == 3 and a[i] % 10 == 5:
        b.append(a[i])
for i in range(len(a)):
    if i + 1 == len(a):
        break
    if ((len(str(a[i])) == 3 and len(str(a[i+1])) != 3) or (len(str(a[i])) != 3 and len(str(a[i+1])) == 3)) and ((a[i] + a[i+1]) % min(b) == 0):
        count += 1
        maxx = min(maxx, a[i] + a[i+1])
print(count, maxx)