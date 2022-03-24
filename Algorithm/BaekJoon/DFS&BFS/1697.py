"""

1697 숨바꼭질

k = 0, n = 100000일때 최대치

그래프가 주어지지 않았는데 어떻게 그래프로 생각?
>> 점의 번호를 정점의 번호로 생각하자.
>> 이동을 의미하는 것을 간선으로 생각 => -1, +1, *2 인 점을 향하는 간선 => 2번 정점에서 1,3,4로 갈 수 있다
가장 빨리 동생을 찾는 방법은 최소 개수로 간선 이동하는 방법이다.
O(10^5) < 2억  ==  쌉가능
"""

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

max_val = 100000

dist = [-1] * (max_val + 1)

def bfs(x):
    q = deque([x])
    dist[x] = 0

    def move(y, d):
        if y < 0 or y > max_val or dist[y] != -1:
            return
        dist[y] = d
        q.append(y)

    while q:
        x = q.popleft()
        move(x + 1, dist[x] + 1)
        move(x - 1, dist[x] + 1)
        move(x * 2, dist[x] + 1)

bfs(n)
print(dist[k])
