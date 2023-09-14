s = input()
k = int(input())
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
    if b[i] >= k:
        a.append(i)
a.sort()
if len(a) == 0:
    print("NOT FOUND") 
else:
    for i in a:
        print(i, b[i], sep = ' ')

#123