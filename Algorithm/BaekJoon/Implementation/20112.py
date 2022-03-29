"""

20112 사토르 마방진

"""
import sys
input = sys.stdin.readline

n = int(input())
ls = [input().strip() for _ in range(n)]
tmp = []

for i in range(n):
    s = ''
    for j in range(n):
        s += ls[j][i]
    tmp.append(s)

print('YES' if tmp == ls else 'NO')
