t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 1
    fl = True
    while cnt <= 1000:
        if n % 7 == 0:
            print(n)
            break
        s = ''.join(reversed(str(n)))
        n = n + int(s)
        cnt += 1
    if cnt > 1000:
        print(-1)

