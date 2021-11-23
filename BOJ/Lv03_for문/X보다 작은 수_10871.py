n, x = map(int, input().split())  # n : 정수의 개수, x : 대소비교할 정수
a = list(map(int, input().split()))  # 수열 a를 이루는 n개의 정수 입력

for i in a:
    if i < x:
        print("{0} ".format(i), end="")
