"""
16935 배열돌리기 3
"""
import sys

input = sys.stdin.readline

def updown(ls):
    ls = ls[::-1]
    return ls

def leftright(ls):
    temp = []
    for i in ls:
        temp.append(i[::-1])
    return temp

def cw_rotate(ls):
    return list(map(list, zip(*reversed([*ls]))))

def ccw_rotate(arr):
    arr = [list(each) for each in reversed(tuple(zip(*arr)))]
    return arr

def five(ls):
    row = len(ls)
    col = len(ls[0])
    temp = [[0] * col for _ in range(row)]
    # 1 > 2
    for i in range(row // 2):
        for j in range(col // 2):
            temp[i][j + (col//2)] = ls[i][j]
    # 2 > 3
    for i in range(row // 2):
        for j in range(col // 2, col):
            temp[i + (row // 2)][j] = ls[i][j]
    # 3 > 4
    for i in range(row // 2, row):
        for j in range(col // 2 , col):
            temp[i][j - (col // 2)] = ls[i][j]
    # 4 > 1
    for i in range(row // 2, row):
        for j in range(col // 2):
            temp[i - (row // 2)][j] = ls[i][j]
    return temp

def six(ls):
    row = len(ls)
    col = len(ls[0])
    half_row = row // 2
    half_col = col // 2
    temp = [[0] * col for _ in range(row)]
    # 1 > 4
    for i in range(half_row):
        for j in range(half_col):
            temp[i + half_row][j] = ls[i][j]
    # 2 > 1
    for i in range(half_row):
        for j in range(half_col, col):
            temp[i][j - half_col] = ls[i][j]
    # 3 > 2
    for i in range(half_row, row):
        for j in range(half_col, col):
            temp[i - half_row][j] = ls[i][j]
    # 4 > 3
    for i in range(half_row, row):
        for j in range(half_col):
            temp[i][j + half_col] = ls[i][j]
    return temp


n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

for i in order:
    if i == 1:
        arr = updown(arr)
    elif i == 2:
        arr = leftright(arr)
    elif i == 3:
        arr = cw_rotate(arr)
    elif i == 4:
        arr = ccw_rotate(arr)
    elif i == 5:
        arr = five(arr)
    elif i == 6:
        arr = six(arr)


for i in arr:
    print(*i)
