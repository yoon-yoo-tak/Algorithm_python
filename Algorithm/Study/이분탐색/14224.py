"""
14224 작은 정사각형 2
"""
import sys

input = sys.stdin.readline


def check(x, y) -> int:
    res = 0
    for q in range(n):
        if x <= dots[q][0] <= x + mid - 2 and y <= dots[q][1] <= y + mid - 2:
            res += 1
    return res


def ok() -> bool:
    for i in range(n):
        for j in range(n):
            xx = min(dots[i][0], dots[j][0])
            yy = min(dots[i][1], dots[j][1])
            cnt = check(xx, yy)
            if cnt >= k:
                return True
    return False


n, k = map(int, input().split())
dots = [list(map(int, input().split())) for _ in range(n)]
l, r = 2, int(2e9 + 2)

while l < r:
    mid = (l + r) // 2
    if ok():
        r = mid
    else:
        l = mid + 1
print(int(l * l))