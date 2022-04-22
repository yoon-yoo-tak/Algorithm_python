"""
21771 가희야 거기서 자는거 아니야
"""
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
rg, cg, rp, cp = map(int, input().split())
c_area = rp * cp
ls = [list(input().strip()) for _ in range(r)]
cnt = 0
for i in ls:
    cnt += i.count('P')

print(1 if cnt != c_area else 0)
