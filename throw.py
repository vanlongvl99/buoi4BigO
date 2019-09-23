import queue
while True:
    n = int(input())
    if n == 0:
        break
    deck = queue.Queue()
    for i in range(n):
        deck.put(i+1)
    i = 0
    throw = []
    while True:
        if i%2 == 0:
            throw.append(deck.get())
        else:
            deck.put(deck.get()) 
        if deck.empty():
            break
        i = i + 1
    print("Discarded cards:",end="")
    if len(throw) == 1:
        print("")
    else:
        for i in range(len(throw)):
            if i == len(throw) - 2: 
                print("",throw[i])
                break
            else:
                print("",throw[i],end=",")
    print("Remaining card:",throw[len(throw) - 1])