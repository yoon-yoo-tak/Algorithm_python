"""
22988 재활용 캠페인
"""
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
ls = sorted(map(int, input().split()))
ans = ls.count(x)
# ls = ls[:-ans]  0이면 틀림
for i in range(ans):
    ls.pop()
l, r = 0, len(ls) - 1
rest = len(ls)

while l < r:
    if ls[l] + ls[r] >= x / 2:
        rest -= 2
        l += 1
        r -= 1
        ans += 1
    else:
        l += 1

ans += rest // 3  # 뭐든 3개만 있으면 가능
print(ans)

