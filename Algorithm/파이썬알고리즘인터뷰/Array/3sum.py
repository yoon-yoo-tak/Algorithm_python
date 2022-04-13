"""
리트코드 15 세 수의 합

"""

import sys

input = sys.stdin.readline

nums = sorted(map(int, input().split()))
ans = []
for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    l, r = i + 1, len(nums) - 1
    while l < r:
        if nums[i] + nums[l] + nums[r] < 0:
            l += 1
        elif nums[i] + nums[l] + nums[r] > 0:
            r -= 1
        else:
            ans.append([nums[i], nums[l], nums[r]])

            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            l += 1
            r -= 1

print(ans)