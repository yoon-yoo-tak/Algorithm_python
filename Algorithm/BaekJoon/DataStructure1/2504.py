"""
2504 괄호의 값

1. 아이디어
2. 시간복잡도
3. 자료구조
"""
import sys
input = sys.stdin.readline
ls = list(input().strip())

stack = []
answer = 0
tmp = 1

for i in range(len(ls)):

    if ls[i] == "(":
        stack.append(ls[i])
        tmp *= 2

    elif ls[i] == "[":
        stack.append(ls[i])
        tmp *= 3

    elif ls[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if ls[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if ls[i-1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)