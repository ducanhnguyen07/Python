s = input()
a = []
b = {}
idx = 0
while True:
    if idx > len(s)-2:
        break
    n = str(int(s[idx])*10 + int(s[idx+1]))
    if n not in b:
        b[n] = 1
    else:
        b[n] += 1
    idx += 2
for i in b:
    print(i, b[i], sep = ' ')
#123