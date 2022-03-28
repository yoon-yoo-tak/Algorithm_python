"""

1729 오큰수

"""
import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and ls[stack[-1]] < ls[i]:
        answer[stack.pop()] = ls[i]
    stack.append(i)

print(*answer)
