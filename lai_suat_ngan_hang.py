t = int(input())

for i in range(t):
    n, x, m = map(float, input().split())

    cnt = 0
    x = x/100
    while(1):
        if n >= m:
            break
        n = n + n * x
        cnt = cnt + 1
    print(cnt)