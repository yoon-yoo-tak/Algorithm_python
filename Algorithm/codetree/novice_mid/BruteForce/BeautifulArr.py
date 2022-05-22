"""
아름다운 수열 2
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(map(int, input().split()))
cnt = 0
for i in range(n - m + 1):
    if sorted(a[i:i + m]) == b:
        cnt += 1
print(cnt)