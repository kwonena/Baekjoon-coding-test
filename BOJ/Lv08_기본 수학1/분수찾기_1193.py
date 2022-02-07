x = int(input())

cnt = 0
count = 0

while count < x:
    cnt += 1
    count += cnt

count -= cnt

num = x - count
a = cnt - num + 1
b = num

if cnt % 2 == 0:  # cnt 짝수
    print("{0}/{1}".format(b, a))
else:  # cnt 홀수
    print("{0}/{1}".format(a, b))
