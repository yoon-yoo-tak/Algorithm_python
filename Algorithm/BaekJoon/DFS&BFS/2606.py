"""

2606 바이러스

1번이 감염되었을때 감염되는 컴퓨터 수 출력

"""
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

def dfs(v):
    visit[v] = True
    for i in a[v]:
        if not visit[i]:
            dfs(i)
            visit[i] = True

dfs(1)
print(visit.count(True)-1)