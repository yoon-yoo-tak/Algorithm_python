"""

2343 기타 레슨

블루레이의 크기가 L 일때 m개로 나눈것을 담을 수 있느냐?

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(map(int, input().split()))

def determination(len):
    cnt, sum = 1, 0
    for x in a:
        if sum + x > len:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt <= m


l, r, ans = max(a), 1000000000, 0
while l <= r:
    mid = (l + r) // 2
    if determination(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)

