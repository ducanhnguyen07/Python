a = {}
for _ in range(int(input())):
    id_class = input()
    name_class = input()
    format_class = input()
    a[id_class] = (name_class, format_class)
b = list(a.items())
b.sort(key=lambda x : x[0])
for i in b:
    print(i[0], i[1][0], i[1][1])