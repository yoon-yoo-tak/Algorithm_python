"""
리트코드 121 주식을 사고팔기 가장 좋은 시점
"""

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit