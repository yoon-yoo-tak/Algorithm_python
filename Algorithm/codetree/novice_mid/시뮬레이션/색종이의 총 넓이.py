"""


"""

import sys

input = sys.stdin.readline

OFFSET = 100
MAX_R = 200

# 변수 선언 및 입력
n = int(input())
rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for x1, y1 in rects:
    # x2, y2를 구합니다.
    x2, y2 = x1 + 8, y1 + 8

    # OFFSET을 더해줍니다.
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    # 직사각형을 칠해줍니다.
    # 격자 단위로 진행하는 문제이므로
    # x2, y2에 등호가 들어가지 않음에 유의합니다.
    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] = 1

# 직사각형 넓이의 총 합을 구합니다.
area = 0
for x in range(0, MAX_R + 1):
    for y in range(0, MAX_R + 1):
        if checked[x][y]:
            area += 1

print(area)