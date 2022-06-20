"""
단순한 동전 챙기기

동전갯수중에 3개 뽑기(오름차순)
뽑아졌을 때,
시작점 -  뽑은거 1 - 뽑은거 2 - 뽑은거 3 - 도착점 의 거리를 구한다
최소거리 저장
"""
import sys

input = sys.stdin.readline

n = int(input())
board = [list(input().strip()) for _ in range(n)]
selected = []
num_cnt = 0
dist = int(1e9)
nums = []
coord = {}
for i in range(n):
    for j in range(n):
        if board[i][j].isdigit():
            num_cnt += 1
            coord[int(board[i][j])] = [i, j]
            nums.append(int(board[i][j]))
        if board[i][j] == 'S':
            start_x, start_y = i, j
        if board[i][j] == 'E':
            end_x, end_y = i, j
nums.sort()
if num_cnt <= 2:
    print(-1)
    sys.exit()

def calc():
    global start_y, start_x, end_x, end_y
    total = abs(start_x - coord[selected[0]][0]) + abs(start_y - coord[selected[0]][1])
    total += abs(coord[selected[0]][0] - coord[selected[1]][0]) + abs(coord[selected[0]][1] - coord[selected[1]][1])
    total += abs(coord[selected[1]][0] - coord[selected[2]][0]) + abs(coord[selected[1]][1] - coord[selected[2]][1])
    total += abs(coord[selected[2]][0] - end_x) + abs(coord[selected[2]][1] - end_y)
    return total


def rec(k, cnt):
    global dist
    if k == num_cnt:
        if cnt == 3:
            dist = min(dist, calc())
    else:
        selected.append(nums[k])
        rec(k + 1, cnt + 1)
        selected.pop()

        rec(k + 1, cnt)

rec(0, 0)
print(dist)
