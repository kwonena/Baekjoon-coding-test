n = input()

# 입력받은 n을 리스트에 문자열로 자릿수별로 저장
n = list(map(int, str(n)))

tmp = 0

# 요소 하나씩을 정수형으로 변환
for i in n:
    i = int(i)

# 크기 비교 후 내림차순으로 정렬
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] < n[j]:
            tmp = n[i]
            n[i] = n[j]
            n[j] = tmp

for i in n:
    print(i, end="")
