"""
5639 이진 검색 트리
"""
import sys
sys.setrecursionlimit(10005)
input = sys.stdin.readline

ls = []

while True:
    now = input().strip()
    if not now:
        break
    ls.append(int(now))

def rec(l, r):
    if l > r:
        return
    mid = r
    for i in range(l, r + 1):
        if ls[i] > ls[l]:
            mid = i - 1
            break
    rec(l + 1, mid)
    rec(mid + 1, r)
    print(ls[l])

rec(0, len(ls) - 1)

