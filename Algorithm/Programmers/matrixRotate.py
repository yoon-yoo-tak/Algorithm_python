"""

프로그래머스 행렬 테두리 회전하기

"""
def solution(rows, columns, queries):

    answer = []
    array = [[0 for _ in range(columns)] for _ in range(rows)]
    a = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = a
            a += 1

    for x1, y1, x2, y2 in queries:
        tmp = array[x1 - 1][y1 - 1]
        min_val = tmp

        for k in range(x1 - 1, x2 - 1):
            test = array[k + 1][y1 - 1]
            array[k][y1 - 1] = test
            min_val = min(min_val, test)

        for k in range(y1 - 1, y2 - 1):
            test = array[x2 - 1][k + 1]
            array[x2 - 1][k] = test
            min_val = min(min_val, test)

        for k in range(x2 - 1, x1 - 1, -1):
            test = array[k - 1][y2 - 1]
            array[k][y2 - 1] = test
            min_val = min(min_val, test)

        for k in range(y2-1, y1 - 1, -1):
            test = array[x1 - 1][k - 1]
            array[x1 - 1][k] = test
            min_val = min(min_val, test)

        array[x1-1][y1] = tmp
        answer.append(min_val)

    return answer