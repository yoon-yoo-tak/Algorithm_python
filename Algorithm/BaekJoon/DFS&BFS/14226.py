"""
14226 이모티콘
"""
import sys
from collections import deque
input = sys.stdin.readline


s = int(input())
q = deque()
q.append((1, 0))
dist = dict()
dist[(1, 0)] = 0

while q:
    now, copy = q.popleft()
    if now == s:
        print(dist[(now, copy)])
        break
    if (now, now) not in dist.keys():
        dist[(now, now)] = dist[(now, copy)] + 1
        q.append((now, now))
    if (now + copy, copy) not in dist.keys():
        dist[(now + copy, copy)] = dist[(now, copy)] + 1
        q.append((now + copy, copy))
    if (now - 1, copy) not in dist.keys():
        dist[(now - 1, copy)] = dist[(now, copy)] + 1
        q.append((now - 1, copy))