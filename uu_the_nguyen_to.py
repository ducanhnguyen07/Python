def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check(s):
    cntP = 0
    cnt = 0
    for i in s:
        if checkPrime(int(i)):
            cntP += 1
        else:
            cnt += 1
    if checkPrime(len(s)) and cntP > cnt:
        return True
    return False

for _ in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
    