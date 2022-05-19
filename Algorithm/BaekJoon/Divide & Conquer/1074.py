"""
1074 Z

"""

import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

ans = 0

while N != 0:
    N -= 1
    two_n = 2 ** N
    if r < two_n and c < two_n:
        ans += two_n * two_n * 0
    elif r < two_n and c >= two_n:
        ans += two_n * two_n * 1
        c -= two_n
    elif r >= two_n and c < two_n:
        ans += two_n * two_n * 2
        r -= two_n
    else:
        ans += two_n * two_n * 3
        r -= two_n
        c -= two_n

print(ans)
