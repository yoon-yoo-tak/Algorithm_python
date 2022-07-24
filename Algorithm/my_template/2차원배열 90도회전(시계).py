def rotate_90(a):
    row_length = len(a)
    col_length = len(a[0])

    res = [[0] * row_length for _ in range(col_length)]
    for r in range(row_length):
        for c in range(col_length):
            res[c][row_length - 1 - r] = a[r][c]
    return res

ls = [list(map(int, input().split())) for _ in range(7)]
n = int(input())
for _ in range(3):
    ls = rotate_90(ls)

for i in ls:
    print(i)
