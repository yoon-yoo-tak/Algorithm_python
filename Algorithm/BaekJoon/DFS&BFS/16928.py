"""

16928 뱀과 사다리 게임

"""
import sys
from collections import deque
input = sys.stdin.readline

# n = 사다리 갯수, m = 뱀 갯수
n, m = map(int, input().split())

a = [0] * 101
visit = [False] * 101

snake = dict()
ladder = dict()
for _ in range(n):
    i, j = map(int, input().split())
    ladder[i] = j
for _ in range(m):
    i, j = map(int, input().split())
    snake[i] = j

def bfs():
    q = deque([1])
    visit[1] = True
    while q:
        start = q.popleft()
        for next in range(1, 7):
            next_step = start + next
            if 0 < next_step <= 100 and not visit[next_step]:
                if next_step in ladder.keys():
                    next_step = ladder[next_step]
                if next_step in snake.keys():
                    next_step = snake[next_step]

                if not visit[next_step]:
                    q.append(next_step)
                    visit[next_step] = True
                    a[next_step] = a[start] + 1
bfs()

print(a[100])
