n = int(input())
num = n
cnt = 0

while True:
    a = n // 10  # 10의 자리(몫)
    b = n % 10  # 1의 자리(나머지)
    c = (a + b) % 10  # c의 1의 자리
    n = (b * 10) + c

    cnt += 1
    if num == n:
        break

print(cnt)
