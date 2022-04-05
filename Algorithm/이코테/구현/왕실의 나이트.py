"""
이코테 구현파트 연습문제 - 왕실의 나이트

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline
dxy = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
a = input().strip()
x, y = int(a[1]), (ord(a[0]) - 96)
count = 0
for dx, dy in dxy:
    nx, ny = x + dx, y + dy
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1
print(count)