from itertools import combinations

n, m = map(int, input().split())

arra = [i for i in combinations(range(1, n + 1), m)]

for i in arra:
    print(*i, sep=' ')
