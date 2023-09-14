n = int(input())
a = []
while True:
    b = [int(i) for i in input().split()]
    a += b
    if len(a) == n:
        break
maxx = 0
fl = 1
for i in a:
    maxx = max(i, maxx)
for i in range(1, maxx):
    if i not in a:
        print(i)
        fl = 0
if fl:
    print("Excellent!")
    