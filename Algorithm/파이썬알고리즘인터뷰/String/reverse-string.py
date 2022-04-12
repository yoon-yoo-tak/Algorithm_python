"""
리트코드 344 Reverse String
"""
import sys
input = sys.stdin.readline

# 내 풀이
def reverseString(self, s: List[str]) -> None:
    s.reverse()

# 책 풀이 1(투포인터)
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 책 풀이 2(reverse)
def reverseString(self, s: List[str]) -> None:
    s.reverse()