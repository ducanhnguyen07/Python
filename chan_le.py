def check(s):
    for i in range(0, len(s) - 1, 1):
        if abs(ord(s[i]) - ord(s[i+1])) != 2:
            return False
    sum = 0
    for i in range(len(s)):
        sum += ord(s[i]) - ord('0')
    if sum % 10 != 0:
        return False
    return True

t = int(input())
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
