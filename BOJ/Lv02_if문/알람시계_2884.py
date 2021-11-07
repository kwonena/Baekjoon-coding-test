# 알람시계의 시간 45분 앞당기기
h, m = map(int, input().split())  # h : 시간, m : 분
m = m - 45

if m >= 60:
    m = m - 60
    h = h + 1
    print("{0} {1}".format(h, m))
elif h >= 24:
    h = h - 24
    print("{0} {1}".format(h, m))
elif m < 0:
    m = m + 60
    h = h - 1
    if h < 0:
        h = h + 24
    print("{0} {1}".format(h, m))
else:
    print("{0} {1}".format(h, m))
