import sys
#[0, 12, 7, 4, 0, 10, 9, 8, 0, 0]
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def dfs(cur, prv):  # dfs를 통해 부모 노드의 color_cnt에 자식 노드들의 color_cnt 값과 자기 자신의 색을 더해줌
    color_cnt[cur][arr[cur]] += 1
    for nxt in v[cur]:
        if nxt == prv:
            continue

        dfs(nxt, cur)
        for i in range(2):
            color_cnt[cur][i] += color_cnt[nxt][i]


N = int(input())  # 입력값 받기
arr = [-1] + list(map(int, input().split()))
v = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

color_cnt = [[0] * 2 for i in range(N + 1)]
dfs(1, 0)  # 루트를 1로 잡고 dfs 실행
print(color_cnt)
Q = int(input())
for i in range(Q):
    q = int(input())  # q 노드의 자식노드들 + 부모노드를 colors에 저장
    ans = 0

    C = len(v[q])
    colors = sorted([color_cnt[j][:] for j in v[q]])
    print(colors)
    if q != 1:  # 루트일때를 제외하고, colors 값 중 가장 큰 값인 부모노드에서 현재 노드의 color_cnt 값을 빼줌
        colors[-1][0] -= color_cnt[q][0]
        colors[-1][1] -= color_cnt[q][1]  # 그러면 q 노드를 지나가는 모든 노드들의 color_cnt 값이 저장됨.

    for j in range(C - 1):  # color에서 두개를 골라서 인덱스 0, 1 값이랑 인덱스 1, 0 값 곱한것을 ans 에 더해주고 최종 출력
        for k in range(j + 1, C):
            ans += colors[j][0] * colors[k][1] + colors[j][1] * colors[k][0]
    print(ans)