"""
4가지 연산을 이용하여 1 만들기
"""
import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
dist = [-1] * (n * 2)
q = deque()
q.append(n)
dist[n] = 0

while q:
    x = q.popleft()
    if x == 1:
        break
    if dist[x - 1] == -1:
        q.append(x - 1)
        dist[x - 1] = dist[x] + 1
    if dist[x + 1] == -1:
        q.append(x + 1)
        dist[x + 1] = dist[x] + 1
    if x % 2 == 0 and dist[x // 2] == -1:
        q.append(x // 2)
        dist[x // 2] = dist[x] + 1
    if x % 3 == 0 and dist[x // 3] == -1:
        q.append(x // 3)
        dist[x // 3] = dist[x] + 1


print(dist[1])
