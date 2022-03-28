"""

1325 소트 게임

"""
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
L = list(input().split())


visit_set = set("".join(L))
q = deque([["".join(L), 0]])

ans = -1


while(q):
    a, cnt = q.popleft()
    tmp = list(a)

    if tmp == sorted(tmp):
        ans = cnt
        break

    isFirst = False

    for i in range(N - K + 1):
        n_ls = list(tmp)
        target_ls = n_ls[i:i+K]
        target_ls.reverse()

        for j in range(K):
            n_ls[i+j] = target_ls[j]
        new_num = "".join(n_ls)

        if new_num not in visit_set:
            visit_set.add(new_num)
            q.append([new_num, cnt+1])

print(ans)