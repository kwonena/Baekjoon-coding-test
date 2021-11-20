t = int(input())  # 테스트 개수

for i in range(t):
    ox = input()
    list(ox)

    sum = 0
    cnt = 0

    for j in ox:
        if j == 'O':  # 맞은 문제일 때
            cnt += 1
            sum += cnt
        else:  # 틀린 문제일 때
            cnt = 0

    print(sum)
