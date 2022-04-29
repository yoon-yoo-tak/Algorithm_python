"""
15270 친구 팰린드롬
"""

import sys

input = sys.stdin.readline

def find(index, count):
    global max_val
    if index >= m:
        max_val = max(max_val, count)
        return
    if visit[friends[index][0]] or visit[friends[index][1]]:
        find(index + 1, count)
    else:
        visit[friends[index][0]] = True
        visit[friends[index][1]] = True

        find(index + 1, count + 1)

        visit[friends[index][0]] = False
        visit[friends[index][1]] = False

        find(index + 1, count)

n, m = map(int, input().split())
friends = [[0, 0] for _ in range(m)]
for i in range(m):
    a, b = map(int, input().split())
    friends[i][0] = a
    friends[i][1] = b

max_val = 0
visit = [False] * (n + 1)
find(0, 0)
max_val *= 2
if max_val < n:
    max_val += 1
print(max_val)


