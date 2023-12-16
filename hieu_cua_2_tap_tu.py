f1 = open("DATA1.in", 'r')
f2 = open("DATA2.in", 'r')
data = []
a = []
b = []
for i in f1:
    data.append(i)
for i in data:
    x = i.lower().split()
    for j in x:
        if j not in a:
            a.append(j)
a.sort()
data.clear()
for i in f2:
    data.append(i)
for i in data:
    x = i.lower().split()
    for j in x:
        if j not in b:
            b.append(j)
b.sort()
for i in a:
    if i not in b:
        print(i, end = ' ')
print()
for i in b:
    if i not in a:
        print(i, end = ' ')