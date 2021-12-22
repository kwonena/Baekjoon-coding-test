# 전체 - 생성자로 계산해야한다
allNumber = [x for x in range(1, 10001)]
notSelfNumArr = []  # 셀프 넘버가 아닌 수의 집합
selfNumArr = []  # 셀프 넘버의 집합

for i in allNumber:
    notSelfNum = i
    for j in str(i):
        notSelfNum += int(j)
    notSelfNumArr.append(notSelfNum)

selfNumArr = list(set(allNumber) - set(notSelfNumArr))
selfNumArr.sort()

for i in selfNumArr:
    print(i)
