"""
1484
"""
import sys

input = sys.stdin.readline

g = int(input())
l, r = 1, 1
ans = []

while True:
    differ = r ** 2 - l ** 2
    if r - l == 1 and differ > g: # 불가능
        break
    if differ > g:
        l += 1
    elif differ < g:
        r += 1
    else:
        ans.append(r)
        r += 1
if ans:
    for i in ans:
        print(i)
else:
    print(-1)