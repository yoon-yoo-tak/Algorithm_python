"""

"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

monster_num = {}
monster_name = {}
for i in range(1, n + 1):
    name = input().strip()
    monster_num[i] = name
    monster_name[name] = i

for _ in range(m):
    x = input().strip()
    if x.isdigit():
        print(monster_num[int(x)])
    else:
        print(monster_name[x])