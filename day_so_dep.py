for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt = 0
    for i in range(n-1):
        mi = min(a[i], a[i+1])
        ma = max(a[i], a[i+1])
        if ma/2 > mi:
            while mi*2 < ma:
                mi *= 2
                cnt += 1
    print(cnt)