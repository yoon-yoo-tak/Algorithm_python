import sys

si = sys.stdin.readline
Q = int(si())


def solve(binary: str, L: int, R: int) -> bool:
    # binary 라는 이진수의 L번지 부터 R번지 까지가 올바르게 포화 이진트리로 표현되느냐?
    if L == R:
        return True
    mid = (L + R) // 2
    root = binary[mid]
    left_child = binary[(L + (mid - 1)) // 2]
    right_child = binary[((mid + 1) + R) // 2]
    if left_child == '1' and root == '0':
        return False
    if right_child == '1' and root == '0':
        return False
    return solve(binary, L, mid - 1) and solve(binary, mid + 1, R)


for _ in range(Q):
    num = int(si())
    binary = bin(num)[2:]
    tree_size = 1
    while tree_size < len(binary):
        tree_size = tree_size * 2 + 1
    binary = '0' * (tree_size - len(binary)) + binary
    if solve(binary, 0, len(binary) - 1):
        print('Yes')
    else:
        print('No')
6.
import sys

si = sys.stdin.readline
N, M, sx, sy, ex, ey, K = map(int, si().split())


def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def possible(x, y, K):
    # (x, y)에서 도착 지점까지 K번 만에 갈 수 있어?
    if not (1 <= x <= N and 1 <= y <= M):
        return False
    if get_dist(x, y, ex, ey) > K:
        return False
    return True


x, y = sx, sy
ans = []
for _ in range(K):
    move = None
    for dir, dx, dy in [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]:
        if possible(x + dx, y + dy, K - 1):
            move = dir
            x += dx
            y += dy
            K -= 1
            break
    if move == None:
        print("Impossible")
        exit()
    ans.append(move)
print(''.join(ans))
7.
import sys

si = sys.stdin.readline
n = int(si())
people = list(map(int, si().split()))
children = [[] for _ in range(n)]
for _ in range(n - 1):
    par, child = map(int, si().split())
    par -= 1
    child -= 1
    children[par].append(child)
for i in range(n):
    children[i].sort()
road = [0 for _ in range(n)]
arrive = []  # 도착하는 마을 순서 기록
unsatisfied_count = 0  # 아직 사람이 더 필요한 마을 수
arrive_count = [0 for _ in range(n)]  # 마을마다 도착한 횟수
for i in range(n):
    if people[i] > 0:
        unsatisfied_count += 1
while unsatisfied_count:
    x = 0
    while children[x]:
        next_x = children[x][road[x]]
        road[x] = (road[x] + 1) % len(children[x])
        x = next_x

    arrive.append(x)
    arrive_count[x] += 1
    if (arrive_count[x] - 1) * 3 < people[x] and arrive_count[x] * 3 >= people[x]:
        # x번 마을에 대해 만족된 순간
        unsatisfied_count -= 1
ans = []
for x in arrive:
    # 현재 도착한 마을은 x 번 마을이다
    cnt = 0
    for t in [1, 2, 3]:
        visit = arrive_count[x]  # 남아있는 방문 횟수
        need = people[x]  # 남아있는 사람 수
        last = need - t  # 갔다고 치면 last 사람이 더 필요함

        # visit-1 번 동안 last 만큼의 사람을 보낼 수 있는 지?
        if (visit - 1) * 1 <= last <= (visit - 1) * 3:
            cnt = t
            break

    if cnt == 0:
        print(-1)
        break
    ans.append(cnt)
    arrive_count[x] -= 1
    people[x] -= cnt
print(*ans)