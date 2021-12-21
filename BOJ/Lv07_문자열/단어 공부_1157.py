string = input().upper()
strList = list(set(string))

# 알파벳별로 개수
cnt = []
for i in strList:
    count = string.count(i)
    cnt.append(count)

# 알파벳 출력
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(strList[(cnt.index(max(cnt)))])
