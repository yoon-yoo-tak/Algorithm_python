import sys

input = sys.stdin.readline

n, m = map(int, input().split())

selected = [0] * m
visited = [False] * (n + 1)


def rec(x):
    if x == m:  # m개 뽑았다 !
        print(*selected)  #출력
        return
    else:
        for i in range(1, n + 1):  # n 까지 돌면서
            if visited[i]:  # i를 뽑았다.
                continue  # 무시하고 다음거
            selected[x] = i
            visited[i] = True
            rec(x + 1)  # 다음거 뽑으러 가기
            selected[x] = 0
            visited[i] = False

rec(0)