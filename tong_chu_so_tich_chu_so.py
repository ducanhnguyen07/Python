def calSum(s):
    sum = 0
    for i in range(0, len(s), 2):
        sum += int(s[i])
    return sum

def calMul(s):
    mul = 1
    x = ""
    cnt = 0
    for i in range(1, len(s), 2):
        x += str(s[i])
        if(s[i] == '0'):
            cnt += 1
    if cnt == len(x):
        return 0
    for i in x:
        if i != '0':
            mul *= int(i)
    return mul

for _ in range(int(input())):
    s = input()
    print(calSum(s), calMul(s), sep = " ")
    