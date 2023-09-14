import math

while True:
    a = [int(i) for i in input().split()]
    if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
        break
    cnt = 0
    while True:
        if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
            break
        x = a[0]
        for i in range(0, 4):
            if i == 3:
                a[i] = abs(a[i] - x)
            else:
                a[i] = abs(a[i] - a[i+1])
        cnt += 1
    print(cnt)