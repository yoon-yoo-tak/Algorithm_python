"""
k개중에 1개를 n번 뽑기
"""
import sys

input = sys.stdin.readline

k, n = map(int, input().split())
sel = [0] * n

def rec(m):
    if m == n:
        print(*sel)
        return
    for i in range(1, k + 1):
        sel[m] = i
        rec(m + 1)
        sel[m] = 0

rec(0)