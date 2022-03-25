"""

11060 점프 점프

"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0)
    sys.exit()
visit = [0] * n


q = deque()
q.append((0, a[0]))

while q:
    now, jump = q.popleft()
    for i in range(1, jump + 1):
        if now + i >= n or visit[now + i]:
            continue
        visit[now + i] = visit[now] + 1
        q.append((now + i,a[now + i]))

print(visit[-1] if visit[-1] else -1)
