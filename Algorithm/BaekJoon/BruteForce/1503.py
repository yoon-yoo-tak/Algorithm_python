"""
1503 세 수 고르기
"""

import sys

input = sys.stdin.readline

arr = [0] * 1001
n, m = map(int, input().split())
s = list(map(int, input().split()))
for i in s:
    arr[i] = 1

ans = int(1e9)

for i in range(1, 1001):
    if arr[i] == 1:
        continue
    for j in range(i, 1001):
        if arr[j] == 1:
            continue
        for k in range(j, 1001):
            if arr[k] == 1:
                continue
            ans = min(ans, abs(n - i * j * k))

print(ans)