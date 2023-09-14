b = {}
for _ in range(int(input())):
    s = input()
    c, t = map(int, input().split())
    b[s] = (c, t)

b = sorted(b.items(), key = lambda x: (-x[1][0], x[1][1], x[0]))

for i in b:
    print(i[0], i[1][0], i[1][1])
