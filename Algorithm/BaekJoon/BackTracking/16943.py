"""
16943 숫자 재배치
"""
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
ls = [i for i in str(a)]
n = len(ls)
visited = [False] * n
selected = []
ans = -1

def rec(k):
    global ans
    if k == n:
        if selected[0] == '0':
            return
        else:
            num = int(''.join(selected))
            if num < b:
                ans = max(ans, num)
    else:
        for i in range(n):
            if not visited[i]:
                selected.append(ls[i])
                visited[i] = True
                rec(k + 1)
                selected.pop()
                visited[i] = False

rec(0)
print(ans)