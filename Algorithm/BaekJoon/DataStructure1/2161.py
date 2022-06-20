"""

"""
import sys
from collections import deque
input = sys.stdin.readline

ls = deque([i for i in range(1, int(input()) + 1)])
ans = []
while len(ls) > 1:
    ans.append(ls.popleft())
    ls.append(ls.popleft())
ans.append(ls.pop())
print(*ans)
