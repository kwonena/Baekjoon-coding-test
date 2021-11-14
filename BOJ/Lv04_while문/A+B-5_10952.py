sum = []

while(True):
    a, b = map(int, input().split())
    sum.append(a + b)

    if a == 0 and b == 0:
        break

for i in range(len(sum)-1):
    print(sum[i])
