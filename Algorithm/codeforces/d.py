"""

"""
import sys

input = sys.stdin.readline

def is_pal(s):
    return s == s[::-1]

for _ in range(int(input())):
    time, m = input().split()
    m = int(m)
    cnt = 0
    if is_pal(time):
        cnt += 1
    a, b = map(int, time.split(":"))
    b = b + (m % 60)
    if b >= 60:
        a += 1
        b -= 60
    a = (a + (m // 60)) % 24
    new_time = str(a).zfill(2) + ':' + str(b).zfill(2)
    while new_time != time:
        if is_pal(new_time):
            cnt += 1
        b = b + (m % 60)
        if b >= 60:
            a += 1
            b -= 60
        a = (a + (m // 60)) % 24
        new_time = str(a).zfill(2) + ':' + str(b).zfill(2)
    print(cnt)


