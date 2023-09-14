n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

asg = []
subAB = []
subBA = []
for i in a:
    if i in b:
        asg.append(i)
    else:
        subAB.append(i)
for i in b:
    if i not in a:
        subBA.append(i)
asg = set(asg)
subAB = set(subAB)
subBA = set(subBA)
asg = sorted(asg)
subAB = sorted(subAB)
subBA = sorted(subBA)
print(*asg)
print(*subAB)
print(*subBA)
    
