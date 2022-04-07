"""
이코테 챕터 11(그리디) 2번. 곱하기 혹은 더하기
"""

import sys

input = sys.stdin.readline
s = input().strip()
ls = [int(x) for x in s]

result = ls[0]
for i in range(1, len(ls)):
    num = ls[i]
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)