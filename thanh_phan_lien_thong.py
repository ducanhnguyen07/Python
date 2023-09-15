visited = [False]*105
l = {}

def dfs(u):
    visited[u] = True
    for i in l[u]:
        if visited[i] == False:
            dfs(i)

n, m, st = map(int, input().split())
for i in range(1, n+1):
    l[i] = []
for i in range(m):
    u, v = map(int, input().split())
    l[u].append(v)
    l[v].append(u)
a = []
visited = [False]*(n+1)
dfs(st)
for i in range(1, n+1):
    if visited[i] == False:
        a.append(i)
if len(a) == 0:
    print(0)
else:
    for i in a:
        print(i)
