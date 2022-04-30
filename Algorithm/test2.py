"""

완전탐색
"""
def solution(grid):
    answer = -1
    cnt = 0
    for i in grid:
        cnt += i.count('?')

    sel = ['' for _ in range(cnt)]
    alpha = ['a', 'b', 'c']
    temp = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '?':
                temp.append((i, j))
    print('temp : ',  temp)
    temp2 = []

    def rec(k):
        if k == cnt:
            for x in sel:
                temp2.append(''.join(sel))
        else:
            for i in range(3):
                sel[k] = alpha[i]
                rec(k + 1)
                sel[k] = 0

    rec(0)
    temp2 = sorted(set(temp2))
    print(temp2)



    print(grid)

    return answer


print(solution(["??b", "abc", "cc?"]))


