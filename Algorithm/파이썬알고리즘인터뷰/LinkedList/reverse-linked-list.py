"""
리트코드 206 역순 연결 리스트
"""

import sys
from typing import Optional
input = sys.stdin.readline


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 재귀 구조로 뒤집기
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

# 반복 구조로 뒤집기
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev