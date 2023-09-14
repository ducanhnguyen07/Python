n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = {}
c = []

sa = set(a)
for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1
max_cnt = 0
maxx = 0
idx = 0
for i in a:
    max_cnt = max(b[i], max_cnt)
for i in a:
    if b[i] < max_cnt:
        maxx = max(b[i], maxx)
for i in a:
    if maxx == b[i]:
        c.append(i)
c.sort()
print(c[0]) if maxx else print("NONE")


