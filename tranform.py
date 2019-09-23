n = int(input())
a = []
for i in range(n):
    a.append(input())
for i in range(n):
    b = []
    for symbol in a[i]:
        if symbol.isalpha():
            print(symbol,end="")
        elif symbol == ")":
            print(b.pop(),end="")
        elif symbol != "(":
            b.append(symbol)
    print()