import queue
count = 0
while True:
    p, n = map(int,input().split())
    if p == 0 and n == 0:
        break
    queueP = queue.Queue()
    for i in range(1,p+1):
        queueP.put(i)
    queueOut = queue.Queue()
    for i in range(n):
        char = input().split(" ")
        if char[0] == "N":
            k = queueP.get()
            queueP.put(k)
            queueOut.put(k)
        else:
            queueP.put(int(char[1]))
            for i in range(p):
                k = queueP.get() 
                if k != int(char[1]):
                    queueP.put(k)
            # queueP.queue.clear()
            # queueP.put(int(char[1]))
            # for i in range(p -1):
            #     queueP.put(newQueue.get())
    count += 1
    print("Case",str(count) + ":")
    for i in range(queueOut.qsize()):
        print(queueOut.get())

