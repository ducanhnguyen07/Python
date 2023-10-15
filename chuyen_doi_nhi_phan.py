a = []
f = open("DATA.in", "r")
for i in f:
    a.append(i)
for i in range(1, len(a), 2):
    base = int(a[i])
    num = int(a[i+1], 2)
    if base == 2:
        print(bin(num)[2:])
    elif base == 8:
        print(oct(num)[2:])
    elif base == 16:
        h = format(num, 'X')
        print(h)
    else:
        res = []
        while num > 0:
            res.append(num % base)
            num //= base
        print(res.reverse())
