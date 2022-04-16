"""
11315 오목 판정
"""


def check(x, y):
    global result

    # 가로 검사
    for i in range(5):
        total = 0
        for j in range(5):
            total += arr[x + i][y + j]
        if total == 5:
            result = "YES"
            return

    # 세로 검사
    for i in range(5):
        total = 0
        for j in range(5):
            total += arr[x + j][y + i]
        if total == 5:
            result = "YES"
            return

    # 좌상 대각선 검사
    total = 0
    for i in range(5):
        total += arr[x + i][y + i]
    if total == 5:
        result = "YES"
        return

    # 우상 대각선 검사
    total = 0
    for i in range(5):
        total += arr[x + i][y + 4 - i]
    if total == 5:
        result = "YES"
        return


for T in range(int(input())):
    N = int(input())
    arr = []
    # 돌이 있으면 1, 없으면 0
    for _ in range(N):
        C = input()
        NC = []
        for i in C:
            if i == ".":
                NC.append(0)
            else:
                NC.append(1)
        arr.append(NC)

    result = "NO"
    for x in range(N - 4):
        for y in range(N - 4):
            check(x, y)

    print(f'#{T + 1} {result}')
