n = int(input())

number = 665
cnt = 0  # 몇 번째 영화인지 계산하는 변수

while True:
    number += 1
    if '666' in str(number):
        cnt += 1
        if cnt == n:
            print(number)
            break
