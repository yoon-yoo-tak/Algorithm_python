"""
씨 오 더블유 2
"""
import sys

input = sys.stdin.readline
cnt = 0
n = int(input())
s = input().strip()

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if s[i] == 'C' and s[j] == 'O' and s[k] == 'W':
                cnt += 1

print(cnt)