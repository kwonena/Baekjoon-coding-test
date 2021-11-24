# 처음 틀린 코드
# c = int(input())  # 테스트 개수
# avg = []  # 전체 학생의 평균
# avgHigh = 0  # 평균을 넘는 학생들
# avgHighStudent = []  # 평균을 넘는 학생들의 비율

# for i in range(c):
#     student = list(map(int, input().split()))
#     avg = (sum(student)-student[0]) // student[0]

#     for j in range(1, len(student)):  # student[1]~student[5] : 학생들의 점수만
#         if avg < student[j]:
#             avgHigh += 1
#     avgHighStudent.append(avgHigh / student[0] * 100)

# for i in range(c):
#     print("{0}%".format(round(avgHighStudent[i], 3)))

c = int(input())
for i in range(c):
    student = list(map(int, input().split()))
    n = student[0]  # n : 학생의 수

    avg = sum(student[1:]) / n  # 각 테스트의 평균
    cnt = 0  # 평균이상 학생 수
    for i in student[1:]:
        if i > avg:
            cnt += 1

    print("{:.3f}%".format(cnt / n * 100))
