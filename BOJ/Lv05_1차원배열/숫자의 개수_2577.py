a = int(input())  # a, b, c 숫자 입력
b = int(input())
c = int(input())

multi = a * b * c
m_list = list(map(int, str(multi)))  # 곱한 수를 리스트에 저장

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zero_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(number)):
    for j in range(len(m_list)):
        if m_list[j] == number[i]:
            zero_list[i] += 1

for i in zero_list:
    print(i)
