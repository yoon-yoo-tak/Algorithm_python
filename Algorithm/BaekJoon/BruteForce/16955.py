"""

"""

import sys
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(10)]
dxy = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 아래쪽, 오른쪽, 대각선
def in_range(x, y):
    return 0 <= x < 10 and 0 <= y < 10

def check() -> bool:
    for i in range(10):  # 모든 점을 확인하면서
        for j in range(10):
            if board[i][j] == 'X':  # O이면
                for dx, dy in dxy:  # 가로, 세로, 대각선 확인해본다.
                    nx, ny = i + dx, j + dy  # 현재 방향으로 쭉 가본다.
                    cnt = 1         # 돌 갯수 카운트 현재 O이니까 1
                    while True:
                        if not in_range(nx, ny) or board[nx][ny] != 'X':  # 범위 벗어나거나, X 가 아니면 break
                            break
                        cnt += 1  # 범위도 안벗어나고 O면 cnt += 1
                        nx, ny = nx + dx, ny + dy  # 다음위치로 이동
                        if cnt == 5:  # cnt 가 5다 > 이길 수 있다 > True 리턴
                            return True
    return False  # True 리턴 못했으면 못이긴다. > False 리턴


for i in range(10):
    for j in range(10):
        if board[i][j] == '.': # . 이면
            board[i][j] = 'X'  # X로 바꿔보고
            if check():        # 검사
                print(1)       # 이길수 있으면 1 출력
                sys.exit()
            board[i][j] = '.'  # 다시 . 으로 돌려놓기
print(0)
