"""

"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

selected = []
def rec(k, cnt):  # k 가 n번까지 왔고 cnt 가 m 개를 뽑아주는 ~~
    if k == n + 1:
        if cnt == m:
            print(*selected)
        return
    else:
        selected.append(k)
        rec(k + 1, cnt + 1)  # k 를 뽑겠다. 1
        selected.pop()
        rec(k + 1, cnt)  # k 를 뽑지않고? 그 다음걸 보겠다.

rec(1, 0)





