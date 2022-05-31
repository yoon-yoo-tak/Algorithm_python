"""
n개 중에 m개 뽑기 (조합)
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
selected = [0] * m
sel = []
# 고를지 말지 결정하는 문제
def rec(k, cnt):
    if k == n + 1:
        if cnt == m:
            print(*sel)
        return
    else:
        sel.append(k)
        rec(k + 1, cnt + 1)  # k 번째 고르는 경우 탐색
        sel.pop()
        rec(k + 1, cnt) # k 번째 고르지 않는 경우 탐색



rec(1, 0)