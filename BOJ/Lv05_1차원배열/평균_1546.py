n = int(input())  # 과목의 개수
score = list(map(int, input().split()))  # 세준이의 점수
sum = 0

max = max(score)  # 최고점

for i in range(n):
    score[i] = score[i] / max * 100
    sum += score[i]

print(sum/n)
