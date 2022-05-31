import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_score(x, y, k, l):
    dx = [-1, -1, 1, 1]
    dy = [1, -1, -1, 1]
    move_nums = [k, l, k, l]
    sum_of_nums = 0

    for dx, dy, move_num in zip(dx, dy, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy
            if not in_range(x, y):
                return 0
            sum_of_nums += board[x][y]
    return sum_of_nums

ans = 0

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, get_score(i, j, k, l))
print(ans)