n = int(input())  # 사람의 수

people = [[0 for _ in range(2)] for _ in range(n)]
rank = [0 for _ in range(n)]

# 학생별 몸무게, 키 입력
for i in range(n):
    x, y = map(int, input().split())
    people[i][0] = x  # 몸무게
    people[i][1] = y  # 키

for i in range(n):
    k = 1  # 등수
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            k += 1
            rank[i] = k
        else:
            rank[i] = k

# 등수 출력
for i in range(n):
    print(rank[i], end=' ')
