t = int(input())  # 테스트 개수

for i in range(t):
    r, s = input().split()  # r : 반복 횟수, s : 문자열
    r = int(r)

    for j in s:
        print(j * r, end="")  # j를 r만큼 반복해서 출력

    print("\n", end="")
