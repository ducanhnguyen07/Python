def check(a, n):
    for i in range(n-1):
        if a[i] != a[i+1]:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        x = input()
        s = int(x)
        a.append(s)
    a.sort()
    if check(a, n):
        print("BANG NHAU")
    else:
        print(a[0], a[n-1], sep = ' ')
    