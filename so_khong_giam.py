def check(s):
    for i in range(0, len(s)-1, 1):
        if s[i] > s[i+1]:
            return False
    return True

t = int(input())
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")