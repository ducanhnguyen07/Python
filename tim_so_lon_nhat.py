import re

t=int(input())
while t>0:
    s=re.findall(r'\d+',input())
    a=[int(i) for i in s]
    print(max(a))
    t-=1