"""

16457 단풍잎 이야기

"""
import sys
from itertools import permutations
input = sys.stdin.readline

n, m, k = map(int, input().split())
quest = [tuple(map(int, input().split())) for _ in range(m)]
compo = [0 for _ in range(n)]
answer = 0

def rec(prev, idx):
    if idx == n:
        tmp = set(compo)
        cnt = 0
        for qu in quest:
            for q in qu:
                if q not in tmp:
                    break
            else:
                cnt += 1
        global answer
        if cnt > answer:
            answer = cnt
        return
    for i in range(prev + 1, 2*n + 1):
        compo[idx] = i
        rec(i, idx + 1)

rec(0, 0)
print(answer)