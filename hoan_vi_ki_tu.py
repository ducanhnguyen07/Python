from itertools import permutations

def Try(s):
    a = permutations(s)
    for i in a:
        print(''.join(i))

s = input()
Try(s)


