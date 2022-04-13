"""
리트코드 234 팰린드롬 연결 리스트
"""

import sys
from typing import List, Deque
from collections import deque

input = sys.stdin.readline

# 리스트로 변환해서 풀이
class Solution:
    def isPalindrome(self, head) -> bool:
        q: List = []

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

# 데크를 이용한 최적화
class Solution:
    def isPalindrome(self, head) -> bool:
        q : Deque = deque()

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next


        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

# 런너를 이용한 풀이
class Solution:
    def isPalindrome(self, head) -> bool:
        rev = None
        slow = fast = head

        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev