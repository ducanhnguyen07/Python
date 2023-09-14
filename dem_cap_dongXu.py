n = int(input())
a = []
for i in range(n):
    a.append(input())

sum = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if a[i][j] == "C":
            cnt += 1
    sum += cnt*(cnt - 1)//2
for i in range(n):
    cnt = 0
    for j in range(n):
        if a[j][i] == "C":
            cnt += 1
    sum += cnt*(cnt - 1)//2
print(sum)