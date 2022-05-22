"""
인접하지 않은 2개의 숫자
"""
import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
ans = -1
for i in range(n - 2):
    for j in range(i + 2, n):
        ans = max(ans, ls[i] + ls[j])
print(ans)
