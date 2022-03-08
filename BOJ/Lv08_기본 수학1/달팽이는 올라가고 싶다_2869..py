import math

a, b, v = map(int, input().split())

day = (v - a) / (a - b) + 1
print(math.ceil(day))

# 시간 초과로 틀린 코드
# a, b, v = map(int, input().split())

# pos = 0  # 달팽이의 위치
# day = 0  # 걸리는 기간

# while True:
#     pos += a
#     day += 1
#     if pos >= v:
#         break
#     pos -= b

# print(day)
