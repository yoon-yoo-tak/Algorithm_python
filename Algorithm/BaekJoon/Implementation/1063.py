"""

1063 킹

R : 한 칸 오른쪽으로
L : 한 칸 왼쪽으로
B : 한 칸 아래로
T : 한 칸 위로
RT : 오른쪽 위 대각선으로
LT : 왼쪽 위 대각선으로
RB : 오른쪽 아래 대각선으로
LB : 왼쪽 아래 대각선으로

"""
from sys import stdin

k, s, n = stdin.readline().rstrip().split()
pos_k = [ord(k[0]), int(k[1])]
pos_s = [ord(s[0]), int(s[1])]

for _ in range(int(n)):
    com = stdin.readline().rstrip()
    if com == 'R':
        if 64 < pos_k[0] + 1 < 73:
            pos_k[0] += 1

            if pos_k == pos_s:
                if 64 < pos_s[0] + 1 < 73:
                    pos_s[0] += 1
                else:
                    pos_k[0] -= 1

    elif com == 'L':
        if 64 < pos_k[0] - 1 < 73:
            pos_k[0] -= 1

            if pos_k == pos_s:
                if 64 < pos_s[0] - 1 < 73:
                    pos_s[0] -= 1
                else:
                    pos_k[0] += 1

    elif com == 'B':
        if 0 < pos_k[1] - 1 < 9:
            pos_k[1] -= 1

            if pos_k == pos_s:
                if 0 < pos_s[1] - 1 < 9:
                    pos_s[1] -= 1
                else:
                    pos_k[1] += 1

    elif com == 'T':
        if 0 < pos_k[1] + 1 < 9:
            pos_k[1] += 1

            if pos_k == pos_s:
                if 0 < pos_s[1] + 1 < 9:
                    pos_s[1] += 1
                else:
                    pos_k[1] -= 1

    elif com == 'RT':
        if 0 < pos_k[1] + 1 < 9 and 64 < pos_k[0] + 1 < 73:
            pos_k[0] += 1
            pos_k[1] += 1

            if pos_k == pos_s:
                if 0 < pos_s[1] + 1 < 9 and 64 < pos_s[0] + 1 < 73:
                    pos_s[0] += 1
                    pos_s[1] += 1
                else:
                    pos_k[0] -= 1
                    pos_k[1] -= 1

    elif com == 'LT':
        if 0 < pos_k[1] + 1 < 9 and 64 < pos_k[0] - 1 < 73:
            pos_k[0] -= 1
            pos_k[1] += 1

            if pos_k == pos_s:
                if 0 < pos_s[1] + 1 < 9 and 64 < pos_s[0] - 1 < 73:
                    pos_s[0] -= 1
                    pos_s[1] += 1
                else:
                    pos_k[0] += 1
                    pos_k[1] -= 1

    elif com == 'RB':
        if 0 < pos_k[1] - 1 < 9 and 64 < pos_k[0] + 1 < 73:
            pos_k[0] += 1
            pos_k[1] -= 1

            if pos_k == pos_s:
                if 0 < pos_s[1] - 1 < 9 and 64 < pos_s[0] + 1 < 73:
                    pos_s[0] += 1
                    pos_s[1] -= 1
                else:
                    pos_k[0] -= 1
                    pos_k[1] += 1

    elif com == 'LB':
        if 0 < pos_k[1] - 1 < 9 and 64 < pos_k[0] - 1 < 73:
            pos_k[0] -= 1
            pos_k[1] -= 1

            if pos_k == pos_s:
                if 0 < pos_s[1] - 1 < 9 and 64 < pos_s[0] - 1 < 73:
                    pos_s[0] -= 1
                    pos_s[1] -= 1
                else:
                    pos_k[0] += 1
                    pos_k[1] += 1


print('{}'.format(chr(pos_k[0]) + str(pos_k[1])))
print('{}'.format(chr(pos_s[0]) + str(pos_s[1])))

