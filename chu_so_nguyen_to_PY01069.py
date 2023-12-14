from queue import Queue

n = int(input())
q = Queue()
q.put("2")
q.put("3")
q.put("5")
q.put("7")
while q.qsize():
    top = str(q.get())
    if len(top) > n:
        break
    if top.count("2") > 0 and top.count("3") > 0 and top.count("5") > 0 and top.count("7") > 0 and ord(top[-1]) % 2:
        print(top) 
    q.put(top + "2")
    q.put(top + "3")
    q.put(top + "5")
    q.put(top + "7")