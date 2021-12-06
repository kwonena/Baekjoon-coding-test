n = int(input())  # 배달해야 하는 총 킬로그램
suga = 0  # 설탕 봉지의 개수

while True:
    if n % 5 == 0:
        suga += (n // 5)
        print(suga)
        break
    n -= 3
    suga += 1

    if n < 0:
        print("-1")
        break
