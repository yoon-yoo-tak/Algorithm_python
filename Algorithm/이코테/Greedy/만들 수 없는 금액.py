"""
이코테 챕터 11(그리디) 4번. 만들 수 없는 금액


1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline
n = int(input())
ls = sorted(map(int, input().split()))

target = 1
for x in ls:
    if target < x:
        break
    target += x

print(target)