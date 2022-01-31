t = int(input())  # 테스트 케이스의 수

for i in range(t):
    k = int(input())  # 층
    n = int(input())  # 호

    def people(k, n):
        if n <= 1:
            return 1
        elif k <= 0:
            return n

        return people(k - 1, n) + people(k, n - 1)

    print(people(k, n))
