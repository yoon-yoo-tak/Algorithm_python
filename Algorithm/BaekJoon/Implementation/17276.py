"""
17276 배열 돌리기
"""
import sys
input = sys.stdin.readline


def save_value(x: list):
    temp = [[] for _ in range(4)]
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                temp[0].append(x[i][j])  # 우하향대각선
            if i + j == len(x) - 1:
                temp[1].append(x[i][j])  # 좌하향대각선
    for i in range(len(x)):
        temp[2].append(x[len(x) // 2][i])  # 중앙 가로
        temp[3].append(x[i][len(x) // 2])  # 중앙 세로
    return temp


def clockWise_rotate(x: list):
    temp = save_value(x)
    for i in range(len(x)):
        for j in range(len(x)):
            if i + j == n - 1:
                x[i][j] = temp[3][i]
            if i == j:
                x[i][j] = temp[2][i]
    temp[1].reverse()
    for i in range(len(x)):
        x[len(x) // 2][i] = temp[1][i]
        x[i][len(x) // 2] = temp[0][i]
    return x


def counterClockWise_rotate(x: list):
    temp = save_value(x)
    temp[2].reverse()
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                x[i][j] = temp[2][i]
            if i == j:
                x[i][j] = temp[3][i]

    for i in range(n):
        x[len(x) // 2][i] = temp[0][i]
        x[i][len(x) // 2] = temp[1][i]
    return x

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    ls = [list(map(int, input().split())) for _ in range(n)]
    total = d // 45
    if total < 0:
        for i in range(abs(total)):
            ls = counterClockWise_rotate(ls)
    else:
        for i in range(total):
            ls = clockWise_rotate(ls)

    for i in ls:
        print(*i)





