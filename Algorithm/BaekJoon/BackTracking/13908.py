"""
13908 비밀번호
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ls = [] if m == 0 else list(map(int, input().split()))
selected = []
cnt = 0
def check():
    for i in ls:
        if i not in selected:
            return False
    return True


def rec(k):
    global cnt
    if k == n:
        if check():
            cnt += 1
    else:
        for i in range(10):
            selected.append(i)
            rec(k + 1)
            selected.pop()

rec(0)
print(cnt)