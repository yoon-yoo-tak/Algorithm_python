"""

9019 DSLR

D - 2 * n % 10000
S - (n - 1) % 10000
L - (10 * n + (n //1000)) % 10000
R - (n // 10 + (n % 10) * 1000) % 10000
"""
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    now, target = map(int, input().split())
    q = deque()
    q.append((now, ""))
    visit = [False] * 10000

    while q:
        num, command = q.popleft()
        visit[num] = True
        if num == target:
            print(command)
            break
        new_num = (2 * num) % 10000
        if not visit[new_num]:
            q.append((new_num, command + "D"))
            visit[new_num] = True

        new_num = (num - 1) % 10000
        if not visit[new_num]:
            q.append((new_num, command + "S"))
            visit[new_num] = True

        new_num = (10 * num + (num // 1000)) % 10000
        if not visit[new_num]:
            q.append((new_num, command + "L"))
            visit[new_num] = True

        new_num = (num // 10 + (num % 10) * 1000) % 10000
        if not visit[new_num]:
            q.append((new_num, command + "R"))
            visit[new_num] = True