n = int(input())

number = list(map(int, input().split()))
sosu = 0

for i in number:
    cnt = 0
    for j in range(2, i + 1):
        if i % j == 0:
            cnt += 1

    if cnt == 1:
        sosu += 1


print(sosu)
