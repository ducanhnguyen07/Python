n = int(input())
a = []
content = []
for i in range(n):
    s = input()
    if len(s) == 0:
        a.append((content[0], len(content)-1))
        content = []
    elif i == n - 1:
        a.append((content[0], len(content)))
    else:
        content.append(s)

for x, y in a:
    print(x, y, sep = ": ")
