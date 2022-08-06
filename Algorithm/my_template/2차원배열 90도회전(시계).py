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


'''
딕셔너리 병합
a={"a":1,"b":2,"c":3}
b={"d":4,"e":5}
c=a|b
'''
arr=[[1,2,3],[4,5,6],[7,8,9]]
rotated_arr=list(zip(*arr[::-1])) # 시계방향으로 90도 회전
roarr=list(zip(*arr))[::-1] # 반시계방향으로 90도 회전
