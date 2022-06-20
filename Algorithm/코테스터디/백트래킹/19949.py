"""
19949 영재의 시험
같은 수 연속해서 최대 2개까지만.
"""
import sys

input = sys.stdin.readline

ans = list(map(int, input().split()))
selected = [0] * 10
total = 0

def rec(k):
    global total
    if k == 10: # 뭘 할것인가?
        cnt = 0
        for i in range(10):
            if selected[i] == ans[i]:
                cnt += 1
        if cnt >= 5:
            total += 1
    else:
        for i in range(1, 6):
            if k >= 2 and i == selected[k - 1] and i == selected[k - 2]:
                continue
            selected[k] = i
            rec(k + 1)
            selected[k] = 0

rec(0)

print(total)
