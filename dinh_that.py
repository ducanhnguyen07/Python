def check(n, k, u, v, l):
    q = []
    q.append(u)
    visit = [0] * (n+1)
    visit[u] = 1
    while len(q) > 0:
        s = q.pop()
        if s == v:
            return False
        for t in l[s]:
            if t != k and visit[t] == 0:
                q.append(t)
                visit[t] = 1
    return True

for _ in range(int(input())):
    n, m, u, v = [int(i) for i in input().split()]
    l = []
    for _ in range(n + 1):
        l.append([])
    for i in range(m):
        s, t = [int(i) for i in input().split()]
        l[s].append(t)
    cnt = 0
    for i in range(1, n+1):
        if i != u and i != v:
            if(check(n, i, u, v, l)):
                cnt += 1
    print(cnt)