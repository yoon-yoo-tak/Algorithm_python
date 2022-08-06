"""
1637 날카로운 눈
"""
import sys

input = sys.stdin.readline


def ok(x):
    total = 0
    for i in li:
        check = min(i[1], x)
        if check < i[0]:
            total += 0
        else:
            total += ((check - i[0]) // i[2]) + 1
    return total


n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

l, r = 1, 2147483649
ans = -1

while l <= r:
    mid = (l + r) // 2
    if ok(mid) % 2:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

if ans == -1:
    print("NOTHING")
else:
    print(ans, ok(ans) - ok(ans - 1))