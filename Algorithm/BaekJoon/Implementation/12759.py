"""
12759 틱! 택! 토!

1. 아이디어
2. 시간복잡도
3. 자료구조
"""

import sys

input = sys.stdin.readline


def check():
    for i in range(3):
        if graph[i][0] == graph[i][1] == graph[i][2] and graph[i][0] != 0:
            return True
        if graph[0][i] == graph[1][i] == graph[2][i] and graph[0][i] != 0:
            return True
    if graph[0][0] == graph[1][1] == graph[2][2] and graph[0][0] != 0:
        return True
    if graph[0][2] == graph[1][1] == graph[2][0] and graph[1][1] != 0:
        return True
    return False


n = int(input())
graph = [[0] * 3 for _ in range(3)]
i = 1
while True:
    a, b = map(int, input().split())
    if n == 1:
        if i % 2 == 1:
            num = 1
        else:
            num = 2
    if n == 2:
        if i % 2 == 1:
            num = 2
        else:
            num = 1
    graph[a - 1][b - 1] = num
    if check():
        print(num)
        break
    i += 1

