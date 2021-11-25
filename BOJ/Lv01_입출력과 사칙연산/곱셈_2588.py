a = int(input())  # 1의 위치
b = int(input())  # 2의 위치

bFirst = b // 100
bSecond = (b - bFirst * 100) // 10
bThird = b - bFirst * 100 - bSecond * 10

print(a * bThird)
print(a * bSecond)
print(a * bFirst)
print(a * b)
