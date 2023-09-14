def checkPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)):
        if(n % i == 0):
            return 0
    return 1
def check(s):
    s1 = 0
    s2 = 0
    for i in range(0, 3):
        s1 = s1*10 + int(s[i])
    for i in range(len(s)-3, len(s)):
        s2 = s2*10 + int(s[i])
    if checkPrime(s1) + checkPrime(s2) == 2:
        return True
    return False

for _ in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
    