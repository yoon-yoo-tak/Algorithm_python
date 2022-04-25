"""
2331 반복수열
"""

import sys

input = sys.stdin.readline

a, p = map(int, input().split())
nums = [a]
while True:
    tmp = 0
    for i in str(nums[-1]):
        tmp += int(i) ** p

    if tmp in nums:
        break
    nums.append(tmp)
print(nums.index(tmp))
