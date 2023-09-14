def check(s):
    sum = 0
    for i in range(0, len(s), 1):
        if i % 2 == 0 and int(s[i]) % 2 != 0:
            return False
        if i % 2 != 0 and int(s[i]) % 2 == 0:
            return False
        sum += int(s[i])
    if sum < 2:
        return False
    for i in range(2, int(sum**0.5)+1):
        if sum % i == 0:
            return False
    return True

for _ in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")