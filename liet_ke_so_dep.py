a = []

def check(n):
    s = str(n)
    for i in range(len(s)):
        if (int(s[i]) - int('0')) % 2 != 0:
            return False
    return True

t = int(input())

nb = 2
while nb <= 888:
    if check(nb):
        s = str(nb)
        a.append(int(s + s[ : : -1]))
    nb = nb + 2

for i in range(t):
    n = int(input())
    for i in a:
        if i >= n:
            break
        print(i, end = ' ')
    print()

