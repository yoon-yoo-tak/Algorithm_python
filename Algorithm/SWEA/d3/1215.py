"""
1215 회문1
"""
T = 10


def rotate(ls):
    row_length = len(ls)
    col_length = len(ls[0])

    res = [[0] * row_length for _ in range(col_length)]
    for r in range(row_length):
        for c in range(col_length):
            res[c][row_length - 1 - r] = ls[r][c]
    return res


for t in range(1, T + 1):
    n = int(input())
    ls = [list(input()) for _ in range(8)]
    ans = 0
    for row in ls:
        for i in range(8 - n + 1):
            now = row[i:i + n]
            if now == now[::-1]:
                ans += 1
    ls = rotate(ls)
    for row in ls:
        for i in range(8 - n + 1):
            now = row[i:i + n]
            if now == now[::-1]:
                ans += 1
    print(f'#{t} {ans}')