t = int(input())
aBox = []
bBox = []
sum = []

for i in range(1, t + 1):
    a, b = map(int, input().split())
    aBox.append(a)
    bBox.append(b)
    sum.append(a+b)

for i in range(t):
    print("Case #{0}: {1} + {2} = {3}".format(i + 1, aBox[i], bBox[i], sum[i]))
