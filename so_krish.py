a = []
for i in range(10):
    a.append(0)
a[0] = 1
for i in range(1, 10):
    a[i] = a[i-1] * i

for _ in range(int(input())):
    s = input()
    sum = 0
    for i in s:
        x = ord(i) - ord('0')
        sum += a[x]
    print("Yes") if sum == int(s) else print("No")