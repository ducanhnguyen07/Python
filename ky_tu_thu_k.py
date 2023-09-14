for _ in range(int(input())):
    n, k = map(int, input().split())
    cnt = 0
    while k % 2 == 0:
        cnt += 1
        k /= 2
    print(chr(cnt + ord('A')))