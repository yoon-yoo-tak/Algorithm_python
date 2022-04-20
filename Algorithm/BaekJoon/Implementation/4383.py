"""
4383 점프는 즐거워
"""
import sys
input = sys.stdin.readline
try:
    while True:
        a, *b = map(int, input().split())
        ls = [i + 1 for i in range(a - 1)]
        temp = []
        for i in range(len(b) - 1):
            temp.append(abs(b[i] - b[i + 1]))
        temp = sorted(set(temp))
        if temp == ls:
            print('Jolly')
        else:
            print('Not jolly')

except:
    sys.exit()
