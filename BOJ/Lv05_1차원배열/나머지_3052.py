list = []
cnt = 0

for i in range(10):
    num = int(input())
    num %= 42
    list.append(num)

cnt = len(set(list))  # 리스트의 중복을 제거하고 길이를 잼
print(cnt)
