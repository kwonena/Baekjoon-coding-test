import sys
input = sys.stdin.readline

n = int(input())  # 도시의 개수

road = list(map(int, input().split()))  # 도로의 길이
price = list(map(int, input().split()))  # 주유소 리터당 가격

current = price[0]
total = 0

for i in range(n - 1):
    if current > price[i]:
        current = price[i]
    total += current * road[i]

print(total)
