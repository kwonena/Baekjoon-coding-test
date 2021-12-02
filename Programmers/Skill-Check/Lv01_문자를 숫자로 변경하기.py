def solution(s):
    answer = 0
    alpha = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
             '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

    alphaNum = alpha.keys()

    for i in alphaNum:
        s = s.replace(alpha[i], i)

    answer = int(s)
    print(answer)
    return answer  # s가 의미하는 원래 숫자


solution("one4seveneight")
