"""
이코테 챕터 11(그리디) 3번. 문자열 뒤집기(백준 1439)


1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline
s = input().strip()
cnt = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        cnt += 1

print((cnt + 1) // 2)
