"""
5373 큐빙 tq
"""
import sys
input = sys.stdin.readline


def rotate(direction, clock_wise):
    if direction == 'F':
        temp_right, temp_bottom, temp_left, temp_top = [[0, 0, 0] for _ in range(4)]
        temp_front = [[0, 0, 0] for _ in range(3)]
        if clock_wise == '+':
            for i in range(3):
                temp_right[i], temp_bottom[2 - i], temp_left[i], temp_top[2 - i] = top[2][i], right[i][0], bottom[0][i], left[i][2]
                for j in range(3):
                    temp_front[j][2 - i] = front[i][j]
        else:
            for i in range(3):
                temp_left[2 - i], temp_bottom[i], temp_right[2 - i], temp_top[i] = top[2][i], left[i][2], bottom[0][i], right[i][0]
                for j in range(3):
                    temp_front[2 - j][i] = front[i][j]

        for i in range(3):
            top[2][i], right[i][0], bottom[0][i], left[i][2] = temp_top[i], temp_right[i], temp_bottom[i], temp_left[i]
            for j in range(3):
                front[i][j] = temp_front[i][j]

    if direction == 'B':
        temp_bottom, temp_right, temp_top, temp_left = [[0, 0, 0] for _ in range(4)]
        temp_behind = [[0, 0, 0] for _ in range(3)]
        if clock_wise == '+':
            for i in range(3):
                temp_right[2 - i], temp_top[i], temp_left[2 - i], temp_bottom[i] = bottom[2][i], right[i][2], top[0][i], left[i][0]
                for j in range(3):
                    temp_behind[j][2 - i] = behind[i][j]
        else:
            for i in range(3):
                temp_left[i], temp_top[2 - i], temp_right[i], temp_bottom[2 - i] = bottom[2][i], left[i][0], top[0][i], right[i][2]
                for j in range(3):
                    temp_behind[2 - j][i] = behind[i][j]

        for i in range(3):
            bottom[2][i], right[i][2], top[0][i], left[i][0] = temp_bottom[i], temp_right[i], temp_top[i], temp_left[i]
            for j in range(3):
                behind[i][j] = temp_behind[i][j]
    if direction == 'L':
        temp_front, temp_bottom, temp_behind, temp_top = [[0, 0, 0] for _ in range(4)]
        temp_left = [[0, 0, 0] for _ in range(3)]
        if clock_wise == '+':
            for i in range(3):
                temp_front[i], temp_bottom[i], temp_behind[i], temp_top[i] = top[i][0], front[i][0], bottom[i][0], behind[i][0]
                for j in range(3):
                    temp_left[j][2 - i] = left[i][j]
        else:
            for i in range(3):
                temp_behind[i], temp_bottom[i], temp_front[i], temp_top[i] = top[i][0], behind[i][0], bottom[i][0], front[i][0]
                for j in range(3):
                    temp_left[2 - j][i] = left[i][j]

        for i in range(3):
            front[i][0], bottom[i][0], behind[i][0], top[i][0] = temp_front[i], temp_bottom[i], temp_behind[i], temp_top[i]
            for j in range(3):
                left[i][j] = temp_left[i][j]

    if direction == 'R':
        temp_front, temp_bottom, temp_behind, temp_top = [[0, 0, 0] for _ in range(4)]
        temp_right = [[0, 0, 0] for _ in range(3)]
        if clock_wise == '+':
            for i in range(3):
                temp_behind[i], temp_bottom[i], temp_front[i], temp_top[i] = top[i][2], behind[i][2], bottom[i][2], front[i][2]
                for j in range(3):
                    temp_right[j][2 - i] = right[i][j]
        else:
            for i in range(3):
                temp_front[i], temp_bottom[i], temp_behind[i], temp_top[i] = top[i][2], front[i][2], bottom[i][2], behind[i][2]
                for j in range(3):
                    temp_right[2 - j][i] = right[i][j]
        for i in range(3):
            front[i][2], bottom[i][2], behind[i][2], top[i][2] = temp_front[i], temp_bottom[i], temp_behind[i], temp_top[i]
            for j in range(3):
                right[i][j] = temp_right[i][j]
    if direction == 'U':
        temp_behind, temp_right, temp_front, temp_left = [[0, 0, 0] for _ in range(4)]
        temp_top = [[0, 0, 0] for _ in range(3)]
        if clock_wise == '+':
            for i in range(3):
                temp_behind[2 - i], temp_right[2 - i], temp_front[i], temp_left[i] = left[0][i], behind[2][i], right[0][i], front[0][i]
                for j in range(3):
                    temp_top[j][2 - i] = top[i][j]
        else:
            for i in range(3):
                temp_front[i], temp_right[i], temp_behind[2 - i], temp_left[2 - i] = left[0][i], front[0][i], right[0][i], behind[2][i]
                for j in range(3):
                    temp_top[2 - j][i] = top[i][j]

        for i in range(3):
            left[0][i], behind[2][i], right[0][i], front[0][i] = temp_left[i], temp_behind[i], temp_right[i], temp_front[i]
            for j in range(3):
                top[i][j] = temp_top[i][j]

    if direction == 'D':
        temp_behind, temp_right, temp_front, temp_left = [[0, 0, 0] for _ in range(4)]
        temp_bottom = [[0, 0, 0] for _ in range(3)]
        if clock_wise == '+':
            for i in range(3):
                temp_right[i], temp_behind[2 - i], temp_left[2 - i], temp_front[i] = front[2][i], right[2][i], behind[0][i], left[2][i]
                for j in range(3):
                    temp_bottom[j][2 - i] = bottom[i][j]
        else:
            for i in range(3):
                temp_behind[2 - i], temp_right[2 - i], temp_front[i], temp_left[i] = left[2][i], behind[0][i], right[2][i], front[2][i]
                for j in range(3):
                    temp_bottom[2 - j][i] = bottom[i][j]

        for i in range(3):
            behind[0][i], right[2][i], front[2][i], left[2][i] = temp_behind[i], temp_right[i], temp_front[i], temp_left[i]
            for j in range(3):
                bottom[i][j] = temp_bottom[i][j]

for _ in range(int(input())):
    n = int(input())
    info = list(input().split())
    top = [['w'] * 3 for _ in range(3)]
    bottom = [['y'] * 3 for _ in range(3)]
    front = [['r'] * 3 for _ in range(3)]
    behind = [['o'] * 3 for _ in range(3)]
    left = [['g'] * 3 for _ in range(3)]
    right = [['b'] * 3 for _ in range(3)]
    for i in info:
        rotate(i[0], i[1])
    for i in top:
        print(*i, sep='')
