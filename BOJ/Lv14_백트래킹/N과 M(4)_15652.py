from itertools import combinations_with_replacement

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
res = list(combinations_with_replacement(arr, m))

for i in res:
    print(*i, sep=' ')
