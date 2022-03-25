n, k = map(int, input().split())

money = []  # 동전의 가치 리스트

# 동전의 가치
for _ in range(n):
    m = int(input())
    money.append(m)

# k원을 만드는데 필요한 동전 개수
coin = 0  # 동전의 개수
money.reverse()

i = 0

while k > 0:
    if money[i] <= k:
        while money[i] <= k:
            k -= money[i]
            coin += 1
    i += 1

print(coin)
