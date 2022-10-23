"""
2304
"""
import sys

input = sys.stdin.readline

n = int(input())
height = [0] * 1001

for _ in range(n):
    a, b = map(int, input().split())
    height[a] = b

idx = height.index(max(height))
mx = ans = 0

for i in range(idx):
    if mx < height[i]:
        mx = height[i]
    ans += mx
mx = 0
for i in range(1000, idx, -1):
    if mx < height[i]:
        mx = height[i]
    ans += mx
print(ans + height[idx])
