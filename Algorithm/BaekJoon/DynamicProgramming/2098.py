"""
2098 외판원 순회
"""
import sys
input = sys.stdin.readline
INF = int(1e9)


def tsp(last, visited):
    if visited == (1 << n) - 1:
        return board[last][0] or INF
    if cache[last][visited] is not None:
        return cache[last][visited]
    temp = INF
    for i in range(n):
        if visited & (1 << i) == 0 and board[last][i] != 0:
            temp = min(temp, tsp(i, visited | (1 << i)) + board[last][i])
    cache[last][visited] = temp
    return temp


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cache = [[None] * (1 << n) for _ in range(n)]
index = 1
print(tsp(0, 1 << 0))
