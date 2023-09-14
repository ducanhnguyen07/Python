for _ in range(int(input())):
    n, p = map(int, input().split())
    cnt = 0
    if n > p:
        i = p
        while i <= n:
            j = i
            while i % p == 0:
                cnt += 1
                i //= p
            i = j + p
    print(cnt)