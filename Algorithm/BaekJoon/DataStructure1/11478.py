"""
11478 서로 다른 부분 문자열의 개수
"""

import sys

input = sys.stdin.readline

s = input().strip()
ls = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        ls.add(s[i:j + 1])
print(len(ls))