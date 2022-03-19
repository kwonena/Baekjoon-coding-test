from itertools import product

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
res = list(product(arr, repeat=m))

for i in res:
    print(*i, sep=' ')
