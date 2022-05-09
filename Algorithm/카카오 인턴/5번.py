from collections import deque
def ShiftRow(rc):
    temp = deque(rc)
    temp1 = []
    temp1.append(temp.pop())
    while temp:
        temp1.append(temp.popleft())
    return temp

def Rotate(rc):
        coord = [0, 0, len(rc) - 1, len(rc[0]) - 1]
        tmp = rc[coord[0]][coord[1]]

        for i in range(coord[0] + 1, coord[2] + 1):
            rc[i - 1][coord[1]] = rc[i][coord[1]]

        for i in range(coord[1] + 1, coord[3] + 1):
            rc[coord[2]][i - 1] = rc[coord[2]][i]

        for i in range(coord[2] - 1, coord[0] - 1, -1):
            rc[i + 1][coord[3]] = rc[i][coord[3]]

        for i in range(coord[3] - 1, coord[1] - 1, -1):
            rc[coord[0]][i + 1] = rc[coord[0]][i]
        rc[coord[0]][coord[1] + 1] = tmp
        return rc

def solution(rc, operations):
    for i in operations:
        if i == 'Rotate':
            rc = Rotate(rc)
        else:
            rc = ShiftRow(rc)
    return rc


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ['Rotate', 'ShiftRow']))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ['Rotate', 'ShiftRow','ShiftRow']))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ['ShiftRow', 'Rotate', 'ShiftRow','Rotate']))