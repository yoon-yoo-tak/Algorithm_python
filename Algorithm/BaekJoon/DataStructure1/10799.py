"""
10799 쇠막대기


"""

import sys

input = sys.stdin.readline
iron = list(input().strip())
ans = 0
ls = []

for i in range(len(iron)):
    if iron[i] == '(':
        ls.append('(')

    else:
        if iron[i-1] == '(':
            ls.pop()
            ans += len(ls)

        else:
            ls.pop()
            ans += 1

print(ans)