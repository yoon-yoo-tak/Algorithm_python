"""

15558 점프 게임

"""

import sys
from collections import deque
input = sys.stdin.readline()

n, k = map(int, input().split())
line = [input().strip() for _ in range(2)]
q = deque([0, 0])
visit = [[False] * n for _ in range(2)]
time = -1
flag = False

while q:
    for _ in range(len(q)):
        d, idx = q.popleft()
        if idx + 1 >= n or idx + k >= n:
            flag = True
            break
        if int(line[d][idx + 1]) and not visit[d][idx + 1]:
            q.append((d, idx + 1))
            visit[d][idx + 1] = True
        if idx - 1 > time + 1 and int(line[d][idx - 1]) and not visit[d][idx + 1]:
            q.append((d, idx - 1))
            visit[d][idx - 1] = True
        if int(line[(d + 1) % 2][idx + k]) and not visit[0][idx + k]:
            q.append(((d + 1) % 2, idx + k))
            visit[(d + 1) % 2][idx + k] = True
    time += 1

print(1 if flag else 0)


