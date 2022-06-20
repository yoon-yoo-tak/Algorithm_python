"""
n개의 점 중 m개 고르기

n 개의 점 중 m개를 뽑는다.
m개중에 2개를 뽑아서 ? 거리를 구하고? 그 중에 최대인거리 저장 > dfs로 해보려 했으나 그냥 완탐으로 해도 될듯
모든 경우에 대해 최대거리를 저장하고?
그중에 최솟값 출력하기.
dist = root( (x1 - x2) ** 2  + (y1 - y2) **2 )
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dots = []
distances = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append([x, y])


# 거리계산해주는 함수
def calc():
    temp = -1
    for i in range(len(selected)):
        for j in range(i + 1, len(selected)):
            temp = max(((selected[i][0] - selected[j][0]) ** 2) + ((selected[i][1] - selected[j][1]) ** 2), temp)
    return temp


# 1. n개의 점 중에 m개를 뽑자.
selected = []
ans = int(1e10)
def rec(k, cnt):
    global ans
    if k == n: # n 개 중에
        if cnt == m: # m 개를 뽑았다!
            ans = min(ans, calc())
    else:
        selected.append(dots[k])
        rec(k + 1, cnt + 1)
        selected.pop()

        rec(k + 1, cnt)

rec(0, 0) # 뽑아줘~
print(ans)