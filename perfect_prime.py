def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check(s):
    if checkPrime(int(s)) == False:
        return False
    t = ''.join(reversed(s))
    if checkPrime(int(t)) == False:
        return False
    for i in s:
        if checkPrime(int(i)) == False:
            return False
    sum = 0
    for i in s:
        sum += int(i)
    if checkPrime(sum) == False:
        return False
    return True

for _ in range(int(input())):
    s = input()
    print("Yes") if check(s) else print("No")