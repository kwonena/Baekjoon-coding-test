t = int(input())  # 테스트 케이스의 수

for i in range(t):
    h, w, n = map(int, input().split())

    floor = n % h  # 층 수
    number = n // h + 1  # 호실 번호

    if n % h == 0:  # n이 h의 배수일 때
        number = n // h
        floor = h

    print(floor * 100 + number)
