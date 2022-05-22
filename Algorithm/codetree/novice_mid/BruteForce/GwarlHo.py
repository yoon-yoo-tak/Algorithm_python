"""
괄호 쌍 만들어주기 2
"""
import sys

input = sys.stdin.readline

s = input().strip()
cnt = 0
for i in range(len(s)):
    for j in range(i + 2, len(s) - 1):
        if s[i] == '(' and s[i + 1] == '(':
            if s[j] == ')' and s[j + 1] == ')':
                cnt += 1
print(cnt)