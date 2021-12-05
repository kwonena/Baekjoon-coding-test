a, b, c = map(int, input().split())

if b >= c:  # 손익분기점이 존재하지 않는 경우
    x = -1
else:  # 손익분기점이 존재하는 경우
    x = a / (c - b)
    x += 1

print(int(x))
