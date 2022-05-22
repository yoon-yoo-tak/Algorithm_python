"""
1963 소수경로
"""
import sys, math
from collections import deque
input = sys.stdin.readline


def set_prime(n):
    ls = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if ls[i]:
            j = 2
            while i * j <= n:
                ls[i * j] = False
                j += 1
    return ls


prime_nums = set_prime(10000)


def bfs(x, tar):
    q = deque()
    q.append(x)
    dist[x] = 0
    while q:
        x = q.popleft()
        strX = str(x)
        if x == tar:
            print(dist[x])
            return
        for i in range(4):
            for j in range(10):
                temp = int(strX[:i] + str(j) + strX[i + 1:])

                if dist[temp] == -1 and prime_nums[temp] and 1000 <= temp <= 9999:
                    q.append(temp)
                    dist[temp] = dist[x] + 1



for _ in range(int(input())):
    start, target = map(int, input().split())
    dist = [-1] * 10000
    bfs(start, target)
