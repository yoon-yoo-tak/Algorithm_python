"""
2차원 바람

"""
import sys

input = sys.stdin.readline

def rotate_square(x1, y1, x2, y2):
    tmp = [[-1] * M for _ in range(N)] # 새로운 배열 생성

    for i in range(y2, y1, -1): # 위에 회전
        tmp[x1][i] = data[x1][i - 1]

    for i in range(x2,x1,-1):
        tmp[i][y2] = data[i-1][y2]

    for i in range(y1,y2):
        tmp[x2][i] = data[x2][i+1]

    for i in range(x1,x2):
        tmp[i][y1] = data[i+1][y1]


    for i in range(N): # 배열 복사
        for j in range(M):
            if tmp[i][j] != -1:
                data[i][j] = tmp[i][j]

def convert_avg(x1,y1,x2,y2):
    global data

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    tmp = [[-1] * M for _ in range(N)]

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            tot = data[i][j]
            cnt = 1
            for d in range(4):
                nx,ny = i + dx[d], j + dy[d]

                if 0 <= nx < N and 0 <= ny < M:
                    tot += data[nx][ny]
                    cnt += 1

            tmp[i][j] = tot // cnt

    for i in range(N): # 배열 복사
        for j in range(M):
            if tmp[i][j] != -1:
                data[i][j] = tmp[i][j]

N, M, Q = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
command = []

for _ in range(Q):
    a1, a2, a3, a4 = map(int, input().split())
    command.append((a1 - 1, a2 - 1, a3 - 1, a4 - 1))

for cmd in command:
    xx1, xy1, yx2, yy2 = cmd

    rotate_square(xx1, xy1, yx2, yy2)
    convert_avg(xx1,xy1,yx2,yy2)

for i in range(N):
    for j in range(M):
        print(data[i][j], end= ' ')
    print()