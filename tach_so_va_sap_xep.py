import re

s = []
for _ in range(int(input())):
    b = re.findall(r"\d+", input())
    b = list(b)
    for i in b:
        s.append(int(i))
s.sort()
for i in s:
    print(i)
