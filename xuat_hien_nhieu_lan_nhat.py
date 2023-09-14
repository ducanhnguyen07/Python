for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    b = {}
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    fl = True
    s = set(a)
    for i in s:
        if b[i] > n//2:
            print(i)
            fl = False
    if fl:
        print("NO")

        
