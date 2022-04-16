"""
10912 외로운문자
"""
t = int(input())

for tt in range(1, t + 1):
    s = sorted(input())
    stack = []

    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if stack:
        print(f'#{tt} {"".join(stack)}')
    else:
        print(f'#{tt} Good')
