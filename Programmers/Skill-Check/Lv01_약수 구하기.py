def solution(n):
    n = int(input())  # 정수 입력
    answer = 0  # 약수 총합 변수

    for i in range(1, n+1):
        if n % i == 0:
            answer += i

    print(answer)
    return answer


solution(5)  # 함수 출력
