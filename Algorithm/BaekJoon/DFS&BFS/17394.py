"""
17394 핑거 스냅

"""

import sys, math
from collections import deque
input = sys.stdin.readline

ls = [True] * 100001
def make_prime():  # a, b 사이에 소수가 존재하는지

    # 에라토스 테네스의 체
    for i in range(2, int(math.sqrt(100000)) + 1):
        if ls[i]:  # i가 소수인 경우
            #  i를 제외한 모든 i의 배수를 지우기
            j = 2
            while i * j <= 100000:
                ls[i * j] = False
                j += 1
make_prime()
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if not ls[a:b + 1].count(True):
        print(-1)
        continue
    dist = [-1] * 1000001
    q = deque()
    q.append(n)
    dist[n] = 0
    while q:
        x = q.popleft()
        if a <= x <= b and ls[x]:
            print(dist[x])
            break
        for nx in (x // 3, x // 2, x + 1, x - 1):
            if nx < 0 or nx > 1000000:
                continue
            if dist[nx] != -1:
                continue
            q.append(nx)
            dist[nx] = dist[x] + 1




