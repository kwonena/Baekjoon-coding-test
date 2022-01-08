n = int(input())
list = []

# n개의 수 입력받기
for i in range(n):
    x = int(input())
    list.append(x)

# 오름차순으로 정렬하기
tmp = 0

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:
            tmp = list[i]
            list[i] = list[j]
            list[j] = tmp

# 출력하기
for i in list:
    print(i)
