"""
9012 괄호

( 일때 push ) 일때 pop > 최종 사이즈 0 이면 YES 아니면 NO
"""

import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    val = 0
    a = input().strip()
    for i in a:
        if i == '(':
            val += 1
        elif i == ')':
            val -= 1
        if val < 0:
            print('NO')
            break
    if val > 0:
        print('NO')
    elif val == 0:
        print('YES')
