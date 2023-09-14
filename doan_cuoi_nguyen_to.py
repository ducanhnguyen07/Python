def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check(s):
    sum = 0
    for i in range(len(s)-4, len(s), 1):
        sum = sum*10 + int(s[i])
    if checkPrime(sum):
        return True
    return False

for _ in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")