# 1 000 000 00
#   12? ?36 *1
for x in range(10):
    for y in range(10):
        a = '12' + str(x) + str(y) + '361'
        if int(a) % 273 == 0:
            print(int(a), int(a) // 273)

for x in range(10):
    for y in range(10):
        for z in range(10):
            a = '12' + str(x) + str(y) + '36' + str(z) + '1'
            if int(a) % 273 == 0:
                print(int(a), int(a) // 273)