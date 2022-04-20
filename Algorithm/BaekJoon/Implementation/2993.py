"""
2993 세 부분
"""

import sys

input = sys.stdin.readline

s = input().strip()
ls = []
for i in range(len(s) - 2):
    for j in range(i + 1, len(s) - 1):
        for k in range(j + 1, len(s)):
            a = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
            ls.append(a)
print(min(ls))