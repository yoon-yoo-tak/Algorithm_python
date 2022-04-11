"""
후위 표기식2

스택
"""

import sys

input = sys.stdin.readline
n = int(input())
s = input().strip()
alpha = [0] * n
for i in range(n):
    alpha[i] = int(input())

stack = []

for i in s:
    if 'A' <= i <= 'Z':
        stack.append(alpha[ord(i) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()

        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(a / b)

print('%.2f'%stack[0])

