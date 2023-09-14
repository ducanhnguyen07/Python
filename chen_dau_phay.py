s = input()
n = 0
if len(s) % 3 != 0:
    n = int(len(s) / 3) - 1
    n = 3*n - len(s)
for i in range(len(s)):
    if n % 3 == 0 and i > 0 and len(s) > 3:
        print(",", end = '')
    print(s[i], end = '')
    n += 1
