for _ in range(int(input())):
    a = [str(i) for i in input().split()]
    cnt = 0
    for i in a:
        if cnt + len(i) <= 100:
            cnt += len(i)
            print(i, end = ' ')
            if cnt == 100:
                break
            else:
                cnt += 1
        else:
            break
    print()
    

