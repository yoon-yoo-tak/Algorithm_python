"""

BruteForce + 그래프탐색
"""

1.
import sys

si = sys.stdin.readline
N = int(si())
a = [list(map(int, si().split())) for _ in range(N)]
# 가장 먼 두 고릴라 찾기
v, I, J = 0, 0, 0
for i in range(N):
    for j in range(N):
        if a[i][j] > v:
            v = a[i][j]
            I, J = i, j


def solve(first):
    # 제일 앞에 first가 올 때의 순서 출력
    ord = [(a[first][i], i) for i in range(N)]  # (거리, 번호)
    ord.sort()
    for dist, idx in ord:
        print(idx + 1, end=' ')
    print()


solve(I)
solve(J)
2.
import sys

si = sys.stdin.readline
n, m = map(int, si().split())
a = [list(si().strip()) for _ in range(n)]
visit = [[0 for _ in range(m)] for __ in range(n)]
Qs = []
for i in range(n):
    for j in range(m):
        if a[i][j] == '?':
            Qs.append((i, j))
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def dfs(x, y):
    visit[x][y] = True
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if visit[nx][ny]: continue
        if a[nx][ny] != a[x][y]: continue
        dfs(nx, ny)


def check_group():
    # 모든 고릴라 종이 하나의 군집을 이루면 True, 아니면 False를 리턴하는 함수
    for i in range(n):
        for j in range(m):
            visit[i][j] = False
    for sp in "GRL":
        cnt = 0  # sp 종의 그룹 개수
        for i in range(n):
            for j in range(m):
                if a[i][j] == sp and not visit[i][j]:
                    cnt += 1
                    dfs(i, j)
        if cnt >= 2:
            return False
    return True


ans = 0


def back(idx):  # 0 ~ idx-1 까지의 물음표 위치에 고릴라 예측했고, idx부터 예측하기
    global ans
    if idx == len(Qs):  # 모든 물음표 예측 완료
        if check_group():
            ans += 1
        return
    for ch in "GRL":
        x, y = Qs[idx]
        a[x][y] = ch
        back(idx + 1)
        a[x][y] = '?'


back(0)
print(ans)
3.
# 8 11 0 3 4
# 0 1
# 1 2
# 2 3
# 4 0
# 5 1
# 6 1
# 7 2
# 7 3
# 4 5
# 5 6
# 6 7
import sys

si = sys.stdin.readline
n, m, A, B, K = map(int, si().split())
is_used = [False for _ in range(m)]  # i번째 간선이 사용된 여부
con = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, si().split())
    con[x].append((y, i))  # (정점의 번호, 간선의 번호)
    con[y].append((x, i))
visit = [0 for _ in range(n)]
path = []  # 사용한 간선의 번호들


def dfs(x, len):
    if len > K:  # 탐색 중단
        return
    if x == B:  # 목적지 도착
        for edge_num in path:
            is_used[edge_num] = True
        return

    visit[x] = True
    for y, edge_num in con[x]:
        # x와 y 연결되어 있고, 그 간선의 번호가 edge_num 인 상황
        if visit[y] == True: continue
        path.append(edge_num)
        dfs(y, len + 1)
        path.pop()
    visit[x] = False


dfs(A, 0)
ans = sum(is_used)
print(ans)