"""
열 중에 한곳에 떨어뜨린다.
공 바로 위 혹은 바닥까지 떨어짐.
가로 연속그룹, 세로연속그룹 > 크기가 x인 그룹에 x가 있으면 그 공은 없어진다. 조건 만족하면 모두 동시에 없어진다.
그리고 공이 떨어진다.

"""
import sys
from copy import deepcopy
input = sys.stdin.readline

def rotate_90(a): # 배열 돌리기
    row_length = len(a)
    col_length = len(a[0])

    res = [[0] * row_length for _ in range(col_length)]
    for r in range(row_length):
        for c in range(col_length):
            res[c][row_length - 1 - r] = a[r][c]
    return  res


def pushing(ls): # 값땡기기 >>
    last = len(ls)
    for i in range(len(ls) - 1, -1, -1):
        if ls[i] == 0:
            continue
        last -= 1
        ls[last] = ls[i]
    for i in range(last - 1, -1, -1):
        ls[i] = 0
    return ls

def gravity(ls: list):
    for i in range(7):
        temp = pushing(ls[i])
        ls[i] = temp

def check_and_bomb(ls: list):
    # 가로 체크
    for i in range(7):
        garo = 0
        saero = 0
        temp = []
        temp1 = []
        for j in range(7):
            if ls[i][j] == 0:
                garo = 0
                continue
            else:
                garo += 1
                temp.append([i, j])
            if ls[j][i] == 0:
                saero = 0
                continue
            else:
                saero += 1
                temp1.append([j, i])
        for x, y in temp:
            if ls[x][y] == garo:
                ls[x][y] = 0
        for x, y in temp1:
            if ls[x][y] == saero:
                ls[x][y] = 0


def flag(ls: list):
    for i in range(7):
        garo = 0
        saero = 0
        temp = []
        temp1 = []
        for j in range(7):
            if ls[i][j] == 0:
                garo = 0
                continue
            else:
                garo += 1
                temp.append([i, j])
            if ls[j][i] == 0:
                saero = 0
                continue
            else:
                saero += 1
                temp1.append([j, i])
        for x, y in temp:
            if ls[x][y] == garo:
                return True
        for x, y in temp1:
            if ls[x][y] == saero:
                return True
    return False

def calc(ls: list):
    cnt = 0
    for i in range(7):
        for j in range(7):
            if ls[i][j] != 0:
                cnt += 1
    return cnt


board = [list(map(int ,input().split())) for _ in range(7)]
ball = int(input())
ans = 49


for i in range(7):
    temp = deepcopy(board)
    for _ in range(3):  # 귀찮으니까 돌려재껴
        temp = rotate_90(temp)
    temp[i][0] = ball  # 공을 넣어
    gravity(temp)  # 공이 떨어져
    while flag(temp): # 터트릴수 있으면
        check_and_bomb(temp) # 터트리고
        gravity(temp) # 중력
    ans = min(ans, calc(temp))


print(ans)