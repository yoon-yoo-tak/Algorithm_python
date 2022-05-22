import sys

input = sys.stdin.readline

dir = ['N', 'W', 'E', 'S']
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
start, end = 0, 0
n = int(input())
for _ in range(n):
    a, b = input().split()
    for i in range(int(b)):
        start += dx[dir.index(a)]
        end += dy[dir.index(a)]

print(end, start)