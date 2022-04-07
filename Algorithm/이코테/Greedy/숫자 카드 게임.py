"""
이코테 그리디 파트 연습문제 - 숫자 카드 게임

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
a = []
for i in ls:
    a.append(min(i))
print(max(a))

