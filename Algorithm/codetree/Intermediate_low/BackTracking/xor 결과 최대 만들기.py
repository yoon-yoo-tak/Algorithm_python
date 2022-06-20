"""
xor 결과 최대 만들기
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
selected = []
ans = 0


def rec(k, cnt):
    global ans
    if k == n:
        temp = 0
        if cnt == m:
            for i in selected:
                temp ^= i
        ans = max(ans, temp)
        return
    else:
        selected.append(nums[k])
        rec(k + 1, cnt + 1)
        selected.pop()
        rec(k + 1, cnt)


rec(0, 0)
print(ans)
