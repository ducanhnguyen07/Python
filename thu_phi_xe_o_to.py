res = {}

for _ in range(int(input())):
    a = []
    a = input().split()
    typeCar = a[1]
    numChair = int(a[2])
    direct = a[3]
    time = a[4]
    fee = 0
    if direct == "IN":
        if typeCar == "Xe_con":
            if numChair == 5:
                fee += 10000
            else:
                fee += 15000
        elif typeCar == "Xe_tai":
            fee += 20000
        else:
            if numChair == 29:
                fee += 50000
            else:
                fee += 70000
    if a[4] in res:
        res[a[4]] += fee
    else:
        res[a[4]] = fee
for i, j in res.items():
    print(i, j, sep = ": ")
