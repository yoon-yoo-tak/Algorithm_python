"""

1326 폴짝폴짝

"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())

def bfs(a, b, bridge, N):
    q = deque()
    q.append(a-1)
    check = [-1]*N
    check[a-1] = 0
    while q:
        node = q.popleft()
        for n in range(node, N, bridge[node]):
            if check[n] == -1:
                q.append(n)
                check[n] = check[node] + 1
                if n == b-1:
                    return check[n]
        for n in range(node, -1, -bridge[node]):
            if check[n] == -1:
                q.append(n)
                check[n] = check[node] + 1
                if n == b-1:
                    return check[n]
    return -1

print(bfs(a, b, bridge, N))