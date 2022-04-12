"""
10703 유성

"""

import sys

input = sys.stdin.readline

R, S = map(int, input().split())
meteor = [input() for _ in range(R)]
arr = [['.'] * S for _ in range(R)]

max_meteor = [-3333] * S  # 유성 좌표를 저장 할 리스트
min_ground = [1 << 14] * S  # 땅 좌표를 저장 할 리스트

for x in range(R):
    for y in range(S):
        if meteor[x][y] == 'X':
            max_meteor[y] = max(max_meteor[y], x)  # 현재 유성의 y좌표(열)를 갱신함
        elif meteor[x][y] == '#':
            min_ground[y] = min(min_ground[y], x)  # 현재 땅의 y좌표(열)를 갱신함

move = min((j - i for i, j in zip(max_meteor, min_ground))) - 1  # 최종적으로 가야 할 move 계산

for x in range(R):
    for y in range(S):
        if meteor[x][y] == 'X':
            arr[x + move][y] = 'X'  # 유성을 최종 move만큼 움직인다.
        if meteor[x][y] == '#':
            arr[x][y] = '#'

for i in range(R):  # 결과 출력
    for j in range(S):
        sys.stdout.write(arr[i][j])
    sys.stdout.write('\n')