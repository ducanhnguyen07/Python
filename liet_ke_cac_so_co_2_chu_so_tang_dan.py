s = input()
a = []
b = {}
idx = 0
while True:
    if idx > len(s)-2:
        break
    n = str((ord(s[idx]) - ord('0'))*10 + (ord(s[idx+1]) - ord('0')))
    if n not in b:
        b[n] = 1
    else:
        b[n] += 1
    idx += 2
for i in b:
    a.append(i)
a.sort()
print(*a)

#123