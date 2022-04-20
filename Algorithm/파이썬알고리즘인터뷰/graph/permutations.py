"""
리트코드 46 순열
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        prev_elements = []
        result = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result

