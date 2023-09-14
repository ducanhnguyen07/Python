import math

def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check(s):
    if checkPrime(len(s)) == False:
        return False
    cntPrime = 0
    for i in range(len(s)):
        if checkPrime(int(s[i]) - int('0')):
            cntPrime += 1
    if cntPrime <= len(s) - cntPrime:
        return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")   
