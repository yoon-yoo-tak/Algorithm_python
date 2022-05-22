"""
괄호쌍 만들어주기 3
"""
import sys

input = sys.stdin.readline
cnt = 0
s = input().strip()
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == '(' and s[j] == ')':
            cnt += 1
print(cnt)