for _ in range(int(input())):
    n = int(input())
    a = [0]*n
    b = [0]*n
    res = []
    for i in range(n):
        a[i], b[i] = map(float, input().split())
    dp = [1]*n
    for i in range(n):
        for j in range(0, i):
            if a[i] > a[j] and b[i] < b[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    print(max(dp))
        

