"""
1차원 윷놀이
"""
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
turn = list(map(int, input().split()))
horse = [0] * (k + 1)
ans = 0
def rec(x):
    global ans
    if x == n:
        temp = 0
        for i in horse:
            if i >= m - 1:
                temp += 1
        ans = max(ans, temp)
    else:
        for i in range(1, k + 1):
            horse[i] += turn[x]
            rec(x + 1)
            horse[i] -= turn[x]

rec(0)
print(ans)