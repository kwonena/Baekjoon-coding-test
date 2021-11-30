a, b = input().split()

a = list(a)
b = list(b)

if a[::-1] > b[::-1]:
    a = a[::-1]
    for i in a:
        print("{0}".format(i), end="")
else:
    b = b[::-1]
    for i in b:
        print("{0}".format(i), end="")
