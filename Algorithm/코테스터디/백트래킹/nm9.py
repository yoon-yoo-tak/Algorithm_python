"""
nm9
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ls = sorted(map(int, input().split()))
selected = []
used = [False] * (n + 1)
def rec(k):
    if k == m:
        print(*selected)
    else:
        remember = 0  # 중복 처리용
        for i in range(n):
            if used[i] or ls[i] == remember:
                continue
            selected.append(ls[i])
            remember = ls[i]
            used[i] = True
            rec(k + 1)
            selected.pop()
            used[i] = False

rec(0)
