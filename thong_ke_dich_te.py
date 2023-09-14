dx = [-1, -1, -1, 0, 1, 1,  1,  0]
dy = [-1,  0,  1, 1, 1, 0, -1, -1]

n, m = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
fl = []
for i in range(n):
    b = [0 for i in range(m)]
    fl.append(b)
cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if x >= 0 and y >= 0 and x < n and y < m and fl[x][y] == 0:
                    fl[x][y] = 1
                    cnt += a[x][y]
print(cnt)

