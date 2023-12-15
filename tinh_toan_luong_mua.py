class Station:
    def __init__(self, id, name, time, quantity):
        self.id = f"T{id:02}"
        self.name = name
        self.time = time
        self.quantity = quantity
    
    def getAvg(self):
        return self.quantity / self.time
    
    def __str__(self):
        return '{} {} {:.2f}'.format(self.id, self.name, self.getAvg())

n = int(input())
cnt = 1
a = []
for i in range(n):
    name = input()
    st = input()
    fi = input()
    time = ((float(fi[:2]) - float(st[:2])) * 60 + (float(fi[3:]) - float(st[3:])))/60.0
    quantity = float(input())
    fl = True
    for i in a:
        if i.name == name:
            i.quantity += quantity
            i.time += time
            fl = False
            break
    if fl:
        a.append(Station(cnt, name, time, quantity))
        cnt += 1
for i in a:
    print(i)