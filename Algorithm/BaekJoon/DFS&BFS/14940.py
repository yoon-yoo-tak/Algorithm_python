# 14940 쉬운 최단거리
from sys import stdin
from collections import deque
n,m = map(int, stdin.readline().split())
area = [list(map(int,stdin.readline().split())) for _ in range(m)]
visit = [[False]*m for _ in range(n)]
re = [[-1]*m for _ in range(n)]
q = deque()
db = [0,1,0,-1] # 하 우 상 좌
da = [1,0,-1,0]
def go():
    while q:
        a,b = map(int,q.popleft())
        for i in range(4):
            nb = b+db[i]
            na = a+da[i]
            if (0<=na <n) and (0<=nb <m) and not visit[na][nb] and area[na][nb] == 1:
                visit[na][nb] = True
                q.append([na,nb])
                re[na][nb] = re[a][b] +1            

for i in range(n):
    for j in range(m):
        if area[i][j] == 2:
            q.append([i,j])
            visit[i][j] = True
            re[i][j] = 0
        elif area[i][j] == 0:
            re[i][j] = 0

go()
            
for i in range(n):
    print(" ".join(map(str,re[i])))