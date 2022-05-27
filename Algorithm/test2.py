import math

ans_list = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        dist = x * x + y * y
        dist = math.sqrt(dist)
        level = math.ceil(dist / 20)
        if level <= 0:
            ans += 10
        elif level <= 11:
            ans += 11 - level

    ans_list.append(f'#{tc} {ans}')
for ans in ans_list:
    print(ans)