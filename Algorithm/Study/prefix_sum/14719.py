"""

"""
import sys

input = sys.stdin.readline

h, w = map(int, input().split())
ls = list(map(int, input().split()))
ans = 0
for i in range(1, w - 1):
    left = max(ls[:i])  # 왼쪽 가장 높은 곳
    right = max(ls[i + 1:])  # 오른쪽 가장 높은 곳
    min_h = min(left, right)  # 둘중 낮은곳
    if ls[i] < min_h:  # 낮은곳 보다 낮다 >> 고인다
        ans += min_h - ls[i]  # 차이만큼 +
print(ans)