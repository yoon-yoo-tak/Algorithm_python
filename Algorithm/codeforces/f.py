"""

"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    flag = False
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (ls[i] + ls[j] + ls[k]) % 10 == 3:
                    print('YES')
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if not flag:
        print('NO')
