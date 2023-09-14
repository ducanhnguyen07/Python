for _ in range(int(input())):
    n = int(input())
    x, y, z = map(int, input().split())
    a = [0]*(n + 2)
    a[0] = 0
    a[1] = x
    for i in range(2, n+2):
        a[i] = a[i-1] + x
        if i % 2 == 0:
            a[i] = min(a[i//2] + z, a[i])
        a[i-1] = min(a[i] + y, a[i-1])
    print(a[n])