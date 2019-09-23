a = input()
b = []
for i in range(len(a)):
    b.append(a[i])
print(b)





# 
# 
# 
# import queue
# count = 0
# while True:
    # p, n = map(int,input().split())
    # if p == 0 and n == 0:
        # break
    # queueP = queue.Queue()
    # if p < n:
        # for i in range(1,p+1):
            # queueP.put(i)
        # queueOut = queue.Queue()
        # for i in range(n):
            # char = input().split(" ")
            # if char[0] == "N":
                # k = queueP.get()
                # queueP.put(k)
                # queueOut.put(k)
            # else:
                # queueP.put(int(char[1]))
                # for i in range(p):
                    # k = queueP.get() 
                    # if k != int(char[1]):
                        # queueP.put(k)
        # count += 1
        # print("Case",str(count) + ":")
        # for i in range(queueOut.qsize()):
            # print(queueOut.get())
    # else:
        # dem = 1
        # arr1 = []
        # arr2 = []
        # for i in range(n):
            # char = input().split(" ")
            # if char[0] == "N":
                # if len(arr1) == 0:
                    # if dem not in arr2:
                        # queueP.put(dem)
                    # dem += 1
                # else:
                    # queueP.put(arr1.pop())
            # else:
                # arr1.append(int(char[1]))
                # arr2.append(int(char[1]))
        # count += 1
        # print("Case",str(count) + ":")
        # for i in range(queueP.qsize()):
            # print(queueP.get())
# 
# 
# 









# c = {}
# c['long'] = 10
# print(c)
# 
# a ={1: 'D', 8: 'B', 3: 'B', 4: 'E', 5: 'A'}
# for i in range(10):
    # if i in a:
        # print(i, a[i])
# 
# b = ["a","b"]
# print(b)

# class student():
    # # def __init__(self,ten,score):
        # # # self.ten = ten
        # # # self.score = score
# 
# # a = []
# # # a.append(student('An', 10))
# # # a.append(student('Nam', 11))
# # # a.append(student('Binh', 5))
# # # a.sort(key=lambda x: (x.ten, x.score))
# # for x in a:
    # print(x.ten, x.score)