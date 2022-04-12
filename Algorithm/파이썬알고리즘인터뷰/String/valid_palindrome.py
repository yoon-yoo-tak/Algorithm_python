"""
리트코드 125 유효한 팰린드롬
"""

import sys
from collections import deque
import re
input = sys.stdin.readline

"""
내 풀이
"""
s = input().strip()
temp = ''
for i in s:
    if i.isalpha() or i.isdigit():
        temp += i
temp = temp.lower()
if temp == temp[::-1]:
    print('true')
else:
    print('false')


"""
책 풀이 1 (리스트)
"""
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

"""
책풀이 2 (데크활용)
"""

def isPalindrome(self, s: str) -> bool:
    strs: deque = deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

"""
책풀이 3 (슬라이싱)
"""
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1]  # 슬라이싱