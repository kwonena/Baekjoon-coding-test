n = int(input())

people = list(map(int, input().split()))
people.sort() # 시간 순서대로 정렬

time = [0] * n # 돈을 인출하는데 필요한 시간 배열

for i in range(len(people)):
    if i > 0:
        time[i] = time[i - 1] + people[i]
    else:
        time[i] = people[i]

print(sum(time))
