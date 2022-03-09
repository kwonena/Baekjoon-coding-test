n = int(input())

honeycomb = 1  # 벌집의 개수
cnt = 1

while n > honeycomb:
    honeycomb += 6 * cnt
    cnt += 1

print(cnt)

# 시간초과로 틀린 코드
# n = int(input())
# x = 0
# c = 1  # 처음 시작
# cnt = 1  # 지나간 벌집 개수

# while True:
#     x += 1
#     b = c + 1
#     c = b + 6 * x - 1
#     if b <= n <= c:
#         cnt += 1
#         break
#     else:
#         cnt += 1

# print(cnt)
