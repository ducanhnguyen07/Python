visited = [False]*105
l = {}

def dfs(u):
    visited[u] = True
    for i in l[u]:
        if visited[i] == False:
            dfs(i)

for _ in range(int(input())):
    n, m = map(int, input().split())
    for i in range(1, n+1):
        l[i] = []
    for i in range(m):
        u, v = map(int, input().split())
        l[u].append(v)
        l[v].append(u)
    a = []
    maxx = -1
    for i in range(1, n+1):
        visited = [False]*(n+1)
        visited[i] = True
        cnt = 0
        for j in range(1, n+1):
            if visited[j] == False:
                cnt += 1
                dfs(j)
        maxx = max(cnt, maxx)
        a.append((i, cnt))
    if maxx == 1:
        print(0)
    else:
        for i in range(len(a)):
            if a[i][1] == maxx:
                print(a[i][0])
                break
    