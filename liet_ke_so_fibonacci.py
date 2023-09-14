f = []
for i in range(93):
    f.append(0)
f[1] = 1
f[2] = 1
for i in range(3, 93):
    f[i] = f[i-1] + f[i-2]

for _ in range(int(input())):
    l, r = map(int, input().split())
    for i in range(l, r+1):
        print(f[i], end = ' ')
    print()
