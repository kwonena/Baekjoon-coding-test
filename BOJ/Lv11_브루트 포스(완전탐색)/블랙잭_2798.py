n, m = map(int, input().split())
num = list(map(int, input().split()))

# 플레이어는 n개중에서 3장의 카드를 고름
# 합은 m을 넘지 않음
# m과 플레이어 카드의 합을 뺀 절대값이 가장 작은 수
player = []

for i in range(n):  # 5부터
    for j in range(i + 1, n):  # 6부터
        for k in range(j + 1, n):  # 7부터
            if k <= n:
                sum = num[i] + num[j] + num[k]
                if sum <= m:
                    player.append(sum)


print(max(player))
