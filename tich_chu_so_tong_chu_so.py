def calSum(s):
    sum = 0
    for i in range(1, len(s), 2):
        sum += int(s[i])
    return sum

def calMul(s):
    mul = 1
    for i in range(0, len(s), 2):
        if s[i] != '0':
            mul *= int(s[i])
    return mul

for _ in range(int(input())):
    s = input()
    print(calMul(s), calSum(s), sep = " ")
    