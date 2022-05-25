"""
[S/W 문제해결 응용] 2일차 - 최대 상금
"""
import sys

input = sys.stdin.readline
def dfs(idx, cnt):
    global answer
    if cnt == int(target):
        answer = max(int("".join(nums)), answer)
        return
    for now in range(idx, n):
        for max_idx in range(now + 1, n):
            if nums[now] <= nums[max_idx]:
                nums[now], nums[max_idx] = nums[max_idx], nums[now]
                dfs(now, cnt + 1)
                nums[now], nums[max_idx] = nums[max_idx], nums[now]
    if not answer and cnt < int(target):
        rotate = (int(target) - cnt) % 2
        if rotate:
            nums[-1], nums[-2] = nums[-2], nums[-1]
        dfs(idx, int(target))


for test in range(1, int(input()) + 1):
    nums, target = input().split()
    n = len(nums)
    nums = list(nums)
    answer = 0
    dfs(0, 0)
    print(f'#{test} {answer}')