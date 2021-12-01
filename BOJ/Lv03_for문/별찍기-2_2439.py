n = int(input())

for i in range(n):
    for j in range(i, n-1):  # 공백 출력
        print(" ", end="")
    for j in range(n-i-1, n):  # 별 출력
        print("*", end="")
    print(" ")
