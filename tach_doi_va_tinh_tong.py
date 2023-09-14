def cal(s):
    idx = len(s)/2-1
    sum1 = 0
    sum2 = 0
    for i in range(len(s)):
        if i <= idx:
            sum1 = sum1*10 + ord(s[i]) - ord('0')
        else:
            sum2 = sum2*10 + ord(s[i]) - ord('0')
    return str(sum1 + sum2)

s = input()
while(True):
    if len(s) == 1:
        break
    s = cal(s)
    print(s)
#1234
#123