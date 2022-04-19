"""
13300 방 배정
"""

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
man = [0] * 7
woman = [0] * 7
for _ in range(n):
    s, y = map(int, input().split())
    if s == 1:
        man[y] += 1
    else:
        woman[y] += 1
cnt = 0
for i in man[1:]:
    if 0 < i <= k:
        cnt += 1
    elif i > k:
        if i % k == 0:
            cnt += i // k
        else:
            cnt += i // k + 1
for i in woman[1:]:
    if 0 < i <= k:
        cnt += 1
    elif i > k:
        if i % k == 0:
            cnt += i // k
        else:
            cnt += i // k + 1
print(cnt)