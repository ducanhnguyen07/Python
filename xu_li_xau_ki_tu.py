a = sorted((str(i).lower() for i in input().split()))
b = sorted((str(i).lower() for i in input().split()))
a = set(a)
b = set(b)
a = sorted(a)
b = sorted(b)
c = set()
for i in a:
    c.add(i)
for i in b:
    if i not in c:
        c.add(i)
c = sorted(c)
for i in c:
    print(i, end = ' ')
print()
for i in b:
    if i in a:
        print(i, end = ' ')