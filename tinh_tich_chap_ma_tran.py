for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    kn = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        kn[i] = list(map(int, input().split()))
    sum = 0
    for i in range(n-2):
        for j in range(m-2):
            for k in range(3):
                for l in range(3):
                    sum += a[i+k][j+l] * kn[k][l]
    print(sum)