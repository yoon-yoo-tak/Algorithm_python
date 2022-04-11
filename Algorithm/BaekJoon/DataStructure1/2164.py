"""
2164 카드

"""

import sys
from collections import deque
input = sys.stdin.readline
ls = deque()
for i in range(int(input())):
    ls.append(i + 1)


while len(ls) > 1:
    ls.popleft()
    ls.append(ls.popleft())

print(ls[0])