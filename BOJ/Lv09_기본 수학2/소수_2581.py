m = int(input())  # 최소값
n = int(input())  # 최대값

sum = 0
min = n

for i in range(m, n+1):
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break

        if cnt == 0:  # 소수 일 때
            sum += i
            if i < min:
                min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
