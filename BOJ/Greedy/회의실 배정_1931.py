import sys
input = sys.stdin.readline

n = int(input())  # 회의의 수

time = []

# 회의의 정보 입력
for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

# 끝나는 시간을 기준으로 정렬
# 끝나는 시간이 같을 경우 시작 시간을 기준으로 정렬
time.sort(key=lambda x: (x[1], x[0]))

cnt = 1
current = time[0][1]

# 최대 회의 개수 구하기
for i in range(1, n):
    if current <= time[i][0]:
        current = time[i][1]
        cnt += 1

print(cnt)
