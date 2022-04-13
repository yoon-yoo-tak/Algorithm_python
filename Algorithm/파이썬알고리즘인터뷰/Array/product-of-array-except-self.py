"""
리트코드 238 자신을 제외한 배열의 곱

"""

import sys
from typing import List
input = sys.stdin.readline


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p *= nums[i]
        print(out)
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= p
            p *= nums[i]
            print(out[i])
        return out

