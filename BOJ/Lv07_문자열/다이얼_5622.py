s = input().upper()  # 알파벳 대문자로 이루어진 단어

alpha = {
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z'],
}

time = 0
for i in s:
    for j in range(2, 10):
        for s in range(len(alpha[j])):
            if i == alpha[j][s]:
                time += (j + 1)

print(time)
