list = []
max = 0
cnt = 0

for i in range(9):
    num = int(input())
    list.append(num)

    if max < list[i]:
        max = list[i]
        cnt = i + 1

print(max)
print(cnt)
