def checkPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if(n % i == 0):
            return 0
    return 1

def check(s):
    for i in range(0, len(s)):
        if checkPrime(i) == 1 and checkPrime(int(s[i])) == 0:
            return False
        if checkPrime(i) == 0 and checkPrime(int(s[i])) == 1:
            return False
    return True


for _ in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")