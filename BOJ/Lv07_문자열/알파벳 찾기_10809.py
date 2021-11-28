from string import ascii_lowercase
s = input()  # 소문자로 이루어진 단어 s 입력

# 알파벳 소문자로 이루어진 리스트 생성
alphabet = list(ascii_lowercase)

# 입력값과 알파벳이 동일하다면 배열의 인덱스값 저장
for i in range(len(s)):
    for j in range(len(alphabet)):
        if s[i] == alphabet[j]:
            alphabet[j] = i

# 인덱스값이 저장되지 않는 것은 -1로 초기화
for i in range(len(alphabet)):
    if type(alphabet[i]) == str:
        alphabet[i] = -1

# 결과 출력
for i in alphabet:
    print("{0} ".format(i), end="")
