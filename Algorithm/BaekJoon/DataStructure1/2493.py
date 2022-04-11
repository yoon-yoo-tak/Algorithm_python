"""
2493 탑

1. 아이디어
2. 시간복잡도
3. 자료구조
"""
import sys
input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))
stack = []
ans = []

for i in range(n):
    while stack:
        if stack[-1][1] > ls[i]:
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i, ls[i]])
print(*ans)