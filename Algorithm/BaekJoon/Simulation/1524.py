"""
1524 세준세비

"""

import sys

input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    S = sorted(map(int, input().split()),reverse = True)
    B = sorted(map(int, input().split()), reverse=True)
    while True:
        if len(S) + len(B) <= 1:
            break
        S_weak = S[-1]
        B_weak = B[-1]
        if S_weak < B_weak:
            S.pop()
        elif S_weak > B_weak:
            B.pop()
        else:
            B.pop()

    if len(S) == 0 and len(B) == 1:
        print('B')
    elif len(S) == 1 and len(B) == 0:
        print('S')
    else:
        print('C')
