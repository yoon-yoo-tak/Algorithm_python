"""
5430 AC
"""

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

# D : 첫번째 수 버림, R = 배열 순서 뒤집음

for _ in range(t):
    p = input().strip()
    n = int(input())
    ls = deque(input().strip()[1:-1].split(','))
    q = deque(ls)

    R_cnt, start , end = 0, 0, len(q) - 1

    flag = False

    if n == 0:
        q = []
        start, end = 0, 0

    for i in p:
        if i == 'R':
            R_cnt += 1
        elif i == 'D':
            if len(q) < 1:
                flag = True
                print('error')
                break
            else:
                if R_cnt % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    if not flag:
        if R_cnt % 2 == 0:
            print('['+','.join(q)+']')
        else:
            q.reverse()
            print('[' + ','.join(q) + ']')




