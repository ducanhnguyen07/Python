parent = [0]*(10**5+1)
sz = [0]*(10**5+1)

def makeSet(v):
    parent[v] = v
    sz[v] = 1

def findSet(v):
    if v == parent[v]:
        return v
    return findSet(parent[v])

def unionSet(a, b):
    u = findSet(a)
    v = findSet(b)
    if u == v:
        return
    if sz[u] < sz[v]:
        u, v = v, u
    parent[v] = u
    sz[u] += sz[v]

for i in range(1, 10**5+1):
    makeSet(i)   
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if z == 1:
        unionSet(x, y)
    else:
        if findSet(x) == findSet(y):
            print(1)
        else:
            print(0)
