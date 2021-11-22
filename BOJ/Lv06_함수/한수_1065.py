n = int(input())


def hansu(n):
    if n < 100:
        print(n)
    else:
        cnt = 0
        for i in range(1, n + 1):
            a = i // 100  # n의 백의 자리
            b = (i - 100 * a) // 10  # n의 십의 자리
            c = i - 100 * a - 10 * b  # n의 일의 자리

            if a != 0:
                if (b - a) == (c - b):  # 한수의 성립 조건
                    cnt += 1
        print(cnt + 99)


hansu(n)
