"""
12933 오리

"""

import sys

input = sys.stdin.readline
duck = 'quack'
s = input().strip()
ans = ''
if s[0] != 'q':
    print(-1)
for j in duck:
    for i in range(len(s)):
        if s[i] == j:
            ans += s[i]

