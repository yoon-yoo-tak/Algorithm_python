"""

1331 나이트 투어

"""
import sys
input = sys.stdin.readline

a = [input().strip() for _ in range(36)]
if len(set(a)) == 36:
    for i in range(35):
        if abs((ord(a[i][0]) - ord(a[i + 1][0])) * (int(a[i][1]) - int(a[i + 1][1]))) != 2:
            print('Invalid')
            break
    else:
        for d, b in [[-2, -1], [-2, 1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2]]:
            c = ord(a[-1][0]) + d
            n = int(a[-1][1]) + b
            if ord('A') <= c <= ord('Z') and 1 <= n <= 6:
                if chr(c) == a[0][0] and n == int(a[0][1]):
                    print('Valid')
                    break
        else:
            print('Invalid')
else:
    print('Invalid')