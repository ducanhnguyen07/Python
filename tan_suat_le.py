for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = {}
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    for i in a:
        if b[i] % 2 != 0:
            print(i)
            break