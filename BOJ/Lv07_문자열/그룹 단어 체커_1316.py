n = int(input())  # 단어의 개수
groupWord = n

for i in range(n):
    word = list(input())  # 단어 입력
    wordList = []
    checkWord = word[0]
    wordList.append(checkWord)
    cnt = 0
    for j in range(1, len(word)):
        if checkWord != word[j]:  # checkWord와 단어가 같지 않을 때
            for s in wordList:
                if s == word[j]:  # 단어가 기존 배열에 저장된 값과 같을 때
                    groupWord -= 1
                    cnt = 1
                    break
            checkWord = word[j]
            wordList.append(checkWord)
            if cnt == 1:  # 그룹단어가 아닌 경우 break로 탈출
                break


print(groupWord)
