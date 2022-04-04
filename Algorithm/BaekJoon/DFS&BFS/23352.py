"""
23352 방탈출

1. 아이디어
 - 모든 칸에서 BFS
2. 시간복잡도
 - O(NM (bfs))
3. 자료구조
"""
import sys
from collections import deque
import copy

def bfs(a,b):
    Mat=copy.deepcopy(mat)
    Visited=copy.deepcopy(visited)

    dx,dy=[-1,1,0,0],[0,0,-1,1]

    queue=deque([(a,b)])
    start = Mat[a][b]
    Mat[a][b]=0

    while queue:
        List = list(queue)
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and Mat[nx][ny]!=0 and Visited[nx][ny]==0:
                Visited[nx][ny]=Visited[x][y]+1
                queue.append((nx,ny))

    end=0
    for i,j in List:
            end=Mat[i][j]
    if end==0:     #시작 방과 끝 방이 동일한 경우
        end=start
    check.append([max(map(max,Visited)),start+end])
    return max(map(max,Visited))

N,M=map(int,sys.stdin.readline().split())

mat=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
check=[]

move=0

for i in range(N):
    for j in range(M):
        if mat[i][j]!=0:
            a=bfs(i,j)
            if move<a:
                move=a
Sum=0

for i,j in check:
    if i==move and j>Sum:
        Sum=j

print(Sum)