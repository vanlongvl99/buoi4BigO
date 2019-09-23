n = int(input())
    while True:
        cars = list(map(int,input().split()))
        if cars[0] == 0:
            break
        oderedCars = sorted(cars)
        cnt = [0]*1005
        for i in range(n):
            cnt[oderedCars[i]] = i
        stack = []
        count = 0
        for i in range(n):
            if cnt[cars[i]] == count:
                count += 1
            else:
                stack.append(cars[i])
        for i in range(len(stack)):
            if cnt[stack.pop()] == count:
                count += 1
            else:
                print("no")
                exit()
        print("yes")