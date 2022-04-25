"""
2799 블라인드
*
0개 1
4개 2
8개 3
12개 4
16개 5
"""

import sys

input = sys.stdin.readline
a, b = map(int, input().split())
ls = [input().strip() for _ in range(5 * a + 1)]
str = ''
for j in range(1, 5 * b + 1, 5):
    for i in range(5 * a + 1):
       str += ls[i][j:j + 4]

str = str.split('####')

blind = {'................': 0
, '****............': 0
, '********........': 0
, '************....': 0
, '****************': 0}

for i in str:
    if i in blind:
        blind[i] += 1
for item in blind:
    print(blind[item], end=' ')

