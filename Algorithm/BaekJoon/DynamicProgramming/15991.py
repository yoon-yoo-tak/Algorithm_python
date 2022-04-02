"""
15991 1, 2, 3 더하기 6
"""
import sys

si = sys.stdin.readline

Q = int(si())
dy = [0] * (100005)

dy[0] = 1
for i in range(1, 100001):
    dy[i] = dy[i - 1]
    if i >= 2: dy[i] += dy[i - 2]
    if i >= 3: dy[i] += dy[i - 3]
    dy[i] %= 1000000009

for _ in range(Q):
    x = int(si())
    res = 0

    for mid in range(1, 4):
        if x - mid >= 0 and (x - mid) % 2 == 0:
            res += dy[(x - mid) // 2]

    if x % 2 == 0:
        res += dy[x // 2]

    res %= 1000000009

    print(res)
